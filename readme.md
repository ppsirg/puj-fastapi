# fastapi startup

to run fastapi, you can do it with:

- docker
- virtualenv


## docker

you need to install docker, once you have docker, run:

docker build -t fastapiDEMO .

that will create an image called fastapiDEMO, to run app, you have to run this:

docker run --name fastapidemo -p 8080:8080 fastapiDEMO

open your web browser and check localhost:8080/docs to check openAPI documentation with all urls implemented

## virtualenv

create a virtualenv, then, install requirements in requirements.txt file, then, run:

uvicorn main:app

add --reload to be able to reload on .py changes