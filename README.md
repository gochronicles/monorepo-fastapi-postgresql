# FastAPI and PostgreSQL Microservices Template

### Create A PostgreSQL Instance

- Use docker and expose ports 5432

```bash
    docker run -d \
        --name fastapi-postgres-test \
        --user $USER \
        -e POSTGRES_PASSWORD=postgres \
        -e PGDATA=/var/lib/postgresql/data/pgdata \
        -v /$(pwd):/var/lib/postgresql/data \
        postgres:12
```

### Export env

``` export NEO4J_URI=neo4j://<IP>:7687```

``` export NEO4J_USERNAME=<>```

``` export NEO4J_PASSWORD=<> ```

### Run a Microservice:

Run a particular microservice (eg domain)

``` go run cmd/domain/main.go`

Endpoint available at

http://<IP>:5000/api/v1/patient
