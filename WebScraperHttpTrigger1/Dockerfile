FROM python:3.10.7

ENV PLAYWRIGHT_BROWSERS_PATH=/usr/lib/playwright

# Install system dependencies
RUN apt-get update && \
    apt-get install -y wget libgbm-dev

# Install Playwright
RUN wget -qO- https://playwright.dev/install.sh | bash
# Install Playwright
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
CMD ["python", "/home/site/wwwroot/__init__.py"]
