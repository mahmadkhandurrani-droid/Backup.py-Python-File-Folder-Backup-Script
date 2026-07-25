Smart File Organizer Pro

Overview

Smart File Organizer Pro is a modular Python automation project that automatically organizes files into categorized folders based on their file extensions. The project follows software engineering best practices, including object-oriented programming, composition, modular architecture, JSON configuration, logging, exception handling, and automated reporting.

Features

- Automatically scans a source folder
- Organizes files into categories based on extensions
- Uses a configurable "config.json" file
- Creates destination folders automatically
- Prevents duplicate filenames
- Creates backups before moving files
- Generates a CSV report of all processed files
- Logs successful operations and errors
- Built with "pathlib" for modern file handling
- Modular and maintainable project structure

Project Structure

Smart_File_Organizer_Pro/
│── main.py
│── organizer.py
│── logger.py
│── config_loader.py
│── duplicate_handler.py
│── backup_manager.py
│── csv_report.py
│── config.json
│── README.md

Technologies Used

- Python 3
- pathlib
- shutil
- json
- csv
- logging

Software Engineering Concepts

- Object-Oriented Programming (OOP)
- Composition
- Single Responsibility Principle (SRP)
- Modular Design
- Exception Handling
- Clean Code Practices

How to Run

1. Clone this repository.
2. Update "config.json" with your source folder and categories.
3. Run:

python main.py

Learning Objectives

This project was developed to strengthen Python automation, software engineering principles, modular programming, and clean project architecture.

License

MIT License
