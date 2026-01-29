import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
  spring,
  useVideoConfig,
} from "remotion";

export const ContactScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Main CTA animation
  const ctaSpring = spring({
    frame,
    fps,
    config: { damping: 12, stiffness: 80 },
  });

  const ctaScale = interpolate(ctaSpring, [0, 1], [0.8, 1]);
  const ctaOpacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Contact info animation
  const contactOpacity = interpolate(frame, [20, 40], [0, 1], {
    extrapolateRight: "clamp",
  });

  const contactY = interpolate(frame, [20, 40], [30, 0], {
    extrapolateRight: "clamp",
  });

  // Website animation
  const websiteOpacity = interpolate(frame, [50, 70], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Pulse effect for CTA
  const pulseScale = 1 + Math.sin(frame / 8) * 0.02;

  // Background particles
  const particles = [...Array(15)].map((_, i) => ({
    x: (i * 7) % 100,
    y: (i * 11) % 100,
    size: 3 + (i % 3),
    speed: 0.5 + (i % 3) * 0.3,
  }));

  return (
    <AbsoluteFill
      style={{
        background:
          "linear-gradient(135deg, #0f172a 0%, #1e3a5f 50%, #0f172a 100%)",
        fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      {/* Animated particles */}
      {particles.map((particle, i) => (
        <div
          key={i}
          style={{
            position: "absolute",
            width: particle.size,
            height: particle.size,
            borderRadius: "50%",
            backgroundColor: i % 2 === 0 ? "#3b82f6" : "#22c55e",
            opacity: 0.3,
            left: `${particle.x}%`,
            top: `${(particle.y + frame * particle.speed) % 100}%`,
          }}
        />
      ))}

      {/* Radial glow */}
      <div
        style={{
          position: "absolute",
          width: 600,
          height: 600,
          background:
            "radial-gradient(circle, rgba(59, 130, 246, 0.2) 0%, transparent 70%)",
          borderRadius: "50%",
          transform: `scale(${pulseScale})`,
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
        {/* CTA Text */}
        <div
          style={{
            opacity: ctaOpacity,
            transform: `scale(${ctaScale})`,
            textAlign: "center",
          }}
        >
          <h2
            style={{
              fontSize: 72,
              fontWeight: 800,
              color: "#ffffff",
              margin: 0,
              textShadow: "0 0 60px rgba(59, 130, 246, 0.5)",
            }}
          >
            Let's Work Together
          </h2>
          <p
            style={{
              fontSize: 26,
              color: "#94a3b8",
              margin: "15px 0 0 0",
              letterSpacing: "2px",
            }}
          >
            Bringing your spatial vision to life
          </p>
        </div>

        {/* Contact Info Cards */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: 20,
            marginTop: 45,
            opacity: contactOpacity,
            transform: `translateY(${contactY}px)`,
          }}
        >
          {/* Email Card */}
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 20,
              background: "linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(59, 130, 246, 0.1))",
              border: "2px solid rgba(59, 130, 246, 0.4)",
              padding: "18px 35px",
              borderRadius: 16,
              boxShadow: "0 10px 40px rgba(59, 130, 246, 0.2)",
              transform: `scale(${pulseScale})`,
            }}
          >
            <svg
              width="32"
              height="32"
              viewBox="0 0 24 24"
              fill="none"
              stroke="#3b82f6"
              strokeWidth="2"
            >
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
              <polyline points="22,6 12,13 2,6" />
            </svg>
            <div style={{ display: "flex", flexDirection: "column" }}>
              <span
                style={{
                  fontSize: 14,
                  color: "#64748b",
                  letterSpacing: "1px",
                  textTransform: "uppercase",
                }}
              >
                Email
              </span>
              <span
                style={{
                  fontSize: 26,
                  fontWeight: 600,
                  color: "#ffffff",
                }}
              >
                eliasfundi6@gmail.com
              </span>
            </div>
          </div>

          {/* Phone/WhatsApp Card */}
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 20,
              background: "linear-gradient(135deg, rgba(34, 197, 94, 0.2), rgba(34, 197, 94, 0.1))",
              border: "2px solid rgba(34, 197, 94, 0.4)",
              padding: "18px 35px",
              borderRadius: 16,
              boxShadow: "0 10px 40px rgba(34, 197, 94, 0.2)",
              transform: `scale(${pulseScale})`,
            }}
          >
            <svg
              width="32"
              height="32"
              viewBox="0 0 24 24"
              fill="#22c55e"
            >
              <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" />
            </svg>
            <div style={{ display: "flex", flexDirection: "column" }}>
              <span
                style={{
                  fontSize: 14,
                  color: "#64748b",
                  letterSpacing: "1px",
                  textTransform: "uppercase",
                }}
              >
                WhatsApp / Call
              </span>
              <span
                style={{
                  fontSize: 26,
                  fontWeight: 600,
                  color: "#ffffff",
                }}
              >
                +254 792 201 418
              </span>
            </div>
          </div>
        </div>

        {/* Website URL */}
        <div
          style={{
            marginTop: 35,
            opacity: websiteOpacity,
            textAlign: "center",
          }}
        >
          <div
            style={{
              display: "inline-block",
              background: "rgba(255, 255, 255, 0.1)",
              padding: "12px 35px",
              borderRadius: 12,
              border: "1px solid rgba(255, 255, 255, 0.2)",
            }}
          >
            <span
              style={{
                fontSize: 22,
                color: "#ffffff",
                fontFamily: "monospace",
                letterSpacing: "1px",
              }}
            >
              eliasfundi.github.io/portfolio
            </span>
          </div>
        </div>
      </div>

      {/* Corner decorations */}
      <div
        style={{
          position: "absolute",
          top: 40,
          right: 40,
          width: 80,
          height: 80,
          borderRight: "3px solid #3b82f6",
          borderTop: "3px solid #3b82f6",
          opacity: ctaOpacity,
        }}
      />
      <div
        style={{
          position: "absolute",
          bottom: 40,
          left: 40,
          width: 80,
          height: 80,
          borderLeft: "3px solid #22c55e",
          borderBottom: "3px solid #22c55e",
          opacity: ctaOpacity,
        }}
      />
    </AbsoluteFill>
  );
};
