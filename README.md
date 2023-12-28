# Star Wars Cron Job

This is my take on the python cron job project found here https://github.com/DivvyPayHQ/devops-exercise#exercise-star-wars-cron-job-python 
I will continue adding to this readme as I go further in the project with instructions on setup/running the project. 

As of now the code fulfills the requirements. It digests the data in input.yaml, makes a call to the Star Wars API, then exports the requested data as json files into the users "Documents" directory

The next things I will be doing with this project is creating a Helm chart to use with MiniKube to have the script run every hour. 


##########################################################


HOW TO RUN THE PROGRAM (Docker Required)


########################################################

1. Download the .zip of the project and extract it. 

2. Next we will build a docker image ro run the project.
   - In terminal, navigate to the project's directory
   - Run the command "docker init"
   - Select "Python" as your application platform
   - Select 3.10.4 as the python version
   - For the port section, you can select whatever port you want. It doesn't really matter for this project.
   - The command to run the app is as follows "python3 -m main run"
   - Now you have built your docker image!

3. Next, you can start your docker application by running "docker compose up --build"

4. This will create several files in your project directory, including a compose.yaml, Dockerfile, and .dockerignore

5. You can now run the docker image. If you run the command "docker run {image name}" you will notice the the API call runs, but then you get a FileNotFoundError, this is because we need to create a bind mount to have the data saved outside of the docker container. This way, it will exist even if the docker image closes.

6. To do this, run the following command: "docker run -it --mount type=bind,source={Path to your documents folder},target=/data {image name}
   - Source is the output location, where you want the files to end up at. In this case, the documents folder.
   - Target is the folder where the data is written to in the container. You'll notice on line 40 of fileexport.py is where we tell the program to write to this folder.
   - A bind mount essentially "links" those two folder locations, whatever is writted in the /data folder will show up in your Documents folder.
   - After you run this command, you'll notice the .json files will show up in your documents folder. 

VIDEO INSUTRCTIONS AND INSTRUCTIONS FOR WINDOWS:

https://www.twitch.tv/videos/2016325437
