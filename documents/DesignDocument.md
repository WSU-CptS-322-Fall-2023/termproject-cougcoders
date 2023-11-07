# Design Document

## Student Research Position App
--------
Prepared by:

* Chance Bradford, WSU
* Andrew Edson, WSU
* Matthew Bruggeman, WSU
---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Design Document](#design-document)
  - [Your Project Title](#your-project-title)
  - [Table of Contents](#table-of-contents)
    - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
- [2.	Architectural and Component-level Design](#2architectural-and-component-level-design)
  - [2.1 System Structure](#21-system-structure)
  - [2.2 Subsystem Design](#22-subsystem-design)
    - [2.2.1 Model](#221-model)
    - [2.2.2 Controller](#222-controller)
    - [2.2.3 View and User Interface Design](#223-view-and-user-interface-design)
- [3. Progress Report](#3-progress-report)
- [4. Testing Plan](#4-testing-plan)
- [5. References](#5-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

### Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |10-16-2023 |Initial draft | 1.0 |
|Revision 1.1 |10-22-2023|Iteraton1 revision  | 1.1 |
|Revision 2.0 |11-7-2023 |Iteration2 draft | 2.0    |


# 1. Introduction

The design document's purpose is to descibe the details of our implementation of the application to the stakeholders. 

Our project is a web application designed to allow WSU faculty members to present research opportunities to prospective undergraduate students. There is a need for an online
platform where faculty can advertise research positions and connect with qualified
undergraduate students. The 'Student Research Position App' website is aimed at fulfilling this need for both students and faculty.


***Document Overview***

[Section II](#2-architectural-and-component-level-design) Section II of the document includes detailed description of our Architectural and Component-level Design. This section consists of two subsections, system structure (2.1) and subsystem design (2.2). System Structure describes the high-level architecture of our software.

[Section III](#22-subsystem-design) Subsystem design is comprised of three sub components, sections (2.2.1) Model, (2.2.2) Controller, and (2.2.3) View and User Interface Design. Lastly in section three we provide a project and developer progress report.

# 2.	Architectural and Component-level Design
## 2.1 System Structure


We chose to adapt and utalize the Model-View-Controller (MVC) architectural design for our application. 
The Model subsystem is mainly used for storing data and communicating with the database.
The Controller subsystem perfroms desired actions between the user interface and the database (bridges the view to the model).
The View subsystem renders data from the model database into suitable user interface output for specific outcomes. 
The rationale for utalizing the (MVC) architectural design is for efficient coupling of software code and based on previous usage. We seperate the system into three main componenents model, view, controller subsystems. This desgin allows major parts of the software to be replaced or changed without having to extensively revise other parts of the system. 


![UML_Component_Diagram](https://github.com/WSU-CptS-322-Fall-2023/termproject-cougcoders/assets/119534848/fc56587b-2a69-4c88-a48a-7f93e9025c8e)


## 2.2 Subsystem Design

<!-- (**Note2**: You should describe the design for the end product (completed application) - not only your iteration1 version. You will revise this document in iteration-2 and make changes  and/or add more details in iteration-2.) -->

### 2.2.1 Model


The role of the Model in our system design structure is to manage fundamental behaviors and data of the application. It can request information from the database and also change that very information stored in said database. Model is the functional core, essentially the data and data-management of the application.


  * User - The User table model holds the faculty and student model common traits.
    - `id` - The sequential, auto-incrementing primary key for the user
    - `email` - The user's WSU email
    - `password_hash` - The hash of the user's password in the database
    - `first_name` - The user's first name
    - `last_name` - The user's last name
    - `phone_number` - The user's phone number
    - `wsu_id` - The user's WSU ID
    - `user_type` - Whether the user is a student or faculty

  * Faculty - a subclass of the User table model, contains components different to other subclasses
    - `research_positions` - A one-to-many relationship representing research positions that the faculty member has created

  * Student - a subclass of the User table model, contains components different to other subclasses
    - `major` - The user's major
    - `gpa` - The user's GPA
    - `graduation_date` - The user's expected graduation date
    - `applications` - A one-to-many relationship representing the research positions that the student has created

  * ResearchPosition - The ResearchPosition table represents an available research position and holds
    - `id` - The sequential, auto-incrementing primary key for the research position
    - `title` - The short name of the research positions
    - `description` - A detailed explanation of the research position
    - `start_date` - A date representing when the research position will start
    - `end_date` - A date representing when the research position will end
    - `time_commitment` - A brief description of how much time a student will be expected to contrtibute to the research position
    - `research_fields` - The relevant research fields for the position
    - `languages_required` - The programming languages that the student should be competent in
    - `additional_requirements` - Any other requirements that the professor would like applicants to have
    - `applications` - A one-to-many relationship representing submitted applications for the position
    - `faculty_id` - A foreign-key representing the faculty member that created the position

  * Application - The Application table represents a student-submitted application for a research field
    - `id` - The sequential, auto-incrementing primary key for the application
    - `reason` - The student's reason for applying to the research position
    - `reference_name` - The name of the student's reference
    - `reference_email` - The email of the student's reference
    - `status` - The status of the student's application
    - `student_id` - A foreign-key reperesenting the student that submitted the application
    - `research_position_id` - A foreign-key representing the research position that the application was submitted for

  * ProgrammingLanguage - The ProgrammingLanguage relationship represents a programming language that a research position may require
    - `id` - The sequential, auto-incrementing primary key for the progamming language
    - `name` - The programming language's name

  * Field - The Field relationship represents a research fields that a research position would fit
    - `id` - The sequential, auto-incrementing primary key for the field
    - `name` - The short name of the research field

We utilize a user table model which holds the main components of both the faculty and student sub class models. Student and Faculty classes inherite common components of the User superclass. These model classes promote cohesion by sharing common traits and properties. Using a super class 'User' makes it easier to expand the database and create other user models is needed.

<!-- (***in iteration -2***) Revise the database model. Provide a UML diagram of your database model showing the associations and relationships among tables. Your UML diagram should also show the methods of your models. -->


### 2.2.2 Controller


The controller subsystem receives user input and makes calls to model objects and the view through forms to perform the required actions. Determines interaction of models and views, essentially defines application behavior. The controller is decomposed into smaller subsystems, one component is the authorization form control which includes the login, logout, and registration forms for both faculty and student users. Another component is the controller routes for User interface interactions. This includes the routes for creating and applying to research position applications, editing user information, toggeling between pages etc...



<!-- **Note:** Some of your subsystems will interact with the Web clients (browsers). Make sure to include a detailed description of the routes your application will implement. For each route specify its “methods”, “URL path”, and “a description of the operation it implements”.
You can use the following table template to list your route specifications. -->

<!-- (***in iteration-2***) Revise your route specifications, add the missing routes to your list, and update the routes you modified. Make sure to provide sufficient detail for each route. In iteration-2, you will be deducted points if you don’t include all major routes needed for implementing the required use-cases or if you haven’t described them in detail. -->

#### Main routes

| Methods | URL Path | Description |
|-|-|-|
| `GET` | `/`, `/index` | Renders the index page containing the base template which includes the navigation bar, along with the list of research positions. If the user is logged in to a faculty account, the research positions are filtered based on whether they have been created by the user or not.
| `GET`, `POST` | `/createposition` | If the user is not logged in to a faculty account, this route will fail. On a `GET` request, will render the position creation form. On a `POST` request, the submitted form is validated, and if validations succeeds, the research position is created.
| `GET`, `POST` | `/apply` | If the user is not logged in to a student account, this route will fail. On a `GET` request, will render the position application form. On a `POST` request, the submitted form is validated, and if validations succeeds, the research position application is created.
| `GET` | `/applications` | If the user is not logged in to a student account, this route will fail. A page showing all of a student's applications will be rendered, including the status of each application.
| `GET` | `/<position_id>/applications` | If the user is not logged in to a faculty account, this route will fail. A page showing all of a research position's applications will be rendered, including the status of each application.
| `DELETE` | `/<application_id>` | If the user is not logged in to a student account, this route will fail. Students will use this route to delete a research position application.
| `DELETE` | `/<position_id>` | If the user is not logged in to a faculty account, this route will fail. Faculty will use this route to delete a research position.
| `POST` | `/<position_id>/<application_id>` | If the user is not logged in to a faculty account, this route will fail. Faculty will use this route to edit the status of an application by approving or denying it.

#### Auth routes

| Methods | URL Path | Description |
|-|-|-|
| `GET`, `POST` | `/faculty_register` | On a `GET` request, will render the faculty registration form. On a `POST` request, the submitted form is validated, and if validation succeeds, the faculty account is created.
| `GET`, `POST` | `/student_register` | On a `GET` request, will render the student registration form. On a `POST` request, the submitted form is validated, and if validation succeeds, the student account is created.
| `GET`, `POST` | `/login` | On a `GET` request, will render the login form that both students and faculty can use. On a `POST` request, the submitted form is validated by checking that the username and password matches a user account, and if validation succeeds, the user is logged in to the account.
| `GET` | `/logout` | If the user is logged in, they are immediately logged out of their account and they must log back in to perform any actions.
| `GET`, `POST` | `/profile` | On a `GET` request, will render the profile form that both students and faculty can use to edit their profile. On a `POST` request, the submitted form is validated, and if validation succeeds, the user's account is edited to their specifications. This may be split into two different routes ('/student_profile', '/faculty_profile') dependent on user type as each user has different profile attributes.


### 2.2.3 View and User Interface Design


The view subsystem provides the user interface element of the application. It will render data from the model into a form suitable for each specific user interface. Our view subsystem will include Bootstap framework to support the User interface design of the view templates. 


* Base - Used for applying common html or bootstrap design to each web page. This template also includes the navigation bar, which has links and buttons used for navigating the application and authenticating users. Renders the Student or Faculty route form like a "home page". Redirects to Base after successful user login.

* Index - The home page for user interface, will render two version, one will render the User Interface for student model users and another will render the faculty user form. The version of UI will be determined be a queery to the User database. This will be implemented later and adjustments to Base will reflect the changes.

* Research Position - The research position template is used to render a single research position including its attributes. 

* Create Research Position - The create research position template is used by faculty members to create research positions, will render the create_position form. Only A faculty User can view this page.

* Apply - The apply template will render the application form used by students to submit an application to a research position. Only Student user can view this page.

* Login - Used for both student and faculty login, will render the authform login form for login of student and faculty models.

* Student Registration - Used by students to register an account, will render the student_registration form used by the student model.

* Faculty Registration - Used by faculty to register an account, will render the faculty_registration form used by the faculty model.

* Profile - Used by students and faculty to view information about their account, will render the profile form used to edit the profile. Will have different attributes based on user type. This view may be split into two different views if the profile route is split based on user-type eg. (faculty_profile, student_profile).

* Application - Used by students and faculty members to view information about an application to a research position, will render the application_edit form to edit the application's status. 

<!-- (***in iteration-2***) Revise your page list and descriptions and include any additional pages that you will include in your view.  In iteration-2, you will be deducted points if your view description is still superficial and doesn't list and explain all pages of your application. -->


# 3. Progress Report

**Iteration1**

Progress for iteration1 is suffiecient. Model and view components have started development addressing several use-cases in our software progression. Each team member has contributed meaningful work towards the project goal. Effective team work has been facilitated in brainstorming architectural design and project documentation. Team member communication is superb and timely. Design and implementation of the controller subsystem is in progress and needs further work.

**Iteration2**

Progress for iteration2 is less than optimal due to time constraints of the development team members. Necessary documentation has been completed and more use-cases have been addressed in this sprint. Team member communication is timely and verbose as before. Team work on brainstorming for testing has been productive and complete. Implememntation of all the routes for the models will need further improvments for the next sprint (Iteration3). Contorller and view subsystems implementation needs further work.
**Main Difficulties:** A major difficulty is time constraints and scheduling of development team members. This has made it difficult to make significant progress on Iteration2. Some desired features will be pushed to Iteration3 because of this.
**Features:** Student and faculty Profile route and view has been added allowing both users to view and edit their profile information. Some form information is blank as it's not created in user registration. 
**Tests:** The testing plan has been facilitated. Implementation and verification of all tests will be executed in Iteration3 sprint. Testing of Iteration2 funtionality has been conducted manually. 


# 4. Testing Plan 

For testing, Our team has deicded to implement unittests with Python Unittests for testing the model subsytem and Pytest for testing the controller subsystem. The Unittests will be whitebox tests hence tests will be designed and conducted by the development team which has knowledge of system implementation. For testing the controller subsystem we will utilize the Python Pytest framework for creating route test automation. View subsystem tests will be paired with model and route tests as possible depended-on-component(DOC) that our system-under-test(SUT) needs for from verification psossibly. Otherwise for UI Testing we will manually test the view pages.

**Test Coverage:** 
A test method for each model and each route will be implemented. Some routes and models utilize the view pages so we can test the view congruently. Each test framework will create the application and intitalize it before conducting automated tests. 
**Model Unittests:** Each model in the model subsystem will have a method for testing with one or more test cases for each method. We will use assertions to compare expected output of the test cases with actual output. Most cases will include equal to and true/false assertions for verification.
**Route PyUnit:** Each route in the controller subsystem will have a method for testing with one or more test cases each method. We will use assertions to compare expected output of the test cases with actual output. Most cases will include equal to and true/false assertions for verification. For **GET request** inputs we will test the route/path URl and parameters of the route. For output we will check status-code (eg. 200 is success, else unsuccessful) and html content that should be displayed. For **POST request** inputs we will test the path URL, parameters of the route, and post data. For output we check the status-code (eg. 200 is success, else unsuccessful) check the state after update, check the html content to be displayed either a flash message or the html page where it redirected. 

Design and implementation of all test will be conducted in iteration 3 sprint as well as automated runs of said tests for verification. Regression and Boundry testing will be considered.

<!-- 
(***in iteration 2***)
In this section , provide a brief description of how you plan to test the system. Thought should be given to  mostly how automatic testing can be carried out, so as to maximize the limited number of human hours you will have for testing your system. Consider the following kinds of testing:
  * *Unit Testing*: Explain for what modules you plan to write unit tests, and what framework you plan to use.  (Each team should write automated tests (at least) for testing the routes)
  * *Functional Testing*: How will you test your system to verify that the use cases are implemented correctly?
  * *UI Testing*: How do you plan to test the user interface?  (Manual tests are OK) -->

# 5. References

- In-class lectures
- Reference slides and pages from Canvas
- [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- [WTForms Documentation](https://wtforms.readthedocs.io/en/3.1.x/)

----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

These is the grading rubric that we will use to evaluate your document.


|**MaxPoints**| **Design** |
|:---------:|:-------------------------------------------------------------------------|
|           | Are all parts of the document in agreement with the product requirements? |
| 10        | Is the architecture of the system described well, with the major components and their interfaces?  Is the rationale for the proposed decomposition in terms of cohesion and coupling explained well? |
| 15        | Is the document making good use of semi-formal notation (i.e., UML diagrams)? Does the document provide a clear and complete UML component diagram illustrating the architecture of the system? |
| 15        | Is the model (i.e., “database model”) explained well with sufficient detail? |
| 10        | Is the controller explained in sufficient detail?  |
| 22        | Are all major interfaces (i.e., the routes) listed? Are the routes explained in sufficient detail? |
| 10        | Is the view and the user interfaces explained well? Did the team provide the screenshots of the interfaces they built so far.   |
| 5         | Is there sufficient detail in the design to start Iteration 2?   |
| 5         | Progress report  |
|           |   |
|           | **Clarity** |
|           | Is the solution at a fairly consistent and appropriate level of detail? Is the solution clear enough to be turned over to an independent group for implementation and still be understood? |
| 5         | Is the document carefully written, without typos and grammatical errors?  |
| 3         | Is the document well formatted? (Make sure to check your document on GitHub. You will loose points if there are formatting issues in your document.  )  |
|           |  |
|           | **Total** |
|           |  |
