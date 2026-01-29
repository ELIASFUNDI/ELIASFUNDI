import { AbsoluteFill, Sequence } from "remotion";
import { IntroScene } from "./components/IntroScene";
import { SkillsScene } from "./components/SkillsScene";
import { ProjectsScene } from "./components/ProjectsScene";
import { ContactScene } from "./components/ContactScene";

export const AdvertVideo: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: "#0a0a0a" }}>
      {/* Intro Scene - 0 to 120 frames (4 seconds) */}
      <Sequence from={0} durationInFrames={120}>
        <IntroScene />
      </Sequence>

      {/* Skills Scene - 120 to 240 frames (4 seconds) */}
      <Sequence from={120} durationInFrames={120}>
        <SkillsScene />
      </Sequence>

      {/* Projects Scene - 240 to 360 frames (4 seconds) */}
      <Sequence from={240} durationInFrames={120}>
        <ProjectsScene />
      </Sequence>

      {/* Contact/CTA Scene - 360 to 450 frames (3 seconds) */}
      <Sequence from={360} durationInFrames={90}>
        <ContactScene />
      </Sequence>
    </AbsoluteFill>
  );
};
