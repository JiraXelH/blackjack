import time
from screen_capture import get_screenshot
from card_detector import CardDetector


def main():
    detector = CardDetector()
    try:
        while True:
            image = get_screenshot()
            cards = detector.detect_cards(image)
            if cards:
                print('Detected cards:', cards)
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nStopping card detection.")


if __name__ == '__main__':
    main()
