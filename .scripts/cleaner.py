import os
import shutil
from pathlib import Path

# Define the path to your Downloads folder
downloads_path = Path.home() / "Downloads"

# Map file extensions to their new destination folders
FOLDERS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
}

print("Starting Downloads folder cleanup...")
moved_count = 0

# Loop through every item inside the Downloads folder
for item in downloads_path.iterdir():
    # Skip directories (folders) and hidden system files
    if item.is_dir() or item.name.startswith("."):
        continue
        
    # Get the file extension in lowercase
    file_ext = item.suffix.lower()
    
    # Check which category matches the file extension
    for folder_name, extensions in FOLDERS.items():
        if file_ext in extensions:
            # Create the destination folder if it doesn't exist yet
            destination_dir = downloads_path / folder_name
            destination_dir.mkdir(exist_ok=True)
            
            # Move the file into its new folder
            shutil.move(str(item), str(destination_dir / item.name))
            print(f"Moved: {item.name} -> {folder_name}/")
            moved_count += 1
            break

print(f"Cleanup finished! Total files organized: {moved_count}")

import os
import shutil
from pathlib import Path

downloads_path = Path.home() / "Downloads"

# Expanded Categories (Added Code, Installers, and Ebooks)
FOLDERS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Code": [".py", ".html", ".css", ".js", ".sh", ".json"],
    "Installers": [".dmg", ".pkg", ".app"],
    "Ebooks": [".epub", ".mobi", ".pdf"]
}

print("Starting smart cleanup...")
moved_count = 0

for item in downloads_path.iterdir():
    # Skip folders and hidden system files, AND protect our script if it's in Downloads
    if item.is_dir() or item.name.startswith(".") or item.name == "cleaner.py":
        continue
        
    file_ext = item.suffix.lower()
    
    for folder_name, extensions in FOLDERS.items():
        if file_ext in extensions:
            destination_dir = downloads_path / folder_name
            destination_dir.mkdir(exist_ok=True)
            
            target_path = destination_dir / item.name
            
            # Conflict Protection: If a file with that name exists, rename the new one safely
            if target_path.exists():
                base, ext = os.path.splitext(item.name)
                counter = 1
                while target_path.exists():
                    new_name = f"{base}_{counter}{ext}"
                    target_path = destination_dir / new_name
                    counter += 1
                print(f"Name conflict resolved! Renamed to: {target_path.name}")

            shutil.move(str(item), str(target_path))
            print(f"Moved: {item.name} -> {folder_name}/")
            moved_count += 1
            break

print(f"Cleanup finished! Total files organized: {moved_count}")


