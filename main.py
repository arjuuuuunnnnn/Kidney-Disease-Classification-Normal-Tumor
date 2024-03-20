from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"STAGE >>>> {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed x==========x\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"STAGE >>>> {STAGE_NAME} started")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"STAGE >>>> {STAGE_NAME} completed x==========x\n\n")
except Exception as e:
    logger.exception(e)
    raise e
