# api-shop
---
```docker build -t flask_app .
docker run --name app -d -p 5000:5000 flask_app # run container in detached mode
docker exec -it app bash # go to container
docker rm $(docker ps -aq)
```
---
```
FLASK_APP=app.py
FLASK_DEBUG=1
flask run --host=0.0.0.0
```
---
```docker build -t pg_db .
docker run --name db -d -p 5431:5432 -v $PWD/data:/var/lib/postgresql/data pg_db
docker exec -it db bash

psql -d postgres -h localhost -U antonio -p 5431
\conninfo
```


