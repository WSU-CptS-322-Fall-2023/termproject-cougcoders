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
|Revision 1 |10-16-2023 |Initial draft | 1.0        |
|      |      |         |         |
|      |      |         |         |


# 1. Introduction

Explain the purpose for providing this design document. If this is a revision of an earlier document, please make sure to summarize what changes have been made during the revision (keep this discussion brief). 

Then provide a brief description of your project and state your project goal.

Our project is a web application designed to allow WSU faculty members to present research opportunities to prospective undergraduate students. There is a need for an online 
platform where faculty can advertise research positions and connect with qualified 
undergraduate students. The 'Student Research Position App' website is aimed at fulfilling this need for both students and faculty. 

At the end of the introduction, provide an overview of the document outline.

[Section II](#2-architectural-and-component-level-design) includes …

[Section III](#22-subsystem-design) includes …

# 2.	Architectural and Component-level Design
## 2.1 System Structure

This section should describe the high-level architecture of your software:  i.e., the major subsystems and how they fit together. 
If you adopted the application structure we used in the Smile App, your application would have the Model-View-Controller (MVC) pattern. If you adopted a different architectural pattern, mention the pattern you adopted in your software and briefly discuss the rationale for using the proposed architecture (i.e., why that pattern fits well for your system).

We choose to adapt and utalize the Model-View-Controller (MVC) architectural design for our application. 
The Model subsystem ...
The Controller subsystem ...
The View subsystem ... 
The rationale for utalizing the (MVC) Architectural design is for efficient coupleing of software code. Where parts can be replaced or changed without having to extensively change other parts. We seperate the system into three main componenents model, view, controller subsystems we can make major changes to the overall system with minimal revisions throught the software. 


In this section:
 * ==Provide a UML component diagram== that illustrates the architecture of your software.
 * Briefly mention the role of each subsystem in your architectural design. 
 * Discuss the rationale for the proposed decomposition in terms of coupling and re-use.

## 2.2 Subsystem Design 

(**Note1**: This is just a suggested template. If you adopted a pattern other than MVC, you should revise this template and the list the major subsystems in your architectural design.)

(**Note2**: You should describe the design for the end product (completed application) - not only your iteration1 version. You will revise this document in iteration-2 and make changes  and/or add more details in iteration-2.)

### 2.2.1 Model

Briefly explain the role of the model. 

The role of the Model in our system design structure is to manage fundamental behaviors and data of the application. It can request information from the database and also change that very information stored in said database. Model is the functional core, essentially the data and data-management of the application.

(***in iteration-1***) Include a list of the tables (models) in your database and explain the role of each table. Provide the attributes of the tables (including relationships).

  * User - The User table model hold the faculty and student model common traits.

  * Faculty - a subclass of the User table model, contains components different to other subclasses

  * Student - a subclass of the User table model, contains components different to other subclasses

We utalize a user table model which holds the main components of both the faculty and student sub class models. Student and Faculty classes inherite common components of the User superclass. These model classes promote cohesion by sharing common traits and properties. Using a super class 'User' makes it easier to expand the database and create other user models is needed.

(***in iteration -2***) Revise the database model. Provide a UML diagram of your database model showing the associations and relationships among tables. Your UML diagram should also show the methods of your models.

**utalize bullet points**

### 2.2.2 Controller

Briefly explain the role of the controller. If your controller is decomposed into smaller subsystems (similar to the Smile App design we discussed in class), list each of those subsystems as subsections. 

The controller subsystem receives user input and makes calls to model objects and the view through forms to perform the required actions. Determines interaction of models and views, essentially defines application behavior. The controller is decomposed into smaller subsystems, one component is the authorization form control which includes the login, logout, and registration forms for both faculty and student users. Another component is the controller routes for User interface interactions. This includes the routes for creating and applying to research position applications, editing user information, toggeling between pages etc...

For each subsystem:
 * Explain the role of the subsystem (component) and its responsibilities.
 * 	Provide a detailed description of the subsystem interface, i.e., 
    * which other subsystems does it interact with?  
    * what are the interdependencies between them? 

**Note:** Some of your subsystems will interact with the Web clients (browsers). Make sure to include a detailed description of the routes your application will implement. For each route specify its “methods”, “URL path”, and “a description of the operation it implements”.  
You can use the following table template to list your route specifications. 

(***in iteration-1***) Brainstorm with your team members and identify all routes you need to implement for the completed application and explain each route briefly. If you included most of the major routes but you missed only a few, it maybe still acceptable.

 **MAJOR PART OF THIS Iteration 1(detailed route descriptions)**

(***in iteration-2***) Revise your route specifications, add the missing routes to your list, and update the routes you modified. Make sure to provide sufficient detail for each route. In iteration-2, you will be deducted points if you don’t include all major routes needed for implementing the required use-cases or if you haven’t described them in detail.

|   | Methods           | URL Path   | Description  |
|:--|:------------------|:-----------|:-------------|
|1. |                   |            |              |
|2. |                   |            |              |
|3. |                   |            |              |
|4. |                   |            |              |
|5. |                   |            |              |
|6. |                   |            |              |


### 2.2.3 View and User Interface Design 

Briefly explain the role of the view. **Explain how you plan to build the user interfaces** and mention the frameworks/libraries you plan to use (e.g., Bootstrap).  

The view subsystem provides the user interface element of the application. It will render data from the model into a form suitable for each specific user interface. Our view subsystem will include Bootstap framework to support the User interface design of the templates. 

Provide a list of the page templates you plan to create (or you already created). Briefly describe the information that will be displayed on those pages and the forms that will be rendered (i.e., explain the input and output for each page). Make sure to mention which use-cases in your “Requirements Specification” document will utilize these interfaces for user interaction. You can supplement your description with UI sketches or screenshots. 

* Base - Used for applying common html or bootstrap design to each web page, no form rendered

* index - home page for user interface, will render two version, one will render the User Interface for student model users and another will render the faculty user form. The version of UI will be determined be a queery to the User database.  

* login - used for user login, will render the authform login form for login of student and faculty models.

* Register - used to register user as faculty or student model, will render the authform registration form for registration of faculty and user models.

* Logout - used to lougout a User from the application, 

... **add more view templetes here**

(***in iteration-1***) Brainstorm with your team members and identify the pages that you think should be created.  If you included most of the major pages, it will be acceptable. 

(***in iteration-2***) Revise your page list and descriptions and include any additional pages that you will include in your view.  In iteration-2, you will be deducted points if your view description is still superficial and doesn't list and explain all pages of your application. 


# 3. Progress Report

Write a short paragraph summarizing your progress in iteration1 / iteration2.

**Iteration1**

Progress for iteration1 is suffiecient. Model and view components have started development addressing several use-cases in our software progression. Each team member has contributed meaningful work towards the project goal. Effective team work has been facilitated in brainstorming architectural design and project documentation. Team member communication is superb and timely. Design and implementation of the controller subsystem is in progress and needs further work. 

# 4. Testing Plan

(***in iteration 1***)
Don't include this section.

(***in iteration 2***)
In this section , provide a brief description of how you plan to test the system. Thought should be given to  mostly how automatic testing can be carried out, so as to maximize the limited number of human hours you will have for testing your system. Consider the following kinds of testing:
  * *Unit Testing*: Explain for what modules you plan to write unit tests, and what framework you plan to use.  (Each team should write automated tests (at least) for testing the routes)
  * *Functional Testing*: How will you test your system to verify that the use cases are implemented correctly? 
  * *UI Testing*: How do you plan to test the user interface?  (Manual tests are OK)

# 5. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.


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