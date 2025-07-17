from setuptools import setup, find_packages

setup(name = "RAG_BOT",
      version = "0.1",
      author="Ayush Panchaity",
      author_email="panchaityayush@gmail.com",
      packages=find_packages(),install_requires=[
          "langchain_astradb","langchain"
      ] 
)
