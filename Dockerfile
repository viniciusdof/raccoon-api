FROM node:lts
WORKDIR /app
COPY package*.json yarn.lock ./
RUN yarn set version 3.6.2
RUN yarn install
COPY . .
RUN yarn build
EXPOSE 8000
CMD ["yarn", "serve"]