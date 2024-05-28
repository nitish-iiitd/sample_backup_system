# backup.py

import time

def main(username: str):
    print(f"Starting backup for user: {username}")
    time.sleep(15)
    print(f"Backup completed for user: {username}")

if __name__ == "__main__":
    username = "test_user"  # Example username for direct execution
    main(username)
