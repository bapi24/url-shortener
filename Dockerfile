# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

#install dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY test.py .

# Specify the command to run on container start
CMD [ "python", "./test.py" ]