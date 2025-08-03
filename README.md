```
create the virtual environment you can use conda, venv or any library management services 
 conda create -p env python=3.10 -y
```
```
activate the environment and install alll the required libraries 
conda activate env
```
```
below line is to run the code 
uvicorn - to run the fastapi 
main - because our script name is main.py
app - fastapi object created by name app 
reload - to relaod automatically while developers are making changes  
uvicorn main:app --reload --port 8001
```
