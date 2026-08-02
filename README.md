# Backup Utility — Intelligent File Backup System

# Description

Backup Utility is a modular Python automation project designed to create reliable backups of files and folders while following professional software engineering practices. The system automatically scans a source directory, preserves the original folder structure, copies files safely to a backup location, and records every operation through a logging system. It uses JSON-based configuration management, pathlib for modern path handling, and separated modules based on the Single Responsibility Principle. The project is designed to be easy to understand, maintain, test, and extend with future features such as scheduling, duplicate detection, database reports, and command-line support.

# Features

- Automatic file and folder backup
- Preserves directory structure
- JSON configuration support
- Professional logging system
- Modular architecture
- Error-safe file operations
- Uses "pathlib" for path management
- Uses "shutil.copy2()" to preserve file metadata
- Pytest test coverage

# Project Architecture

BackupUtility/
│
├── main.py                 # Application workflow
├── config.py               # Configuration loader
├── backup_engine.py        # Backup process controller
├── file_operations.py      # Copy and delete operations
├── logger.py               # Logging system
├── config.json             # Application settings
│
├── tests/
│   ├── test_config.py
│   ├── test_file_operations.py
│   └── test_backup_engine.py
│
└── README.md

# Workflow

main.py
    ↓
Load Configuration
    ↓
Create Logger
    ↓
Initialize Backup Engine
    ↓
Scan Source Folder
    ↓
Copy Files
    ↓
Log Operations
    ↓
Complete Backup

Installation

Clone the repository:

git clone YOUR_REPOSITORY_URL

Install requirements:

pip install pytest

Configuration

Example "config.json":

{
    "source_folder": "source",
    "destination": "backup",
    "log_file": "logs/backup.log"
}

# Usage

Run the application:

python main.py

# Run tests:

pytest
# Output 
================ test session starts ================
3 passed
================
# Engineering Concepts Used

- Modular programming
- Single Responsibility Principle
- Configuration management
- Logging
- Exception handling
- File system automation
- Unit testing with pytest

# Future Improvements

- Scheduled backups
- Incremental backups
- Duplicate file detection
- CSV backup reports
- Command-line interface using argparse
- Database backup history

# License

MIT License
