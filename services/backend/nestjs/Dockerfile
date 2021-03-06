FROM node:14-alpine

ENV PORT=4000
EXPOSE 4000

WORKDIR /app
COPY . .
RUN yarn install
CMD ["nest", "build"]
CMD ["nest", "start"]