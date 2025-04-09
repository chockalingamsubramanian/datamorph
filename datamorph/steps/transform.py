# Simulates a data transformation step
import os

def transform_data(input_path):
    try:
        with open(input_path, "r") as f:
            lines = f.readlines()

        # Simulated transformation: uppercase each line
        transformed = [line.upper() for line in lines]

        output_path = os.path.splitext(input_path)[0] + "_transformed.txt"
        with open(output_path, "w") as f:
            f.writelines(transformed)

        print(f"🔁 Transformed data written to: {output_path}\n")
        return {"output_path": output_path}

    except Exception as e:
        print(f"[❌] Failed to transform data: {e}")
        return {"error": str(e)}
