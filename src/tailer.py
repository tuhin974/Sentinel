import time

def tail_file(filepath):
    with open(filepath, "r") as file:
        file.seek(0, 2)

        while True:
            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            yield line.strip()