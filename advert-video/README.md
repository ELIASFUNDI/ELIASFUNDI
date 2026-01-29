# Elias Fundi - Professional Advertisement Video

A programmatic advertisement video created with [Remotion](https://www.remotion.dev/) showcasing GIS/Geomatics expertise.

## Video Specifications

- **Duration**: 15 seconds (450 frames at 30fps)
- **Resolution**: 1920x1080 (16:9) for standard, 1080x1920 (9:16) for social media
- **Format**: MP4/GIF

## Scenes

1. **Intro Scene** (0-4s) - Name reveal with animated globe decoration
2. **Skills Scene** (4-8s) - Technical expertise showcase with animated cards
3. **Projects Scene** (8-12s) - Featured projects with floating cards
4. **Contact Scene** (12-15s) - Call-to-action with contact information

## Setup

```bash
# Install dependencies
npm install

# Start Remotion Studio (preview in browser)
npm start

# Render video to MP4
npm run build

# Render as GIF
npm run build:gif
```

## Customization

### Modify Content
- Edit `src/components/IntroScene.tsx` for name/title changes
- Edit `src/components/SkillsScene.tsx` to update skills
- Edit `src/components/ProjectsScene.tsx` for project highlights
- Edit `src/components/ContactScene.tsx` for contact details

### Modify Timing
- Adjust `durationInFrames` in `src/Root.tsx`
- Modify `Sequence` components in `src/AdvertVideo.tsx`

### Color Scheme
The video uses a professional blue/green gradient theme:
- Primary: `#3b82f6` (blue)
- Secondary: `#22c55e` (green)
- Background: `#0f172a` (dark navy)

## Requirements

- Node.js 18+
- npm or yarn

## Output

Rendered videos are saved to the `out/` directory:
- `out/advert.mp4` - Standard video
- `out/advert.gif` - Animated GIF

## Tech Stack

- Remotion 4.0
- React 18
- TypeScript
