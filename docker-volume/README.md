# docker-volume

This app contains 3 files :
- Dockerfile
- app.py
- requirements.txt
<br></br>
## Dockerfile
The Dockerfile contains all data to build an image for docker.
> The first line specifies which base image we need to use. In this example, we are using a container with python, and some modules already installed (uvicorn, gunicorn and fastapi).
```dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim
```
<br></br>
> The second line specifies that we will work in a specific path. For this project, we will work in "/"
```dockerfile
WORKDIR /
```
<br></br>
> The thirst line specifies that we will copy all files in ./app in the folder /app in the container.
```dockerfile
COPY ./app /app
```
<br></br>
> The fourth line is a command that we would like to execute in the container. The goal of this command is to add requirements of our script. In this example this is not necessary because we are already using a base image that contains all required modules for our script.
```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```
<br></br>
> The last line is the command that will execute the python script when the container will be up. In our case, we will execute the command **uvicorn** with some options
> - app:app is the name of the file
> - host 0.0.0.0 will be used
> - port 80 will be used
```dockerfile
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
```
<br></br>
## app.py
This is the python script. It using the FastAPI module. In this script, we would like to get a message when user is connecting to the "/" directory. In the example of a website, it will show the message **Hello : World** on http://localhost/
<br></br>
## requirements.txt
This file contains all requirements for the script to be executed with the version that we would like to use.
