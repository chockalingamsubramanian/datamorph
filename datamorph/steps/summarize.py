# Summarizes input text from a file
def summarize_text(input_path):
    try:
        with open(input_path, "r") as f:
            content = f.read()

        # Naive summarizer: first 2 lines as summary
        summary = "\n".join(content.splitlines()[:2])
        print(f"📝 Summary:\n{summary}\n")
        return {"summary": summary}

    except Exception as e:
        print(f"[❌] Failed to summarize text: {e}")
        return {"error": str(e)}
