# Use an official Node.js runtime as the base image
FROM node:14-slim

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install frontend dependencies
RUN npm install

# Copy the rest of the project files to the container
COPY . .

# Expose the Next.js dev server port
EXPOSE 3000

# Command to start the Next.js development server
CMD ["npm", "run", "dev"]