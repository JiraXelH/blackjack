import os
from typing import List
import cv2
import torch
from ultralytics import YOLO


class CardDetector:
    def __init__(self, model_path: str = os.path.join('models', 'cards_yolo.pt')):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YOLO(model_path)
        self.model.to(self.device)

    def detect_cards(self, image, confidence: float = 0.7) -> List[str]:
        """Detect playing cards in an image.

        Args:
            image: OpenCV image (numpy array) or path to an image file.
            confidence: Minimum confidence threshold for detections.

        Returns:
            List of detected card names.
        """
        if isinstance(image, str):
            if not os.path.exists(image):
                raise FileNotFoundError(f"Image not found: {image}")
            image = cv2.imread(image)

        results = self.model(image)[0]
        detections = []
        for box in results.boxes:
            if box.conf < confidence:
                continue
            cls_idx = int(box.cls)
            if 0 <= cls_idx < len(results.names):
                detections.append(results.names[cls_idx])
        return detections


if __name__ == '__main__':
    detector = CardDetector()
    sample_path = os.path.join('data', 'images', 'test.jpg')
    if os.path.exists(sample_path):
        img = cv2.imread(sample_path)
        detected_cards = detector.detect_cards(img)
        print('Detected cards:', detected_cards)
    else:
        print(f'Sample image not found at {sample_path}')
