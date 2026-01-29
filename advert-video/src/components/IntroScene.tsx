import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
  spring,
  useVideoConfig,
} from "remotion";

export const IntroScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Animations
  const titleOpacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateRight: "clamp",
  });

  const titleScale = spring({
    frame,
    fps,
    config: { damping: 12, stiffness: 100 },
  });

  const subtitleOpacity = interpolate(frame, [30, 60], [0, 1], {
    extrapolateRight: "clamp",
  });

  const subtitleY = interpolate(frame, [30, 60], [30, 0], {
    extrapolateRight: "clamp",
  });

  const locationOpacity = interpolate(frame, [60, 90], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Globe/map decorative elements animation
  const globeRotation = interpolate(frame, [0, 120], [0, 360]);
  const pulseScale = interpolate(
    frame % 30,
    [0, 15, 30],
    [1, 1.1, 1],
  );

  return (
    <AbsoluteFill
      style={{
        background: "linear-gradient(135deg, #0f172a 0%, #1e3a5f 50%, #0f172a 100%)",
        justifyContent: "center",
        alignItems: "center",
        fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
      }}
    >
      {/* Animated background grid */}
      <div
        style={{
          position: "absolute",
          width: "100%",
          height: "100%",
          backgroundImage: `
            linear-gradient(rgba(59, 130, 246, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(59, 130, 246, 0.1) 1px, transparent 1px)
          `,
          backgroundSize: "50px 50px",
          opacity: 0.5,
        }}
      />

      {/* Decorative globe circles */}
      <div
        style={{
          position: "absolute",
          width: 400,
          height: 400,
          borderRadius: "50%",
          border: "2px solid rgba(59, 130, 246, 0.3)",
          transform: `rotate(${globeRotation}deg) scale(${pulseScale})`,
        }}
      />
      <div
        style={{
          position: "absolute",
          width: 500,
          height: 500,
          borderRadius: "50%",
          border: "1px solid rgba(34, 197, 94, 0.2)",
          transform: `rotate(${-globeRotation * 0.5}deg)`,
        }}
      />

      {/* Main content */}
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          zIndex: 10,
        }}
      >
        {/* Name */}
        <h1
          style={{
            fontSize: 120,
            fontWeight: 800,
            color: "#ffffff",
            margin: 0,
            opacity: titleOpacity,
            transform: `scale(${titleScale})`,
            textShadow: "0 0 60px rgba(59, 130, 246, 0.5)",
            letterSpacing: "-2px",
          }}
        >
          ELIAS FUNDI
        </h1>

        {/* Title */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 20,
            opacity: subtitleOpacity,
            transform: `translateY(${subtitleY}px)`,
            marginTop: 20,
          }}
        >
          <div
            style={{
              width: 60,
              height: 3,
              background: "linear-gradient(90deg, transparent, #3b82f6)",
            }}
          />
          <h2
            style={{
              fontSize: 42,
              fontWeight: 400,
              color: "#3b82f6",
              margin: 0,
              letterSpacing: "8px",
              textTransform: "uppercase",
            }}
          >
            Geomatics Engineer
          </h2>
          <div
            style={{
              width: 60,
              height: 3,
              background: "linear-gradient(90deg, #3b82f6, transparent)",
            }}
          />
        </div>

        {/* Subtitle */}
        <h3
          style={{
            fontSize: 28,
            fontWeight: 300,
            color: "#22c55e",
            margin: 0,
            marginTop: 15,
            opacity: subtitleOpacity,
            transform: `translateY(${subtitleY}px)`,
            letterSpacing: "4px",
          }}
        >
          GIS Specialist & Spatial Analyst
        </h3>

        {/* Location */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 10,
            marginTop: 40,
            opacity: locationOpacity,
          }}
        >
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="#94a3b8"
            strokeWidth="2"
          >
            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
            <circle cx="12" cy="10" r="3" />
          </svg>
          <span
            style={{
              fontSize: 22,
              color: "#94a3b8",
              letterSpacing: "2px",
            }}
          >
            Nyeri, Kenya
          </span>
        </div>
      </div>

      {/* Corner decorations */}
      <div
        style={{
          position: "absolute",
          top: 40,
          left: 40,
          width: 100,
          height: 100,
          borderLeft: "3px solid #3b82f6",
          borderTop: "3px solid #3b82f6",
          opacity: titleOpacity,
        }}
      />
      <div
        style={{
          position: "absolute",
          bottom: 40,
          right: 40,
          width: 100,
          height: 100,
          borderRight: "3px solid #22c55e",
          borderBottom: "3px solid #22c55e",
          opacity: titleOpacity,
        }}
      />
    </AbsoluteFill>
  );
};
