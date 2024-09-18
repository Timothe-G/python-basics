# docker-registeries

This app is not a python app. This is just a test to upload a docker image to docker hub.
There is 2 files :
- Dockerfile
- index.html
&nbsp;
There is two important commands. The first one is to build, and the second one is to push the image to docker hub :
```docker
docker build -t [DOCKER_HUB_USERNAME]/simple-container:latest .
```

```docker
docker push [DOCKER_HUB_USERNAME]/simple-container:latest
```
