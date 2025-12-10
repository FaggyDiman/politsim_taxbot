import requests  # почему: удобнее и чище, чем urllib

RESULT_FILE = "results.txt"
TEST_URL = "https://www.google.com"
TIMEOUT = 3


def write_result(value: str) -> None:
    with open(RESULT_FILE, "w", encoding="utf-8") as file:
        file.write(value)


def check_internet() -> None:
    try:
        response = requests.get(TEST_URL, timeout=TIMEOUT)
        if response.status_code == 200:
            write_result("1")
        else:
            write_result("0")
    except Exception:
        write_result("0")

if __name__ == "__main__":
    check_internet()

