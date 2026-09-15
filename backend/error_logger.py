from datetime import datetime
import os


def log_errors(errors, file_path):
    if not errors:
        return

    with open(file_path, "a") as file:
        file.write("\n")
        file.write("Validation errors - " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        for error, count in errors.items():
            file.write(error + " : " + str(count) + "\n")


if __name__ == "__main__":
    log_file = "data/error_log.txt"

    test_errors = {
        "missing_values": 3,
        "invalid_age": 2,
        "invalid_interest_rate": 1
    }

    log_errors(test_errors, log_file)

    print("Errors logged successfully")