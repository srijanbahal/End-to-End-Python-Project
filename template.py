import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name= "mlProject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__inti__.py",
    f"{project_name}/componenets/data_ingestion.py",
    f"{project_name}/componenets/data_transformation.py",
    f"{project_name}/componenets/model_trainer.py",
    f"{project_name}/componenets/model_monitering.py",
    f"{project_name}/piplines/__init__.py",
    f"{project_name}/piplines/training_pipline.py",
    f"{project_name}/piplines/prediction.py",
    f"{project_name}/execution.py",
    f"{project_name}/logger.py",
    f"{project_name}/utils.py",
    "app.py",
    "setup.py",
    "DockerFile",
    "requirements.txt",
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Created Empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}") 
