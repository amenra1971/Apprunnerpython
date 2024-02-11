FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the application files from GitHub
COPY Egg.py /app/Egg.py
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Run the Python application
CMD ["python", "Egg.py"]