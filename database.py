import time
import subprocess
from config import read_config

config = read_config()


def sync_db():
    path = config.get("database", "path")
    db_copy_path = config.get("database", "db_copy_path")
    subprocess.run(["bash", "./scripts/resync.command", path, db_copy_path])
    print("Syncing database")
    time.sleep(1)
    print("Database synced")
