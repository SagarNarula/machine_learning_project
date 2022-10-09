from housing.exception import HousingException
import yaml
import sys,os

def read_yaml_file(file_path:str)->dict:
    """
    Read a yaml file and return the content as a dictionary
    file_path->str
    """
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e