# Run a local instance of MySQL Server using Docker

## Quickstart

1. Ensure Docker Desktop is running.
   To ensure the Docker is running, run the following command at the terminal. If you see Docker's version - it is running. Otherwise, open the `Docker Desktop` application, and wait until it gets started.
   > $ docker ps

   Expected output: <br>
   ![](./imgs/docker-version.png)

2. Try to run `MySQL` server
   To run `The MySQL server, run the next command in the terminal
   > docker run -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 -v "${env:USERPROFILE}\.mysql:/var/lib/mysql" --name my-sql MySQL.


> [!IMPORTANT]
> This command is a Windows-based command.
> You must create the directory `.mysql` on Windows at the `%USERPROFILE%`. To open the `%USERPROFILE%` directory, press Win+R and paste `%USERPROFILE%` to the opened window. Then press `OK`
>
> To run it on a Unix-like system, create the `.mysql` directory and set the path instead of `${env:USERPROFILE}\.mysql`. 

3. If an instance of MySQL started correctly in the terminal, you have to see the following output:
   ![](./imgs/mysql-instance-running.png)

4. Open Rider or any other UI tool and connect to the database with the following credentials:

   | User     | Password     |
   |----------|--------------|
   | root     | my-secret-pw |


## Errors Handling

### Conflict. The container name "/my-sql" is already in use
![](./imgs/my-sql-already-in-use.png)

This error means that you already have a container with the same name. First of all, you have to check the status
of this container. If it's running - you can use the existing one. Go to step 4 from the quickstart guide.

To check the container's status, run the `docker ps -f name=my-sql --format '{{.ID}}' -a' command.
![](./imgs/docker-ps-mysql-status.png)

If you see that the status is not `Running,` copy the container ID and remove it with the command `docker rm -f <CONTAINER_ID>`.
![](./imgs/docker-rm.png)

Now, try to retry the Quickstart guide.

### Bind for 0.0.0.0:3306 failed: port is already allocated
![](./imgs/port-already-in-use.png)

To fix this issue, you must modify the running command to replace `3306:3306` with `3307:3306` and rerun the command.
Then,, when you try to connect to the database from Rider (or any other UI tool), instead of port `3306`,, use `3307`.
