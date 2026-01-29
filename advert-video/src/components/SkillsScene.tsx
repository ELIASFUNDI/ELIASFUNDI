import {
  AbsoluteFill,
  Img,
  interpolate,
  useCurrentFrame,
  spring,
  useVideoConfig,
  staticFile,
} from "remotion";

const skills = [
  { name: "Land Surveying", color: "#f59e0b", icon: "📐" },
  { name: "GNSS/GPS", color: "#ef4444", icon: "📡" },
  { name: "Total Station", color: "#8b5cf6", icon: "🔭" },
  { name: "ArcGIS Pro", color: "#2563eb", icon: "🗺️" },
  { name: "QGIS", color: "#22c55e", icon: "🌍" },
  { name: "PostGIS", color: "#3b82f6", icon: "🗄️" },
  { name: "Python", color: "#eab308", icon: "🐍" },
  { name: "Cartography", color: "#ec4899", icon: "🧭" },
];

const SkillCard: React.FC<{
  skill: { name: string; color: string; icon: string };
  index: number;
  frame: number;
  fps: number;
}> = ({ skill, index, frame, fps }) => {
  const delay = index * 6;

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
        width: 200,
        height: 120,
        background: `linear-gradient(135deg, ${skill.color}20, ${skill.color}10)`,
        border: `2px solid ${skill.color}50`,
        borderRadius: 16,
        opacity,
        transform: `scale(${scale})`,
        boxShadow: `0 10px 40px ${skill.color}30`,
      }}
    >
      <span style={{ fontSize: 32, marginBottom: 8 }}>{skill.icon}</span>
      <span
        style={{
          fontSize: 18,
          fontWeight: 600,
          color: "#ffffff",
          letterSpacing: "1px",
          textAlign: "center",
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

  // Image animation
  const imageOpacity = interpolate(frame, [10, 30], [0, 1], {
    extrapolateRight: "clamp",
  });

  const imageScale = spring({
    frame: frame - 10,
    fps,
    config: { damping: 15, stiffness: 80 },
  });

  return (
    <AbsoluteFill
      style={{
        background: "linear-gradient(180deg, #0f172a 0%, #1e293b 100%)",
        fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        padding: 50,
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
          marginBottom: 30,
        }}
      >
        <h2
          style={{
            fontSize: 56,
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
            margin: "15px auto",
            borderRadius: 2,
          }}
        />
      </div>

      {/* Main Content - Image + Skills */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          gap: 60,
        }}
      >
        {/* Survey Equipment Image */}
        <div
          style={{
            opacity: imageOpacity,
            transform: `scale(${Math.max(0.8, imageScale)})`,
          }}
        >
          <div
            style={{
              width: 320,
              height: 420,
              borderRadius: 20,
              overflow: "hidden",
              border: "3px solid #f59e0b",
              boxShadow: "0 20px 60px rgba(245, 158, 11, 0.3)",
            }}
          >
            <Img
              src={staticFile("survey-equipment.jpg")}
              style={{
                width: "100%",
                height: "100%",
                objectFit: "cover",
              }}
            />
          </div>
          <p
            style={{
              textAlign: "center",
              color: "#f59e0b",
              fontSize: 16,
              marginTop: 12,
              fontWeight: 500,
              letterSpacing: "1px",
            }}
          >
            Professional Survey Equipment
          </p>
        </div>

        {/* Skills Grid */}
        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            justifyContent: "center",
            gap: 20,
            maxWidth: 680,
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
      </div>

      {/* Bottom text */}
      <div
        style={{
          position: "absolute",
          bottom: 50,
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
            fontSize: 24,
            color: "#94a3b8",
            margin: 0,
            letterSpacing: "2px",
          }}
        >
          Land Surveying • Boundary Mapping • Cadastral Surveys • Topographic Mapping
        </p>
      </div>
    </AbsoluteFill>
  );
};
