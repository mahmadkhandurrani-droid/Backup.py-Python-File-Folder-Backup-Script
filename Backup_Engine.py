from pathlib import Path
from file_operations import FileOperations


class BackupEngine:

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

        self.source = Path(config["source_folder"])
        self.destination = Path(config["destination"])


    def run(self):

        self.logger.info("Backup started")

        self.source.mkdir(
            parents=True,
            exist_ok=True
        )

        self.destination.mkdir(
            parents=True,
            exist_ok=True
        )

        for file in self.source.rglob("*"):

            if file.is_file():

                relative_path = file.relative_to(
                    self.source
                )

                backup_path = self.destination / relative_path

                FileOperations.copy_file(
                    file,
                    backup_path
                )

                self.logger.info(
                    f"Backed up: {file.name}"
                )

        self.logger.info("Backup completed")
