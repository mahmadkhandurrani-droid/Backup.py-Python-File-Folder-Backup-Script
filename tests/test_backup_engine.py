from backup_engine import BackupEngine


class DummyLogger:

    def info(self, message):
        pass


def test_backup_engine(tmp_path):

    source = tmp_path / "source"
    destination = tmp_path / "backup"

    source.mkdir()

    test_file = source / "data.txt"

    test_file.write_text(
        "Backup Test",
        encoding="utf-8"
    )

    config = {
        "source_folder": str(source),
        "destination": str(destination)
    }

    engine = BackupEngine(
        config=config,
        logger=DummyLogger()
    )

    engine.run()

    backup_file = destination / "data.txt"

    assert backup_file.exists()
