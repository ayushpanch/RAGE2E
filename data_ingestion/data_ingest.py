""" ingesting the data into vector database """
from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd
from data_ingestion.data_transform import data_convertor
from langchain_google_genai import GoogleGenerativeAIEmbeddings
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["ASTRA_DB_API_ENDPOINT"] = ASTRA_DB_API_ENDPOINT
os.environ["ASTRA_DB_APPLICATION_TOKEN"] = ASTRA_DB_APPLICATION_TOKEN
os.environ["ASTRA_DB_KEYSPACE"] = ASTRA_DB_KEYSPACE
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


class ingest_data:

    def __init__(self):
        print("this is initialisation class of data_ingest class")
        self.embeddings = GoogleGenerativeAIEmbeddings(model = 'models/text-embedding-004')
        self.data_convertor = data_convertor()
        pass

    def ingest_data(self,status):
        vectorstore = AstraDBVectorStore(
            embedding=self.embeddings,
            collection_name="RAGE2E",
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            token=ASTRA_DB_APPLICATION_TOKEN,
            namespace=ASTRA_DB_KEYSPACE)

        storage = status

        if storage==None:
            docs = self.data_convertor.data_transformation()
            inserted_ids = vectorstore.add_documents(docs)

        else:
            return vectorstore
        
        return vectorstore,inserted_ids 

if __name__ == "__main__":
    obj_data_ingest = ingest_data()
    vec_store, inserted_ids = obj_data_ingest.ingest_data(status="yrd")
    print(f"the len of inserted ids is {len(inserted_ids)}")
    results = vec_store.similarity_search("please help me with the low budget phone?", k=3)
    for res in results:
        print(f"the page content is {res.page_content}")
        print(res.metadata)