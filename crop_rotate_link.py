import autocrop
import orientation_detection.predict_onnx as predict_onnx
from pathlib import Path

def run_pipeline(input_path,model_path="orientation_model_v2_0.9882.onnx"):
    print("--- Starting Crop ---")
    autocrop.run_crop(input_path=input_path)
    print("--- Starting Rotation ---")
    predict_onnx.run_prediction_onnx(input_path=f"{input_path}/crop",output_path=f"{input_path}/rotated",model_path=model_path)
if __name__ == "__main__":
    run_pipeline(input_path='pics')

