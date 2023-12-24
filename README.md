
# Cristiane Tanaka - She Codes News Project

## About This Project
This is a Travel blog that allows: 
 - users to read Travel Stories
 - authors to create and edit their travel stories

## How to Run This Code
1. Clone the repo to your local machine by chosing a directory

 * `git clone [https://github.com/cristianetanaka/shecodesnews]`

2. Set up a virtual environment 
    - Change directory into the repo you just cloned and create a new virtual environment using: 
    `python -m venv venv`
    - Activate the environment
        - Windows: `.venv/Scripts/activate`
        - Mac: `source venv/bin/activate`
    - Install the requirements
        `python -m pip install -r requirements.txt`
3. Make the initial migrations
    - Change directories so that you're next to the manage.py file. 
    - Make the initial migrations using `python manage.py migrate`
    - Test that this is working correctly by running the server `python manage.py runserver`

4. View the She Codes News site: http://localhost:8000/news

## Database Schema
![My ERD](\she_codes_news\static\images\DB Diagram.png)

## Project Features
Link to Youtube: https://www.youtube.com/watch?v=XspzppJZmU8

### Required Features:
- [X] Log-in/log-out functions
- [X] Form for adding new stories
- [X] Order stories by date
- [X] field for new story model and image url (user can choose images instead of default ones)
- [X] style form for adding new stories  
- [X] "Account view" page
- [X] "Create Account" page
- [X] View stories by a particular author
- [X] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in
- [X] "Create Story" functionality only available when user is logged in

### Additional Features:
- [X] Add the ability to update and delete stories by autheticated user 
- [X] Ability to set a time a story is published
- [X] Ability to delete and update account details
- [X] Profile Bio
- [X] Like Button

### Further improvements
- [X] Updated account does not fully work. Further investigation needs to be done using what was covered in class using class instead of function.
- [X] Like button needs to be fully deployed with total count of likes
- [X] forms needs to be fully styled so as the Website.
- [X] comments and serach function to be implemented