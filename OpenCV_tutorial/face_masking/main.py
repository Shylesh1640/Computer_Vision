from pathlib import Path
import time
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "face.jpg"
MODEL_PATH = BASE_DIR / "blaze_face_short_range.tflite"
MODEL_URL = (
    "https://storage.googleapis.com/mediapipe-models/face_detector/"
    "blaze_face_short_range/float16/latest/blaze_face_short_range.tflite"
)


if not MODEL_PATH.exists():
    raise FileNotFoundError(
        "Missing model file. Download it and place it here:\n"
        f"{MODEL_PATH}\n"
        f"Model URL: {MODEL_URL}"
    )


def clamp_bbox(bbox, width: int, height: int):
    x1 = max(0, int(bbox.origin_x))
    y1 = max(0, int(bbox.origin_y))
    x2 = min(width, int(bbox.origin_x + bbox.width))
    y2 = min(height, int(bbox.origin_y + bbox.height))
    if x2 <= x1 or y2 <= y1:
        return None
    return x1, y1, x2, y2


def blur_faces_in_frame(frame, detections):
    output = frame.copy()
    frame_h, frame_w = output.shape[:2]

    for detection in detections:
        box = clamp_bbox(detection.bounding_box, frame_w, frame_h)
        if box is None:
            continue
        x1, y1, x2, y2 = box

        face_region = output[y1:y2, x1:x2]
        if face_region.size == 0:
            continue

        # Ensure odd kernel dimensions and avoid tiny-region blur errors.
        kx = max(3, (face_region.shape[1] // 3) | 1)
        ky = max(3, (face_region.shape[0] // 3) | 1)
        blurred_face = cv2.GaussianBlur(face_region, (kx, ky), 0)
        output[y1:y2, x1:x2] = blurred_face

        cv2.rectangle(output, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return output


def create_detector(running_mode):
    base_options = python.BaseOptions(model_asset_path=str(MODEL_PATH))
    options = vision.FaceDetectorOptions(
        base_options=base_options,
        min_detection_confidence=0.5,
        running_mode=running_mode,
    )
    return vision.FaceDetector.create_from_options(options)


def process_image(image_path: Path):
    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    bgr_image = cv2.imread(str(image_path))
    if bgr_image is None:
        raise RuntimeError(f"Could not load image: {image_path}")

    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)

    with create_detector(vision.RunningMode.IMAGE) as detector:
        result = detector.detect(mp_image)

    annotated_image = blur_faces_in_frame(bgr_image, result.detections)
    cv2.imwrite(str(BASE_DIR / "annotated_face.jpg"), annotated_image)
    cv2.imshow("Face Detection", annotated_image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


def process_webcam(camera_index: int = 0):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam. Check camera index and permissions.")

    with create_detector(vision.RunningMode.VIDEO) as detector:
        while True:
            success, frame = cap.read()
            if not success:
                print("Skipping empty camera frame.")
                continue

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            timestamp_ms = int(time.time() * 1000)
            result = detector.detect_for_video(mp_frame, timestamp_ms)

            annotated_frame = blur_faces_in_frame(frame, result.detections)
            cv2.imshow("Face Masking Webcam", annotated_frame)

            # Press q to exit.
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    process_image(IMAGE_PATH)
    process_webcam(0)

