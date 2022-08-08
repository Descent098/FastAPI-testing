# FastAPI Testing

This repository is used to test fastAPI for my most common use cases. This is not the best implementation that can be done with fastapi, this is intended to see what a quick and dirty implementation that works for me looks like

## Why

For some background I primarily work with flask for creating my simple projects. Particularly I've been using Flask in situations where I just need simple get and post requests. There are however several problems:

1. Documentation is pretty janky using a custom CI/CD pipeline and pdoc3, which works well for regular API's but not great for flask routes
2. Performance optimization is possible but quite annoying. Particularly using a proper wsgi client is a pain because solutions like gunicorn are not cross platform (no windows version)

I decided to try FastAPI since it has a default `/docs` route that is an interactive docs section and is incredibly fast while supporting asynchronus routes.

## What

This demo is a demo that just allows you to add new users and displays a table of all the users that exist. The values are all tied to the python runtime and **are not persistant**. This means they will be deleted once the runtime environment closes.

## Setup

There are three options for setup, you can install natively, use virtualenv or you can use docker

### Natively

*Prerequisites*:
You need python 3.6+ and pip for python installed

1. install dependencies with pip using `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
2. run `python main.py` or `uvicorn main:app --reload --debug` to run the project
3. Head to http://localhost:8000

### Virtualenv

*Prerequisites*:
You need python 3.6+ and pip for python installed

1. install virtualenv using `pip install virtualenv` or `pip3 install virtualenv`
2. Setup a virtual environment using `virtualenv venv`
3. Run `/venv/Scripts/activate` to start your virtual environment
4. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` to install dependencies to your virtual environment
5. Run `python main.py` or `uvicorn main:app --reload --debug` to run the project
6. Head to http://localhost:8000

### Docker

*Prerequisites*:
You need a working docker installation

1. Run `docker build -t fastapi-test .` to build the image
2. Then run `docker run -dp 8000:8000 fastapi-test` to create container
3. Head to http://localhost:8000
