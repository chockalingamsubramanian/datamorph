import streamlit as st
from datamorph.core.pipeline_loader import load_pipeline
from datamorph.core.executor import execute_pipeline

st.set_page_config(page_title="DataMorph UI", layout="wide")

st.title("📊 DataMorph Orchestrator")

uploaded_file = st.file_uploader("Upload a Pipeline YAML", type=["yml", "yaml"])

if uploaded_file is not None:
    st.success("Pipeline uploaded. Running...")
    # Save to a temporary file
    with open("temp_pipeline.yml", "wb") as f:
        f.write(uploaded_file.read())

    pipeline = load_pipeline("temp_pipeline.yml")
    execute_pipeline(pipeline)
