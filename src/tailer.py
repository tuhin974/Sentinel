import time
from pathlib import Path


class LogTailer:
    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def follow(self):
        while not self.file_path.exists():
            print(f"Waiting for {self.file_path}")
            time.sleep(1)

        print(f"Monitoring: {self.file_path}")

        last_position = self.file_path.stat().st_size

        while True:
            with self.file_path.open("r", encoding="utf-8") as file:
                file.seek(last_position)

                new_lines = file.readlines()

                if new_lines:
                    for line in new_lines:
                        yield line.strip()

                    last_position = file.tell()

            time.sleep(0.5)