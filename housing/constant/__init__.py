import os
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()


ROOT_DIR=os.getcwd()
CONFIG_DIR="config"
CONFIG_FILE_NAME="config.yaml"

CONFIG_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

### TRAINING_PIPELINE_CONFIG_VARIABLES:

TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"

### DATA_INGESTION_CONFIG_VARIABLES:

DATA_INGESTION_CONFIG_KEY="data_ingestion_config"
DATA_INGESTION_DATASET_DOWNLOAD_URL_KEY="dataset_download_url"
DATA_INGESTION_RAW_DATA_KEY="raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY="tgz_download_dir"
DATA_INGESTION_DIR_KEY="ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY="ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY="ingested_test_dir"
DATA_INGESTION_ARTIFACT_DIR="data_ingestion"  ### use of this variable to store the output for data ingestion stage.

### DATA_VALIDATION_CONFIG_VARIABLES:

DATA_VALIDATION_CONFIG_KEY="data_validation_config"
DATA_VALIDATION_SCHEMA_DIR_KEY="schema_dir"
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY="schema_file_name"
DATA_VALIDATION_REPORT_FILE_NAME_KEY="report_file_name"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY="report_page_file_name"
DATA_VALIDATION_ARTIFACT_DIR_NAME="data_validation"