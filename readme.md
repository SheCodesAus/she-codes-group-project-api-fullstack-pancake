# 🥞 She Codes Full-stack Pancakes 

The Fullstack Pancakes team has created a website, **Thinkle**💡, that is designed to allow workshop organisers to attract mentors to their workshops.
### Heroku Link
https://whispering-lake-52626.herokuapp.com/workshops/

## About Thinkle💡

### Project Description ✍
Learning a new skill can be challenging, and sometimes you need someone to give you a
helping hand to get started. On the flip side, a lot of us know a skill and would love to help
teach and inspire others.

We are all also often asked “do you know about any other workshops coming up that I can mentor at?” There are so many people in the tech
community who want to help others to get started, and just don't know how and/or don’t have the means to run their own workshop. 
With **Thinkle**💡, users can register themselves as a programming mentor or organiser, be matched with events they can mentor at, and post upcoming workshops and hackathons.

### Mission Statement 🦾
To connect the Australian technical mentoring community with active workshops and hackathons.

### Target Audience 🎯
Our platform has two user groups: Organisers and Mentors. 

The Organiser user group will be community builders and tech leaders who are responsible for organising technology events and hackathons. This user group will be most likely to visit the platform using a desktop rather than a mobile. 

The Mentor user group will likely work within technology and will be technologically savvy. We anticipate the Mentors will use the platform on either mobile or desktop. 

## To Get Started 🐱‍🏍
### Create Virtual Environment and Active it 🎮
*Windows Users*

`env\Scripts\activate`

*Mac Users*

`. venv/bin/activate`
### Install Requirements 👩‍💻
*Windows Users*

`pip install -r requirements.txt`

*Mac Users*

`pip3 install -r requirements.txt`
### Migrate Database ⚾
*Windows Users*

`python manage.py makemigrations`

`python manage.py migrate`

*Mac Users*

`python3 manage.py makemigrations`

`python3 manage.py migrate`
### Run the Server 🏃‍♀️
*Windows Users*

`python manage.py runserver`

*Mac Users*

`python3 manage.py runserver`

You can then see an example of the API endpoints at:

Workshops: http://localhost:8000/workshops

Users: http://localhost:8000/users/

