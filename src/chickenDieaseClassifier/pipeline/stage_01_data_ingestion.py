from chickenDieaseClassifier.config.configuration import ConfigurationManager
from chickenDieaseClassifier.components.data_ingestion import DataIngestion
from chickenDieaseClassifier import logger

STAGE_NAME = "Data Ingestion"


class DataIngestionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_inegstion_config = config.get_data_ingestion_configuration()
        data_ingestion = DataIngestion(config=data_inegstion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
