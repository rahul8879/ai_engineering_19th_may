from ingestions.pipeline import ingest_resume

if __name__ == "__main__":
    file_path ="resume/Andrew_Green_Resume_27.pdf"
    nodes = ingest_resume(file_path)
    print(f"Processed nodes: {nodes}")