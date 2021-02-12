# set base image (host OS)
FROM python

# set the working directory in the container
WORKDIR /scrapping

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY mysql_query.py /scrapping/

VOLUME [ "/Users/farouk/Documents/simplon/amine/scrapping" ]

# command to run on container start
CMD [ "python3", "./mysql_query.py" ]