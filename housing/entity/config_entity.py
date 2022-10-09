from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])


DataValidationConfig=namedtuple("DataValidationConfig",["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room",
                                                                   "transformed_train_dir",
                                                                   "transformed_test_dir",
                                                                   "preprocessed_object_file_path"])

 ### preprocessed_object_file_path-- where you want to save your pickle file.


ModelTrainingConfig=namedtuple("ModelTrainingConfig",["trained_model_file_path","base_accuracy"])

### base_accuracy-- our model performance should be greater than our base_accuracy.
### trained_model_path--- path where our pickle will be saved

ModelEvaluatorConfig=namedtuple("ModelEvaluatorConfig",["model_evaluation_file_path","timestamp"])

## model_evaluation_file_path -- This file will contains information regarding all the models which are deployed to production.
## timestamp -- the timestamp at which we have perform our model evaluation.

ModelPusherConfig=namedtuple("ModelPusherConfig",["export_dir_path"])

TrainingPipelineConfig=namedtuple("TrainingPipelineConfig",["artifact_dir"])


