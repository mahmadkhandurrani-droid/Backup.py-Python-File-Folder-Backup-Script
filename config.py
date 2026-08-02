import json
from pathlib import Path


def load_config(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    with path.open("r", encoding="utf-8") as file:
        config = json.load(file)

    return config
