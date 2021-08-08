FROM python:3.8-alpine as domain_builder
WORKDIR /app
# RUN apt-get update && apt-get install -y libpq-dev gcc
COPY . .
RUN apk update \
        && apk add --no-cache git openssh-client postgresql-dev gcc python3-dev musl-dev
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
# RUN apk update && apk upgrade && apk add --no-cache postgresql-libs gcc libc-dev
RUN pip install -U pip \ 
        && pip install --no-cache-dir -r requirements.txt
FROM python:3.8-alpine
RUN apk update && apk upgrade
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
COPY --from=domain_builder /app /app
COPY --from=domain_builder /venv /venv
WORKDIR /app
ENV PATH="/venv/bin:$PATH"
CMD ["python", "main.py"]