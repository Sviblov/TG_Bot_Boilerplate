FROM python:3.11-slim

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /usr/src

COPY ./infrastructure /usr/src/infrastructure
COPY ./webapp_backend /usr/src/webapp_backend

COPY alembic.ini /usr/src
COPY ./webapp_backend/docker-entrypoint-webapp_backend.sh /usr/src

RUN pip install -r /usr/src/requirements.txt --pre

CMD ["bash", "/usr/src/docker-entrypoint-webapp_backend.sh"]
