# Video Transcript Converter

A powerful web application that converts Instagram and Facebook videos to text transcripts with automatic speaker identification, timestamps, and chapter detection.

## Features

- **Multi-Platform Support**: Works with Instagram (Reels, Posts, Stories) and Facebook videos
- **Speaker Diarization**: Automatically identifies and labels different speakers (Speaker 1, Speaker 2, etc.)
- **Timestamps**: Accurate timestamps for each speaker segment
- **Chapter Detection**: Automatically detects and summarizes different sections of the video
- **Multiple Export Options**: Copy to clipboard or download as text file
- **Clean UI**: Modern, responsive interface that works on all devices
- **Free & Open Source**: Built with open-source technologies

## Demo

Simply paste an Instagram or Facebook video URL and get:
- Full transcript with speaker labels
- Timestamps for each segment
- Automatic chapter detection
- Plain text version for easy copying

## Technology Stack

- **Backend**: Flask (Python)
- **Video Processing**: yt-dlp (video download)
- **Transcription**: AssemblyAI API (with speaker diarization)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Can be deployed on Heroku, Railway, or any Python hosting

## Prerequisites

- Python 3.8 or higher
- FFmpeg (for audio extraction)
- AssemblyAI API key (free tier available)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ELIASFUNDI/ELIASFUNDI.git
cd ELIASFUNDI
```

### 2. Install FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Get your free AssemblyAI API key:
   - Visit [AssemblyAI](https://www.assemblyai.com/)
   - Sign up for a free account
   - Copy your API key from the dashboard

3. Edit `.env` and add your API key:
```
ASSEMBLYAI_API_KEY=your-actual-api-key-here
```

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

1. **Open the Application**: Navigate to `http://localhost:5000` in your browser

2. **Paste Video URL**: Copy the URL of an Instagram or Facebook video and paste it into the input field

3. **Convert**: Click "Convert to Transcript" and wait for processing

4. **View Results**: The transcript will display with:
   - Video title
   - Detected speakers
   - Chapters (if available)
   - Full transcript with speaker labels and timestamps
   - Plain text version

5. **Export**: Use the "Copy All" button to copy to clipboard or "Download" to save as a text file

## Supported URL Formats

### Instagram
- Posts: `https://www.instagram.com/p/[POST_ID]/`
- Reels: `https://www.instagram.com/reel/[REEL_ID]/`
- Stories: `https://www.instagram.com/stories/[USERNAME]/[STORY_ID]/`

### Facebook
- Videos: `https://www.facebook.com/watch/?v=[VIDEO_ID]`
- Posts: `https://www.facebook.com/[USER]/videos/[VIDEO_ID]/`
- Short URLs: `https://fb.watch/[SHORT_ID]/`

## API Endpoints

### `GET /`
Renders the main application page

### `POST /api/transcribe`
Transcribes a video from URL

**Request Body:**
```json
{
  "url": "https://www.instagram.com/p/example/"
}
```

**Response:**
```json
{
  "title": "Video Title",
  "speakers": {
    "Speaker A": ["text1", "text2"],
    "Speaker B": ["text3", "text4"]
  },
  "utterances": [
    {
      "speaker": "Speaker A",
      "text": "Hello world",
      "start": "00:00",
      "end": "00:05",
      "start_ms": 0,
      "end_ms": 5000
    }
  ],
  "chapters": [
    {
      "headline": "Introduction",
      "summary": "Speaker introduces the topic",
      "start": "00:00",
      "end": "01:30"
    }
  ],
  "full_text": "Complete transcript text..."
}
```

### `GET /health`
Health check endpoint

## Deployment

### Heroku

1. Create a Heroku app:
```bash
heroku create your-app-name
```

2. Add FFmpeg buildpack:
```bash
heroku buildpacks:add --index 1 https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
heroku buildpacks:add --index 2 heroku/python
```

3. Set environment variables:
```bash
heroku config:set ASSEMBLYAI_API_KEY=your-api-key
```

4. Deploy:
```bash
git push heroku main
```

### Railway

1. Connect your GitHub repository to Railway
2. Add FFmpeg buildpack in settings
3. Set `ASSEMBLYAI_API_KEY` environment variable
4. Deploy automatically on push

## Project Structure

```
ELIASFUNDI/
├── app.py                 # Flask application & API endpoints
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
├── runtime.txt           # Python version
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
├── templates/
│   └── index.html       # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css    # Styles
│   └── js/
│       └── script.js    # Frontend JavaScript
└── downloads/           # Temporary video/audio storage (gitignored)
```

## Limitations

- **AssemblyAI Free Tier**: Limited to 5 hours of transcription per month (check current limits)
- **Video Length**: Longer videos take more time to process
- **Private Videos**: Cannot access private or login-required videos
- **File Size**: Limited by your hosting platform's constraints

## Troubleshooting

### "Failed to download video"
- Ensure the video URL is public and accessible
- Check if yt-dlp supports the URL format
- Update yt-dlp: `pip install --upgrade yt-dlp`

### "Transcription failed"
- Verify your AssemblyAI API key is correct
- Check your API quota hasn't been exceeded
- Ensure the audio was extracted successfully

### FFmpeg not found
- Install FFmpeg following the installation instructions
- Ensure FFmpeg is in your system PATH

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Video downloader
- [AssemblyAI](https://www.assemblyai.com/) - Transcription API
- [FFmpeg](https://ffmpeg.org/) - Audio/video processing

## Contact

Elias Fundi - eliasdavi965@gmail.com

Project Link: [https://github.com/ELIASFUNDI/ELIASFUNDI](https://github.com/ELIASFUNDI/ELIASFUNDI)

---

Built with Flask & AssemblyAI
