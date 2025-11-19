from config.paths_config import CONFIG_PATH
from utils.common_functions import read_yaml


print(read_yaml(CONFIG_PATH)["data_ingestion"])