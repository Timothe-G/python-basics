# docker-compose

The goal of this app is to show a webpage that uses a cache to see how many times the page was seen by a user.
This app contains 4 files :
- docker-compose.yml
- app/Dockerfile
- app/app.py
- app/requirements.txt
<br></br>
## docker-compose.yml
The docker-compose file is used to create and run multi container in Docker.
In this docker-compose file you will see two container : web and redis. I will not explain each line of the docker-compose. If you need more information you already have lot of informations on internet.
<br></br>
## app/Dockerfile
The Dockerfile contains all data to build an image for docker.
> The first line specifies which base image we need to use. In this example, we are using a container with python 3.6.
```dockerfile
FROM python:3.6
```
<br></br>
> The second line specifies that we will work in a specific path. For this project, we will work in "/app"
```dockerfile
WORKDIR /app
```
<br></br>
> The thirst line specifies that we will copy all files in the current folder in the root folder in the container.
```dockerfile
COPY . .
```
<br></br>
> The fourth line is a command that we would like to execute in the container. The goal of this command is to add requirements of our script.
```dockerfile
RUN pip install -r requirements.txt
```
<br></br>
> The last line is the command that will execute the python script when the container will be up.
```dockerfile
CMD python app.py
```
<br></br>
## app/app.py
This is the python script. In this, we will use redis to get a cache. It will store how many times the webpage has been seen by a user and it will show the number.
<br></br>
## requirements.txt
This file contains all requirements for the script to be executed.
