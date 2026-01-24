from flask import Flask, render_template, request, jsonify
import os
import yt_dlp
import assemblyai as aai
from pathlib import Path
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'downloads'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max

# Create downloads folder if it doesn't exist
Path(app.config['UPLOAD_FOLDER']).mkdir(exist_ok=True)

# AssemblyAI API key (set via environment variable)
aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY', 'your-api-key-here')


def download_video(url):
    """Download video from Instagram or Facebook and extract audio"""
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], f'video_{int(time.time())}')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            audio_file = f'{output_path}.mp3'
            return audio_file, info.get('title', 'Unknown')
    except Exception as e:
        raise Exception(f"Failed to download video: {str(e)}")


def transcribe_audio(audio_file):
    """Transcribe audio with speaker diarization using AssemblyAI"""
    try:
        config = aai.TranscriptionConfig(
            speaker_labels=True,
            auto_chapters=True,
        )

        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_file, config=config)

        if transcript.status == aai.TranscriptStatus.error:
            raise Exception(f"Transcription failed: {transcript.error}")

        return transcript
    except Exception as e:
        raise Exception(f"Transcription error: {str(e)}")


def format_timestamp(milliseconds):
    """Convert milliseconds to HH:MM:SS format"""
    seconds = milliseconds / 1000
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def format_transcript(transcript):
    """Format transcript with timestamps and speaker labels"""
    formatted_output = {
        'title': 'Transcript',
        'speakers': {},
        'utterances': [],
        'chapters': []
    }

    # Format speaker utterances
    if transcript.utterances:
        for utterance in transcript.utterances:
            speaker = f"Speaker {utterance.speaker}"
            formatted_output['utterances'].append({
                'speaker': speaker,
                'text': utterance.text,
                'start': format_timestamp(utterance.start),
                'end': format_timestamp(utterance.end),
                'start_ms': utterance.start,
                'end_ms': utterance.end
            })

            # Track unique speakers
            if speaker not in formatted_output['speakers']:
                formatted_output['speakers'][speaker] = []
            formatted_output['speakers'][speaker].append(utterance.text)

    # Format chapters if available
    if transcript.chapters:
        for chapter in transcript.chapters:
            formatted_output['chapters'].append({
                'headline': chapter.headline,
                'summary': chapter.summary,
                'start': format_timestamp(chapter.start),
                'end': format_timestamp(chapter.end),
                'start_ms': chapter.start,
                'end_ms': chapter.end
            })

    # Add full text
    formatted_output['full_text'] = transcript.text

    return formatted_output


@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')


@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    """Handle video URL and return transcript"""
    try:
        data = request.get_json()
        video_url = data.get('url')

        if not video_url:
            return jsonify({'error': 'No URL provided'}), 400

        # Validate URL (basic check)
        if not ('instagram.com' in video_url or 'facebook.com' in video_url or 'fb.watch' in video_url):
            return jsonify({'error': 'Please provide a valid Instagram or Facebook video URL'}), 400

        # Download video and extract audio
        audio_file, title = download_video(video_url)

        # Transcribe audio
        transcript = transcribe_audio(audio_file)

        # Format output
        result = format_transcript(transcript)
        result['title'] = title

        # Clean up audio file
        try:
            if os.path.exists(audio_file):
                os.remove(audio_file)
        except:
            pass

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
