import sys
from pathlib import Path

# Allow running this script directly (python scripts/test_ingestion.py) from
# any directory by putting the project root on sys.path.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ingestions.pipeline import ingest_resume

if __name__ == "__main__":
    file_path = "resume/Andrew_Green_Resume_27.pdf"
    nodes = ingest_resume(file_path)
    print(f"Processed nodes: {nodes}")
