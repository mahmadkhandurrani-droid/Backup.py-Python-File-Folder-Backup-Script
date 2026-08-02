from config import load_config
from logger import setup_logger
from backup_engine import BackupEngine


def main():
    config = load_config("config.json")

    logger = setup_logger(config["log_file"])

    backup_engine = BackupEngine(
        config=config,
        logger=logger
    )

    backup_engine.run()


if __name__ == "__main__":
    main()
