# docker-postgres

The goal of this app is to show a webpage that uses PostgreSQL to show information from database.
This app contains 4 files :
- docker-compose.yml
- Dockerfile
- main.py
- northwind.sql
- requirements.txt
&nbsp;
## docker-compose.yml
The docker-compose file is used to create and run multi container in Docker.
This docker-compose file is from this github : https://github.com/pthom/northwind_psql
The only modification is the "app" part to get a container named "app" with port 8000 to get a website.
&nbsp;
## Dockerfile
The Dockerfile contains all data to build an image for docker.
> The first line specifies which base image we need to use. In this example, we are using a container with python 3.8 and some modules that we need
```dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim
```
&nbsp;
> The second line specifies that we will copy all files in the current folder in the root folder in the container.
```dockerfile
COPY . .
```
&nbsp;
> The thirst line specifies that we will listen on port 8000 for TCP connections.
```dockerfile
EXPOSE 8000
```
&nbsp;
> The fourth line is a command that we would like to execute in the container. The goal of this command is to add requirements of our script.
```dockerfile
RUN pip install -r requirements.txt
```
&nbsp;
> The last line is the command that will execute the python script when the container will be up.
```dockerfile
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
&nbsp;
## main.py
This is the python script. In this, we will use the module sqlalchemy to connect to the database that are in another container (with the same network) and we have the SELECT query that is displayed on the website.
&nbsp;
## northwind.sql
This file is from this github : https://github.com/pthom/northwind_psql
It contains a test database.
&nbsp;
## requirements.txt
This file contains all requirements for the script to be executed.
