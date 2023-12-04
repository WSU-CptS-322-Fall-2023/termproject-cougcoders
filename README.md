# CptS 322 Term Project
### Project Title: Student Research position App
### Team Name : CougCoders
### Team Members 
* Chance Bradford
* Andrew Edson
* Matthew Bruggeman

-----------------------
## Running the application
-----------------------
To run this App:
- Start the application with the following command:

Windows:    
```
set FLASK_DEBUG=1 && python -m flask run
```
Mac/Linux:   
``` 
export FLASK_DEBUG=1 && python3 -m flask run
```
To Close this App:
- Close the application with the following command:  
```
Ctrl + c 
```
### to run tests
- run tests for Model (unittest)
```
python -m unittest tests/test_models.py
```
- run tests for routes (pytest)
```
python -m pytest tests/test_routes.py
```
