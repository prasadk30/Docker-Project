# Use a small Node image
FROM node:20-alpine

# Set the working directory inside the container
WORKDIR /app

# Install dependencies first (so Docker can cache this layer)
COPY package*.json ./
RUN npm install --omit=dev

# Copy the application code
COPY . .

# Express runs on port 3000
EXPOSE 3000

CMD ["npm", "start"]