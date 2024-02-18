import logger
import os
from datetime import datetime

# Naming convention to store the .log files 
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# Create path where the .log file will be stored.
log_path  = os.path.join(os.getcwd(), "logs")

# make directory if not exist 
os.makedirs(log_path, exist_ok=True)

# Create final path where the .log file will be stored 
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logger.basicConfig(
    level = logger.INFO,
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

