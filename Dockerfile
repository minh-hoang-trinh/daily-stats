FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y build-essential python3-dev libblas3 liblapack3 liblapack-dev libblas-dev gfortran

RUN pip install --upgrade pip \
    && pip install poetry

COPY . /app

RUN poetry install --no-interaction --no-dev

CMD poetry run streamlit run stats_dashboard/app.py --server.port 4242