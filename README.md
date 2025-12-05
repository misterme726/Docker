Project 1 : Dockerize Your Own App. 
Name : Vamshi Krishna Cheguri 
ID : RIS00479 
Batch 4. 
Introduction 
This project shows how to containerize a python application and a PostgreSQL database 
using Docker. The Python app accepts user input, inserts it into a PostgreSQL table, and 
retrieves the stored data. The goal of the project is to understand Docker networking, image 
building, container orchestration, and database connectivity. 
Step 1 :Setting up the files 
Create two files in the folder and name them as “app.py” and “Dockerfile”. 
Fig1: Files setup in the VScode. 
Step 2 : Postgres Container Setup 
The PostgreSQL container setup involves launching a dedicated database instance inside 
Docker using predefined credentials and connecting it to a custom Docker network. 
The commad used to create network is “docker network create network ”. 
Fig2: Setting up the docker network. 
Step 3 : Building Python App 
The python application dynamically connects to the PostgreSQL container using environment 
variables, ensuring flexibility and portability across different environments. It asks the user 
for input, creates a database table if it doesn't exist, inserts the data, and retrives it. 
The command used to crate the python app is “docker build --no-cache -t my-python-app .” 
Fig3: Building Python App. 
Step 4: Running the application 
The Dockerfile defines a lightweight Python environment, installs necessary dependencies 
such as psycopg2, and ensures the application can run consistently across different systems. 
By packaging the Python script and its requirements into a Docker image, it guarantees 
reproducibility, simplifies deployment, and eliminates configuration issues on the host 
machine. 
The commad used to run application and for user input ” docker run -it --rm --network 
mynetwork -e DB_HOST=my-postgres -e DB_NAME=mydb -e DB_USER=user -e 
DB_PASS=pass my-python-app”. 
Fig4: Running the application. 
Fig5: User input. 
Step 5: Verification in PostgreSQL 
Uses SQL queries executed inside the container to confirm that user input is correctly stored 
in the database. Validates successful end-to-end integration between Python, Docker, and 
PostgreSQL. 
Fig6: Data stored in SQL. 
Step 6: Conclusion 
From this project i learnt how to create a docker container and image and learnt how docker 
works and gained some practical knowledge and hands-on-experience on the basics of the 
docker tool. 
