# elt_fuelprice_data.gov

# ETL Pipeline Project

## Project Description
The goal of the project is to build an ETL pipeline. ETL (Extract, Transform, Load) is a data pipeline used to collect data from various sources, transforms the data according to business requirements, and loads the data into a destination data storage.

This project contains the following files:
- ``src/extract.py`` - a python script that contains instructions to connect to Amazon Redshift data warehouse and to extract online transactions data with transformation tasks performed using SQL<br>
- ``src/transform.py`` - a python script that contains instructions to identify and remove duplicated records<br>
- ``src/load_data_to_s3.py`` - a python script that contains instructions to connect to Amazon S3 cloud object storage and to write the cleaned data as a CSV file into an S3 bucket<br>
- ``main.py`` - a python script that contains all instructions to execute all the steps to extract, transform, and load the transformed data using the functions from extract.py, transform.py, and load_data_to_s3.py<br>
- ``.env.example`` - a text document that contains the list of environment variables used in .env file<br>
- ``requirements.txt`` - a text document that contains all the libraries required to execute the code<br>
- ``Dockerfile`` - a text document that contains all the instructions a user could call on the command line to assemble an image<br>
- ``.dockerignore`` - a text document that contains files or directories to be excluded when docker CLI sends the context to docker daemon. This helps to avoid unnecessarily sending large or sensitive files and directories to the daemon and potentially adding them to images using ADD or COPY.<br>
- ``.gitignore`` - a text document that specifies intentionally untracked files that Git should ignore<br>

## How to Run the ETL Pipeline project
### A. To run the ETL pipeline from Command Line Interface:

### Requirements
- Python 3+
- Python IDE or Text Editor and Command Line Interface


- Instructions:
  - Copy the ``.env.example`` file to `.env` and fill out the environment variables.
  - Install all the libraries needed to execute main.py.
  - Run the main.py script
  

- Windows:
```
  pip3 install -r requirements.txt
```
```
  python main.py
```

- Mac:
```
  pip3 install -r requirements.txt
```

```
  python3 main.py
```

### B. To run ETL pipeline using Docker:

### Requirements
- Docker Installation:
    - Docker for Mac: 
        - Installation: [Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/)
    - Docker for Windows: 
        - Installation: [Install Docker Desktop on Windows](https://docs.docker.com/desktop/install/windows-install/)
        - WSL2 Linux Kernel Update: [Download the Linux kernel update package](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
- Text Editor and Command Line Interface


- Instructions:
  - Ensure Docker is running locally
  - Comment out the code `from dotenv import load_dotenv` and `load_dotenv()` in the main.py script
  - Copy the `.env.example` file to `.env` file and fill out the environment variables
  

- Build an image
  
```bash
  docker image build -t etl-pipeline .
```

- Run the etl job

```bash
  docker run --env-file .env etl-pipeline
```
