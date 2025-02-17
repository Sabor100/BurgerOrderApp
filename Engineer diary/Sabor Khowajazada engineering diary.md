# **Every week, I write in my programmer's diary.**

## Content in file:
- Summaries of the work
This engineering journal documents my progress over 10 weeks of project development. Each week I've summarized the most important tasks I completed, including implementing features, designing databases, and conducting user testing. I've also focused on collaborating with my team, improving code quality, and preparing for the project's launch. This journal serves as a reflection on my experiences and lessons learned during the development process and provides an overview of the challenges I encountered and how I overcame them.
   
## 1. Summaries of the work (The things I have done every week: (update planning, engineer diary)
a) Collaboration with the team has been critical to the success of the project. Every week we have had meetings to discuss the progress of the project, distribute tasks, and solve problems that have arisen. By using GitHub, we have been able to share code, manage pull requests, and ensure that everyone is working on the same code base.

## (b) Configuration Management
We have implemented a robust configuration management process by using Git for version control. By creating separate branches for different functions, we have been able to work in parallel without disturbing the main project. Once a feature has been tested and approved, it has been merged into the master branch, ensuring continuous integration.

## (c) Implementation and Documentation
The implementation work has focused on developing new functions and improving existing components. Documentation has been created in parallel to ensure that all code is easy to understand and that instructions are provided on how to set up and use the system. Every week I have updated the documentation to reflect changes in the architecture or functionality.

## (d) Testing and Debugging
Testing has been a continuous process throughout the development work. at the end of the project, we've been running unit tests to ensure that new functionality works as expected and doesn't break previous code. Debugging has been challenging at times, but by analyzing error messages and using tools like breakpoints and logging, we've been able to solve most problems efficiently.

## Documented Debugging Experience 
During week 38, I encountered a hard-to-find error in our ordering function in the BurgerOrderer module. The user was unable to submit their order, and no product selections were correctly recorded in the system. To solve this, we started by analyzing log files and stepped through the code with the debugger. By setting breakpoints, we were able to identify that the problem was in the handling of POST data from the HTML form. After we fixed the bug, we verified the functionality by running unit tests and manual tests, and the issue was resolved.

## Debugging Session: Week 38
1. Chosen Functionality
During week 38, I found a hard-to-detect bug in the ordering function of the BurgerOrderer module. The bug prevented users from submitting their orders, and product choices were not correctly recorded. I chose to debug the function for ordering a menu, specifically focusing on the "done" function and menu.

2. Breakpoints and File I Worked With
To start the debugging session, I set breakpoints in the code that handles POST data from the HTML form. The relevant file was appy.py in `Burger_Orderer` folder, where the ordering functionality is implemented. I placed breakpoints at these points:
- The line handling the receipt of POST data (`request.form`).
- The line that adds product choices to the order.
- Finally, the line where the order is saved in the database.
  
3. Debug Process and Tools I Used  
Once the breakpoints were set, I continued with these steps:
- Continue**: I used "Continue" to run the program to the next breakpoint to see where the code broke down.
- Step Over**: When I reached a function that validated the POST data, I used "Step Over" to move forward and see the result without going into the function code.
- Step Into**: When I suspected a specific validation step was not working correctly, I used "Step Into" to see what was happening inside the function.
- Step Out**: When I wanted to return to the main code after stepping into a function, I used "Step Out" to continue from where I left.

4. Watching a Variable
I chose to watch the variable `form_data`, which contained information about the current order.
- How did I do this?** I added the variable to the watch list in the debugger.
- Variable value**: At first, `form_data` was empty, but after handling POST data, I saw that the product values did not match the user's choices.
- Watching changes**: By setting a watch on `form_data`, I noticed it didn't update as expected after the form data was sent. I also used breakpoints to see exactly when the value failed to update.

5. Different Paths Through the Functionality**  
I tested different scenarios to see how they affected the code:
- **Order something else**: I tried ordering a different menu to see if the problem was specific to the "done" The same issue happened for all menus.
- **Cancel the order halfway**: I tried to cancel the order before finishing. I noticed that the code flow did not update `form_data` at all, which showed that there was an issue with handling canceled orders.
These tests helped me understand that the problem was with validating user data, where the form did not always interpret the user's choices correctly.

## Summary and Reflection
- What went well?** Using the debugger to systematically find the error worked well, and I got a better understanding of how POST data is handled in our application.
- What went less well?** It was hard to understand exactly where the data was lost, especially since the error only happened sometimes. Setting the correct breakpoints and choosing the right function to step into took time.
- What was easy?** Setting up breakpoints and using "Continue" to move through the code was easy once I identified where the problem was.
- What was difficult?** Understanding the subtle bugs related to user data and how it flowed through form handling was challenging, especially with asynchronous processes.
- Can debugging be a useful tool for me?** Absolutely. Debugging is a valuable tool to really understand how code behaves under different conditions. By seeing variable values in real-time and understanding how the flow is affected by user interactions, I now feel more confident in handling similar problems in the future.
- Reflections:
Debugging was a learning process where we not only solved a technical problem but also gained insights into how important proper validation of user input is. We learned to improve our testing process by introducing more test cases to prevent similar bugs from occurring in the future.

#### Week 35:
###### I had no idea what to do, everything was unclear for me.
#### Week 36:
###### Task 1: Started learning about Flask, Git, and GitHub (03/09/24)
###### Task 2: continuation with Githubb: learned about how to make a Repository (05/09/24)
###### Task 3: continuation with Githubb: how to commit, how to save changes (07/09/24)

#### Week 37:
###### Task 1: continuation with Flask: Learned about Flask and how to use it. (09/09/24)
###### Task 2: Started learning about HTML and CSS. (10/09/24)
###### Task 3: Implemented the burger customization feature: I made a BurgerOreder application, a user could order a burger and send it to the kitchen and you could see it on the KitchenView page. Created HTML templates for the burger ordering interface. Conducted a code review session with the team. (14/09/24)

#### Week 38:
###### Task 1: Worked with KitchenView to display orders.(16/09/24)
###### Task 2: Started learning about databases (Docker Compose, SQLite ...) (17/09/24)
###### Task 3: Updated the documentation for the project. (20/09/24)
#### Week 39:
###### Task 1: Collaborated with team members on the design of the pages (23/09/24)
###### Task 2: Conducted user tests of the interface for ordering burgers. (25/09/24)
###### Task 3: Fixed bugs discovered during user testing. (27/09/24)
#### Week 40:
###### Task 1: Implemented the menu management system. (01/10/24)
###### Task 2: Integrated the menu management with the database. (02/10/24)
###### Task 3: Fixed debug and changed template structures on VS code. (02/10/24)
#### Week 41:
###### Task 1: Improved the performance of database queries. (08/10/24)
###### Task 2: Worked on deploying the application using Docker. (10/10/24)
###### Task 3: Collaborated with team members on the assignments. (14/10/24)
#### Week 42:
###### Task 1: Collaborated with team members on the assignments. (16/10/24)
###### Task 2: Completed the application features. (16/09/24)
###### Task 3: Performed final code review and merged branches. (17/10/24)

