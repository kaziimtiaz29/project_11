# Fundamental project
# the meal ordering app

## contents
* [Project requirements](#project-requirements)
 * [Project_description](#the-project-description)
* [app's function](#App's-function)
* [project tracking](#Project-tracking)
  * [TRELLO](#Trello-board)
  * [ ERD](#Entity-Relationship-diagram)
  * [risk assessment](#Risk-assessment)
  * [ci](#Continuous-Integration-pipeline)
 * [ Front-End Design](#Front-End-Design)
 * [Running on Jenkins and Testing ](#Running-on-Jenkins-and-Testing)
  * [unit and integration testing](#unit-and-integration-testing)
* [Future improvements](#Future-Improvements)



## Project Requirements:
the task of this fundamental project is as follows:
"To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training"
this requires us to create an app which shall perform the CRUD task which mean CREATE,READ, UPDATE and DELETE.
# the project description
this project involves the creation of an app that would perform 
Moreover,I am additionally obliged to submit the following in addition to what is stated in the brief:

* A Trello board with user stories 
* A relational database with at least two tables that model a relationship 
* Clear documentation of the design phase, app architecture, and risk assessment 
* A python-based functional application that adheres to best practises and design principles 
* Application test suites, which will contain automated tests for application validation 
* Flask was used to build a front-end website. 
* Code will be incorporated into a Version Control System and built using a Continuous Integration server before being distributed to a cloud-based virtual machine.


## App's function

the main functions  in the table (meal) are it allows customers to :

* insert name of food
* the category of meal 
* quantity/amount

these three functions are satifying the CREATE task.

Next I have the option of viewing the meals that has been ordered which are saved once the meals are selected.

Next is the Tables table where customers can:

* in the tables' section the customer can book table and 
* selected how many people are there and how man seats needed.
* time of booking
* here they can combine the tables relationship and show which meal is selected for this table.

these fulfill the Create requirements. For update, the meals can be modified and updated. Also the table and the meals can be deleted if necessary

## Project tracking 
# Trello board 
(user stories)
below is trello board showing the user stories for my project and also showing all the steps taken in the project. it has individual lists showing the different elements on the list. They are as follows:
* Project requeirement -Showing the objectives.
* User stories – they are made in the format ""As a [User]..., I want [Feature], so that... [Details]"
* To do - Lists of essential and non-essential works needed for this project.
* Doing  - Which contains task that is currently being worked on.
* Testing - Features that need to be tested.
* Complete - All tasks that are completed.
* presentation - shows things i need to do to present my project i.e. readme.md file


 
 ![trreelo](https://github.com/kaziimtiaz29/project_1/blob/master/pics/trello.png)
 
 the link for the trello board :https://trello.com/b/0zlAQYwK/fundamental-project1
# Entity Relationship diagram
An entity relationship diagram (ERD) depicting the database's structure is shown below. The user and movies are linked in a one-to-many relationship. As a result, the foreign key is in the meal_ID column, allowing a meals to be served in several tables.

![erd](https://github.com/kaziimtiaz29/project_1/blob/master/pics/erd.png)

https://drive.google.com/file/d/1FRquQ4AeuKKR8q10_Vjg3qRP5NO5fy8i/view?usp=sharing
# Risk assessment
The risk assessment completed before any work on the web application began is shown in the first image below.
A screenshot of my risk assessment at the start of the project is shown below:

![risk1](https://github.com/kaziimtiaz29/project_1/blob/master/pics/risk_asses_1.png)

and afterwards i revisited and change my risk assessment

![risk2](https://github.com/kaziimtiaz29/project_1/blob/master/pics/risk_asses_2.png)
https://docs.google.com/spreadsheets/d/1uLJCYWtSiROfvL5YYhkLHYQMFc6CEGuVZG3iDaI5qsE/edit?usp=drive_web&ouid=109159636375856234989
# Continuous Integration pipeline
A continuous integration pipeline is depicted here, along with the frameworks and services that go with it. By automating the integration process, this pipeline enables speedy and straightforward development-to-deployment. This means that python code written on my local system using the Visual Studio Code platform can be published to Github.The new code in the repo will be posted to Jenkins via webhook, allowing it to be created on the cloud virtual machine. Unit and integration tests are run automatically after that, and reports are generated. The programmer can evaluate the report and adjust the software as needed.

![ci](https://github.com/kaziimtiaz29/project_1/blob/master/pics/ci_pipeline.png)

## Front-End Design
The project utilises Flask to develop a CRUD website with a working front-end website and integrated APIs.
When visiting the home page (/) or a URL without a path, the user is shown with a list of current (meal) entries or a blank page awaiting the creation of meals.
A navigation bar is located at the top of the page (defined in a base layout template, and is available on every page).


![front-end1](https://github.com/kaziimtiaz29/project_1/blob/master/pics/front_end1.png)
![front-end2](https://github.com/kaziimtiaz29/project_1/blob/master/pics/front_end_2.png)
![front-end3](https://github.com/kaziimtiaz29/project_1/blob/master/pics/front_end_3.png)
![front-end4](https://github.com/kaziimtiaz29/project_1/blob/master/pics/front_end_4.png)
![front-end5](https://github.com/kaziimtiaz29/project_1/blob/master/pics/front_end_5.png)



## Running on Jenkins and Testing 

Unit testing was the first step in the project. Individual route functions are put to the test in a variety of scenarios. For a function to be considered successful, it must return the desired response in each case.
code for running on jenkins:


# unit and integration testing
Separating the route functions and testing each one with multiple scenarios is how unit testing is utilised here. For the test to be successful, each function must return the expected result under each case.The proportion of the application that was tested is also shown in a coverage report. This data aids the developer in determining how much of the app's code has been successfully tested.

..pics of unit testing and reports
![jenkins-test](https://github.com/kaziimtiaz29/project_1/blob/master/pics/jenkins_test.png)
below shows the test coverage

![testing-cov](https://github.com/kaziimtiaz29/project_1/blob/master/pics/cov%20reprot.png)

## Future Improvements
Integration testing, as part of the selenium methodology, isperfect for testing the programme as a whole. Selenium  simulates a user exploring the site (by clicking on items on each page) and filling out forms in the manner specified by the testing, and then my tests will verify the database for the expected data.I would have liked to perform more integration testings in the future to further improve the functionality of the app.
Also the relationship of many to many would allow more variability to the app since it would allow many tables to have many types of meals.


Acknowledgements:
Ben, Heskett
Raji, Kolluru
