import os
import urllib.request as request
import zipfile
from text_summarizer.logging import logger
from text_summarizer.utils.common import get_size
from text_summarizer.entity import DataIngestionConfig
from pathlib import Path
from text_summarizer.utils.common import get_size


class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            fileName, headers=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
        else:
            logger.info(f"File already present at {self.config.local_data_file}")

    def unzip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)