# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    xvfb \
    chromium \
    chromium-driver \
    fonts-liberation \
    libappindicator3-1 \
    libgbm-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies using requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the local directory contents into the container
COPY . .

# Start Xvfb to run Chrome in headless mode and execute the Selenium script
CMD ["sh", "-c", "Xvfb :99 -screen 0 1920x1080x24 & pytest --html=/usr/src/app/reports/report.html"]