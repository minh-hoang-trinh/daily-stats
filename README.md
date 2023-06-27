# Stats Dashboard

A POC for read-models statistics dashboard.

## Quick Start

You can run the app with docker-compose

```bash
docker-compose up
```

navigate to http://localhost:4242

## Development

Install poetry if you don't have it already:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

or with brew:

```bash
brew install poetry
```

Install dependencies:

```bash
poetry install
```

Run the app:

```bash
poetry run streamlit run stats_dashboard/app.py
```
