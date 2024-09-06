import logging
import os
from datetime import datetime

# Option 1 (Remove unnecessary backslashes)
LOG_File = datetime.now().strftime('%m_%d_%Y_%H_%M_%S') + ".log"

# Option 2 (Escape backslashes)
# LOG_File = f"{datetime.now().strftime('%m\%d\%Y\%H\%M\%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_File)

# Create directory conditionally (not using exist_ok for clarity)
if not os.path.exists(logs_path):
    os.makedirs(logs_path)  # Create directory structure if needed
else:
    print(f"Directory '{logs_path}' already exists.")

LOG_FILE_PATH = os.path.join(logs_path, LOG_File)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

