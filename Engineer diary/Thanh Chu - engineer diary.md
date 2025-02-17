# **This is the programmer diary I write every day, every week**

## Content in file:
- .1. Summaries of the work
   + a. The things I have done every week:
   + b. The things I have learned every week
- .2. My thoughts about:
   + a. Collaboration
   + b. Configuration management
   + c. Implementation and documentation
   + d. Testing and debugging (include debug sections)
#### I updated the file daily, weekly from the beginning of the project but as of Oct 11th have renamed, moved files and completely restructured the file, so you may not see that in the Blame section or histories.

## 1. Summaries of the work
### a. The things I have done every week: (update planning, engineer diary)
#### Week 35+36: 
  - Create many documents in Github to update the work: readme, planning, reflecktion, engineer diary
  - Learn about Github.
  - Create Github accounts and GitHub repo. Link: <https://github.com/HaileyLV/PA1489-project.git>
  - Try to start with Github
#### Week 37:
- Learn about md syntax. Link: <https://www.markdownguide.org/basic-syntax/>
- Draw a draft design <https://app.moqups.com/CNsCqWOjxAXBnT1q7BVJIuRvwCjqD6zl/view/page/ad64222d5>
#### Week 38:
- Learn about Flask and download the software. Link: <https://flask.palletsprojects.com/en/3.0.x/installation/>.
- Set the SSH keys to Github. Come to Settings -> SSH and GPG key Link <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account> and <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>
- Learn about Flask commands to create a simple application. Link: <https://www.geeksforgeeks.org/flask-creating-first-simple-application/>
#### Week 39
- Download and use FLask-Menu to code. Link <https://flask-menu.readthedocs.io>
- Work together with team to release _BurgerOrderer (BO) and KitchenView (KV)_ version 1 and 2.
  
| Version 1                                 | Version 2                                         |
| ----------------------------------------- | ------------------------------------------------- |
|Use buttons to save orders| Use check-boxes to temporarily record the user's choice |
|The order is recorded after each click so user can not change their choices | The order is only actually saved when user click on "Order Now" button so they can make change before this action|
|It is possible to move bach and forth between BO and KT through the "Go to kitchen" and "Back to order" links. BO and KV 2 parts of 1 program. | BO and KV are 2 separate programs that point to the database _(set up with hardcode, not yet complete)_|
|The kitchen receives all orders in an unnumbered list | Orders are managed by customer name _(need to check if programs crashes when customer have the same name)_|

- Learn about using a virtual machine
#### Week 40:
- Download and try to learn how to use Docker Desktop. Link <https://www.docker.com/products/docker-desktop/>
- Download Docker compose
- Download Adminer
- Docker commands
#### Week 41:
- Work together with team to release product version 3
  
| Version 3                                 | Version 2                                         |
| ----------------------------------------- | ------------------------------------------------- |
|Use dropdown lists to temporarily store user selections. Menus pulled from database. Have actual database files with tables and relations.| Use check-boxes to temporarily record the user's choice. Menu is only hard code. Database had been created by manual code in .py file, had no tables or relations |
|The orders will be sent to the database and save to tables | The order will be sent to the database file without tables|
|The kitchen receives the beautiful order with all information | Orders are managed by customer name _(need to check if programs crashes when customer have the same name)_|
- Database with help by DB browser for SQLite
- Rewrited Docker-compose file, Docker file and Requirments: add database and pytest
#### Week 42:
- Use pytest to test and debug: link: <https://docs.pytest.org/en/stable/getting-started.html>
- Finish with engineer diary
- Check all things and submit submissions
- Create setup.py

### b. The things I have learned every week:
#### Week 35 - 39:
- Learn about necessary material that need to know: Github, markdown, app.moqups, flask.
- Github command:
  
##### Start with Github
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git init                                    | Initialize a local Git repository     |
| git clone <git@github.com:HaileyLV/PA1489-project.git> |Creat a local copy on your computer. Read more: <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>   |

##### Work with branches:
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git checkout -b <branch's name>             | creat a branch or move to the branch    |
| git checkout -                            | jump between two branches                       |    
| git branch                           | check all the branches on local                    |
| git branch --delete <branch's name>  | delete branch on local                  |
|git branch -a|Confirm Git branch deletion|
|git push origin --delete|Remove a remote Git branch|

##### Creat/remove file, folder 
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|touch <file_name.py]       |Create a python file _(on local_)      |
|mkdir <folder_name]       |Create a folder _(on local)_      |
|git rm [file_name.py]                   |remove a file _(local) _                                      |
|git rm file_name.py.txt         | To remove a file both from the Git repository and the filesystem _(when file has been pushed to Github) _   |
|git rm file_name.py --cached  |  To remove the file from the repository, but keep it on the filesystem _(when file has been pushed to Github)_ |
|git add [file_name.py]                    | add a python file to the staging area _(on local) _     |
|git add -A                 | add all new and changed files to the staging area _(on local)_ **(not recommended because it can lead to commiting/pushing unsued files)**  |

##### Pull och push from local to Github:
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|git pull                   | pull code from remote to local (**must do this every time before starting anything**)
|git status                                | check status in local _(if you did not add a file to the staging area, this file will be in red text)_  |
|git commit -m "[commit mesage]"           | commit changes . **Always need to type the commit message for everyone know about what's the new things in your commit** |
|git push origin main                       | push your local content to GitHub _(main)_                   |
|git push origin <branch's name> | push your local content to GitHub _(branch)_  |
|*Solve problem when using pushing code to Github but the previous pull code is not the latest version*||   
|git log |Read and check the difference between local and remote   |
|git reset --soft HEAD~1 |Reset current HEAD to the specified state. Link: <https://git-scm.com/docs/git-reset> |
|git stash |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |
|git fetch |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |
|git stash pop |Apply the changes as well as remove stored files from stash area.. Link: <https://git-scm.com/docs/git-stash> _(then check git status och use git add, git commit -m, git push origin...) _  |
- Solve problem when using pushing code to Github but the previous pull code is not the latest version: See section "Pull och push from local to Github" 
- **Issue:** the Deleted BurgerOrderer (BO) branch directly from the Github screen without reading the message from the terminal window. This resulted in the BO branch on the local but not on the remote, user lost connection with the remote and could not pull or push the code. Solution: evaluated that user did not use this branch locally, so user deleted it locolly and pulled from Github again. Lear more how to delete a branch on local and on remote. See section "Work with branches" 
#### Week 40:
 - Virtual machine
**- How to activate virtual machine from terminal/iTerm...with Mac:**
  
| Commands                                  | To do                                             |
| ----------------------------------------- | ------------------------------------------------- |
|cd <path to navigate to the virtual machine installed directory>. Ex: on my laptop: <cd myproject/.venv/bin> With your laptop, it can be diffirence| move to the virtual machine installed directory|
|soucre activate | turn on the virtual machine|
- Can make an automate.sh to run the docker file more quickly without type every lines in terminal. Run automate.sh with commands: ./automat-run.sh
- Docker commands:

 |Commands                                 | To do                                      |
| ----------------------------------------- | ------------------------------------------------- |
|docker build -t <image's name>:<version> .| Build dockers images. Best att use ex: customer: lastest'for the images name and version  |
|docker images | Show all images|
|docker run -d --name <containers name> -p <ports> <image's name>:<version> | run the docker image|
#### Week 41:
- SQLite commands:
  
|Commands                                 | To do                                                |
| ----------------------------------------- | -------------------------------------------------  |
|CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT); | Create a table named test, if it was not exists in database with two elements: id and name.|
|DROP TABLE IF EXISTS test; | Drop a test table if it was exists in database |
|SELECT name FROM sqlite_master WHERE type = 'table' AND name='test';| Check the positions of table if it exists in database. Returns None if the table does not exist in the database |
|select * from burger b join order_burger ob on b.id = ob.burger_id join orders o on ob.order_id = o.id join items i on ob.items_id = i.id where o.id = ? |Join data in table burger with tabler order_burger, table items with table order_burger based on burger_id, order_id, items_id |
|INSERT INTO burger (id, name) VALUES (1, "cheese burger") | Insert a row in table burger with two elements: id = 1 and name = cheese burger|
|('SELECT id FROM items WHERE name = ? AND type = ? AND action = ?',(item_name, item_type, action)) | pull data of item_name, item_type, action based on items_id|
|('INSERT INTO order_burger (order_id, burger_id, items_id) VALUES (?, ?, ?)',(order_id, burger_id, item_id))|insert input data to database|
|with sqlite3.connect('orders.db') as conn:...|use this code to open database so that database will be closed outside "with"|
- Docker-compose file.
  Docker compose commands:

|Commands                                 | To do                                      |
| ----------------------------------------- | ------------------------------------------------- |
|docker-compose up|run docker compose file to run all applications in this file. Need to cd to the folder that contains docker-compose file. |
|docker rmi -f customer:latest kitchen:latest && docker-compose up| run docker compose file if you have build and used images before|

#### Week 42:
- Need to set up logging. Very helpful for debug. Print out to console with command: app.logger.info("Burger: %s", burger). Don't need to write ""Burger: %s"," but it's easier to read when it have many row will be printed to console.
- Run pytest from terminal: pytest <pytest file name>
   + Use "@pytest.fixture" for beginning a function if want to define a reusable setup for testing
   + A test function start with "test"
   + Set up a function to connect to the database in an other folder: def db_connection()
- Setup.py
Setup.py commands:

|Commands                                 | To do                                      |
| ----------------------------------------- | ------------------------------------------------- |
|python setup.py install|installs the package by copying its files into your Python environment|
|python setup.py develop|install my package in development mode|
 
### 2. My thoughts about:
#### a. Collaboration:
- **Chalenges**: We have 5 members in the team. All of us are new, and none of us had any programming experience. Faced with a project that was far beyond our skill level and imagination, we were really discouraged. We had to constantly motivate each other and work hard to learn or search for the necessary knowledge. Together, we helped each other find information, create accounts, download software, and more. By supporting each other, we felt more confident and capable.
- **What went well**: We planned to meet together min two times per week but it's not working so well in the beginning. We have different circumstances. As I need to take care of my family so I usually study from 8-12, 13-15 and 20-23. During the work, unfortunately, many of our members got sick. We changed to another way to connect to each other with another ways: via zoom, discord. I tried to write everything and push to Github so everyone could read about what we did this week, what we will do next week etc... It worked. We splited the work, worked at different times and everyone tried to be part of the project.
- **What need to change next time** We had absolutely no idea about the workload, the work sequence, and no one had enough experience to be a team leader, so we struggled to understand the project. I think each of us learned certain lessons after this project. With me, the most important things need to do first is the process. 
#### b. Configuration management
- **About Github**:
   + _What went well_: We have lerned how to get famliar with Github. Not really proficient and professional bur already know a certain number of commands related to Github, enough for our project.
   + _What went less well_: It took us a while to start using GitHub effectively. We only recently gained a better understanding of how branches work. Since we mostly meet to make decisions together, we probably encounter and resolve fewer problems than others might. We haven't fully established a proper review and commit approval process. Often, the same person who created the merge request also approved and merged the code. Additionally, we frequently pushed code directly to the remote repository and merge it into the main branch.
   + _What need to change next time_: For our next project, we should aim to be more proactive and engage with GitHub earlier in the process to build deeper familiarity with its features.
- **And Markdown**: In the beginning, our vision for the project was very different from reality. We drew a schematic design of a burger ordering website (check out Planning for that cool design if you're interested) and even considered details like adding ice to drinks to make the website feel more realistic. However, the implementation turned out to be too difficult. When we started working, we had little knowledge, so we had to change the design multiple times. We used .md files for weekly planning, documenting everything we learned so that everyone on the team could refer back to it and practice whenever they wanted—like our own project dictionary. This made things easier.
- **About docker-compose**: When we had the first product, we put all the files in the same folder. Then we learned that we need to do two separate programs. We split them but the problem was that we needed to link the BurgerOrderer app and the KitchenView app to the database. We ran docker and an automate.sh file (to automatically run docker commands on ther terminal).  But the difficulty was that the path to the file on each machine was different. We were suggested to use _Docker Compose_. It really worked.
#### c. Implementation and documentation:
- **I have learned much during the work**. For examples: I understand a lite bit why our teacher asked us to do that:
   + a container based platform, with separate containers for BurgerOrderer, KitchenView, and MenuStore => to manage code easier and it is the reason why we need to learn how to use Docker-compose.
   + using docker and requirements => to ensure the user environment is consistent with the environment in which we build the product.
   + using setup.py (like package.json in Java and Javascript) som a external library.
- **Short summary of what I have implemented:**
   + _The project as a whole_: I and my team work together to build two web clients that customer can order burger and people in kitchen can see the burger orders, and a database that contains information about each type of goods.
   + _Each container, each module_. What are they used for? You can know about it when you see our project's tree:
```
Containers: Our project, of course
│   ├── BurgerOrderer
│   │   ├── BO_test.py: File test for modul app.py
│   │   ├── Dockerfile: To built and run a customer's image
│   │   ├── app.log: File we have after set up logging to debug. We use commands: app.logger.info many times during working to print. It's very helpful to debug.
│   │   ├── app.py: A back-end file? We built it to take information from database, collect orders and sent orders to database
│   │   ├── requirements.txt: All needed applications to ensure the program runs in the same environment as when we built the product.
│   │   └── templates: All front-end files for Burger Order
│   │       ├── error.html: Error screen during execution. We put a lot of try-except to catch errors and throw it to the error screen. Here, the customer can press return to the main screen and start over. The program will be not crash by it.
│   │       ├── index.html: Simple CSS to make the home page a little nicer.
│   │       ├── main_menu.html: Burger order page. When the customer clicks on the burger type, the information is temporarily saved, the home page switches to the topping page for the customer to continue choosing the toppings and options for the burger.
│   │       ├── topping.html: Customer choose options to burger. The customer can return to the previous page by clicking the "Go back" button and "Submit" to sumbit the order.
│   │       └── order_done.html: After the customer clicks submit in the topping page, the burger information and options are collected and sent to the database. The order notification page has been collected. The customer order more py clicking the "Click here if you want to order more" button.
│   ├── KitchenView
│   │   ├── Dockerfile: To built and run kitchen's image
│   │   ├── app.py: A back-end file to Kitchen. It used to receive infomation from database and print on the customer scrren.
│   │   ├── requirements.txt: All needed applications to ensure the program runs in the same environment as when we built the product.
│   │   └── templates
│   │       └── kitchen.html: The kitchen can view orders or delete them if desired
│   ├── MenuStore
│   │   ├── db_test.py: test database with pytest
│   │   ├── orders.db: database with SQLite (we used DB Browser for SQLite to built it)
│   │   └── orders.sqbpro: A executable file rendered by DB Browser for SQLite to when we use it to built database
│   ├── PA1489.egg-info: The folder and all files was automatically created when running the setup.py command
│   │   ├── PKG-INFO
│   │   ├── SOURCES.txt
│   │   ├── dependency_links.txt
│   │   ├── entry_points.txt
│   │   ├── requires.txt
│   │   └── top_level.txt
│   ├── README.md: The file with tree diagram of folders and file locations in Containers
│   ├── build: The folder and all files was automatically created when running the setup.py command.
│   │   └── bdist.macosx-10.9-universal2
│   ├── dist: The folder and all files was automatically created when running the setup.py command.
│   │   └── PA1489-0.1-py3.9.egg
│   ├── docker-compose.yaml: One for all. Run this file to define and run multi-container Docker applications.
│   └── setup.py: a central part of packaging a Python project. It defines metadata about the project (such as name, version, and author) and instructions on how to install the project and its dependencies. I copied this sentense from internet. I understand only that is's importand and helpful.
```
- **My experiences of conducting the project**.
   + **What went well**:
      + We have fulfilled most of the requirements of the assignment:
           + We use a single command to run the project**: docker-compose command. <docker-compose up> or <docker rmi -f customer:latest kitchen:latest && docker-compose up>
           + We have list types of burgers and options can see all different type as retreived from the MenuStore database. Our database is full of information, defining the types of coponents and the relationships betwwen them.
           + User can search database MenuStore contains infomation about the different type of goods and is being used by BurgerOrderer.
           + Customers can order burger, add or remove items, get the choice of options and drink. Then the order will be sent to database.  Order id is automatically numbered with function lastrowid.
           + KitchenView receives the orders, prints them and can delete them. When user delete orders in KitchenView, all information of order will be removed in database.
           + Use many try-except to catch and show errors. Customers can return to the main screen from the error screen and re-excute the transaction, the program is not interrupted.
   + **What did not go well?**
      + Most of our code was collected from many sources, under our efforts to learn, but there were still may limitations. Therefore, our code maybe has many duplicates, redundancies, omissions and imperfections. Howerver, we tried to do the best we could.
      + We don't have a good process, the division of work is not clear, so there is a lot of duplication. It took times but the efficiency was not high.
   + **How did you solve your challenges? What could you have done differently**?
      + The first challenge was that we had just started learning python when the project started. There was one team member who knew CSS and HTML. So it took us very long time to figure out what to do. Since we did not know where to start, we just coded the same functions at the same time. Then we showed it to each other and chose the best on to work on. This made the project progress very slow but we learned a bit more.
      + When we had our first product, we did not understand the assignment requirements properly so we only wrote code for one single application code for the whole product. Therefore, we had to re-edit the entire code.
      + When we finished version 2, we had to run two applications on two different text-based interfaces (iTerm and Terminal). Then we learned about Docker.
      + Finally is database. We chose SQLite instead of NoSQL because it gave us chance to pratice with database before the following courses. We spent a lot of time figuring out how many tables we needed, what the relationships were between the columns in the tables, and what joins commands we needed to use. It'difficult and confusing during working with database so we used many times command app.logger.info to print data and edited it to fit our needs.
   + **What did you not manage to solve? Why not?**
      + We understod that it was not mandatory to use REST API completely for the whole project, so we use REST API to collect orders, the rest, we use Jinja2 template. It's much more familiar, convenient and easty to learn and use for newbies like us. But we will learn more about REST APT after this course.
      + There are many things we wrote that are not complete, I will come back to this exercise when I know more about programming. I guess that it will be intresting to see the lines I have coded nowaday.
      + The process. We did not have a good process. In the next project, we need to pay more attention to establishing the implementation process before starting to work.
- **My experiences of working with containers**.
   + **What went well**?
        + We learned how to work with containers and ran the produckt with two applications located in two containers BurgerOrderer and KitchenView, while the database is in MenuStore.
        + We know lite about how to buid a docker file, docker-compose and how to run it.
   + **What did not go well**?
        + Like I wrote above, we are new developers so out code still has many problem.
   + **How did you solve your challenges? What could you have done differently**?
      + The challenge was when the app.py files were located in two different folders and database was in MenyStore. We found a way to create vitual databases in BurgerOrderer and KitchenView and built docker images, created an automate.sh file to run one command for all. However, the problem was that the path to each person's file database was different so it did not work as we expected. We were recommended by the teacher to use docker-compose. It worked.
   + **What did you not manage to solve? Why not**?
      + We tried out best to complete the assignment with the best quality with our current level. Some functions we have thougt of but dare nor risk implementing when the time for the project was not much. We may come back and implement it after this course.
#### d. Testing and debugging
- **Test**: I use Pytest to test with some functions som contact to the database:
   + 4 test with database: I sat up a function to connect to the database in an other folder: def db_connection(), then tested if a table exist/not exist in database and test to create and drop a table in database.
   + 2 test with BurgerOrderer: tested function select_a_column and function index in BurgerOrderer. I used the relative path from the BurgerOrderer folder to MenuStore during this test.
```
     db_path = os.path.join(os.path.dirname(__file__), '..', 'MenuStore', 'orders.db')
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    yield cur
    con.close()
```

   + All my test failed in the beginning because I did not set up a function to connect to the database (with 4 test) and did not use the relative path from the BurgerOrderer folder to MenuStore (with 2 test). But they were all pass after I edited the codes.
      + **What went well**: I know how to use Pytest and could write a few test case.
      + **How did you solve your challenges? What could you have done differently?**
         + When I started write som test cases, all of them failed. I tried to set up a function to connect to the database and use the relative path from the BurgerOrderer forder to MenuStore. It worked.
         + Our functions are grouped quite a lot so testing is also more difficult. I have splitted the function to make it easier to test and I could write two test with BurgerOrderer because of it.
      + **What did you not manage to solve? Why not?**
         + We started with assignment 3 very late. The time was too urgent so I could not perform as many test cases as expected. In the next project, we had to adjust the time estimate.
         + I wanted to test creating and sending orders to the database but out order_id is automatically generated, so I had not dared to try, afraid of conflicts.
         + My test in BurgerOrderer are all hard-code tests. It the user changes the details in database, my tests are no longer valid. I still do not know if there is a way to fix these things.
- **Debugging section**:
   - **Reflections:**
     - **What went well**: I fixed all bugs that I found and the program ran fine without errors or bugs when we ran and tested it.
     - **How did you solve your challenges? What could you have done differently?**
        - I ran  "run and debug" in VS code everytime I done something new, tried to understand the error message, found bugs and fixed it. It became useful tool for me mostly when I started coding individual python files, especially when I "step into" and follow the changing values of variables, functions to find the error. But it became harder when we had a database and slited two applications into two separate containers. I use logger instead to print everything out to localize and find the error. I printed everything with the name of variebel so I could control which was right and wrong.
             - For example: app.logger.info("Burger: %s", burger)
        - Besides that, I use try-except to catch the fail and avoid program interruption. It's also very helpful.
      - **What did you not manage to solve? Why not?**
        - Updating the debug section became very difficult because I did not do it from the beginning, when errors occurred continuously and we struggled to find the error and fix it. I only did it when I was near the end of the project, so I missed many cases to update. When the program was running well, sitting down to remember the exact error as well as the code I did wrong and how to fix it was really a challenge.
        - The exprerience is that next time, I need to read the requirements more carefully so as not to miss the requirements at the last minute like this.
   - **Details on what is being debugged:**
####  **OCTOBER 1, 2024**
- **Debug purpose**: Ran the program, got the error message: tuple index out of range
     ```
   File "/app/app.py", line 72, in index
   def index():Open an interactive python shell in this frame
       # Using a context manager for the database connection
       try:
           listBurgerData = select_a_column ('name', 'burger')
           # Use list comprehension to fetch and create the list
           listBurger = [name[1] for name in listBurgerData]
      ```
- **Breakpoints Set**:
     - Line 70: when the listBurgerData is retrieved from the database.
     - Line 72: when the listBurger is collected
- **Variables Monitored**: listBurgerData, listBurger
- **Debug Process**:
     - Line 70: listBurgerData = [('cheese burger',), ('fish burger',), ('vegan burger')]
     - Line 72: listBurger: index name[1] out of range. Reason: name = ('cheese burger',): name is a tuple that has only one element so that name[1] is out of range.
- **Results**: Changed the index [1] to [0], then it worked.  
         
####  **OCTOBER 2, 2024**
- **Debug purpose**: Check the reason why the order, that was printed in KitchenView, was incorrect.
   - _The order collected in BurgerOrderer was_:
     ```
      Burger: CHEESE BURGER, Added Items: vegan cheese, Removed Items: salad, Added Sides: chicken nugget, Drinks: coca-cola, Order_ID: 159
      ```
   - _But the order we had in KitchenView was_:
      ```
      Order ID 159 : (Order content: Burger: (1, 'CHEESE BURGER', 'INCLUES: CHEESE, HAMBURGER, SAUCE, SALAD', 159, 1, 5, 159, 'NOT DONE', 5, 'VEGAN CHEESE', 'ITEMS', 'ADD')) : (Options: cheese burger | inclues: cheese, hamburger, sauce, salad | 159 )
      ```
- **Breakpoints Set**:
     + Line 20: when the order was collected before join
     + Line 29, 30: during the order was collected after join
     + Line 35: when the order collected
- **Variables Monitored**: 'result' and 'result_items'. Check the elements in the result and the result_item list to get the exact position of the elements to collect the correct order. 
- **Debug Process**:
     - Line 20: list was created. result = []
     - Line 29:
       ```
         result_item = [159]
         result = []
         ```
     - Line 30:
       ```
         result_item = [159, 'cheese burger']
         result = []
         ```
     - Line 35: 
         ```
         result_item = [159, 'cheese burger', 'vegan cheese', 'ITEMS', 'ADD', 'salad', 'ITEMS', 'REMOVE', 'chicken nugget', 'SIDES', 'ADD', 'coca-cola', 'DRINKS', 'ADD']
         result = [[159, 'cheese burger', 'vegan cheese', 'ITEMS', 'ADD', 'salad', 'ITEMS', 'REMOVE', 'chicken nugget', 'SIDES', 'ADD', 'coca-cola', 'DRINKS', 'ADD']]`
         ```
- **Results**: Count the index of all elements in the list, fix the position of the elements tobe printed in the KitchenView scrren:
         ```
         Order ID 159 : (Order content: Burger: CHEESE BURGER) : (Options: add items : vegan cheese | remove items : salad | add sides : chicken nugget | add drinks : coca-cola) )
         ```
#### **OCTOBER 11, 2024**
- **Debug purpose**: tried to run test cases but all test cases fail, had a problem with error message:
```
  file /Users/chuhathanh/Workspaces/Thanhs Workspaces/PA1489-project/Containers/MenuStore/db_test.py, line 4
  def test_table_orders_exist (db_connection):
E       fixture 'db_connection' not found
>       available fixtures: _configure_application, _monkeypatch_response_class, _push_request_context, accept_any, accept_json, accept_jsonp, accept_mimetype, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, client, client_class, config, doctest_namespace, live_server, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, request_ctx, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.`
.....
```
- **Breakpoints Set**: line 4
- **Debug Process**: I imported 'pytest fixtures' function to build the connect to database.
- **Result**: After done with the solution, all tests passed.
- **References**: https://stackoverflow.com/questions/35337704/how-to-open-a-file-by-its-path-relative-to-the-python-module-when-that-module-i
