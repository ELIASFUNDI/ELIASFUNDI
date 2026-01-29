# Elias Fundi - Professional Advertisement Video

A programmatic advertisement video created with [Remotion](https://www.remotion.dev/) showcasing GIS/Geomatics and Land Surveying expertise.

## Video Specifications

- **Duration**: 19 seconds (570 frames at 30fps)
- **Resolution**: 1920x1080 (16:9) for standard, 1080x1920 (9:16) for social media
- **Format**: MP4/GIF

## Scenes

1. **Intro Scene** (0-4s) - Profile photo with name, title "Licensed Surveyor | GIS Specialist | Spatial Analyst"
2. **Skills Scene** (4-8s) - Technical expertise with survey equipment image (Land Surveying, GNSS/GPS, Total Station, ArcGIS Pro, QGIS, PostGIS, Python, Cartography)
3. **Field Work Scene** (8-12s) - Fieldwork and graduation photos with experience stats
4. **Projects Scene** (12-16s) - Featured projects (HydroGPT, Earthquake Tracker, Route Optimizer)
5. **Contact Scene** (16-19s) - Email, WhatsApp/Phone, and website

## Required Images

Before running, add these images to the `public/` folder:

```
public/
├── headshot.jpg        # Professional portrait photo
├── graduation.jpg      # Graduation ceremony photo
├── survey-equipment.jpg # GNSS/GPS tripod in field
└── fieldwork.jpg       # Photo doing field survey work
```

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
- Edit `src/components/FieldWorkScene.tsx` for experience stats
- Edit `src/components/ProjectsScene.tsx` for project highlights
- Edit `src/components/ContactScene.tsx` for contact details

### Contact Information
Current contact details in ContactScene.tsx:
- Email: eliasfundi6@gmail.com
- Phone/WhatsApp: +254 792 201 418
- Website: eliasfundi.github.io/portfolio

### Modify Timing
- Adjust `durationInFrames` in `src/Root.tsx`
- Modify `Sequence` components in `src/AdvertVideo.tsx`

### Color Scheme
The video uses a professional blue/green/orange gradient theme:
- Primary: `#3b82f6` (blue)
- Secondary: `#22c55e` (green)
- Accent: `#f59e0b` (orange/amber for surveying)
- Background: `#0f172a` (dark navy)

## Requirements

- Node.js 18+
- npm or yarn

## Output

Rendered videos are saved to the `out/` directory:
- `out/advert.mp4` - Standard landscape video (1920x1080)
- `out/advert.gif` - Animated GIF

## Tech Stack

- Remotion 4.0
- React 18
- TypeScript
