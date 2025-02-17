# **My Engineering Diary**

## Things I've done weekly
- I have tried my best to read up on everything that has been done within the project.
- Taking notes of new commands I learn.
- Research different methods of doing the project (trying to decide which program is best).
- Keeping track of things I've done durring each week by writing in my Engineering diary.

## Things about the text
- Text is divided into two parts
    1. My work throughout the weeks
    2. Thoughts about the project and how it went
  
**I'll be updating progress, problems I've encountered and solutions along with other things I've learned in this course.**

## 1. My work throughout the weeks
#### Week 35 and 36: 

- Created a group of five people (Myself, Ebba, Wilma, Thanh, Sabor).
- Learned about Git and Github (https://www.youtube.com/watch?v=mJ-qvsxPHpY)
    Note: Also touched on the topic of branches.
- Created Github account and GitHub repo (https://github.com/HaileyLV/PA1489-project.git)
- Planed and structured how the work should be distributed. 



#### Week 37:
- Watched videos and read about md syntax (https://www.markdownguide.org/basic-syntax/)
- Created SSH key for Github
- Group agreed and decided to divide parts of the project and assign it to smaller groups. (Ex. two people do KitchenView.)


#### Week 38:
- Researched about Flask and installed the program.
- Two people in the group strayed from the original plan of dividing the project into sections, and did almost the whole project on their own. 
    Note: Concerned about not being able to partake in the project.
- Group member took my computer and I was confused on what they were trying to do. (This later caused issues in committing things to the project.)
    Note: Don't let others do things on your computer if you are unaware what they are doing.
- Learned different git commands.
- Downloaded Docker desktop (https://www.docker.com/products/docker-desktop/).

| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|git pull                   | pull code from remote to local (**must do this every time before starting anything**)
|git status                                | check status in local _(if you did not add a file to the staging area, this file will be in red text)_  |
|git commit -m "[commit message]"           | commit changes . **Always need to type the commit message for everyone know about what's the new things in your commit** |
|git push origin main                       | push your local content to GitHub _(main)_                   |
|git push origin <branch's name> | push your local content to GitHub _(branch)_  |
|*Solve problem when using pushing code to Github but the previous pull code is not the latest version*||   
|git log |Read and check the difference between local and remote   |
|git reset --soft HEAD~1 |Reset current HEAD to the specified state. Link: <https://git-scm.com/docs/git-reset> |
|git stash |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |
|git fetch |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |

#### Week 39

- Expanded my knowledge with branches 
- Try to catch up and find something I can work on the project.
    Note: Was given instructions to do debugging (though never got to do that since that one teem member decided to do that too).
- Downloaded Docker compose.
- Downloaded Adminer. 
- Read about what docker was and installed the program. 
    - Start to understand the concept of what a container is. (Tried doing one by myself.)

| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git checkout -b <branch's name>             | creat a branch or move to the branch    |
| git checkout -                            | jump between two branches                       |    
| git branch                           | check all the branches on local                    |
| git branch --delete <branch's name>  | delete branch on local                  |
|git branch -a|Confirm Git branch deletion|
|git push origin --delete|Remove a remote Git branch|


#### Week 40:
- Downloaded Docker desktop (https://www.docker.com/products/docker-desktop/).
- Downloaded Docker compose.
- Downloaded Adminer. 
- Read about what docker was and installed the program. 
- Start to understand the concept of what a container is. (Tried doing one by myself.)

#### Week 41:
- Started with my own database using MySQL.
- Trying to do my own take on the project
    Side note: Have been trying to structure the work from the beginning, however one of the members seems to do the project by herself without including the rest of the group. Talked to her and thought wew were on the same page until she eventually did the thing she said I should do. Decided to do my project on the side to show my understanding.
- Test & Debug - Check if vscode can run and debug more than one file and if it can see whether the files work together or not - It can debug more than one only you might need extensions to see if the files work together (not sure if it works for this project however).
        Note: Ended up using pytest to see if it works.
- Installed pytest and ran & debugged project.
- For debuggin I used the test_select_a_column() function and ran the test. I start by connecting to the database using the file path, and then we use a cursor to execute SQL commands. The test then calls another_select_a_column, specifying that it should retrieve all entries from the "name" column in the "burger" table.

The test compares the retrieved data to a known set of values: 'cheese burger', 'fish burger', 'vegan burger'. By seeing whether or not this comparison matches, we can determine if another_select_a_column is functioning correctly. If there’s a mismatch, it could indicate an issue with data retrieval, an error in the column name, or even a problem with the database connection. This test thus provides a quick way to check and debug issues in data selection within the database.

To initiate the debugging process, I inserted breakpoints at pivotal locations in the code housed within the appy.py file, located in the Burger_Orderer directory. These breakpoints targeted key moments in the order submission process:

Handling POST data: The line where the system processes incoming form data (request.form).
Adding product selections: The point where user choices are appended to the order.
Database save operation: The final step where the order is stored in the database.
Debugging Techniques:
Continue: I employed the "Continue" function to execute the code until the next breakpoint, observing where the logic broke down.
Step Over: When validating POST data, I used "Step Over" to bypass function internals and view results at a higher level.
Step Into: For deeper inspection, particularly in suspected faulty validation steps, "Step Into" allowed me to dissect the internal workings of functions.
Step Out: Once satisfied with the internal analysis, "Step Out" returned me to the main code flow.
Variable Tracking and Insights
A critical variable, form_data, became the focal point of my investigation. Initially, this variable was empty, but after processing the form, it was evident that user choices were not correctly mapped. By adding form_data to the debugger’s watch list, I observed its behavior in real time and pinpointed where updates failed.

Analyzing Divergent Code Paths
Testing multiple scenarios revealed deeper insights:

Ordering alternative menus: I tested different menus to confirm whether the issue was isolated to the "done" menu. The problem persisted across all options, indicating a broader flaw in the validation logic.
Order cancellation: Cancelling an order mid-process exposed a complete failure to update form_data, highlighting flaws in handling partial transactions.
- Reflection: The debugging journey highlighted parallels with database testing challenges. Similar to the unpredictability of using live databases, reliance on real-time form data introduced variability. Mocking techniques, as used in database tests, could be adapted here to stabilize form input validation. Implementing controlled test cases would ensure consistent results, enhancing both accuracy and reliability.

This experience emphasized the importance of breakpoint-driven debugging and strategic variable monitoring to diagnose and resolve complex issues, ultimately leading to a more robust and user-friendly ordering system.
     
#### Week 42:
    - Edited my engineering diary and added some final touches.


### Commands I learned but don't remember when I learned them

- All the commands below are from notes taken during the project.  

  
##### Start with Github
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git init                                    | Initialize a local Git repository     |
| git clone <git@github.com:HaileyLV/PA1489-project.git> |Creat a local copy on your computer. Read more: <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>   |



##### Create/remove file, folder 
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|touch <file_name.py]       |Create a python file _(on local_)      |
|mkdir <folder_name]       |Create a folder _(on local)_      |
|git rm [file_name.py]                   |remove a file _(local) _                                      |
|git rm file_name.py.txt         | To remove a file both from the Git repository and the filesystem _(when file has been pushed to Github) _   |
|git rm file_name.py --cached  |  To remove the file from the repository, but keep it on the filesystem _(when file has been pushed to Github)_ |
|git add [file_name.py]                    | add a python file to the staging area _(on local) _     |
|git add -A                 | add all new and changed files to the staging area _(on local)_ **(not recommended because it can lead to commiting/pushing unsued files)**  |



  
| Commands                                  | To do                                             |
| ----------------------------------------- | ------------------------------------------------- |
|cd <path to navigate to the virtual machine installed directory>. Ex: on my laptop: <cd myproject/.venv/bin> With your laptop, it can be diffirence| move to the virtual machine installed directory|
|source activate | turn on the virtual machine|
- Can make an automate.sh to run the docker file more quickly without type every lines in terminal. Run automate.sh with commands: ./automat-run.sh
- Docker commands:

 |Commands                                 | To do                                      |
| ----------------------------------------- | ------------------------------------------------- |
|docker build -t <image's name>:<version> .| Build dockers images. Best att use ex: customer: latest for the images name and version  |
|docker images | Show all images|
|docker run -d --name <containers name> -p <ports> <image's name>:<version> | run the docker image|

### 2. My thoughts about:
#### 2.1. Collaboration:
**- Challenges:** It has been extremely difficult with the groups collaboration, and some of the members inability to work together, as well as following the agreed structure. Also, having done the reading and practice for the different parts of the project without being able to participate has been frustrating.
**- Things that went well:** Understood the concept pretty easily. Learning the things we were doing wasn't that much of a challenge. The course in general was educational. 
**- What need to change next time** Laying down a structure and making sure everyone follows it is so important. Would have been better if we did this course after the Python course. Having some experience within the field of programming could have been of great help. 

#### 2.2. Configuration management
- **Github**: I used GitHub for version control and project management. It has been essential in tracking the development process and ensuring that the codebase remains organized. Though most of this was made from the side due to issues within the team.

Version Control: I learned about creating new branches for feature development, which allowes me to work on specific parts of the project without affecting the main branch. This workflow prevents code conflicts and makes it easier to merge changes once the feature is complete. I tried doing this on a project made by myself.

Collaboration: I pushed my changes to GitHub, which automatically created a pull request. This enables other team members to review my code and provide feedback before merging. It fosters better collaboration and code quality within the team.

Documentation: I also updated the README.md file to include instructions on how to install dependencies and run the project. Having clear documentation makes it easier for anyone joining the project to get started quickly. Also made it easier for myself to see what was beeing done in the project by my team members.

- **Docker-compose**: I researched about Docker Compose that manages the deployment of multiple services for the project. Docker Compose has simplified the process of setting up and running the entire application stack in a consistent, reproducible environment.

Multi-Service Setup: With Docker Compose I was able to define the configuration for both the web application (Flask) and the database (Sqlite) in a single docker-compose.yaml file. This file describes the services, networks, and volumes required for the application to run smoothly.

Service Isolation: Each service runs in its own container, ensuring that dependencies are isolated and the environment is consistent across development, testing, and production. For example, Flask runs in one container while Sqlite runs in another, but both communicate seamlessly through Docker networks.

Automation: By simply running docker-compose up, it starts all services with a single command. This drastically reduced the setup time for new environments and minimized manual configuration errors. If I would make any changes to the configuration, I can easily bring the services down with docker-compose down, adjust the file, and spin them back up.

Volume Management: Docker Compose also handles persistent data storage for the database by mounting a volume for Sqlite. This ensures that even if I stop the containers, the database data remains intact and available for the next run.

#### 2.3. Implementation and documentation:
- Although I wasn't able to participate directly in the hands-on implementation of the main project as much as I would have liked, I focused on deepening my theoretical understanding and experimenting on my own side projects. My contributions to the project were more observational and based on self-guided learning. 

- I spent time studying the core technologies used in the project, including Docker, Flask, and MySQL (as well as Sqlite, but mostly MySQL). I researched how these components interact in a full-stack web application and learned how Docker is used for containerizing applications, MySQL for database management, and Flask for building web interfaces.

- To reinforce my learning, I created small side projects, such as setting up a local environment with Docker and MySQL, where I could experiment with creating and querying databases, similar to what was used in the main project.
- While I wasn’t actively documenting the main project, I compiled notes and learning materials based on my research and personal exploration. These notes cover Docker, Flask, MySQL, and Git, and provide an overview of the concepts I learned in theory.

Despite my limited hands-on involvement in the project, I was able to gain valuable theoretical knowledge and apply it in a smaller scope. This experience has prepared me for more active participation in future projects, as I now have a clearer understanding of the underlying technologies.
