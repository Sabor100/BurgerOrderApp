# **Reflections 1**

## **1. Name of everyone in the team:**
    - Ebba Bengtsson
    - Hailey Lundkvist
    - Sabor Ahmad Khowajazada
    - Thanh Chu
    - Wilma Eriksson
## **2. Link to the project's page on the git server:**
https://github.com/HaileyLV/PA1489-project.git

## **3.Assignment:**
### *3.1. Short summary about what configuration management is and why it is used:*
Configuration management is about managing and controlling software configurations in a project. It is used to ensure that all components are at the correct version and work together, reducing the risk of errors and conflicts.
- _Version control system (VCS)_: we chose _Git_ as our VCS to host, manage, track and update our project. The web-based platform we used to build our product is Github, a very good platform that facilitates managing and hosting projects with Git. Moreover, Github is open for everyone, free, popular, easy to register and use, and widely supported in the industry, making it the ideal choice for our project. Besides that, Github provides tools for collaborativ development, allowing multiple people to work on projects simultaneously, by offering features like pull requests, branch management, and conflict resolution. GitHub also enhances teamwork and reduces the risk of errors when merging code.
- _Application Configuration_: _Docker compose:_ Our teacher recommended Docker Compose when we had trouble running our project, where two .py files were in separate folders, and the database was in another folder. Docker Compose helps manage these multiple components (like services, databases) by defining them in a single configuration file, allowing everything to run together seamlessly.
- _Documentation Tools_: We decided to use _Markdown_, which was also recommended by our teacher, for project documentation. It is a lightweight, easy-to-learn markup language used for creating formatted text with plain text editors. Markdown is popular because it is simple, efficient, and readable in both its raw and rendered forms. Additionally, it is well-integrated with GitHub, allowing us to maintain clear and concise documentation directly within our repository. It helps us document changes, provide guidelines, create plans, write engineering diaries, and generate README files in a format that is universally recognized and recommended for clarity.

### *3.2. Short summary on the most common workflow with git, including the git commands used:*
The most common workflow with Git includes steps such as cloning a repository, creating a new branch (branch), making changes, committing (commit) the changes and finally sending them to the main branch (merge). Important commands include git clone, git checkout, git add, git commit, and git push.
- **_With Markdown files_**: We edit directly on GitHub, which has an integrated preview feature in the editing process. GitHub offers a built-in editor with a live preview, making real-time editing and review convenient. This simplicity and integration make it our preferred choice for handling documentation files.
- **_Other files_**:
    + In our workflow, when handling tasks independently, we created branches, pushed code to them, and submitted pull requests for review by all team members before merging.
        + Initially, we created three separate branches to work on. However, for various reasons, we decided to remove two of them and focus solely on the _BurgerOrderer_ branch. This branch was used to upload and modify code related to the Burger Order and Kitchen View.
        + Once we reached the database integration phase, we created a _database_ branch to continue developing the Burger Order and Kitchen View while simultaneously working on the Menu Store functionality.
        + Finally, we created a third branch when the product was nearly complete with all its core components but still needed a few feature fixes.
    + When we meet or communicate via Discord, we discuss our progress and share our achievements. Once we agree on the changes, we push them directly to the main branch. This workflow ensures smooth, organized collaboration while minimizing merge conflicts.
- **_Github command_**:
### Start with Github
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git init                                    | Initialize a local Git repository     |
| git clone <git@github.com:HaileyLV/PA1489-project.git> |Creat a local copy on your computer. Read more: <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>   |

### Work with branches:
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git checkout -b <branch's name>             | creat a branch or move to the branch    |
| git checkout -                            | jump between two branches                       |    
| git branch                           | check all the branches on local                    |
| git branch --delete <branch's name>  | delete branch on local                  |
|git branch -a|Confirm Git branch deletion|
|git push origin --delete|Remove a remote Git branch|

### Creat/remove file, forder 
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|touch <file_name.py]       |Create a python file _(on local_)      |
|mkdir <forder_name]       |Create a forder _(on local)_      |
|git rm [file_name.py]                   |remove a file _(local) _                                      |
|git rm file_name.py.txt         | To remove a file both from the Git repository and the filesystem _(when file has been pushed to Github) _   |
|git rm file_name.py --cached  |  To remove the file from the repository, but keep it on the filesystem _(when file has been pushed to Github)_ |
|git add [file_name.py]                    | add a python file to the staging area _(on local) _     |
|git add -A                 | add all new and changed files to the staging area _(on local)_ **(not recommended because it can lead to commiting/pushing unsued files)**  |
|-rm -rf .git                | delete all hidden files on git |
 

### Pull och push from local to Github:
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|git pull                   | pull code from remote to local (**must do this every time before starting anything**)
|git status                                | check status in local _(if you did not add a file to the staging area, this file will be in red text)_  |
|git commit -m "[commit mesage]"           | commit changes . **Always need to type the commit message for everyone know about what's the new things in your commit** |
|git push origin main                       | push your local content to GitHub _(main)_     |
|git push origin <branch's name> | push your local content to GitHub _(branch)_  |
|*Solve problem when using pushing code to Github but the previous pull code is not the latest version*||   
|git log |Read and check the difference between local and remote   |
|git reset --soft HEAD~1 |Reset current HEAD to the specified state. Link: <https://git-scm.com/docs/git-reset> |
|git stash |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |
|git fetch |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |
|git stash pop |Apply the changes as well as remove stored files from stash area.. Link: <https://git-scm.com/docs/git-stash> _(then check git status och use git add, git commit -m, git push origin...) _  |
### *3.3. Your experiences of working with configuration management:*
- **What went well?** We managed to keep track of changes to the code and coordinate my efforts with the team. 
    + We have lerned how to get famliar with Github. Not really proficient and professional bur already know a certain number of commands related to Github, enough for our project.
    + It works very nice with Markdown. We used it a lot in the project with many filer: readme, planning, reflection, engineering diary...
    + When we had the first product, we put all the files in the same folder. Then we learned that we need to do two separate programs. We split them but the problem was that we needed to link the BurgerOrderer app and the KitchenView app to the database. We ran docker and an automate.sh file (to automatically run docker commands on their terminal).  But the difficulty was that the path to the file on each machine was different. We were suggested to use _Docker Compose_, and it worked well.
- **What went less well?**
     + In the beginning, we struggled to understand the project, the workload, and how to organize our work, as no one had enough experience to lead the team. We lacked an effective process, which ultimately hindered progress and is something we need to improve for future projects.

     + Team members struggled to work together effectively, which led to a lack of commitment from everyone involved. This lack of alignment slowed down our progress and negatively impacted the project's success. Additionally, since no one had formal education in programming, starting the project was particularly difficult. We faced challenges in knowing where to begin, how to divide tasks, and how to work efficiently. As we had no prior programming experience, we were learning everything as we progressed, which resulted in varying levels of understanding within the group. Those who were able to advance more quickly often ended up doing most of the work, creating disparities within the team. The sheer amount of information was overwhelming, especially for beginners, adding significantly to the challenge.

     + We also faced challenges with GitHub. Initially, everyone committed to the same main branch, which led to issues when changes were pulled and integrated. This caused conflicts and delays. Later, we started using branches, which helped a lot in reducing these problems and improving our workflow. For our next project, we aim to utilize these features from the start.

     + Our meeting schedule didn't work as planned due to differing personal circumstances and illness. We adapted by switching to Zoom and Discord meetings and documenting everything on GitHub so everyone could follow our progress. This helped us stay on track despite the challenges.

     + Our original vision for the project was too ambitious. We designed an advanced burger ordering page, but the implementation turned out to be too complex. We simplified the design multiple times and used Markdown files for weekly plans, which made it easier to keep track of our progress and learn together.

     + We also split the program into two separate apps: BurgerOrderer and KitchenView. Linking these to the database was challenging since we used Docker and an automation script, which became complicated due to different file paths. Switching to Docker Compose helped resolve these issues.
    
- **How did you solve your challenges? What could you have done differently?**
     + Due to our inexperience, we initially felt overwhelmed. However, we supported each other, collaborated, and shared knowledge, which helped us move forward. We assisted each other in setting up software and documenting our progress, which boosted our confidence.

     + We recognized the need for clearer roles and responsibilities, which we gradually established by assigning specific tasks to different team members. This improved our efficiency, even if it took time to implement.

     + Our version control and merge request process were disorganized. Initially, everyone committed directly to the main branch, causing conflicts when merging. We later introduced branches, which significantly improved our workflow. For our next project, we need to establish a structured review process to ensure better quality control.

     + Despite the difficulties in keeping regular meetings, we switched to digital platforms and documented our work thoroughly, which kept everyone informed even if they couldn't attend meetings.

     + Our ambitious design had to be simplified as we realized our technical limitations. Using Markdown documentation helped us maintain a common reference point, making the work more manageable.

     + Docker Compose became a crucial solution for integrating our two apps, significantly simplifying the development process.

- **What did you not manage to solve? Why not?**
     + We have yet to implement a proper review and commit approval process. Often, the same person would create, approve, and merge, merge requests, and we tended to push code directly to the main branch. These issues stemmed from our lack of experience and insufficient planning.
