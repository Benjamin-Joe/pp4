# Falloutinator  

## What is Falloutinator
Falloutinator is a website where Fallout fans can gather and share their experiences, opinions and even some tips and tricks they have learnt along the way. The aim of this website is to create a small community of hardcore fans and allos them to share their thoughts in blog form. There is also a Fallout news page with all the latest websites and news related to Fallout. To those who don't know, Fallout is a very popular gaming franchise owned by Bethesda Softworks. They have created multiple fallout games and with any luck they will create more in the future!

## Keys  
1. [ Introduction ](#introduction)
2. [ Setup ](#setup)
3. [ Installations ](#installations)
4. [ Deployment ](#deployment)
5. [ Admin ](#admin)
6. [ Models ](#models)
7. [ Styles ](#styles)
8. [ Build ](#build)
9. [Testing ](#testing)
10. [ Help ](#help)
11. [ Bugs ](#bugs)

<a name="introduction"></a>
# Introduction
This is project four with Code Institute's full stack developer course. For this project I needed to build a Full-Stack website. I decided to combine my favorite game type with one of my favorite websites. So I created a Fallout blog/reddit style website. I chose to create this for a few reasons as listed below:  
It allowed me to show my skills as a developer  
I believe it hits all the criteria needed for this project  
It was a challenge to me personally and is also something that I am very passionate about  
It is a website that has the potential to take off and grow as there is no real place for Fallout fans to go and share thought and tips with one another  
The website has many other features that can be added over time, increasing it's UI.  

The client base I am looking at for this website is a fairly small number of users. A few hundred or so users, But these users will be pasionate Fallout fans. My hope is to create a close and caring community with a common interest.  
Because the website is only about Fallout I think that it will prevent toxic/dangerous users from posting harmful content as only true Fallout fans are going to be interested in signing up for an account.


<a name="setup"></a>
# Setup

<a name="installations"></a>
# Installations
In order to complete this website. Several installations were needed, they are all listed below along with a link to a website for each item installed:  
[Django-3.2](https://docs.djangoproject.com/en/4.0/releases/3.2/)  
[Gunicorn](https://gunicorn.org/)  
[Dj_Database_url](https://pypi.org/project/dj-database-url/)  
[Psycopg2](https://pypi.org/project/psycopg2/)  
[Cloudinary-Storage-Django](https://pypi.org/project/django-cloudinary-storage/)  




<a name="deployment"></a>
# Deployment
Early deployent was key to creating a successful website as it removed any stress of last minute deployment issues. 
In order to deploy this website I followed the django blog cheat sheet provided by Code Institute, The steps are as follows:  
Install django, gunicorn, dj_database_url, psycopg2, cloudinary-storage in the terminal.  
Create a requirements.txt file with 
```bash
pip3 freeze --local > requirements.txt
```  
Start a project using 
```bash
django-admin startproject falloutinator .
```  
Create an app using 
```bash
pip3 manage.py startapp blog
```  
Add the blog app to the installed apps section in the settings file within the falloutinator project  
Then migrate the changes using  
```bash
python3 manage.py migrate
```  
After that it was time to create the Heroku app on the Heroku website and connect it up to github below are the Heroku dev center website pages on how to deploy on Heroku, there are two methods of doing this, the first one is from Heroku itself and the second one is using the git bash terminal. I chose the first method as I found it easier to do  
[Heroku-Dev-Center-Method-1](https://devcenter.heroku.com/articles/github-integration)  
[Heroku-Dev-Center-Method-2](https://devcenter.heroku.com/articles/git)  
I used cloudinary to store images for this website (to prevent images being deleted without permission to do so). Connecting this up to the project was very easy and only took a couple of steps:  
Login to cloudinary account  
copy API Environment Variable from dashboard  
Paste it into env.py file and also into the config vars setting on Heroku app  
Add cloudinary storage to settings.py  

Once cloudinary was installed it was just a case of creating the media, static and templates folders and adding them to settings.py  
Then create a Procfile and add the project name to the procfile. Then it was time for deployment.





<a name="admin"></a>
# Admin

<a name="models"></a>
# Models

<a name="styles"></a>
# Styles

<a name="build"></a>
# Build

<a name="testing"></a>
# Testing

<a name="help"></a>
# Help

<a name="bugs"></a>
# Bugs

