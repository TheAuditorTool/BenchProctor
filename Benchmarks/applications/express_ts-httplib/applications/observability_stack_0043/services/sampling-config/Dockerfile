FROM node:20-alpine
WORKDIR /app
COPY package.json ./
COPY tsconfig.json ./
RUN npm install
COPY . .
RUN apk add --no-cache openssl && npx prisma generate
USER node
CMD ["npm", "start"]
