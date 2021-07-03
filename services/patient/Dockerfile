FROM python:3.8-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libpq-dev gcc
COPY . .
# RUN apk update \
#         && apk add --no-cache git openssh-client postgresql-dev gcc python3-dev musl-dev
RUN pip install -U pip \ 
        && pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]