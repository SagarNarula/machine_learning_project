from tkinter import E
from housing.entity.config_entity import DataIngestionConfig,DataValidationConfig, \
DataTransformationConfig,ModelTrainingConfig,ModelEvaluatorConfig,ModelPusherConfig,TrainingPipelineConfig
from housing.util.util import read_yaml_file
from housing.constant import *
from housing.exception import HousingException
from housing.logger import logging
import sys,os
from housing.entity.artifact_entity import DataIngestionArtifact


class Configuration:


    def __init__(self,
    config_file_path:str=CONFIG_FILE_PATH,
    timestamp:str=CURRENT_TIME_STAMP
    )-> None:
        try:
            self.config_info=read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config=self.get_training_pipeline_config()
            self.time_stamp=timestamp
        except Exception as e:
            raise HousingException(e,sys) from e



        
    
    def get_data_ingestion_config(self) ->DataIngestionConfig:
        try:
            artifact_dir=self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir=os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR,self.time_stamp)

            data_ingestion_info=self.config_info[DATA_INGESTION_CONFIG_KEY]

            dataset_download_url=data_ingestion_info[DATA_INGESTION_DATASET_DOWNLOAD_URL_KEY]
            tgz_download_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY])
            raw_data_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_RAW_DATA_KEY])
            data_ingestion_dir=data_ingestion_info[DATA_INGESTION_DIR_KEY]
            ingested_train_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_dir,data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])
            ingested_test_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_dir,data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY])

            data_ingestion_config=DataIngestionConfig(
                                                      dataset_download_url=dataset_download_url,
                                                      tgz_download_dir=tgz_download_dir,
                                                      raw_data_dir=raw_data_dir,
                                                      ingested_train_dir=ingested_train_dir,
                                                      ingested_test_dir=ingested_test_dir
                                                      )
            
            logging.info(f"Data Ingestion config :{data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys) from e


    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            
            artifact_dir=self.training_pipeline_config.artifact_dir
            data_validation_artifact_dir=os.path.join(artifact_dir,DATA_VALIDATION_ARTIFACT_DIR_NAME,self.time_stamp)
            
            data_validation_info=self.config_info[DATA_VALIDATION_CONFIG_KEY]
            schema_dir=data_validation_info[DATA_VALIDATION_SCHEMA_DIR_KEY]
            schema_file_name=data_validation_info[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY]

            schema_file_path=os.path.join(ROOT_DIR,schema_dir,schema_file_name)

            report_file_path=os.path.join(data_validation_artifact_dir,data_validation_info[DATA_VALIDATION_REPORT_FILE_NAME_KEY])

            report_page_file_path=os.path.join(data_validation_artifact_dir,data_validation_info[DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY])



            data_validation_config=DataValidationConfig(schema_file_path=schema_file_path,report_file_path=report_file_path,
                                                        report_page_file_path=report_page_file_path)
            logging.info(f"Data Validation config :{data_validation_config}")
            return data_validation_config
        except Exception as e:
            raise HousingException(e,sys) from e



    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            artifact_dir=self.training_pipeline_config.artifact_dir
            data_transformation_artifact_dir=os.path.join(artifact_dir,DATA_TRANSFORMATION_ARTIFACT_DIR,self.time_stamp)

            data_transformation_info=self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]

            add_bedroom_per_room=data_transformation_info[DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM_KEY]

            preprocessed_object_file_path=os.path.join(data_transformation_artifact_dir,
                                                        data_transformation_info[DATA_TRANSFORMATION_PREPROCESING_DIR_NAME_KEY],
                                                        data_transformation_info[DATA_TRANFORMATION_PREPROCESSED_FILE_NAME_KEY])
            

            transformed_train_dir=os.path.join(data_transformation_artifact_dir,
                                                        data_transformation_info[DATA_TRANSFORMATION_TRANSFORMED_DIR_NAME_KEY],
                                                        data_transformation_info[DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY])
            
            transformed_test_dir=os.path.join(data_transformation_artifact_dir,
                                                        data_transformation_info[DATA_TRANSFORMATION_TRANSFORMED_DIR_NAME_KEY],
                                                        data_transformation_info[DATA_TRANSFORMATION_TEST_DIR_NAME_KEY])

            data_transformation_config=DataTransformationConfig(
                add_bedroom_per_room=add_bedroom_per_room,
                transformed_train_dir=transformed_train_dir,
                transformed_test_dir=transformed_test_dir,
                preprocessed_object_file_path=preprocessed_object_file_path)
            
            logging.info(f"Data transformation config {data_transformation_config}")

            return data_transformation_config

        except Exception as e:
            raise HousingException(e,sys) from e

    def get_model_trainer_config(self) -> ModelTrainingConfig:

        pass

    def get_model_evaluator_config(self) -> ModelEvaluatorConfig:
        pass

    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass

    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir=os.path.join(ROOT_DIR,training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])

            training_pipeline_config=TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training Pipeline config :{training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e


