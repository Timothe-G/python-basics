FROM node
WORKDIR /app
ADD package.json /app/ 
RUN npm install
ADD . /app
EXPOSE 8000
ENTRYPOINT ["npm", "start"]
