# File Backup Tool

This is a simple command-line tool for backing up files from a source directory to a backup directory. It supports features like skipping files that haven't changed and handling permission issues gracefully.

## Features
- Back up files from a source directory to a specified backup location.
- Optionally compress the files.
- Skip files that have not changed since the last backup.
- Detect permission issues and skip directories/files that cannot be accessed.
- Ability to automate backups via scripting or scheduled tasks.

## Requirements

- Python 3.7+
- `shutil` (comes with Python standard library)
- `os` (comes with Python standard library)

## Installation

Clone the repository or download the files into your local environment.

```bash
git clone <repository_url>

Once you've done it all you can use it using this command

python file_backup_tool.py <source_directory> <backup_directory>
