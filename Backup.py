print("Hello, World!")
# Backup.py
# A Python script to safely back up files from a source folder to a destination folder
# with timestamped folders, logging, and error handling

# Date: 22 March 2026

import os
import shutil
from datetime import datetime

# --- Function: Logging ---
def log_backup(message, log_file):
    """Write a message to the log file"""
    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

# --- Function: Backup Folder ---
def backup_folder(src_folder, dest_folder):
    """
    Copy all files from src_folder to dest_folder.
    Create a timestamped backup folder.
    Logs each file backed up and errors.
    """
    if not os.path.exists(src_folder):
        print(f"Source folder '{src_folder}' does not exist!")
        return
    
    # Create timestamped backup folder
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = os.path.join(dest_folder, f"Backup_{timestamp}")
    os.makedirs(backup_path, exist_ok=True)

    # Log file path
    log_file = os.path.join(backup_path, "log.txt")
    
    # Backup files
    for item in os.listdir(src_folder):
        src_item = os.path.join(src_folder, item)
        dest_item = os.path.join(backup_path, item)
        try:
            if os.path.isfile(src_item):
                shutil.copy2(src_item, dest_item)
                print(f"Backed up: {item}")
                log_backup(f"Backed up file: {item}", log_file)
            elif os.path.isdir(src_item):
                shutil.copytree(src_item, dest_item)
                print(f"Backed up folder: {item}")
                log_backup(f"Backed up folder: {item}", log_file)
        except Exception as e:
            print(f"Error backing up {item}: {e}")
            log_backup(f"Error backing up {item}: {e}", log_file)

    print(f"\nBackup completed successfully at '{backup_path}'")
    log_backup("Backup completed successfully.", log_file)

# --- Main function ---
def main():
    print("=== Backup Script ===")
    src = input("Enter the path of the folder to back up: ").strip()
    dest = input("Enter the destination folder for backup: ").strip()
    backup_folder(src, dest)

# Run only if script executed directly
if __name__ == "__main__":
    main()
