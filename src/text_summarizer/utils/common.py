import os
from box.exceptions import BoxValueError
import yaml
from text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(yaml_path: Path) -> ConfigBox:
    
    try:
        with open(yaml_path, 'r') as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"Loaded yaml file from {yaml_path}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Error in yaml file {yaml_path}")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory {path}")


@ensure_annotations
def get_size(path:Path) -> str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"