import requests

TEST_URL = "https://www.google.com"
TIMEOUT = 3

def check_internet() -> None:
    try:
        response = requests.get(TEST_URL, timeout=TIMEOUT)
        if response.status_code == 200:
            print('1')
        else:
            print('0')
    except Exception:
        write_result("0")

if __name__ == "__main__":
    check_internet()

