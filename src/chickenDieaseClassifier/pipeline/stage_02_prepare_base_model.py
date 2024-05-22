from chickenDieaseClassifier.config.configuration import CongigurationManager
from chickenDieaseClassifier.components.prepare_base_model import PrepareBaseModel
from chickenDieaseClassifier import logger

STAGE_NAME = "Prepare Base Model"


class PrepareBaseModelPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = CongigurationManager()
        prepare_base_mode_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_mode_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e