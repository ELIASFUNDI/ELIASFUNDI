import {
  AbsoluteFill,
  Img,
  interpolate,
  useCurrentFrame,
  spring,
  useVideoConfig,
  staticFile,
} from "remotion";

export const FieldWorkScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleOpacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: "clamp",
  });

  // First image animation (fieldwork)
  const image1Opacity = interpolate(frame, [10, 30], [0, 1], {
    extrapolateRight: "clamp",
  });

  const image1X = interpolate(frame, [10, 30], [-100, 0], {
    extrapolateRight: "clamp",
  });

  // Second image animation (graduation)
  const image2Opacity = interpolate(frame, [30, 50], [0, 1], {
    extrapolateRight: "clamp",
  });

  const image2X = interpolate(frame, [30, 50], [100, 0], {
    extrapolateRight: "clamp",
  });

  // Stats animation
  const statsOpacity = interpolate(frame, [50, 70], [0, 1], {
    extrapolateRight: "clamp",
  });

  const statsY = interpolate(frame, [50, 70], [30, 0], {
    extrapolateRight: "clamp",
  });

  // Counter animation for years
  const yearsCount = Math.min(
    Math.floor(interpolate(frame, [60, 90], [0, 3], { extrapolateRight: "clamp" })),
    3
  );

  const projectsCount = Math.min(
    Math.floor(interpolate(frame, [65, 95], [0, 50], { extrapolateRight: "clamp" })),
    50
  );

  return (
    <AbsoluteFill
      style={{
        background: "linear-gradient(135deg, #0f172a 0%, #1a1a2e 50%, #0f172a 100%)",
        fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        padding: 50,
      }}
    >
      {/* Background pattern */}
      <div
        style={{
          position: "absolute",
          width: "100%",
          height: "100%",
          backgroundImage: `radial-gradient(circle at 20% 50%, rgba(245, 158, 11, 0.1) 0%, transparent 50%),
                           radial-gradient(circle at 80% 50%, rgba(34, 197, 94, 0.1) 0%, transparent 50%)`,
        }}
      />

      {/* Title */}
      <div
        style={{
          opacity: titleOpacity,
          textAlign: "center",
          marginBottom: 40,
        }}
      >
        <h2
          style={{
            fontSize: 56,
            fontWeight: 700,
            color: "#ffffff",
            margin: 0,
          }}
        >
          Field Experience
        </h2>
        <div
          style={{
            width: 180,
            height: 4,
            background: "linear-gradient(90deg, #f59e0b, #22c55e)",
            margin: "15px auto",
            borderRadius: 2,
          }}
        />
      </div>

      {/* Images Row */}
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          gap: 50,
        }}
      >
        {/* Fieldwork Image */}
        <div
          style={{
            opacity: image1Opacity,
            transform: `translateX(${image1X}px)`,
          }}
        >
          <div
            style={{
              width: 380,
              height: 480,
              borderRadius: 20,
              overflow: "hidden",
              border: "3px solid #f59e0b",
              boxShadow: "0 20px 60px rgba(245, 158, 11, 0.3)",
              position: "relative",
            }}
          >
            <Img
              src={staticFile("fieldwork.jpg")}
              style={{
                width: "100%",
                height: "100%",
                objectFit: "cover",
              }}
            />
            {/* Label overlay */}
            <div
              style={{
                position: "absolute",
                bottom: 0,
                left: 0,
                right: 0,
                background: "linear-gradient(transparent, rgba(0,0,0,0.8))",
                padding: "40px 20px 20px",
              }}
            >
              <p
                style={{
                  color: "#ffffff",
                  fontSize: 20,
                  fontWeight: 600,
                  margin: 0,
                  textAlign: "center",
                }}
              >
                On-Site Survey Work
              </p>
            </div>
          </div>
        </div>

        {/* Stats in the middle */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: 30,
            opacity: statsOpacity,
            transform: `translateY(${statsY}px)`,
          }}
        >
          {/* Years Experience */}
          <div
            style={{
              background: "rgba(245, 158, 11, 0.1)",
              border: "2px solid rgba(245, 158, 11, 0.3)",
              borderRadius: 16,
              padding: "25px 40px",
              textAlign: "center",
            }}
          >
            <span
              style={{
                fontSize: 56,
                fontWeight: 800,
                color: "#f59e0b",
              }}
            >
              {yearsCount}+
            </span>
            <p
              style={{
                color: "#94a3b8",
                fontSize: 18,
                margin: "8px 0 0",
                letterSpacing: "1px",
              }}
            >
              Years Experience
            </p>
          </div>

          {/* Projects */}
          <div
            style={{
              background: "rgba(34, 197, 94, 0.1)",
              border: "2px solid rgba(34, 197, 94, 0.3)",
              borderRadius: 16,
              padding: "25px 40px",
              textAlign: "center",
            }}
          >
            <span
              style={{
                fontSize: 56,
                fontWeight: 800,
                color: "#22c55e",
              }}
            >
              {projectsCount}+
            </span>
            <p
              style={{
                color: "#94a3b8",
                fontSize: 18,
                margin: "8px 0 0",
                letterSpacing: "1px",
              }}
            >
              Projects Completed
            </p>
          </div>

          {/* Degree */}
          <div
            style={{
              background: "rgba(59, 130, 246, 0.1)",
              border: "2px solid rgba(59, 130, 246, 0.3)",
              borderRadius: 16,
              padding: "20px 30px",
              textAlign: "center",
            }}
          >
            <span
              style={{
                fontSize: 20,
                fontWeight: 600,
                color: "#3b82f6",
              }}
            >
              B.Sc. Geomatics Engineering
            </span>
            <p
              style={{
                color: "#94a3b8",
                fontSize: 14,
                margin: "5px 0 0",
              }}
            >
              Dedan Kimathi University
            </p>
          </div>
        </div>

        {/* Graduation Image */}
        <div
          style={{
            opacity: image2Opacity,
            transform: `translateX(${image2X}px)`,
          }}
        >
          <div
            style={{
              width: 380,
              height: 480,
              borderRadius: 20,
              overflow: "hidden",
              border: "3px solid #22c55e",
              boxShadow: "0 20px 60px rgba(34, 197, 94, 0.3)",
              position: "relative",
            }}
          >
            <Img
              src={staticFile("graduation.jpg")}
              style={{
                width: "100%",
                height: "100%",
                objectFit: "cover",
              }}
            />
            {/* Label overlay */}
            <div
              style={{
                position: "absolute",
                bottom: 0,
                left: 0,
                right: 0,
                background: "linear-gradient(transparent, rgba(0,0,0,0.8))",
                padding: "40px 20px 20px",
              }}
            >
              <p
                style={{
                  color: "#ffffff",
                  fontSize: 20,
                  fontWeight: 600,
                  margin: 0,
                  textAlign: "center",
                }}
              >
                Certified Professional
              </p>
            </div>
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
