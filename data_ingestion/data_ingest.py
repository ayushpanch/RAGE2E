""" ingesting the data into vector database """
from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd
from data_ingestion.data_transform import data_convertor

load_dotenv()

class ingest_data:

    def __init__(self):
        print("this is initialisation class of data_ingest class")
        pass

    def ingest_data(self):
        pass


if __name__ == "__main__":
    obj_data_ingest = ingest_data()
