# API for Resource Manager

### Stack
- Django
- Django REST Framework
- Docker
- Postgres
- Adminer for db access (`localhost:8080`)

### Setup environment
- In terminal, run
  - `docker-compose up`

- In other terminal, run
  - `docker exec -it resmanager_web_1 bash`
  - `python manage.py migrate`

### Start Server
`docker-compose up` 