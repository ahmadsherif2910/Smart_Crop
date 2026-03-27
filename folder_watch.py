import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import crop_rotate_link

class ImageDetectorHandler(FileSystemEventHandler):
    def __init__(self, black_bg=False):
        super().__init__()
        self.black_bg = black_bg
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = Path(event.src_path)
        valid_extensions = {'.bmp', '.tiff', '.tif', '.jpg', '.jpeg', '.png'}

        if file_path.suffix.lower() in valid_extensions:
            print(f"📸 image detected: {file_path.name}",file_path)
            crop_rotate_link.run_pipeline(file_path,black_bg=self.black_bg)


def start_monitoring(path_to_watch=".",black_bg=False):
    """Configures and runs the watchdog observer."""
    event_handler = ImageDetectorHandler(black_bg=black_bg)
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=False)

    print(f"Watching: {Path(path_to_watch).absolute()}")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopping...")

    observer.join()

def folder_watch(path,toggle = False,black_bg=False):
    if toggle:
        start_monitoring(path,black_bg)
    else:
        crop_rotate_link.run_pipeline(path,black_bg=black_bg)



if __name__ == "__main__":
    folder_watch("pics/dark",True,black_bg=True)