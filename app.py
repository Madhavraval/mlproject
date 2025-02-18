from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngenstion
from src.mlproject.components.data_ingestion import DataIngestionConfig




if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion_config=DataIngenstionConfig()
        data_ingestion=DataIngenstion()
        data_ingestion.initiate_data_ingenstion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)