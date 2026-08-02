from pathlib import Path

from file_operations import FileOperations


def test_copy_file(tmp_path):

    source = tmp_path / "test.txt"
    destination = tmp_path / "backup/test.txt"

    source.write_text(
        "Hello Backup",
        encoding="utf-8"
    )

    FileOperations.copy_file(
        source,
        destination
    )

    assert destination.exists()
    assert destination.read_text(
        encoding="utf-8"
    ) == "Hello Backup"


def test_delete_file(tmp_path):

    file = tmp_path / "delete.txt"

    file.write_text(
        "Delete me",
        encoding="utf-8"
    )

    FileOperations.delete_file(file)

    assert not file.exists()
