# Python REST API with FastAPI and MongoDB

### Install poetry as a global dependecies 
```
pip install poetry
```

### Install dependecies for the project 
```
poetry install
```

### RUN
```
poetry run ./run.sh
```

### Dockerize Mongo
```
docker run --name docker-mongo -d -p 27017:27017 -v $(pwd)/data:/data/db -e MONGO_INITDB_ROOT_USERNAME=<USER> -e MONGO_INITDB_ROOT_PASSWORD=<PASS> mongo:latest
```
