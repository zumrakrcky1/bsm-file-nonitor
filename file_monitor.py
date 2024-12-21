import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

# İzlenecek dizin ve log dosyası
WATCH_DIR = "/home/kali/bsm/test"
LOG_FILE = "/home/kali/bsm/logs/changes.json"

class ChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        event_data = {
            "event_type": event.event_type,
            "file_path": event.src_path,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # JSON log dosyasına yaz
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'w') as f:
                json.dump([], f)

        with open(LOG_FILE, 'r+') as f:
            data = json.load(f)
            data.append(event_data)
            f.seek(0)
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    os.makedirs(WATCH_DIR, exist_ok=True)
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIR, recursive=True)
    observer.start()

    try:
        print(f"İzleme başladı: {WATCH_DIR}")
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
