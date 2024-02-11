# Use an appropriate base image that includes pip
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the application files from GitHub
COPY Egg.py /app/Egg.py
COPY requirements.txt /app/requirements.txt

# Install pip (if not included in the base image) and install dependencies
RUN apt-get update && apt-get install -y python3-pip
RUN pip install -r requirements.txt

# Run the Python application
CMD ["python", "Egg.py"]
