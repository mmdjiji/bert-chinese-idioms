FROM node:16 AS vue

COPY ./web /web
WORKDIR /web

RUN npm install && npm run build

FROM ubuntu:20.04

COPY . /app
COPY --from=vue /web/dist /app/web/dist

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip python-is-python3 && \
    pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]