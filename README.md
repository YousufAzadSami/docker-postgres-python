# What is this project?
This project demonstrates how data from a Postgres container can be accessed(e.g. CRUD operations can be run) from another container using python. This was done as an interview task. This is meant to be a barebone minimal project, i.e. the codes here are kept simple and are for experimental purpose. In no shape or form, they are production-ready code. 

- Container 1: Postgres container (preloaded with data using .sql files)  
- Container 2: Python container (accesses data from the first container)

# How to run this project 
Prerequisites: Docker needs to be installed in the local machine 
- Clone or download the `repo` 
- Open terminal in the root directory of this `repo`. Then run the command `docker compose up` (tested from CMD and PowerShell). Add `--build` if you wish to force rebuild. This comes helpful when there is a change in the code after the first build. 
- Upon running the command - 
  - The Postgres container and Python container will start as instructed in the `docker-compose.yml` file
  - The Postgres container has some data (`customer` table in `postgres_super_db` database) preloaded into it from the `customers.sql` file. 
  - The python container will wait 5 seconds so that the Postgres container can start up first. I used ``sleep()`` function to wait manually. This is a adhoc solution for developtment puposes only. 
  - The python container will connect to the database, read and split out outputs in command line. This output can be seen either in the terminal or in Docker Hub inside the python container > output tab. 
- To stop the containers run the command `docker compose down`. Adding `-v` will delete the volumes. This will come in handy, when new databases/tables needs to be initialized via .sql files. 

# Rooms for improvemnts 

This project was made in a hurry, needless to say there are many rooms for improvents. Some of them are - 
- Instead of manually waiting for the Postgres container to start, find some alternative solution. 
- Genarate data automatically. It is part of the task description. Right now, it is done manually via .sql file. 
- Use `sqlachemy` instead of `psycopg2`. The reason being, `sqlalchemy` offers much more pythonic way of handling sql queries instead of handling raw sql queries, which can get more difficult to manange as the query gets more complicated. 
