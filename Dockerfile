FROM python:3.10.7

# Install system dependencies
RUN apt-get update && \
    apt-get install -y wget libgbm-dev

# Install Playwright dependencies
RUN apt-get install -y xvfb libatk-bridge2.0-0 libgtk-3-0 libxcomposite1 libxcursor1 libxdamage1 libxi6 libxtst6 libnss3 libcups2 libxss1 libxrandr2 libgconf-2-4 libasound2 libpangocairo-1.0-0 libatk1.0-0 libatk-bridge2.0-0 libgtk-3-0

# Install Playwright Python package
RUN pip install playwright

# Set the working directory to the function code directory
WORKDIR /home/site/wwwroot

# Copy the function code and requirements.txt to the working directory
COPY . .
COPY requirements.txt /app/requirements.txt
COPY WebScraperHttpTrigger1/__init__.py /home/site/wwwroot/__init__.py

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Run the script
CMD ["bash", "-c", "playwright install && python /home/site/wwwroot/__init__.py"]
