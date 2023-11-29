docker image  build -t isdb .
docker container run -d -p 5432:5432 isdb