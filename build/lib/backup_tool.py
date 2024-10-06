import os
import shutil
import time
import argparse

def backup_files(source,backup):
    if not os.path.exists(backup):
        os.makedirs(backup)

    for filename in os.listdir(source):
        source_file = os.path.join(source,filename)
        backup_file = os.path.join(backup,filename)

        if not os.path.exists(backup_file) or os.path.getmtime(source_file) > os.path.getmtime(backup_file):
            shutil.copy2(source_file,backup_file)
            print(f'Backed up:{filename}')
        else:
            print(f"Skipped:{filename} (No changes)")
def main() :
    parser= argparse.ArgumentParser(description='File Backup Tool')
    parser.add_argument('source', help='Source folder to backup')
    parser.add_argument('backup', help='Backup destination folder')

    args = parser.parse_args()
    backup_files(args.source,args.backup)
           