# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /dough-scaler

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY runner/ .

# command to run on container start
CMD [ "python3", "./scaler.py" ]