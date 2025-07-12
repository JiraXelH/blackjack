from ultralytics import YOLO
import os
import shutil


def main():
    # Load the pre-trained YOLOv8 nano model
    model = YOLO('yolov8n.pt')

    # Path to data configuration
    data_config = os.path.join('data', 'data.yaml')

    # Train the model for 100 epochs using the dataset configuration
    model.train(data=data_config, epochs=100)

    # Path to the best weights produced by training
    best_model = os.path.join(model.trainer.save_dir, 'weights', 'best.pt')
    target_path = os.path.join('models', 'cards_yolo.pt')

    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    shutil.move(best_model, target_path)
    print(f"Model saved to {target_path}")


if __name__ == '__main__':
    main()
