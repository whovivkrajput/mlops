import logging
import sys , os
from datetime import datetime


LOG_DIR = "logs"

CURR_TIME_STAMP = f"logs{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"
LOG_FILE_NAME = f"logs{CURR_TIME_STAMP}.log"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)


logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode="w",
                    format="[%(asctime)s] %(name)s %(levelname)s - %(message)s",
                    level=logging.INFO
                    )