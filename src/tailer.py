import time
from src.parser import parse_log


def tail_file(filepath):
    with open(filepath, "r") as file:
        file.seek(0, 2)


        while True:
            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            parsed_data = parse_log(line.strip())

            print("\n========== NEW LOG ==========")
            print(line.strip())

            print("\nParsed Data:")
            print(parsed_data)