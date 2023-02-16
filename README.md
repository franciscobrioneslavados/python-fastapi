# Python REST API with FastAPI and MongoDB

### Create a Virtual Environment for Python
## Linux
```
python -m venv venv
source venv/lib/activate
```
## Windows
```
python -m venv venv
venv\Scripts\activate.bat
```

### Install Dependecies
```
pip install -r requirements.txt
```
### RUN
```
uvicorn main:app --reload
```

### Dockerize Mongo
```
docker run --name docker-mongo -d -p 27017:27017 -v $(pwd)/data:/data/db -e MONGO_INITDB_ROOT_USERNAME=<USER> -e MONGO_INITDB_ROOT_PASSWORD=<PASS> mongo:latest
```