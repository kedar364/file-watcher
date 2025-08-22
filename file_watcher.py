import time
import os

FOLDER_TO_WATCH = "watched_folder"

def get_files_snapshot(folder):
    return {f: os.stat(os.path.join(folder, f)).st_mtime for f in os.listdir(folder)}

def main():
    if not os.path.exists(FOLDER_TO_WATCH):
        os.mkdir(FOLDER_TO_WATCH)

    print(f"Monitoring folder: {FOLDER_TO_WATCH}")
    previous = get_files_snapshot(FOLDER_TO_WATCH)

    while True:
        time.sleep(2)
        current = get_files_snapshot(FOLDER_TO_WATCH)

        added = set(current.keys()) - set(previous.keys())
        removed = set(previous.keys()) - set(current.keys())
        modified = {f for f in current if f in previous and current[f] != previous[f]}

        for f in added:
            print(f"🟢 Added: {f}")
        for f in removed:
            print(f"🔴 Removed: {f}")
        for f in modified:
            print(f"🟡 Modified: {f}")

        previous = current

if __name__ == "__main__":
    main()
