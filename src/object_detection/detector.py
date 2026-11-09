"""Live object detection using Ultralytics YOLO and OpenCV."""
import time

import cv2
from ultralytics import YOLO

from .config import (
    CAMERA_INDEX, CONFIDENCE_THRESHOLD, FRAME_HEIGHT, FRAME_WIDTH,
    IMAGE_SIZE, MODEL_PATH, WINDOW_NAME,
)


def calculate_fps(previous_time: float, current_time: float,
                  previous_fps: float = 0.0) -> tuple[float, float]:
    """Return smoothed FPS and elapsed time."""
    elapsed = current_time - previous_time
    if elapsed <= 0:
        return previous_fps, elapsed
    current_fps = 1.0 / elapsed
    smoothed = current_fps if previous_fps <= 0 else (
        0.8 * previous_fps + 0.2 * current_fps
    )
    return smoothed, elapsed


def is_quit_key(key: int) -> bool:
    """Check whether Q or ESC was pressed."""
    return key in (ord("q"), ord("Q"), 27)


def main() -> None:
    """Run YOLO detection on frames captured from the webcam."""
    camera = None
    try:
        print(f"Loading AI model: {MODEL_PATH}")
        model = YOLO(MODEL_PATH)

        camera = cv2.VideoCapture(CAMERA_INDEX)
        if not camera.isOpened():
            raise RuntimeError(
                "Unable to open the camera. Check the connection or "
                "change CAMERA_INDEX in config.py."
            )

        camera.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
        print("AI detection started. Press Q or ESC to quit.")

        previous_time = time.perf_counter()
        fps = 0.0

        while True:
            success, frame = camera.read()
            if not success:
                print("Unable to read a frame from the camera.")
                break

            results = model.predict(
                source=frame,
                conf=CONFIDENCE_THRESHOLD,
                imgsz=IMAGE_SIZE,
                verbose=False,
            )
            result = results[0]
            annotated_frame = result.plot()
            object_count = len(result.boxes)

            current_time = time.perf_counter()
            fps, _ = calculate_fps(previous_time, current_time, fps)
            previous_time = current_time

            cv2.putText(
                annotated_frame, f"Objects detected: {object_count}",
                (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
            )
            cv2.putText(
                annotated_frame, f"FPS: {fps:.1f}",
                (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2,
            )
            cv2.imshow(WINDOW_NAME, annotated_frame)

            key = cv2.waitKey(1) & 0xFF
            if is_quit_key(key):
                break

    except KeyboardInterrupt:
        print("\nDetection interrupted by user.")
    except Exception as error:
        print(f"Error: {error}")
    finally:
        if camera is not None:
            camera.release()
        cv2.destroyAllWindows()
        print("Camera released. Program closed.")


if __name__ == "__main__":
    main()
