# Proof of concept for neo4j 

Simple proof of concept for geolocation data neo4j

# Makefile 

A simple make file to pull the image and start up the container.


Pull the neo4j docker container 
```
make docker_pull
```

Run the container (Should pop-up: http://localhost:7474/)
```
make run 
```

# Requirements.txt 

Python requirements file needed to create an env with all the required packages.

# sample.ipynb
Notebook to connect to the DB, generate people and locationss and connect them. 
The bottom of the file contains a couple of example queries to find locations with multiple 
users.  The second query finds ids within a specific range. 
