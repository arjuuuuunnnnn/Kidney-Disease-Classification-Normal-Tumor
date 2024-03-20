from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_training import Training
from src.cnnClassifier import logger


STAGE_NAME = "Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training.get_base_model()
        training.train_vaild_generator()
        training.train()


    if __name__ == "__main__":
        try:
            logger.info(f"STAGE >>>> {STAGE_NAME} started")
            obj = ModelTrainingPipeline()
            obj.main()
            logger.info(f"STAGE >>>> {STAGE_NAME} completed x=========x\n\n")

        except Exception as e:
            logger.exception(e)
            raise e
