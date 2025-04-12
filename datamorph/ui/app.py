# Streamlit UI entry point
import streamlit as st
import yaml
from datamorph.core.pipeline_loader import load_pipeline
from datamorph.core.executor import execute_pipeline
from datamorph.ui.pipeline_utils import parse_yaml_steps

st.set_page_config(page_title="DataMorph UI", layout="wide")

st.markdown("<h1 style='text-align: center;'>🧠 DataMorph</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Adaptive pipelines powered by LLMs</p>", unsafe_allow_html=True)

st.sidebar.markdown("### ⚙️ Upload Pipeline Config")

uploaded_file = st.sidebar.file_uploader("Choose a YAML file", type=["yml", "yaml"])

if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")
    st.code(file_content, language="yaml")

    # Parse and preview steps
    steps = parse_yaml_steps(file_content)
    st.markdown("### 📋 Pipeline Preview")
    for i, step in enumerate(steps, 1):
        st.markdown(f"**Step {i}:** `{step.get('step')}` — Input: `{step.get('input')}`")

    if st.button("▶️ Run Pipeline"):
        #with open("temp_pipeline.yml", "w") as f:
        #    f.write(file_content)
        with open("temp_pipeline.yml", "w", encoding="utf-8") as f:
            f.write(file_content)

        st.success("Running pipeline...")
        pipeline = load_pipeline("temp_pipeline.yml")
        execute_pipeline(pipeline)

else:
    st.info("Upload a pipeline YAML file to get started.")
