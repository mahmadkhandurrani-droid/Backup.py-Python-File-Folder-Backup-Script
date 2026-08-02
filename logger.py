import logging
from pathlib import Path


def setup_logger(log_file):

    log_path = Path(log_file)

    log_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    logger = logging.getLogger(
        "BackupUtility"
    )

    logger.setLevel(
        logging.INFO
    )

    handler = logging.FileHandler(
        log_path,
        encoding="utf-8"
    )

    logger.addHandler(handler)

    return logger
