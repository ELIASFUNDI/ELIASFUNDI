import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
  spring,
  useVideoConfig,
} from "remotion";

const skills = [
  { name: "ArcGIS Pro", color: "#2563eb", icon: "🗺️" },
  { name: "QGIS", color: "#22c55e", icon: "🌍" },
  { name: "PostGIS", color: "#3b82f6", icon: "🗄️" },
  { name: "Python", color: "#eab308", icon: "🐍" },
  { name: "React", color: "#06b6d4", icon: "⚛️" },
  { name: "FastAPI", color: "#10b981", icon: "⚡" },
];

const SkillCard: React.FC<{
  skill: { name: string; color: string; icon: string };
  index: number;
  frame: number;
  fps: number;
}> = ({ skill, index, frame, fps }) => {
  const delay = index * 8;

  const cardSpring = spring({
    frame: frame - delay,
    fps,
    config: { damping: 12, stiffness: 80 },
  });

  const opacity = interpolate(frame - delay, [0, 15], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const scale = interpolate(cardSpring, [0, 1], [0.5, 1]);

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        width: 250,
        height: 140,
        background: `linear-gradient(135deg, ${skill.color}20, ${skill.color}10)`,
        border: `2px solid ${skill.color}50`,
        borderRadius: 20,
        opacity,
        transform: `scale(${scale})`,
        boxShadow: `0 10px 40px ${skill.color}30`,
      }}
    >
      <span style={{ fontSize: 40, marginBottom: 10 }}>{skill.icon}</span>
      <span
        style={{
          fontSize: 24,
          fontWeight: 600,
          color: "#ffffff",
          letterSpacing: "1px",
        }}
      >
        {skill.name}
      </span>
    </div>
  );
};

export const SkillsScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleOpacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: "clamp",
  });

  const titleY = interpolate(frame, [0, 20], [-30, 0], {
    extrapolateRight: "clamp",
  });

  // Progress bar animation
  const progressWidth = interpolate(frame, [0, 100], [0, 100], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        background: "linear-gradient(180deg, #0f172a 0%, #1e293b 100%)",
        fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        padding: 80,
      }}
    >
      {/* Animated background dots */}
      {[...Array(20)].map((_, i) => (
        <div
          key={i}
          style={{
            position: "absolute",
            width: 4,
            height: 4,
            borderRadius: "50%",
            backgroundColor: "#3b82f6",
            opacity: 0.2,
            left: `${(i * 5) % 100}%`,
            top: `${(i * 7) % 100}%`,
            transform: `scale(${1 + Math.sin(frame / 10 + i) * 0.5})`,
          }}
        />
      ))}

      {/* Title */}
      <div
        style={{
          opacity: titleOpacity,
          transform: `translateY(${titleY}px)`,
          marginBottom: 60,
        }}
      >
        <h2
          style={{
            fontSize: 64,
            fontWeight: 700,
            color: "#ffffff",
            margin: 0,
            textAlign: "center",
          }}
        >
          Technical Expertise
        </h2>
        <div
          style={{
            width: 200,
            height: 4,
            background: "linear-gradient(90deg, #3b82f6, #22c55e)",
            margin: "20px auto",
            borderRadius: 2,
          }}
        />
      </div>

      {/* Skills Grid */}
      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          justifyContent: "center",
          gap: 30,
          maxWidth: 900,
          margin: "0 auto",
        }}
      >
        {skills.map((skill, index) => (
          <SkillCard
            key={skill.name}
            skill={skill}
            index={index}
            frame={frame}
            fps={fps}
          />
        ))}
      </div>

      {/* Bottom text */}
      <div
        style={{
          position: "absolute",
          bottom: 80,
          left: 0,
          right: 0,
          textAlign: "center",
          opacity: interpolate(frame, [80, 100], [0, 1], {
            extrapolateRight: "clamp",
          }),
        }}
      >
        <p
          style={{
            fontSize: 28,
            color: "#94a3b8",
            margin: 0,
            letterSpacing: "2px",
          }}
        >
          Spatial Analysis • Cartography • Web Mapping • AI Integration
        </p>

        {/* Progress indicator */}
        <div
          style={{
            width: 300,
            height: 4,
            background: "#1e293b",
            borderRadius: 2,
            margin: "30px auto 0",
            overflow: "hidden",
          }}
        >
          <div
            style={{
              width: `${progressWidth}%`,
              height: "100%",
              background: "linear-gradient(90deg, #3b82f6, #22c55e)",
              borderRadius: 2,
            }}
          />
        </div>
      </div>
    </AbsoluteFill>
  );
};
