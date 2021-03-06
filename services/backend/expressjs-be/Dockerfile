FROM node:14-alpine

WORKDIR /app
COPY . .
ENV PORT=4000
EXPOSE 4000

RUN npm install
CMD [ "node", "index.js" ]