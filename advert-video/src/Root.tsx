import { Composition } from "remotion";
import { AdvertVideo } from "./AdvertVideo";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="AdvertVideo"
        component={AdvertVideo}
        durationInFrames={570}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="AdvertVideoVertical"
        component={AdvertVideo}
        durationInFrames={570}
        fps={30}
        width={1080}
        height={1920}
      />
    </>
  );
};
