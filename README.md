# FastAPI and PostgreSQL Microservices Template

### Create A PostgreSQL Instance

- Use docker and expose ports 5432

```bash
./postgres.sh # docker should be running
```

### Export env

```bash
export POSTGRES_URI="postgresql://postgres:postgres@0.0.0.0:5432/postgres"
```

### Run a Microservice on local:

Run a particular microservice (eg domain)

```
cd services/domain
pipenv install # for first time use
pipenv run python main.py
```

Endpoint available at

`http://0.0.0.0:8000/api/v1/domain`
