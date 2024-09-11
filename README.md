# ETL Pipeline Project

## Project Description
The goal of the project is to build an ETL pipeline. ETL (Extract, Transform, Load) is a data pipeline used to collect data from various sources, transforms the data according to business requirements, and loads the data into a destination data storage.

## Project Summary
This ETL pipeline objective is to extract fuel price data in Malaysia from data.gov API and load it into local PostgreSQL database. The pipeline will be automated with Airflow to continue fetching new updated data weekly and transformed accordingly using pandas.

This project contains the following files:
- ``src/extract.py`` - a python script that contains instructions to connect to PostgreSQL data warehouse and to extract data from data.gov API<br>
- ``src/transform.py`` - a python script that contains instructions to remove unwanted columns and for data selection<br>
- ``fuelprice_etl.py`` - a DAG task in python script that contains workflow of this pipeline project in Airflow<br>
- ``main.py`` - a python script that for contains all instructions to execute all the steps to extract, transform, and load the transformed data using the functions from extract.py and transform.py
- ``.env.example`` - a text document that contains the list of environment variables used in .env file<br>
- ``requirements.txt`` - a text document that contains all the libraries required to execute the code<br>
- ``.gitignore`` - a text document that specifies intentionally untracked files that Git should ignore<br>


