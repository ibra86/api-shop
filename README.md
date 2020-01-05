# api-shop
docker build -t flask_app .
docker run --name app -d -p 5000:5000 flask_app # run container in detached mode
docker exec -it app bash # go to container

 docker rm $(docker ps -aq)


