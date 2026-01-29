import {
  AbsoluteFill,
  Img,
  interpolate,
  useCurrentFrame,
  spring,
  useVideoConfig,
  staticFile,
} from "remotion";

export const IntroScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Image animation
  const imageScale = spring({
    frame,
    fps,
    config: { damping: 15, stiffness: 80 },
  });

  const imageOpacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Name animation
  const titleOpacity = interpolate(frame, [15, 40], [0, 1], {
    extrapolateRight: "clamp",
  });

  const titleScale = spring({
    frame: frame - 15,
    fps,
    config: { damping: 12, stiffness: 100 },
  });

  const subtitleOpacity = interpolate(frame, [40, 65], [0, 1], {
    extrapolateRight: "clamp",
  });

  const subtitleY = interpolate(frame, [40, 65], [30, 0], {
    extrapolateRight: "clamp",
  });

  const locationOpacity = interpolate(frame, [65, 90], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Globe/map decorative elements animation
  const globeRotation = interpolate(frame, [0, 120], [0, 360]);
  const pulseScale = interpolate(frame % 30, [0, 15, 30], [1, 1.1, 1]);

  return (
    <AbsoluteFill
      style={{
        background:
          "linear-gradient(135deg, #0f172a 0%, #1e3a5f 50%, #0f172a 100%)",
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
          flexDirection: "row",
          alignItems: "center",
          gap: 80,
          zIndex: 10,
        }}
      >
        {/* Profile Image */}
        <div
          style={{
            opacity: imageOpacity,
            transform: `scale(${imageScale})`,
          }}
        >
          <div
            style={{
              width: 280,
              height: 280,
              borderRadius: "50%",
              overflow: "hidden",
              border: "4px solid #3b82f6",
              boxShadow: "0 0 60px rgba(59, 130, 246, 0.5)",
            }}
          >
            <Img
              src={staticFile("headshot.jpg")}
              style={{
                width: "100%",
                height: "100%",
                objectFit: "cover",
              }}
            />
          </div>
        </div>

        {/* Text Content */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "flex-start",
          }}
        >
          {/* Name */}
          <h1
            style={{
              fontSize: 100,
              fontWeight: 800,
              color: "#ffffff",
              margin: 0,
              opacity: titleOpacity,
              transform: `scale(${Math.max(0.8, titleScale)})`,
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
              gap: 15,
              opacity: subtitleOpacity,
              transform: `translateY(${subtitleY}px)`,
              marginTop: 15,
            }}
          >
            <div
              style={{
                width: 50,
                height: 3,
                background: "linear-gradient(90deg, transparent, #3b82f6)",
              }}
            />
            <h2
              style={{
                fontSize: 36,
                fontWeight: 400,
                color: "#3b82f6",
                margin: 0,
                letterSpacing: "6px",
                textTransform: "uppercase",
              }}
            >
              Geomatics Engineer
            </h2>
          </div>

          {/* Subtitle */}
          <h3
            style={{
              fontSize: 26,
              fontWeight: 300,
              color: "#22c55e",
              margin: 0,
              marginTop: 12,
              opacity: subtitleOpacity,
              transform: `translateY(${subtitleY}px)`,
              letterSpacing: "3px",
            }}
          >
            Licensed Surveyor | GIS Specialist | Spatial Analyst
          </h3>

          {/* Location */}
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 10,
              marginTop: 30,
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
