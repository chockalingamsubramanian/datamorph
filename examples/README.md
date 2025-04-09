# Example Pipelines – DataMorph

This folder contains ready-to-run pipeline examples to help you explore the capabilities of DataMorph.

---

## Available Pipelines

| File                        | Description                                                  |
|-----------------------------|--------------------------------------------------------------|
| `simple_text_summarizer.yml`   | Summarizes the contents of a local text file               |
| `adaptive_branching.yml`       | Uses LLM to suggest next steps dynamically                |
| `s3_ingest_and_transform.yml`  | Simulates S3 download + transformation                    |
| `text_to_dynamo.yml`           | Summarizes text and writes the result to DynamoDB         |

---

## Sample Data

The pipelines expect a test file at:  
 `data/sample.txt`

Use this as a mock input or replace with real data to test behaviors.

---

## Running a Pipeline

```bash
datamorph run examples/simple_text_summarizer.yml


--

launch the UI:
in bash, streamlit run ui/app.py
