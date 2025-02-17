# **diary layout**

1. Weekly Report
 * what i learned
 * meetings
 * what i did

2.What I learned, in more detail:

 * github
 * html and css
 * python in a working invierment
 * flask app
 * adminer
 * id
 * session
 * running your app
 * docker file docker compose
 * debugging
 * mock

3. what i thought about the project:
   
 * what went well
 * what went less well
 * Next time
--------------

# **diary**

# **v.35**

walk-through:

For the upcoming two weeks, we’ve been instructed to complete the following tasks:

* Form a group of 3 to 5 members.

I’ve already teamed up with Hailey, and over the next week, 
we’ll be working on recruiting one or more additional members, 
as the group needs to have at least three people.

Additionally, I’ve set up my computer for the course and created a GitHub account to manage our projects.

# **v.36**

This Week's Progress:

We found three more people who needed a group, so we formed a team of five members.

To stay in touch, I created a group on Discord for easy communication.


Meeting 1:

In our first meeting, we introduced ourselves and got to know each other a bit. 
Hailey set up a project on GitHub and shared it with everyone for collaboration.

Project Task Distribution:

We decided to divide the project into the following sections:

Main Menu: Sabor

Burger Order

Hamburger: Thanh

Choices: Ebba & Hailey

Sides: Wilma

Kitchen View: Sabor, Thanh

# **v.37-38**

v.37

 * What i learned:
            
I gained knowledge in using Markdown, App.Moqups, Flask and branches.
started to look att html and css.

I also learned about essential tools and resources, such as GitHub, that are crucial for the project.


 * What happen in the group:

Our group agreed to use Python as our programming language, VS Code as the development environment, and GitHub for version control. 
These decisions could be changed.


meeting 2:

This week, we decided to focus on learning Python, 
as we didn’t have enough information to start the main project.

In our Discord group, one member suggested changing our approach to task division, 
preferring that we work on everything together. 
I proposed that we discuss this further as a team during our next meeting.


 * What i did:
   
Learn about Flask and download the software.
Practice pulling and pushing data from each person's computer to Github. (created my own github project so i would not disturb our project)
Code BurgerOrderer and KitchenView

v.38

 * What happen in the group:

At our next meeting, I found out that two group members had already completed most of the burger-order section, even though we hadn’t agreed to start yet. 
Our original plan was to wait another week so we could gather enough information to work on the burger-order together.

They suggested I work on adding a feature to remove items from the burger. 
I spent the next week preparing my own GitHub solution to demonstrate how we could implement it. 
However, when they showed their progress at the next meeting, they had already completed the task.


what I have done in my Burger-app:

made a running website. 

Used wsl, html and pip flask.

python def

litle bit of dockerfile 


 * What i did:
            
how to get github to terminal:

ssh key

git init -> Initialize a local Git repository

git clone <git@github.com:HaileyLV/PA1489-project.git> Creat a local copy on your computer. 

Read more: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

----

Github command:

git checkout -b <branch's name> creat a branch or move to the branch

git checkout - jump between two branches

git branch -> check all the branches on local

git branch --delete <branch's name> delete branch on local 

git branch -a -> Confirm Git branch deletion

git push origin --delete -> Remove a remote Git branch

git rm [file name] -> remove a file _(local) _

git rm file name -> To remove a file both from the Git repository and the filesystem _(when file has been pushed to Github) _

git rm file name --cached -> To remove the file from the repository, but keep it on the filesystem (when file has been pushed to Github)

git add [file name] -> add a python file to the staging area _(on local) _

git add -A -> add all new and changed files to the staging area (on local) (not recommended because it can lead to commiting/pushing unsued files)

git pull -> pull code from remote to local (must do this every time before starting anything)

git status -> check status in local (if you did not add a file to the staging area, this file will be in red text. if added its going to be green)

git commit -m "[commit message (short comprehensible summary of change!)]" -> commit changes . Commit message is for other people to get a short summery on what was commit.

git push origin main -> push your local content to GitHub (main -> were the main project is)

git push origin <branch's name> push your local content to GitHub (branch)

(Solve problem when using pushing code to Github but the previous pull code is not the latest version.)

git log -> 	Read and check the difference between local and remote

git reset --soft HEAD~1 -> Reset current HEAD to the specified state. Link: https://git-scm.com/docs/git-reset

git stash -> Stash the changes in a dirty working directory away. Link: https://git-scm.com/docs/git-stash

git fetch -> Stash the changes in a dirty working directory away. Link: https://git-scm.com/docs/git-stash

git stash pop -> Apply the changes as well as remove stored files from stash area.. Link: https://git-scm.com/docs/git-stash _(then check git status och use git add, git commit -m, git push origin...) _

----

commands for project:

touch <file name] -> Create a python file (on local)

mkdir <folder name] -> Create a folder (on local)

Set up Github for terminal use:

Set up a SSH key:

In the terminal, type the following command, replacing youremail@example.com with your email address (the 

same one you use for GitHub):

ssh-keygen -t rsa -b 4096 -C "youremail@example.com"


In order for your SSH key to be used automatically by Git, you need to add it to your SSH agent.

Start SSH-agent-> 

eval "$(ssh-agent -s)"

Add your SSH key to the SSH agent: 

ssh-add ~/.ssh/id_rsa

Copy the public SSH-key and add it to GitHub.

cat ~/.ssh/id_rsa.pub

Copy the entire key showing in terminal.

Go to GitHub:

Log in on your GitHub-account.

Go to SSH and GPG keys- settings.

Click on New SSH key.

Give key a name (example "My computer (lenovo)") and paste the key you copied from the terminal into the 

Key field.

Click Add SSH key.

(now you have added your own specified code, that acts like a log in for when you work in a project.
It is to know that you are you when you commit things in a project at Github.)

To test if it worked:

ssh -T git@github.com

if correct set up: Hi username! You've successfully authenticated, but GitHub does not provide shell access. (in terminal)

Now you can clone, push and pull via SSH.

To clone a repository, use SSH-link instead of HTTPS:

git clone git@github.com:username/repository.git

Github:

Set the SSH keys to Github. Come to Settings -> SSH and GPG key Link 

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account and https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

You only need one SSH-key, so you probably only need to do this once.

----

install Flask using the following command in terminal:

pip install Flask

Verify the Installation:

python -m flask --version

Learn about Flask and download the software. Link: 

https://flask.palletsprojects.com/en/3.0.x/installation/.

How i learn about flask: 
Learn about Flask commands to create a simple application. Link: https://www.geeksforgeeks.org/flask-creating-first-simple-application/

-----

# **v.39**

 * learned:
   
Learn about Flask. Link: https://www.geeksforgeeks.org/flask-creating-first-simple-application/

and docker file, database. 

 * what happen in the group:

Meeting 3:

We decided that everyone would research Dockerfiles and attempt to create one for our individual burger ordering systems.

Set up a database for our respective applications.

My Contributions to My Burger Ordering Project:

Created a Dockerfile to containerize the application.

Added a requirements.txt file for managing dependencies.

Developed a Python function to ensure the website operates correctly.

Tested the website to confirm functionality.

Integrated a database to store burger orders.


Contributions to the Group Project:

Committed my burger ordering application to the group repository so everyone could use it as a reference.

Provided insights on how I created the Dockerfile and implemented the database, offering guidance to others.

 * What i did:
   
Download flask-menu:

pip install Flask-Menu

Verify the Installation:

pip list | grep Flask-Menu

if correct-> Flask-Menu (0.7)

Download and use FLask-Menu to code. Link https://flask-menu.readthedocs.io

----

Install Docker:

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

Download and try to learn how to use Docker Desktop. Link https://www.docker.com/products/docker-desktop/

Install Docker Desktop (windows):

Invoke-WebRequest -Uri https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe -OutFile DockerDesktopInstaller.exe

Docker commands:

docker build -t <image's name>: . -> Build dockers images. Best att use ex: customer: lastest'for the images name and version

docker images -> Show all images

docker run -d --name -p <image's name>: -> run the docker image

running container stop or start:

docker stop adminer

docker start adminer

----

# **v.40**

 * learn:
   
the difference between Dockerfile and Docker Compose.

-> If you have downloaded Docker, Docker Compose is included automatically, so no additional downloading is needed.

Adminer ->allows you to access your database and make changes there.

learned about Virtual machine and adminer

 * What happen in the group:
Assembled and tested the product for the first time.

Coded MenuStore and documented its functionality.

Meeting 3:

We agreed to transition to Docker Compose.
Each team member will research the implementation process at home.

what i did on my Burger order:

change my burger-order docker file to a docker compose. 
This was because with a docker compose file you can run through all 3 docker files. 
with docker file you need to open up all there every time. With compose it just runs a lot smother.
Moved the database to a different map.

Created a kitchen view (still needs improvement).

 * What i did:

Download Adminer with docker:

docker run --name adminer -d -p 8080:8080 adminer -> 8080 web place.

Access Adminer in your browser: Open your browser and navigate to http://localhost:8080.


running container stop or start:

docker stop adminer

docker start adminer


run docker compose: 

docker-compose up -> runs the services using existing images/containers.

docker-compose up --build --force-recreate -> rebuilds images and recreates all containers, regardless of changes.

----

# **v.41**

 * learn:
            
Adminer dose not work for sqlite3 (need to fiend a way)


 * What happen in the group:
            
fiend away to make adminer work. 

Read about debugging and start doing a python test. 


what i did on my Burger order:

Finish with database and Docker-compose file.

started doing python tests and debugging.

Put in a error web site in docker compose file. 

fixed a list for my burger-order so I can add more burgers if i want to the order.


Id for orders:

used ->unique_id = str(uuid.uuid4()) 

generates a unique string using a random UUID (version 4). 
It's used to create secure and unique identifiers.

Added session instead of a list:

session is better than a list in Flask because it manages data per user instead of globally, is more secure (encrypted), saves server memory, and maintains user data across different requests. 
A list shares data between all users and is less secure.
            
 * What i did:

TEST OCH DEBUG:
Read about "Testing Flask Applications with pytest" and try implementing it on your own.
Our initial focus will be to test whether the input data from the order page is correctly sent to the kitchen view.

----

SQLite commands:

CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);

->
Create a table named test, if it was not exists in database with two elements: id and name.

DROP TABLE IF EXISTS test; -> Drop a test table if it was exists in database

SELECT name FROM sqlite_master WHERE type = 'table' AND name='test';

->
Check the positions of table if it exists in database. Returns None if the table does not exist in the database

select * from burger b join order_burger ob on b.id = ob.burger_id join orders o on ob.order_id = o.id join items i on ob.items_id = i.id where o.id = ?

->
Join data in table burger with tabler order_burger, table items with table order_burger based on burger_id, order_id, items_id

INSERT INTO burger (id, name) VALUES (1, "cheese burger")

->
Insert a row in table burger with two elements: id = 1 and name = cheese burger

('SELECT id FROM items WHERE name = ? AND type = ? AND action = ?',(item_name, item_type, action))

->
pull data of item_name, item_type, action based on items_id

('INSERT INTO order_burger (order_id, burger_id, items_id) VALUES (?, ?, ?)',(order_id, burger_id, item_id))

->
insert input data to database

with sqlite3.connect('orders.db') as conn:...

->
use this code to open database so that database will be closed outside "with"

----

# **v.42**

 * learn:
How to do a pytest for debugging.

How to use mock. 


 * What happen in the group:
            
we decided to meet up and write the last part of the projects. 

fixed all writing assignments.

Last touches on ower burger order. 

what i did on my Burger order:

changed adminer to SQLite Web because its specifically made for managing SQLite databases only. No need for login.

Added test map for all test files.

made test for kitchen and order.

used mockup for kitchen.


 * What i did:

Use pytest to test and debug: link: https://docs.pytest.org/en/stable/getting-started.html
A test function start with "test"

group project: 

Testing was particularly challenging because the database was not directly accessible in the kitchen view and order components. 
The database was set up as a Docker volume, which made it difficult to test any functionality that depended on it. 
Moving forward, it would be better to mock the database instead of using the real one. 
By doing this, we can control what data is in the database, ensuring that tests are always consistent and reliable.

For example, when testing a function that retrieves data, using the real database can lead to unpredictable results since the data may change between test runs. 
Mocking, on the other hand, allows us to define exactly what data is available during a test. 
This eliminates the variability and ensures that tests always run under the same conditions, providing more stable and trustworthy results.

mockup on my own project:

I initially tried using a mockup, but the test didn't work as expected, so I switched to Magic Mockup.
The difference between a mockup and Magic Mockup is:

Mockup: A manually created static design used to visualize a product.

Magic Mockup: An automated tool that makes it easy to place your design into realistic scenes.

----

# **What I learned, in more detail**
 
* Github:

I successfully tracked changes and coordinated efforts using GitHub. 
While I’m not yet fully proficient, I learned enough commands to support the project. 
GitHub proved to be a powerful tool, not only for version control but also for collaboration, automation, security, and project management. 
It helped me and the team organize our work, collaborate efficiently, and keep track of code changes in a structured way.

We chose Git as our Version Control System (VCS), hosted on GitHub. 
It’s a popular, free platform that supports collaborative development with features like pull requests and branch management, which enhanced teamwork and reduced merging errors. 
I used Markdown extensively for various files like readme, planning, and reflections. 
Recommended by our teacher, Markdown is a lightweight, easy-to-read language that integrates well with GitHub, making it easier to maintain clear project documentation such as README files and engineering notes.

 * about branches:

A branch is for project/ work where more then one is working on the project. Its to make it easier for the group to work on the project together.
Usually one or two people works on one branch with one specific part of the project. When that part is completed you can send a request for the other people in the group
to check if they think it looks good and everything works together. After that you can push the branch to main without having any problems that it dose not fit in with the other work.

If you don't have a branch´s, its can be complected to push what you have done to main. It may interfere with things that others users have submitted without you nowing about it. 
Sometimes maybe two people have done the same thing. 


 * html and css:

HTML (HyperText Markup Language) is the standard for creating and structuring web pages and their content. 

By using HTML, developers can describe different elements of the page, such as headings, paragraphs, links, images, and forms. 

HTML is the foundation of all web pages and defines how the browser should display the content to the user.

HTML provides the structure and content of the page, while CSS gives it its presentation and layout.

HTML uses a system of tags (<>), which surround different parts of the content to define their purpose or type. 

For example,  is used for headings,  for paragraphs, and  for links. Together with CSS and JavaScript, HTML provides structure, design, and interactivity to web pages.

In summary, HTML is the building block of the web, allowing us to create organized and functional pages for all kinds of purposes, 
from simple informational pages to complex web applications.

To create a well-designed homepage, I used ChatGPT extensively to shape the basic structure. 
Then, I modified and added my own pages. I used the homepage that ChatGPT helped me create as inspiration. 

Additionally, I used their official website to add all the small operational elements, such as buttons and links. HTML provided the structure and content for the page, while CSS was used to create an attractive presentation and layout.

I chose to use CSS to control the look and feel of the website because it allows me to style HTML elements and create a visually appealing design. 

With CSS, I can easily define layout, colors, fonts, and spacing to make the site more attractive and user-friendly. 

It also helps ensure the site looks good across different devices by making it responsive. 
By separating the content from the presentation, CSS keeps the code clean and easy to maintain.


 * python in a working invierment:
   
Using Flask and Python, I have defined several different routes. I explained their structure and how they work, including which URL paths they respond to, which HTTP methods are supported (such as GET and POST), and how each route processes incoming requests and returns responses.

 * flask app:
   
Flask is a simple tool for building web apps with Python. I use it to quickly create websites and APIs. 
It's easy to work with and gives me full control over how the app functions. 

With Flask, I can define which URLs exist and what they should do, making it perfect for small projects and prototypes. 

I can also easily add features like database support or login functionality using different extensions.


 * Docker file and Docker compose:
 
Because the project has two apps: BurgerOrder and KitchenView. 
Connecting them to the database was challenging due to different file paths on each machine, but Docker Compose provided an effective solution. 

Setting up Docker Compose was straightforward because I had already created Docker files for both Kitchen and BurgerOrderer, which formed the base for the Compose setup. 
While a Dockerfile is used to build a container from an image, Docker Compose orchestrates multiple containers, allowing them to communicate and function together. 
This made Docker Compose ideal for managing the different components of the project, such as services and databases. 

Additionally, the volumes defined in my Docker files were crucial for data persistence, ensuring data wouldn't be lost when containers were recreated or removed.

 * adminer:
   
Adminer is a simple tool for managing databases through your web browser. 
You just upload one file to your server, and then you can use Adminer to create and edit databases directly in your browser.

I used SQLite Web because its specifically made for managing SQLite databases only.

 * id:
   
unique_id = str(uuid.uuid4())

generates a unique string using a random UUID (version 4). 
It's used to create secure and unique identifiers. 
This is a good function to use because it simplifies the process of creating unique IDs without needing to worry about collisions or manual generation.

* session and lista:
  
Using session in Flask for handling orders is preferable to a list because:

User-Specific Storage: session isolates data per user, ensuring individual orders are kept separate.

Persistence Across Requests: session maintains data across different requests, allowing users to build orders as they navigate.

Security: session data is encrypted, whereas a global list could expose sensitive information.

Overall, session ensures data isolation, persistence, and security, making it the superior choice for managing user orders.

 * Virtual machine:

A virtual machine (VM) is software that acts like a real computer, allowing you to run an operating system and programs just like on a physical machine. 

It’s used to isolate environments, run different systems on the same hardware, and improve flexibility and security.

 * Pytest:
Pytest is a Python tool for testing code. It helps you write and run tests to make sure your code works correctly.

It is easy to use and shows detailed reports when tests fail. 
You can also use features like reusable setups (fixtures) and running the same test with different data (parameterized tests). 
Overall, pytest is helpful way to ensure your code is working as expected.

 * Debugging and mock:
   
**Summary of Tests Implemented:**

**db_connection()**
A pytest fixture that creates a connection to the SQLite database orders.db.
The connection is used during testing and is closed afterward.
This allows the database connection to be easily reused across multiple test cases without having to open and close it each time.

**test_select_a_column()**
Tests the function another_select_a_column to verify if it correctly fetches values from the column "name" in the "burger" table of the database.
The test checks if the result matches the expected burgers: ('cheese burger',), ('fish burger',), ('vegan burger',).

**test_index()**
Tests the function another_index to ensure it properly retrieves a list of burger names from the "burger" table.
Verifies that the list contains the correct burger names in the expected format: ['cheese burger', 'fish burger', 'vegan burger'].

**Challenges Faced**
Testing was challenging because the database was not directly accessible in the kitchen view and order components. 

The database was set up as a Docker volume, which made it difficult to test any functionality that depended on it. 

For example, when testing a function that retrieves data, 
using the real database can lead to unpredictable results since the data may change between test runs. 
Mocking allows us to define exactly what data is available during a test, 
which eliminates the variability and ensures that tests always run under the same conditions.

Mocking is a valuable tool when testing or debugging because it allows you to replace certain parts of the code, like functions or objects, with "fake" versions. 
These fake versions behave just like the real ones but are simpler and more controllable. 
This makes it possible to test specific parts of the code without loading the entire system or depending on external factors, like a database or an API. 
Mocking lets you simulate different scenarios, such as errors or special data, making it easier to find and fix bugs.

Moving forward, it would be better to mock the database instead of using the real one. 
By doing this, we can control what data is in the database, making sure that tests are always consistent and reliable.

* My own burger project debugging

While testing the Flask application with pytest, several key features were checked to make sure that different routes and endpoints worked as expected. Below is a detailed overview of the testing approach and some challenges that were encountered:

**Summary of Tests Implemented:**

**Kitchen View Testing** (`test_view`, `test_verified_order`): Additional tests were implemented to ensure that the kitchen view works correctly. Mocking of the SQLite database connection was utilized to provide sample order data for testing the `/` view route. The tests verified that the mock data, including different types of burgers and customer details, are correctly displayed in the response, and ensured that the status code returned is 200 OK. The `test_verified_order` specifically checked that certain expected order data (e.g., "Cheeseburger" and "Fishburger") is present in the HTML response, confirming correct rendering.

**Delete Orders Functionality** (`delete_orders`): A route for deleting all orders was added to support administrative actions during development and testing. The `/delete_orders` route deletes all records from the orders database and redirects the user to the main view after successful deletion, ensuring that no residual orders are present in the system.

**Index Route** (`test_index_route`): Verified that the root page (`/`) returns a 200 status code and contains the expected welcome text ("Welcome to Free Burger!").

**Burger Pages** (`test_cheese_route`, `test_fish_route`, `test_vegan_route`): Checked that specific routes (`/cheese`, `/fish`, `/vegan`) correctly display their respective content such as "Cheese Burger", "Fish Burger", and "Vegan Burger".

**Error Page** (`test_error_route`): Tested the `/error` route to confirm that the error message is appropriately displayed.

**Add Order Functionality** (`test_add_order_route`): Verified that the `/add_order` route functions as expected, simulating adding an order to the session without interacting with the database. The assertions include ensuring session values correctly reflect the order data provided, including customer name, burger type, additional items, sides, and drink. (I couldn't not make this one work)

**Order Completion** (`test_order_done_route`): Tested the `/order_done` functionality by using the `patch` decorator to mock database connections, ensuring no direct database interaction during testing. It verified that the order was successfully committed to the database and that the session was cleared after the completion.

**Error Handling Route** (`test_error_page`): Confirmed that a specific route (`/cause_error`) triggers a 500 Internal Server Error response and displays the proper error message.

During development, I continuously verified that everything functioned correctly by frequently testing the website.

**Debugging Techniques Used:**

Breakpoints: I set breakpoints at key points in the code to understand how things were working:

In Each Route Method: I placed breakpoints in functions like add_order, order_done, and delete_orders to verify if the data was sent and received as expected.

**Step Into, Step Over, Continue:**

Step Into: I used "step into" when I wanted to dive deeper into a function and see exactly what was happening, like how data was updated in the session or how mocked data was being processed.

Step Over: I used "step over" to skip over parts of the code I knew were working correctly, such as Flask or SQLite functions, and focus on my own code.

Continue: I used "continue" to run until the next breakpoint, especially after I verified that a specific section was functioning properly.

**Watched Variables:**

response.status_code: I checked that all routes responded as expected, for instance, with a status code of 200.

sess['orders']: I monitored the session's order list to ensure new orders were being added correctly and that the session was cleared as expected, like after deleting all orders with delete_orders.

mock_cursor.fetchall(): Made sure the right data was being returned and used.

mock_conn.commit(): I checked that the database commit() was called at the right time, especially when handling orders or deleting all orders.

**Challenges Faced:**

I started using mockups to create a kitchen view so that I did not need to rely on the actual database and could conduct identical and consistent tests each time. Initially, I struggled to make this work, as the test wouldn't run properly with the standard mocking approach. Eventually, I discovered MagicMock, which proved to be far easier to use than traditional mockups because it offers a faster, automated process that does not require design or Photoshop skills. MagicMock allows you to upload your setup and directly place it in realistic scenarios without having to manually adjust perspectives, shadows, or lighting. This made it much simpler for me to implement effective mockups for the test.

One problem I encountered was that when adding multiple orders, only the last one would be saved to the database when I clicked "done." I used the debugger to figure out why this was happening. I set a breakpoint in the done function to check the session variable to ensure it was adding an order, but I noticed that it was always empty. Initially, I was using a list to store the data, but after searching online, I found that Flask has a built-in session feature, so I decided to use that instead.

Using Flask’s session feature helped keep the orders as I wanted, but testing became tricky because the session would reset after each round.

Testing Multiple Orders in a Session: When trying to implement the test_add_two_orders function, I realized that the Flask session automatically resets after each request in the testing environment. This makes it challenging to verify scenarios where multiple orders are added to the session at the same time. The default session behavior prevents keeping state across multiple test requests, which makes testing these scenarios hard without cumbersome workarounds or changes to how the session is handled.

Even after several attempts, keeping a stable session with multiple orders wasn't feasible using the default test client configuration. To address this limitation, adjustments to session handling might be necessary, or it may be worth considering alternative state management approaches to allow more reliable testing in the future.

**Summary**

By keeping an eye on key variables and using debugging tools effectively, I made sure everything was working correctly and was able to quickly identify and solve any issues that came up. Breakpoints at critical spots helped me understand what was happening at each stage of the code. I used "step into" to dig deeper into functions when I wanted to see how data was being handled, and "step over" to skip over code that I knew worked. "Continue" was useful when I didn’t need to pause anymore.

**Next time:** 

I began the debugging process later than planned, which led to time constraints that prevented me from running as many test cases as I had intended. Moving forward, I will ensure to allocate a full week dedicated to debugging in order to thoroughly test and refine the application before completion.
During development, I continuously verified that everything functioned correctly by frequently testing the website.


----- 

# **what i thought about the project**

 * What went less good:

In the beginning, we struggled to understand the project, the workload, and how to organize our work, as no one had enough experience to lead the team. 
We lacked an effective process, which ultimately hindered progress and is something we need to improve for future projects.

Team members struggled to work together effectively, which led to a lack of commitment from everyone involved. 

This lack of alignment slowed down our progress and negatively impacted the project's success. 
Additionally, since no one had formal education in programming, starting the project was particularly difficult. 

We faced challenges in knowing where to begin, how to divide tasks, and how to work efficiently. 
As we had no prior programming experience, we were learning everything as we progressed, which resulted in varying levels of understanding within the group. 
Those who were able to advance more quickly often ended up doing most of the work, creating disparities within the team. 

The sheer amount of information was overwhelming, especially for beginners, adding significantly to the challenge.

We also faced challenges with GitHub. Initially, everyone committed to the same main branch, which led to issues when changes were pulled and integrated. 

This caused conflicts and delays. Later, we started using branches, which helped a lot in reducing these problems and improving our workflow. 

For our next project, we aim to utilize these features from the start.

 * What went good:

However, a positive aspect was that I learned a lot throughout the process. 
I had the opportunity to engage in many new tasks, which was very informative and enriching. 
We also helped each other a lot to understand all the new information and different parts of the project, and fixed issues whenever someone had a problem with their computer. 
Even though it was a lot of information to take in, it was probably really good for future projects and for the next time we have this course.


 * Next time:
To improve for next time, we need to plan more effectively by assigning specific roles to each member. 
This approach will ensure that everyone contributes to the project and prevents any one person from shouldering the entire workload.
 
Furthermore, fostering better listening and communication among team members will enhance our collaboration and overall success.
