import pandas as pd
from langchain_core.documents import Document
import os


""" transforming the data """

class data_convertor:

    def __init__(self):
        print("this is initialisation class of data_convertor class")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, '..'))
        data_path = os.path.join(project_root, 'data', 'flipkart_product_review.csv')
        self.input_data = pd.read_csv(data_path)
        # print(f"thr rows are {self.input_data.shape[0]} and columns are {self.input_data.shape[1]}")
        pass

    def data_transformation(self):
        self.req_cols = self.input_data.columns
        # print(f"the required cols are ---- {self.req_cols}")
        self.req_cols = list(self.req_cols[1:])

        prd_list = []
        for index, rows in self.input_data.iterrows():
            # create the dictionary
            object = {
                'product_name': rows['product_title'],
                'product_rating': rows['rating'],
                'product_summary': rows['summary'],
                'product_review': rows['review']
            }
            prd_list.append(object)
            # print(f"the new dataframe is --- {prd_list[0]}")

        docs = []
        for key in prd_list:
            # create the metadata dictionary
            metadata = {
                'product_name': key['product_name'],
                'product_rating': key['product_rating'],
                'product_review': key['product_review']
            }

            doc = Document(page_content=key['product_review'], metadata=metadata)
            docs.append(doc)
            # print(f"the docs are ----- {docs[0]}")
        return docs


if __name__ == "__main__":
    obj_data_conv = data_convertor()
    obj_data_conv.data_transformation()
