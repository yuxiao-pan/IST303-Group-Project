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


