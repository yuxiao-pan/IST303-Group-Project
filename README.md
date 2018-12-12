# How to run the application
## Environment to run the application
- Python 3.7.8 
- Pip 18.1
- Virtual Environment 16.0.0

## Run Application command 
- from application root activate the virtual environment 
```
### Mac OS
source ./venv/bin/activate 
### Windows OS
execute/run "activate" file
```
- run Dango server from app folder
```
cd ./app
python manage.py runserver
```
- Stop server by Ctrl + C
```
Ctrl + C
```
- Deactivate the virtualenv when not in use
```
deactivate
```
- Access application from http://localhost:8000/

- Sample Application RUN
```
WL-223-234:IST303-Group-Project abinash$
WL-223-234:IST303-Group-Project abinash$ ls
README.md       app             venv
WL-223-234:IST303-Group-Project abinash$ cd app/
WL-223-234:app abinash$ ls
db.sqlite3      manage.py       mysite          news
WL-223-234:app abinash$ source ../venv/bin/activate
(venv) WL-223-234:app abinash$ python3 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
October 15, 2018 - 23:13:27
Django version 2.1.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```
## Tests
- Test Settings

Test uses following pytest.ini settings
```
[pytest]
DJANGO_SETTINGS_MODULE=mysite.settings_test
addopts = --reuse-db
```
DJANGO_SETTINGS_MODULE setting is required for providing django context to test. 

"--reuse-db" is option provided by pytest-django plugin. It is used so that test enviroment does not delete the test database

- Run Tests

Run Test from inside "app" folder with command "pytest test" after activating virtual environment. Test are located in app/test folder
```
(venv) WL-198-226:app abinash$ pytest test
================================================ test session starts =================================================
platform darwin -- Python 3.7.0, pytest-3.10.0, py-1.7.0, pluggy-0.7.1
Django settings: mysite.settings_test (from ini file)
rootdir: /Users/abinash/Desktop/CGU/Courses/Software Development/project/IST303-Group-Project/app, inifile: pytest.ini
plugins: django-3.4.3, cov-2.6.0
collected 25 items

test/test_endpoint.py ......x.x.x........                                                                      [ 76%]
test/test_model.py ......                                                                                      [100%]

======================================== 22 passed, 3 xfailed in 2.08 seconds ========================================
(venv) WL-203-33:app abinash$
```

## Coverage
- How to run test coverage
After virutal environment activation, from inside the app folder, Run "pytest --cov=news"

```
(venv) WL-203-33:app abinash$ pytest --cov=news
================================= test session starts =================================
platform darwin -- Python 3.7.0, pytest-3.10.0, py-1.7.0, pluggy-0.7.1
Django settings: mysite.settings_test (from ini file)
rootdir: /Users/abinash/Desktop/CGU/Courses/Software Development/project/IST303-Group-Project/app, inifile: pytest.ini
plugins: django-3.4.3, cov-2.6.0
collected 25 items

test/test_endpoint.py ......x.x.x........                                       [ 76%]
test/test_model.py ......                                                       [100%]

---------- coverage: platform darwin, python 3.7.0-final-0 -----------
Name                             Stmts   Miss  Cover
----------------------------------------------------
news/__init__.py                     0      0   100%
news/admin.py                       11      0   100%
news/apps.py                         3      0   100%
news/models.py                      43      4    91%
news/service/__init__.py             0      0   100%
news/service/authentication.py      12      3    75%
news/service/news_service.py        83     15    82%
news/urls.py                         7      0   100%
news/views.py                      103      7    93%
----------------------------------------------------
TOTAL                              262     29    89%


======================== 22 passed, 3 xfailed in 2.55 seconds =========================
(venv) WL-203-33:app abinash$
```
## Install FAQ
- Django not found/ installed
Some user reported that in the first run Django was not loaded from Virtual Environment. 
In such case please install Django after virtual environment activation by 
```
pip install Django
```

- Pytest run fail/ pytest error
At first run pytest sometimes fails due to unable to locate the pytest-django library 
To fix the issue pytest-django needs to be installed from within virtual environment
```
pip install pytest-django
```

# IST303-Group-Project

## Part A

## Team members: 
Abinash, Jerry, Emily, Chu
## Team name: 
NewsTo5
## Product:
Web app consisting of Claremont Colleges student news 

## Stakeholders: 
Professor (will meet with regularly to discuss scope), users are the students at the Claremont Colleges as well as the institutions themselves, team members mentioned above who will work on the project

## Research:
The Student Life newspaper covers the Claremont Colleges: https://tsl.news/

## User Stories (estimate of completion times) and development priority:
1. As an admin user, I would like to see a login page so that I can login to the admin system (frontend: 1 week, backend: 1 week) (priority 10)
2. As an admin user, I would like to see a create, edit, delete content feature so that I can create content/news (frontend: 1 week, backend 1 week) (priority 20)
3. As a normal user, I would like to see user action features so that I can like content
4. As a normal user, I would like to see a registration page so that I can subscribe to the website
5. As an non-subscriber normal user, there will be a limit to reading the number of articles, so that if I wanted to read more, I would have to subscribe
6. As a subscriber normal user, there will be premium content for me to view so that I can see the articles not available to non-subscribers
7. As a normal user, there will be a basic search function so that I can search for articles

## Tech Stack
- GUI frontend: HTML, CSS, Bootstrap (http://getbootstrap.com/), Javascript
- Backend: Python, Django Web Framework (https://www.djangoproject.com/)
- Database: Sqlite 
- Project Management: KanbanFlow

## Process:
- Database and design will be parallel
- Integrating front end and backend 
- 11 weeks to complete

## Class Presentation Slides:
- Agile Frameworks: https://docs.google.com/presentation/d/1zyiA0ii2AIDF4uxA5hnii_2x6P5RebO-YOB6lcBKrsM/edit?usp=sharing
- User stories: https://docs.google.com/presentation/d/1YfMjBXggA67HTTifOh4YS0UdOrBOvvI4hXP53z6Uixw/edit?usp=sharing

## Part B

## User Stories broken into Tasks with Team Member Allocated:
1. As an admin user, I would like to see a login page so that I can login to the admin system (frontend: 1 week, backend: 1 week) (priority 10)
  - Fronted user interface for login (Abinash)
  - Backend API for login (Chu)
  - Access control in login API (Jerry)
2. As an admin user, I would like to see a create, edit, and delete content feature so that I can create content/news (frontend: 1 week, backend 1 week) (priority 20)
  - Frontend user interface for adding product (Abinash)
  - Edit product and delete product (Emily)
  - Backend API for adding, updating, deleting content (Jerry)
  - Access control in the Content API (Chu)
3. As a normal user, I would like to see user action features so that I can like content
  - Create algorithm and functions for user to like content (Jerry)
4. As a normal user, I would like to see a registration page so that I can subscribe to the website
  - Frontend user interface for registration (Jerry)
  - Backend API for registration (Emily)
  - Access control in registration API (Chu)
5. As an non-subscriber normal user, there will be a limit to reading the number of articles, so that if I wanted to read more, I would have to subscribe
  - Frontend for Public to see content (Abinash)
  - Backend API to get for public content with access control (Chu)
6. As a subscriber normal user, there will be premium content for me to view so that I can see the articles not available to non-subscribers
  - Frontend for premium users to see content (Abinash)
  - Backend API to get premium content with access control (Chu)
7. As a normal user, there will be a basic search function so that I can search for articles
  - Create algorithm for search function (Jerry)

## Features in Milestone 1:
- Backend database 
- Frontend site
- Views function
- Admin users

## 2 Iterations for Milestone 1 (4 weeks):
- Iteration 1 (2 weeks):
  - Develop Database Model
  - Create Django Project and Venv
  - Create Database

- Iteration 2 (2 weeks):
  - Create Template Site
  - Create Views
  - Create Admin Users

## Velocity
- Timeline: 4 weeks to milestone 1, 5 weeks to milestone 2
- Starting velocity: 31.25%
  - Total: 8 hours per week
  - Current: 2.5 hours per week

## Burn Down Chart:
https://docs.google.com/spreadsheets/d/1DuGii5SZX_DNYLPneqJOXInUprdrSd-mRr-syshv3D8/edit?usp=sharing

## Stand Up Meeting:
https://docs.google.com/document/d/1rAzH6GMmugfKS4JFjQ0hQ07VHuIqE7W7QaEKBNH3C5A/edit?usp=sharing

## Functional and Test Code:
All code will be in app folder.

