# FastAPI and PostgreSQL Microservices Template

### Create A PostgreSQL Instance

- Use docker and expose ports 5432

```bash
./postgres.sh # docker should be running
```

### Run a Microservice on local

Export env

```bash
export POSTGRES_URI="postgresql://postgres:postgres@0.0.0.0:5432/postgres"
```

Run a particular microservice (eg domain)

```
cd services/domain
pipenv install # for first time setup
pipenv run python main.py # or
pipenv run uvicorn main:app --reload # for hot reload
```

Endpoint available at

`http://0.0.0.0:8000/api/v1/domain`

### Run a Microservices on Docker & Docker compose

```
cd services
docker-compose up
```

Endpoints available at

`http://0.0.0.0:7000/api/v1/domain`

`http://0.0.0.0:8000/api/v1/patient`
