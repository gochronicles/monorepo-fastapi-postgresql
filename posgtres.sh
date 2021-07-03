docker run -d \
    -p 5432:5432 \
    --name domain-pg \
    -e POSTGRES_PASSWORD=postgres \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v $(pwd)/pgdata:/var/lib/postgresql/data \
    postgres:12-alpine
