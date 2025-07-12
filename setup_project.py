import os

PROJECT_STRUCTURE = {
    "data": {
        "images": {},
        "labels": {},
        "data.yaml": None,
    },
    "models": {
        "cards_yolo.pt": None,
    },
    "screenshots": {},
    "screen_capture.py": None,
    "card_detector.py": None,
    "train.py": None,
    "main.py": None,
    "gui_overlay.py": None,
    "card_counter.py": None,
    "requirements.txt": None,
    "README.md": None,
}

BASE_DIR = "Blackjack-CardCounter"


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            if not os.path.isdir(path):
                os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            if not os.path.exists(path):
                open(path, "w").close()


def main():
    if not os.path.isdir(BASE_DIR):
        os.makedirs(BASE_DIR)
    create_structure(BASE_DIR, PROJECT_STRUCTURE)


if __name__ == "__main__":
    main()
