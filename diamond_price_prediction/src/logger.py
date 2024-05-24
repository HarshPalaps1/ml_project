import logging
import os
from datetime import datetime

#What info log file should contain about output
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 
#path where logs folder will be created and which have name in LOG_FILE  will be created
logs_paths=os.path.join(os.getcwd(),"logs",LOG_FILE)
#below line will cheak file of  present log is  exist or not if not then create it
os.makedirs(logs_paths,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_paths,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)