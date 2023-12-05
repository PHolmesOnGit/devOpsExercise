# Star Wars Cron Job

This is my take on the python cron job project found here https://github.com/DivvyPayHQ/devops-exercise#exercise-star-wars-cron-job-python 
I will continue adding to this readme as I go further in the project with instructions on setup/running the project. 


The Python part of this project is done! I may touch up/add some things to unittest, also potentially restructure apicall.py.

As of now the code fulfills the requirements. It digests the data in input.yaml, makes a call to the Star Wars API, then exports the requested data as json files into the users "Documents" directory

The next things I will be doing with this project is containerizing the script in Docker, creating a Helm chart to use with MiniKube to have the script run every hour. 


##########################################################


HOW TO RUN THE PROGRAM


########################################################

At the moment is is pretty simple to set up and run. The program doesn't require any libraries that aren't usually preinstalled with python 3



Download the code as a .zip file and open it in your preferred IDE. Configure the interpreter if needed, and run main.py. 

You will see .json files appear in your documents folder with the requested info from input.yaml.



