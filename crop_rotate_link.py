import autocrop
import orientation_detection.predict_onnx as predict_onnx
from pathlib import Path

def run_pipeline(input_path,model_path="orientation_model_v2_0.9882.onnx"):
    path = Path(input_path)
    # 1. Run Crop
    print("--- Starting Crop ---")
    if path.is_file():
        autocrop.main(["-s","-i", f"{path}", "-o", f"{path.parent}/crop"])
    else:
        autocrop.main(["-i", f"{path}", "-o", f"{path}/crop"])

    # 2. Run Rotate
    print("--- Starting Rotation ---")
    predict_onnx.main([
        "--input_path", f"{path}/crop",
        "--model_path", f"{model_path}",
        "--output_path", f"{path}/final_output"
    ])

if __name__ == "__main__":
    # run_pipeline(input_path='pics/Scan_20260316 (2).jpg')
    run_pipeline(input_path='pics')

