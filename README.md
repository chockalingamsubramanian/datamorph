
<p align="center">
  <img src="datamorph.png" alt="DataMorph Logo" width="150"/>
</p>

<p align="center">
  <strong>Adaptive, LLM-native pipeline orchestrator</strong><br>
  Pipelines that change behavior based on data, context, or intent.
</p>


## 🚀 Features

- ⚙️ Declarative YAML pipeline configs
- 🧠 LangChain / OpenRouter integration for step inference
- 🧠 Simple context and memory simulation
- 🔁 Memory/context simulation (coming soon)
- 🖥️ CLI + optional Streamlit UI for visualization

---

## Run All Tests (with pytest)
pip install pytest
pytest datamorph/tests/

---

## 📦 Installation

```bash
pip install pydatamorph
datamorph run examples/simple_text_summarizer.yml
