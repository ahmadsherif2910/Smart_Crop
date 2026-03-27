from pathlib import Path

import autocrop
import orientation_detection.predict_onnx as predict_onnx

def run_pipeline(input_path =".",model_path="orientation_model_v2_0.9882.onnx",black_bg=False):
    print("--- Starting Crop ---")
    autocrop.run_crop(input_path=input_path,black_bg=black_bg)
    print("--- Starting Rotation ---")
    input_path = Path(input_path)
    input_path = input_path.parent if input_path.is_file() else input_path
    predict_onnx.run_prediction_onnx(input_path=f"{input_path}/crop",output_path=f"{input_path}/rotated",model_path=model_path)

if __name__ == "__main__":
    run_pipeline("pics/dark",black_bg=True)

