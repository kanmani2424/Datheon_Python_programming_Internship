import os
import shutil
from pathlib import Path

# Folder to organize
TARGET_FOLDER = Path.home() / "Downloads"

# File extension categories
EXTENSION_MAP = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".zip": "Archives",
    ".rar": "Archives",
    ".py": "Code",
    ".java": "Code",
    ".html": "Code",
    ".css": "Code",
}

def organize_files(folder):
    total_files = 0
    moved_files = 0
    errors = 0

    if not folder.exists():
        print("Folder not found!")
        return

    for file in folder.iterdir():

        # Skip folders
        if not file.is_file():
            continue

        # Skip this organizer script
        if file.name == "organizer.py":
            continue

        total_files += 1

        extension = file.suffix.lower()
        category = EXTENSION_MAP.get(
            extension, "Others"
        )

        destination_folder = folder / category

        try:
            destination_folder.mkdir(
                exist_ok=True
            )

            destination = destination_folder / file.name

            # Avoid overwriting existing files
            count = 1
            while destination.exists():
                destination = (
                    destination_folder
                    / f"{file.stem}_{count}{file.suffix}"
                )
                count += 1

            shutil.move(
                str(file),
                str(destination)
            )

            print(f"Moved: {file.name} -> {category}")
            moved_files += 1

        except (PermissionError, OSError) as error:
            print(f"Could not move {file.name}: {error}")
            errors += 1

    print("\n========== SUMMARY ==========")
    print(f"Total files scanned : {total_files}")
    print(f"Files moved        : {moved_files}")
    print(f"Errors             : {errors}")
    print("============================")

if __name__ == "__main__":
    organize_files(TARGET_FOLDER)
