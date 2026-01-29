import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
  spring,
  useVideoConfig,
} from "remotion";

const projects = [
  {
    name: "HydroGPT",
    description: "AI-Enhanced Water Accessibility Analysis",
    stat: "96%",
    statLabel: "Query Accuracy",
    gradient: "linear-gradient(135deg, #06b6d4, #3b82f6)",
  },
  {
    name: "Earthquake Tracker",
    description: "Real-time USGS Seismic Visualization",
    stat: "Live",
    statLabel: "Data Feed",
    gradient: "linear-gradient(135deg, #ef4444, #f97316)",
  },
  {
    name: "Route Optimizer",
    description: "Intelligent Path & Distance Calculator",
    stat: "Fast",
    statLabel: "Computation",
    gradient: "linear-gradient(135deg, #22c55e, #84cc16)",
  },
];

export const ProjectsScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleOpacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        background: "linear-gradient(135deg, #0f172a 0%, #1e1e2e 100%)",
        fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        padding: 60,
      }}
    >
      {/* Background decoration */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          width: 800,
          height: 800,
          background: "radial-gradient(circle, rgba(59, 130, 246, 0.1) 0%, transparent 70%)",
          borderRadius: "50%",
        }}
      />

      {/* Title */}
      <div
        style={{
          opacity: titleOpacity,
          textAlign: "center",
          marginBottom: 50,
        }}
      >
        <h2
          style={{
            fontSize: 58,
            fontWeight: 700,
            color: "#ffffff",
            margin: 0,
          }}
        >
          Featured Projects
        </h2>
        <div
          style={{
            width: 150,
            height: 4,
            background: "linear-gradient(90deg, #3b82f6, #22c55e)",
            margin: "15px auto",
            borderRadius: 2,
          }}
        />
      </div>

      {/* Projects row */}
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          gap: 40,
          marginTop: 40,
        }}
      >
        {projects.map((project, index) => {
          const delay = 20 + index * 15;

          const cardSpring = spring({
            frame: frame - delay,
            fps,
            config: { damping: 14, stiffness: 100 },
          });

          const opacity = interpolate(frame - delay, [0, 20], [0, 1], {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
          });

          const translateY = interpolate(cardSpring, [0, 1], [60, 0]);
          const scale = interpolate(cardSpring, [0, 1], [0.9, 1]);

          // Floating animation after entry
          const floatY = frame > delay + 30
            ? Math.sin((frame - delay - 30) / 15) * 5
            : 0;

          return (
            <div
              key={project.name}
              style={{
                width: 380,
                background: "rgba(30, 41, 59, 0.8)",
                borderRadius: 24,
                padding: 35,
                opacity,
                transform: `translateY(${translateY + floatY}px) scale(${scale})`,
                border: "1px solid rgba(255, 255, 255, 0.1)",
                boxShadow: "0 20px 60px rgba(0, 0, 0, 0.4)",
              }}
            >
              {/* Stat badge */}
              <div
                style={{
                  display: "inline-block",
                  background: project.gradient,
                  padding: "12px 24px",
                  borderRadius: 12,
                  marginBottom: 25,
                }}
              >
                <span
                  style={{
                    fontSize: 32,
                    fontWeight: 800,
                    color: "#ffffff",
                  }}
                >
                  {project.stat}
                </span>
                <span
                  style={{
                    fontSize: 14,
                    color: "rgba(255, 255, 255, 0.9)",
                    marginLeft: 10,
                    textTransform: "uppercase",
                    letterSpacing: "1px",
                  }}
                >
                  {project.statLabel}
                </span>
              </div>

              {/* Project name */}
              <h3
                style={{
                  fontSize: 32,
                  fontWeight: 700,
                  color: "#ffffff",
                  margin: "0 0 12px 0",
                }}
              >
                {project.name}
              </h3>

              {/* Description */}
              <p
                style={{
                  fontSize: 18,
                  color: "#94a3b8",
                  margin: 0,
                  lineHeight: 1.5,
                }}
              >
                {project.description}
              </p>

              {/* Bottom decoration */}
              <div
                style={{
                  marginTop: 25,
                  height: 4,
                  background: project.gradient,
                  borderRadius: 2,
                  opacity: 0.5,
                }}
              />
            </div>
          );
        })}
      </div>

      {/* Bottom tagline */}
      <div
        style={{
          position: "absolute",
          bottom: 60,
          left: 0,
          right: 0,
          textAlign: "center",
          opacity: interpolate(frame, [90, 110], [0, 1], {
            extrapolateRight: "clamp",
          }),
        }}
      >
        <p
          style={{
            fontSize: 24,
            color: "#64748b",
            margin: 0,
            fontStyle: "italic",
          }}
        >
          Transforming spatial data into actionable insights
        </p>
      </div>
    </AbsoluteFill>
  );
};
