from text_summarizer.constants import *
from text_summarizer.utils.common import read_yaml,create_directories
from text_summarizer.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
            self,
            config_file_path: Path = CONFIG_FILE_PATH,
            params_file_path: Path = PARAMS_FILE_PATH
            ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion

        create_directories([config.root_dir])

        data_Ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_Ingestion_config