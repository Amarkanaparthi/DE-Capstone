# DE-Capstone
# Data Engineering Capstone

An end-to-end data pipeline built while learning data engineering.

## Goal
Ingest e-commerce data from Postgres (batch) and Kafka (streaming), clean it
into Bronze, Silver and Gold layers, orchestrate it with Airflow, and serve
it in Power BI.

## Stack
Python, SQL, PostgreSQL, PySpark, Kafka, Airflow, Databricks, dbt, Power BI,
Docker, GitHub Actions

## Setup
1. Clone the repo and create a virtual environment: `python -m venv .venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Copy your settings into a `.env` file (never commit it)
4. Start Postgres: `docker start de-pg`
5. Check the connection: `python test_connection.py`

## Status
Setup done. Next: Python and Postgres ingestion sprint.