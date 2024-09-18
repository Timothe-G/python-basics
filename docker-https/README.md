# docker-https

The goal of this app is to show a webpage that uses PostgreSQL to show information from database but with HTTPS. This is the same app has docker-postgres. So here is the difference :
This app contains 3 new files :
- nginx.conf
- certs/cert.pem
- certs/key.pem
And the docker-compose.yml file has been modified.
&nbsp;
## nginx.conf
This is a conf for nginx. In this configuration we specify the certs file to be used on https.
&nbsp;
## certs/cert.pem and certs/key.pem
These files are generated by OpenSSL. This is 2 files needed for https. They have been generated with Let's Encrypt.
&nbsp;
## docker-compose.yml
We have added a container named nginx. This container use the configuration of nginx and certs. We also have added a network shared between nginx and app containers.