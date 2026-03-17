import autocrop
import orientation_detection.predict_onnx as predict_onnx

def run_pipeline():
    # 1. Run Crop
    print("--- Starting Crop ---")
    autocrop.main(["-i", "pics", "-o", "pics/crop"])

    # 2. Run Rotate
    print("--- Starting Rotation ---")
    predict_onnx.main([
        "--input_path", "pics/crop",
        "--model_path", "orientation_model_v2_0.9882.onnx",
        "--output_path", "pics/final_output"
    ])

if __name__ == "__main__":
    run_pipeline()

