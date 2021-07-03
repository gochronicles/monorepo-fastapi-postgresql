FROM python:3.9-slim
RUN apk update \
        && apk add --no-cache git openssh-client \
        && pip install pipenv \
        && addgroup -S -g 1001 app \
        && adduser -S -D -h /app -u 1001 -G app app

COPY . /app
WORKDIR /app
RUN chown -R app:app /app
USER app
RUN pipenv install
ENTRYPOINT ["/bin/sh"]
CMD ["pipenv", "run", "python", "main.py"]