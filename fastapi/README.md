# fastapi

This app contains 2 files :
- Dockerfile
- app/main.py
<br></br>
## Dockerfile
The Dockerfile contains all data to build an image for docker.
> The first line specifies which base image we need to use. In this example, we are using a container with python, and some modules already installed (uvicorn, gunicorn and fastapi).
```dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim
```
<br></br>
> The second line specifies that we will copy all files in ./app in the folder /app in the container.
```dockerfile
COPY ./app /app
```
<br></br>
> The third line specifies that we will listen on port 80 for TCP connections.
```dockerfile
EXPOSE 80
```
<br></br>
> The last line is the command that will execute the python script when the container will be up. In our case, we will execute the command **uvicorn** with some options
> - main:app is the name of the file
> - host 0.0.0.0 will be used
> - port 80 will be used
```dockerfile
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```
<br></br>
## app/main.py
This is the python script. It using the FastAPI module. In this script, we would like to get a message when user is connecting to the "/" directory. In the example of a website, it will show the message **Bienvenue dans mon monde** on http://localhost/
In addition to that, we are adding all path of the module FastAPI. For example you will have access to http://localhost/docs
