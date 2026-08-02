import shutil
from pathlib import Path


class FileOperations:

    @staticmethod
    def copy_file(source, destination):

        destination = Path(destination)

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy2(
            source,
            destination
        )


    @staticmethod
    def delete_file(file_path):

        file_path = Path(file_path)

        if file_path.exists():
            file_path.unlink()
