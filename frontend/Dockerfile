# FRONTEND Dockerfile
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy dependency manifests first
COPY package*.json ./

# Clear npm cache & force install all dependencies
RUN npm config set registry https://registry.npmjs.org/ \
 && npm cache clean --force \
 && npm install --include=dev --force \
 && ls -la node_modules/.bin

# Copy the rest of your app
COPY . .

# Expose port 3000
EXPOSE 3000

# Use npx to guarantee 'next' runs even if it's not globally linked
CMD ["npx", "next", "dev", "-p", "3000"]
