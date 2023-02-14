# What the project does
This is meant to be a minimal project, that demonstrates how data from a Postgres container can be accessed and CRUD operations can be run from another container using python. 

Container 1: Postgres container (preloaded with data using .sql files)
Container 2: Python container 

# How to run this project 
- Prerequisites: Docker needs to be installed in the local machine 
- Open terminal in the root directory of this repo and run the command `docker compose up`
- Upon running the command, the Postgres container and Python container will start. The python container will split out outputs in command line. This output can be seen either in the terminal or in Docker Hub inside the python container > output tab. 
- To stop the containers run the command `docker compose down -v`. The `-v` will make the volumes are deleted. This will come in handy, when new databases/tables needs to be initialized via .sql files. 

# Rooms for improvemnts 

This project was made in a hurry, needless to say there are many rooms for improvents. Some of them are - 
- Use `sqlachemy` instead of `psycopg2`. The reason being, `sqlalchemy` offers much more pythonic way of handling sql queries instead of handling raw sql queries, which can get more difficult to manange as the query gets more complicated. 