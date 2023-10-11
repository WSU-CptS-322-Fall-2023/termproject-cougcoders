# Software Requirements Specification


## Student Research position App
--------
Prepared by:


* `Chance Bradford`,`WSU`
* `Andrew Edson`,`WSU`
* `Matthew Bruggeman`,`WSU`


---


**Course** : CptS 322 - Software Engineering Principles I


**Instructor**: Sakire Arslan Ay


---


## Table of Contents
- [Software Requirements  Specification](#software-requirements-specification)
  - [Your Project Title](#your-project-title)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
  - [1.1 Document Purpose](#11-document-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 Document Overview](#13-document-overview)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 Use Cases](#22-use-cases)
  - [2.3 Non-Functional Requirements](#23-non-functional-requirements)
- [3. User Interface](#3-user-interface)
- [4. Product Backlog](#4-product-backlog)
- [4. References](#4-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)


<a name="revision-history"> </a>


## Document Revision History


| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 | 08-10-2023 |Initial draft | 1.0        |
|      |      |         |         |
|      |      |         |         |


----
# 1. Introduction


This document describes the web application Student Research Position app. It outlines the purpose of the application. Also clearly defines and explains all use cases of the web application.


## 1.1 Document Purpose


This document is intended for all stakeholders of the web application. The purpose is to clearly outline the requirements and use cases of the application.


## 1.2 Product Scope


The product specified in the following document is the Student Research Position app. The application allows students looking for undergraduate research positions to view open research positions and professors to post their research positions. Then students can apply through the app to the research positions posted by the professors. This benefits both faculty and students because they can connect in order for the student to gain experience and the professor to obtain willing and interested candidates. The main goal of the application is to connect students with undergraduate research positions and to connect professors with quality candidates for their positions.



## 1.3 Document Overview


The requirements document contains a requirements specifications section which specifies the software’s requirements in sufficient detail. This is to allow designers to engineer a system that can satisfy those requirements. A list of customers, users and stakeholders involved. A Use cases section. Use cases are an expansion of users stories which describes a sequence of actions that a user performs to complete a task. Each use case is formatted in a table with iteration labels. A concise list of non-functional requirements. A user interface description. A product backlog, and any references used.


# 2. Requirements Specification


On the student page, a student user can:
 1. Create a student account and enter the profile information:
 a. Set the account username and password (username should be the WSU email)
 b. Enter contact information (name, last name, WSU ID, email, phone)
 c. Enter additional information (major, cumulative GPA, expected graduation date, etc. )
 d. Select the research topics they are interested in. You can assume a predetermined list
 of research fields and have the student choose among those.
 e. Choose the programming languages with which they are familiar. You can assume a
 predetermined list of programming languages and have the instructor choose among
 those.
 f. Describe their prior research experience if there is any.
 2. Login with username and password.
 3. View the open research positions.
 − Your app should list all open research positions.
 − In addition, it should identify the research positions that match the student’s
 “research interests” and list them separately under the “Recommended Research
 Positions”. You can implement a simple recommendation algorithm to find the
 matching positions. For example: If the student’s research interests include “Machine
 Learning”, the positions in that field should be recommended to the student. Similarly,
 if the position requires Python experience and if the student chose Python in their
 profile, the position should be recommended to the student.
4. For each research position, various information should be displayed:
 a. Research project title
 b. A brief description of the project goals and objectives
 c. Start date and end date
 d. Required time commitment (e.g., 10 hours per week)
 e. Research field(s) (e.g., “Machine Learning, High Performance Computing, etc.)
 f. Required programming language experience (e.g., “C++”, “Java”, “Python”, etc.)
 g. A brief description of other required qualifications
 h. Faculty’s name and contact information
 5. Apply for research positions. A student can apply for more than one research position.
 For each position they apply to,
 − They should submit a brief statement describing why they are interested in this
 research topic and what they hope to gain by participating in that project.
 − They should provide the name and email of one faculty who can provide them a
 reference for the position.
 6. View the research positions they already applied to and check the statuses of their
 applications.
 a. When the application is submitted, its status will appear as “Pending”.
 b. After a faculty accept this application, the status should be updated as “Approved for
 Interview”. Student would do the interview in person.
 c. After the interview, the faculty should update the status as either “Hired” or “Not
 hired”. Once updated, the changed status should be displayed on the student page.
 7. Withdraw their pending applications.
 − If the student is no longer interested in a research position, they can withdraw their
 application.
 On the faculty page, a faculty user can:
 1. Create a faculty account and enter profile information:
 − Set the account username and password (user name should be the WSU email)
 − Enter contact information (name, last name, WSU ID, email, phone)
 2. Login with username and password
 3. Create undergraduate research positions. Faculty should enter the details of the
 position and qualifications needed, i.e.,:
 a. Research project title,
 b. A brief description of the project goals and objectives
 c. Start date and end date
 d. Required time commitment (e.g., 10 hours per week)
e. Research field(s) (e.g., “Machine Learning”, “High Performance Computing”, etc.). You
 can assume a predetermined list of research fields and have the instructor choose among
 those.
 f. Required experience with programming languages (e.g., “C++”, “Java”, “Python”, etc.)
 You can assume a predetermined list of programming languages and have the instructor
 choose among those.
 g. A brief description of other required qualifications.
 Of course, a faculty can create more than one positions.
 4. See the list of the students who applied for their positions.
 − A faculty should be informed about the other offers students get. If a student was
 “Approved for Interview” or was “Hired” for another position, those information
 should also be displayed.
 5. View the qualifications of each student, i.e.,
 a. their GPAs,
 b. the technical elective courses they have taken,
 c. the research topics they are interested in,
 d. the programming languages they have experience with, and
 e. prior research experience.
 6. The faculty can approve the application of one or more students and the status of those
 applications should be updated as “Approved for Interview”.
 7. After interviewing with the student, the faculty can update the status of applications as
 either “Hired” or “Not hired”
 8. The faculty may delete the existing research positions. Once deleted, the status of all applications should be updated as “Position is not available”.







## 2.1 Customer, Users, and Stakeholders


A brief description of the customer, stakeholders, and users of your software.


Customer: Sakire Arslan Ay has employed us to make the following product


Stakeholder: Our customer Sakire benefits from the making of this application. The developers salary and bonuses (grades) are dependent on the quality and functionality of the application.


User: Students looking for undergraduate research positions and professors looking for students to work their undergraduate research positions.


----
## 2.2 Use Cases


This section will include the specification for your project in the form of use cases. The section should start with a short description of the actors involved (e.g., regular user, administrator, etc.) and then follow with a list of the use cases.


For each use case you should have the following:


* Name,
* Actors,
* Triggers (what initiates the use case),
* Preconditions (in what system state is this use case applicable),
* Actions (what actions will the code take to implement the use case),
* Alternative paths
* Postconditions (what is the system state after the use case is done),
* Acceptance tests (list one or more acceptance tests with concrete values for the parameters, and concrete assertions that you will make to verify the postconditions).


Each use case should also have a field called "Iteration" where you specify in which iteration you plan to implement this feature.


You may use the following table template for your use cases. Copy-paste this table for each use case you will include in your document.


| Use case # 1      |   |
| ------------------ |--|
| Name              | Student Account Creation |
| Users             | Students |
| Rationale         | Allow students to select research topics |
| Triggers          | When users click the create student button|
| Preconditions     | User does not already have a student account |
| Actions           | Creates a student account |
| Alternative paths | Sign in to student account |
| Postconditions    | User is logged in to student account |
| Acceptance tests  | Username and email are unique, email is a valid email address |
| Iteration         | Iteration 2 |


| Use case # 2      |   |
| ------------------ |--|
| Name              | Login with username and password |
| Users             | Students |
| Rationale         | Allow users to login to their account |
| Triggers          | When users click the login link |
| Preconditions     | User is not logged in |
| Actions           | User is logged into their account, and can submit user-related requests |
| Alternative paths | Create a student account |
| Postconditions    | User is logged in to student account |
| Acceptance tests  | Username and password are valid |
| Iteration         | Iteration 2 |


| Use case # 3      |   |
| ------------------ |--|
| Name              | View the open research positions |
| Users             | Logged-in students |
| Rationale         | Allow students to identify research position that match the student’s interests |
| Triggers          | Student navigates to the research positions page |
| Preconditions     | User is logged in, there are open research positions |
| Actions           | User can view the open research positions in a separate page |
| Alternative paths | None |
| Postconditions    | None |
| Acceptance tests  | None |
| Iteration         | Iteration 1,3 |


| Use case # 4      |   |
| ------------------ |--|
| Name              | View information about each open research position |
| Users             | Logged-in students |
| Rationale         | "Allow students to view more information about possible research interests"  |
| Triggers          | User navigates to the research positions page |
| Preconditions     | User is logged in, there are open research positions |
| Actions           | User can see information about the research position including research project title, a brief description of the project goals and objectives, start date and end date, required time commitment, research fields, required programming language experience, a brief  description of other required qualifications, and faculty’s name and contact information.|
| Alternative paths | None |one |
| Iteration         | Iteration 1 |


| Use case # 5      |   |
| ------------------ |--|
| Name              | Apply for a research position |
| Users             | Logged-in students |
| Rationale         | Allow students to apply for any open research positions that they have an interest in |
| Triggers          | User submits a form to apply for the position |
| Preconditions     | User is logged-in |
| Actions           | An application is submitted on behalf of the user for the position |
| Alternative paths | None |
| Postconditions    | User cannot apply to the same position again |
| Acceptance tests  | Application form contains a brief statement describing why they are interested in this research topic and what they hope to gain by participating in that project along with the name and email of one faculty member who can provide them a reference for the position. |
| Iteration         | Iteration 1 |


| Use case # 6      |   |
| ------------------ |--|
| Name              | View the research positions that students already applied to and check the status of their application |
| Users             | Students that have submitted an application |
| Rationale         | Allow students to view information about their application |
| Triggers          | User click information about their applications |
| Preconditions     | User is logged-in and has submitted an application for an open research position |
| Actions           | User can see whether their information is pending, a faculty member has accepted the application, or if the faculty member has hired or not hired the student |
| Alternative paths | None |
| Postconditions    | None |
| Acceptance tests  | User has applied to the position |
| Iteration         | Iteration 3 |


| Use case # 7      |   |
| ------------------ |--|
| Name              | Withdraw their pending applications |
| Users             | Students that have submitted an application |
| Rationale         | Allow a student that is no longer interested in a research position to withdraw their application |
| Triggers          | User click the withdraw button |
| Preconditions     | User clicks the confirm button |
| Actions           | User’s application is withdrawn |
| Alternative paths | None |
| Postconditions    | User can no longer view their application |
| Acceptance tests  | User click the confirm button |
| Iteration         | Iteration 3 |


| Use case # 9      |   |
| ------------------ |--|
| Name              | Create a faculty account and enter profile information |
| Users             | Non-logged in users |
| Rationale         | Allow faculty members to create an account |
| Triggers          | User clicks the create faculty account button |
| Preconditions     | User is not logged in |
| Actions           | A faculty account is created|
| Alternative paths | User logs in to their faculty account |
| Postconditions    | User is logged in to their new account |
| Acceptance tests  | Username and email is unique and email is a valid email address. Contact information is present |
| Iteration         | Iteration 2 |


| Use case # 10      |   |
| ------------------ |--|
| Name              | Login to faculty account with username and password |
| Users             | Faculty members |
| Rationale         | Allow users to login to their faculty account |
| Triggers          | When users click the faculty login link |
| Preconditions     | User is not logged in |
| Actions           | User is logged into their faculty account, and can submit faculty-related requests |
| Alternative paths | Create a faculty account |
| Postconditions    | User is logged in to faculty account |
| Acceptance tests  | Username and password are valid |
| Iteration         | Iteration 2 |


| Use case # 11      |   |
| ------------------ |--|
| Name              | Create undergraduate research positions |
| Users             | Faculty members |
| Rationale         | Allow faculty members to create undergraduate research positions that students can apply to |
| Triggers          | Users click the create research position button |
| Preconditions     | User is logged in to faculty account |
| Actions           | An undergraduate research position is created |
| Alternative paths | None |
| Postconditions    | Students can apply to the new undergraduate research position |
| Acceptance tests  | Details of the position includes a research project title, a brief description of the project goals and objectives, start date and end date, required time commitment, research fields, required experience with programming languages, and a brief description of other required qualifications. |
| Iteration         | Iteration 1 |


| Use case # 12      |   |
| ------------------ |--|
| Name              | See the list of the students who applied for their positions |
| Users             | Faculty members |
| Rationale         | Faculty members should be informed about the other offers students get.|
| Triggers          | Users click the application list button |
| Preconditions     | Students have applied to the faculty member’s positions |
| Actions           | Show information about whether the student was approved for interview, hired.  |
| Alternative paths | None |
| Postconditions    | None |
| Acceptance tests  | Student has applied for the position |
| Iteration         | Iteration 2 |


| Use case # 13      |   |
| ------------------ |--|
| Name              | View the qualifications of each student |
| Users             | Faculty members |
| Rationale         | Allow faculty members to view the qualifications of each student that has applied for their position |
| Triggers          | Faculty member clicks on a user’s requirements|
| Preconditions     | Student has applied for the faculty member’s position |
| Actions           | Faculty members can view each student’s GPA, the technical courses they have taken, the research topics they are interested in, the programming languages they have experience with, and their prior research experience. |
| Alternative paths | None |
| Postconditions    | None |
| Acceptance tests  | None |
| Iteration         | Iteration 2 |


| Use case # 14      |   |
| ------------------ |--|
| Name              | The faculty can approve the application of one or more students |
| Users             | Faculty members |
| Rationale         | Faculty members should be able to approve an application for their positions |
| Triggers          | Faculty member clicks the approve button next to a student’s name |
| Preconditions     | Student has applied to a faculty member’s position |
| Actions           | Student’s application status should be updated as “Approved for interview” |
| Alternative paths | None |
| Postconditions    | Student’s application has been approved |
| Acceptance tests  | None |
| Iteration         | Iteration 3 |


| Use case # 15      |   |
| ------------------ |--|
| Name              | Faculty member can update the status of the applications |
| Users             | Faculty members |
| Rationale         | Allow the faculty members to update the status of the applications after they have interviewed a student |
| Triggers          | Faculty clicks the update status button |
| Preconditions     | Student has applied for the faculty member’s position |
| Actions           | Student’s applications is updated |
| Alternative paths | None |
| Postconditions    | Student’s application status is either “Hired” or “Not hired” |
| Acceptance tests  | None |
| Iteration         | Iteration 3 |


| Use case # 16      |   |
| ------------------ |--|
| Name              | Faculty members may delete the existing research positions |
| Users             | Faculty members |
| Rationale         | Allow faculty members to delete all of their research positions |
| Triggers          | Faculty members can click the delete button next to a research position |
| Preconditions     | Faculty member owns the research position |
| Actions           | Research position is no longer accessible |
| Alternative paths | None |
| Postconditions    | Status of all applications for the position are updated to “Position is not available” |
| Acceptance tests  | None |
| Iteration         | Iteration 3 |




----
## 2.3 Non-Functional Requirements


1. Response Time:
- Pages should load in a reasonable amount of time


2. Scalability:
- Should be able to handle multiple users at a time.


3. Reliability:
- software Should recover from failure.


4. Availability:
- Should be accessible on most web browsers


5. Quality:
	- Constraints on the design to meet specified levels of quality


6. Reusability:
	- subsystems should be reusable or replaceable.




----
# 3. User Interface

![CamScanner 10-11-2023 10 18n_1](https://github.com/WSU-CptS-322-Fall-2023/termproject-cougcoders/assets/119534848/d1992fec-c5f2-4447-a119-af4cb9238593)
![CamScanner 10-11-2023 10 18n_2](https://github.com/WSU-CptS-322-Fall-2023/termproject-cougcoders/assets/119534848/47579caa-9334-4753-a97d-9c52eb3d045b)
![CamScanner 10-11-2023 10 18n_3](https://github.com/WSU-CptS-322-Fall-2023/termproject-cougcoders/assets/119534848/e6c9d9e6-8179-4720-8965-b75f800b02a6)
![CamScanner 10-11-2023 10 18n_4](https://github.com/WSU-CptS-322-Fall-2023/termproject-cougcoders/assets/119534848/95f9c373-025c-465a-ab8d-62676c090da7)

----
# 4. Product Backlog


Link to GitHub issues:
https://github.com/WSU-CptS-322-Fall-2023/termproject-cougcoders/issues


----
# 4. References


WSU, Sakire Arslan Ay, CPTS-322 https://wsu.instructure.com/courses/1650001


For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.


For the websites, give the title, author (if applicable) and the website URL.
