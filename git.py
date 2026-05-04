import os
from datetime import datetime, timedelta
import random

start_date = datetime(2024, 1, 1)
end_date = datetime(2026, 5, 1)

current = start_date

while current <= end_date:
    commits_per_day = random.randint(1, 4)

    for _ in range(commits_per_day):
        date_str = current.strftime("%Y-%m-%dT12:00:00")

        with open("file.txt", "a") as f:
            f.write(date_str + "\n")

        os.system("git add .")
        os.system(f'GIT_AUTHOR_DATE="{date_str}" GIT_COMMITTER_DATE="{date_str}" git commit -m "commit {current.strftime("%Y-%m-%d")}"')

    current += timedelta(days=1)
