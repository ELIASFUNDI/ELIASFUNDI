let currentTranscript = null;

async function convertVideo() {
    const urlInput = document.getElementById('videoUrl');
    const convertBtn = document.getElementById('convertBtn');
    const status = document.getElementById('status');
    const result = document.getElementById('result');
    const btnText = convertBtn.querySelector('.btn-text');
    const loader = convertBtn.querySelector('.loader');

    const url = urlInput.value.trim();

    if (!url) {
        showStatus('Please enter a video URL', 'error');
        return;
    }

    // Disable button and show loader
    convertBtn.disabled = true;
    btnText.textContent = 'Processing...';
    loader.style.display = 'inline-block';
    result.style.display = 'none';

    showStatus('Downloading video and extracting audio...', 'info');

    try {
        const response = await fetch('/api/transcribe', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: url }),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Failed to process video');
        }

        currentTranscript = data;
        displayTranscript(data);
        showStatus('Transcript generated successfully!', 'success');

        setTimeout(() => {
            status.style.display = 'none';
        }, 3000);

    } catch (error) {
        showStatus(`Error: ${error.message}`, 'error');
        console.error('Error:', error);
    } finally {
        convertBtn.disabled = false;
        btnText.textContent = 'Convert to Transcript';
        loader.style.display = 'none';
    }
}

function showStatus(message, type) {
    const status = document.getElementById('status');
    status.textContent = message;
    status.className = `status ${type}`;
    status.style.display = 'block';
}

function displayTranscript(data) {
    const result = document.getElementById('result');
    const videoTitle = document.getElementById('videoTitle');
    const chaptersSection = document.getElementById('chaptersSection');
    const chapters = document.getElementById('chapters');
    const speakersSummary = document.getElementById('speakersSummary');
    const transcript = document.getElementById('transcript');
    const fullText = document.getElementById('fullText');

    // Set title
    videoTitle.textContent = data.title || 'Transcript';

    // Display chapters if available
    if (data.chapters && data.chapters.length > 0) {
        chaptersSection.style.display = 'block';
        chapters.innerHTML = data.chapters.map(chapter => `
            <div class="chapter">
                <div class="chapter-header">
                    <span class="chapter-title">${escapeHtml(chapter.headline)}</span>
                    <span class="chapter-time">${chapter.start} - ${chapter.end}</span>
                </div>
                <div class="chapter-summary">${escapeHtml(chapter.summary)}</div>
            </div>
        `).join('');
    } else {
        chaptersSection.style.display = 'none';
    }

    // Display speakers summary
    const speakersList = Object.keys(data.speakers);
    if (speakersList.length > 0) {
        speakersSummary.innerHTML = `
            <h3>Speakers Detected</h3>
            ${speakersList.map(speaker =>
                `<span class="speaker-badge">${speaker}</span>`
            ).join('')}
        `;
    }

    // Display utterances with speaker labels
    if (data.utterances && data.utterances.length > 0) {
        transcript.innerHTML = `<h3>Transcript with Speakers & Timestamps</h3>` +
            data.utterances.map(utterance => `
                <div class="utterance">
                    <div class="utterance-header">
                        <span class="speaker-label">${escapeHtml(utterance.speaker)}</span>
                        <span class="timestamp">${utterance.start} - ${utterance.end}</span>
                    </div>
                    <div class="utterance-text">${escapeHtml(utterance.text)}</div>
                </div>
            `).join('');
    }

    // Display full text
    fullText.textContent = data.full_text || '';

    result.style.display = 'block';
    result.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function copyTranscript() {
    if (!currentTranscript) return;

    let text = `${currentTranscript.title}\n\n`;

    if (currentTranscript.chapters && currentTranscript.chapters.length > 0) {
        text += '=== CHAPTERS ===\n\n';
        currentTranscript.chapters.forEach(chapter => {
            text += `[${chapter.start} - ${chapter.end}] ${chapter.headline}\n`;
            text += `${chapter.summary}\n\n`;
        });
    }

    text += '=== TRANSCRIPT WITH SPEAKERS ===\n\n';
    currentTranscript.utterances.forEach(utterance => {
        text += `[${utterance.start} - ${utterance.end}] ${utterance.speaker}:\n`;
        text += `${utterance.text}\n\n`;
    });

    navigator.clipboard.writeText(text).then(() => {
        showStatus('Transcript copied to clipboard!', 'success');
        setTimeout(() => {
            document.getElementById('status').style.display = 'none';
        }, 2000);
    }).catch(err => {
        showStatus('Failed to copy to clipboard', 'error');
    });
}

function downloadTranscript() {
    if (!currentTranscript) return;

    let text = `${currentTranscript.title}\n`;
    text += `Generated: ${new Date().toLocaleString()}\n`;
    text += '='.repeat(60) + '\n\n';

    if (currentTranscript.chapters && currentTranscript.chapters.length > 0) {
        text += '=== CHAPTERS ===\n\n';
        currentTranscript.chapters.forEach(chapter => {
            text += `[${chapter.start} - ${chapter.end}] ${chapter.headline}\n`;
            text += `${chapter.summary}\n\n`;
        });
        text += '\n';
    }

    text += '=== TRANSCRIPT WITH SPEAKERS ===\n\n';
    currentTranscript.utterances.forEach(utterance => {
        text += `[${utterance.start} - ${utterance.end}] ${utterance.speaker}:\n`;
        text += `${utterance.text}\n\n`;
    });

    text += '\n' + '='.repeat(60) + '\n';
    text += '=== FULL TRANSCRIPT (PLAIN TEXT) ===\n\n';
    text += currentTranscript.full_text;

    const blob = new Blob([text], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `transcript-${Date.now()}.txt`;
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
    document.body.removeChild(a);

    showStatus('Transcript downloaded!', 'success');
    setTimeout(() => {
        document.getElementById('status').style.display = 'none';
    }, 2000);
}

// Allow Enter key to submit
document.getElementById('videoUrl').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        convertVideo();
    }
});
