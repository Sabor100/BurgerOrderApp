# **Reflections 3**

## **1. Name of everyone in the team:**
    - Ebba Bengtsson
    - Hailey Lundkvist
    - Sabor Ahmad Khowajazada
    - Thanh Chu
    - Wilma Eriksson
## **2. Link to the project's page on the git server:**
https://github.com/HaileyLV/PA1489-project.git

## **3.Assignment:**
### *3.1. Short summary of which functionality we have tested:*
- **Test**: We use Pytest to test with some functions som contact to the database.
### *3.2. Short summary of how we have completed the test:*
- All our test failed in the beginning because we did not set up a function to connect to the database (with 4 test) and did not use the relative path from the BurgerOrderer folder to MenuStore (with 2 test). Though, everything passed after we edited the codes.
- 
### *3.3. Printout from your last test session, so you can see:*
- How many tests you have written: 6 tests
- What they test:
    + 4 test with database: We sat up a function to connect to the database in another folder: def db_connection(), then tested if a table exists/not exists in database and test to create and drop a table in the database.
    + 2 test with BurgerOrderer: tested function select_a_column and function index in BurgerOrderer. We used the relative path from the BurgerOrderer folder to MenuStore during this test.
- How many tests succeed or fail: all of them succeeded.

### *3.4. Your experiences about writing automated unit tests:*
- What went well?:
    + We know how to use Pytest and could write a few test case.
    + During the "Test and Debug" phase, we had to break down the code and carefully analyzing our test cases, which was challenging but highly educational.
- What went less well? 
- How did you solve the difficulties? Could you have done differently?
    + When we started to write som test cases, all of them failed. We tried to set up a function to connect to the database and use the relative path from the BurgerOrderer forder to MenuStore, which worked.
    + Our functions are grouped quite a lot so testing is also more difficult. We have splitted the function to make it easier to test and we could write two test with BurgerOrderer because of it.         
- What did you not manage to solve? Why not?
     + Testing was challenging because the database was not directly accessible in the kitchen view and order components. The database was set up as a Docker volume, which made it difficult to test any functionality that depended on it. Moving forward, it would be better to mock the database instead of using the real one. By doing this, we can control what data is in the database, making sure that tests are always consistent and reliable. For example, when testing a function that retrieves data, using the real database can lead to unpredictable results since the data may change between test runs. Mocking allows us to define exactly what data is available during a test, which eliminates the variability and ensures that tests always run under the same conditions.
    + We started with assignment 3 very late. The time was too urgent so We could not perform as many test cases as expected. In the next project, we had to adjust the time estimate.
    + We wanted to test creating and sending orders to the database but our order_id is automatically generated, therefore we had not dared to try, due to being afraid of conflicts.
    + In our current test case, we have only hard-code tests. If the user changes the details in database, our tests are no longer valid. One member of our group try using Mocka to solve this. She showed the group the last version she did and explained how it worked. Since it wasn't finalized, it didn't appear in the project report, but we will be studying it for the rest of the course.
      
### *3.5. Link to the documentation from your respective debug sessions in our individual engineering diarie:*
<https://github.com/HaileyLV/PA1489-project/blob/main/Engineer%20diary/Thanh%20Chu%20-%20engineer%20diary.md?plain=1>


