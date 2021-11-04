"""This script populates the database with all files in the folder indicated by the OUTPUT_FOLDER directory. 
"""
from pymongo import MongoClient
import json
from dateutil import parser
import os 
import time
import logging

logger = logging.getLogger(__name__)

def import_docs(mongo_host, mongo_port, output_dir):
    client = MongoClient(mongo_host, mongo_port)
    db = client.impact
    results = db.results

    impact_files = [f for f in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, f))]

    for filename in impact_files:
        with open(f"{output_dir}/{filename}", "r") as f:
            try:
                document = json.load(f)
                document["filename"] = filename

                # Remove this
                path_name = document["outputs"]["plot_file"]
                document["isotime"] = parser.isoparse(document["isotime"])
                
                if results.count_documents({"filename" : filename}) == 0:
                    results.insert_one(document)
                    logger.info("Processed %s.", filename)
                else:
                    logger.info("%s already processed.", filename)
            except:
                logger.exception("Error processing %s", filename)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

    MONGO_HOST = os.environ["MONGO_HOST"]
    MONGO_PORT = int(os.environ["MONGO_PORT"])
    OUTPUT_DIR = os.environ["OUTPUT_DIR"]
    import_docs(MONGO_HOST, MONGO_PORT, OUTPUT_DIR)


