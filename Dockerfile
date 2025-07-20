FROM node:18-bullseye-slim

# Install Chromium + required libs
RUN apt-get update && apt-get install -y \
    chromium \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libnss3 \
    fonts-liberation \
    libpango1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Puppeteer config
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

# App setup
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 3000
CMD ["node", "index.js"]
