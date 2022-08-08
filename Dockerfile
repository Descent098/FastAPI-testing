FROM python:alpine

# Setup a folder called /app on the container where all the files will be stored and everything will run from
WORKDIR /app

# Add requirements for uvloop package that's necessary for fastapi
RUN apk add build-base

# Copy all the files from the current directory on the host machine into the cwd of the container
COPY . ./

# Update pip
RUN  pip install -U setuptools pip

# Run `pip install -r requirements.txt`
RUN pip install -r requirements.txt 

# Allow for port 8000 of the container to be accessible to the host machine
EXPOSE 8000

# Start using `python3 main.py`
ENTRYPOINT ["python3", "main.py"]