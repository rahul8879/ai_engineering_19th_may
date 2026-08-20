from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

RESUME_DIR = PROJECT_ROOT / "resume"

ENV_FILES = (
    PROJECT_ROOT / "ingestions" / ".env",
    PROJECT_ROOT / ".env",
)


def resolve_path(file_path: str | Path) -> Path:
    """Resolve a user-supplied path.

    Absolute paths are used as-is. A relative path is tried against the cwd
    first (so a path typed in a terminal still works), then against the
    project root (so "resume/foo.pdf" works from anywhere).
    """
    path = Path(file_path)
    if path.is_absolute():
        return path
    if path.exists():
        return path.resolve()
    return (PROJECT_ROOT / path).resolve()
