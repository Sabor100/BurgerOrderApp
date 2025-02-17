# Planning
## 1. Form development team:
- Plan how you want to work: We sit together at least twice a week: Tuesday (after class) and Thursday (after the lab)

# 2. Determine development environment
- We use VS code.

# 3. Decide which git server you want to use
- Github
- We all have our own accounts on Github

# 4. Language:
- Python

# 5. Our products must have these features:
- A container-based platform, with separate containers for BurgerOrderer, KitchenView, and MenuStore.
**BurgerOrderer:** The main web interface. No need to make it fancy. Functionality is most important.
- Presents the different product types
- The customer can choose what they want to include in their order
- Customer **can customize their order** (eg remove “onions” from their “Metric Ton Bacon Burger”)
- Retrieves information about the different product types from the MenuStore database
- When the order is ready, it is sent via a REST call to KitchenView

**MenuStore**: A database that contains information about each type of item.
- Information about the different product types and how to customize them can be managed via a separate interface such as **admins**

**KitchenView**: Receives orders from BurgerOrderer and displays them to the kitchen staff.
- When an order is received via a REST API, it must be printed on the screen.
- Just need a simple text based printout.

# 5. Weekly plan:
## Week 35+36
- Create a team of 5 members.
- Meet 1 to introduce the team.
- Hailey created a project on Github and shared to everyone.

## Week 37:
- Learn about product design.
- Agree on programming language (Python), environment (VS code), gitserver (Github) and preliminary work division.
- Draft design:
  <https://app.moqups.com/CNsCqWOjxAXBnT1q7BVJIuRvwCjqD6zl/view/page/ad64222d5>
## Week 38:
- Learn about Flask and download the software.
- Practice pulling and pushing data from each person's computer to Github.
- Code BurgerOrderer and KitchenView

## Week 39:
- Learn about Flask. Link: <https://www.geeksforgeeks.org/flask-creating-first-simple-application/>
- Code BurgerOrderer and KitchenView, write documents.
- Update Engineer diary
## Week 40:
- Product assembly and testing the first time
- Fix bug, update Engineer diary
- Code MenuStore and write document of MenuStore
- Update Engineer diary
### Practice:
- Did not finish with MenuStore. Need to learn about Docker-compose and Dababase.
- Did not do any test or fix any bug
## Week 41:
- Finish with database and Docker-compose file.
- Test, fix bug, write document about exercise 1,2,3
- Update Engineer diary
- Need to:
  ### **TEST OCH DEBUG:**
    + Read about "Testing Flask applications with pytest" and try to doing it by yourself
    + We will forst test that the input data on the order website is sent to kitchenview. You are welcome to do more tests if you want.
    + Please tell everyone if you find a bug that needs to be fixed before you change any code.
    + Document everything when working. Check 11-pages of Mikael to have the right structure.
    + Finished the lastest Monday night.
  ### **ASSIGNMENT 2**
    + Write yourself first and we will meet on Tuesday to write everything together.
    + Fell free to create an .md file on Github type: thanh-reflection and write there.
## Week 42:
- Finish with document:
  + Individuals update their thoughts into files: Reflection 1, 2, 3. On Wednesday, we will compile everything and summarize it into complete files and submit all.
  + Create License and setup.py
- Check all again before submit
