# [Falloutinator](https://falloutinator.herokuapp.com/)  

## What is Falloutinator
Falloutinator is a website where Fallout fans can gather and share their experiences, opinions and even some tips and tricks they have learnt along the way. The aim of this website is to create a small community of hardcore fans and allow them to share their thoughts in blog form. There is also a Fallout news page with all the latest websites and news related to Fallout. To those who don't know, Fallout is a very popular gaming franchise owned by Bethesda Softworks. They have created multiple fallout games and with any luck they will create more in the future!

## Keys  
1. [ Introduction ](#introduction)
2. [ Installations ](#installations)
3. [ Deployment ](#deployment)
4. [ Admin ](#admin)
5. [ Models ](#models)
6. [ Styles ](#styles)
7. [ Build ](#build)
8. [Testing ](#testing)
9. [ Help ](#help)
10. [ Bugs ](#bugs)

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

<a name="installations"></a>
# Installations
In order to complete this website. Several installations were needed, they are all listed below along with a link to a website for each item installed:  
[Django-3.2](https://docs.djangoproject.com/en/4.0/releases/3.2/)  
[Gunicorn](https://gunicorn.org/)  
[Dj_Database_url](https://pypi.org/project/dj-database-url/)  
[Psycopg2](https://pypi.org/project/psycopg2/)  
[Cloudinary-Storage-Django](https://pypi.org/project/django-cloudinary-storage/)  
[Django-Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)  


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
This site required three models:  
Comment - Enables users to comment on other user's posts  
Post - Enables users to write posts and allows others to view them  
Categories - Gives users the ability to allocate a post to a category making it easier for other users to find.  
The Post model was created by following Django Central blog website (link in help section). I also added an image field using Cloudinary and a like field. I feel that both of these give users a better experience as they can interact and share with eachother easier.  
The Comment model will prove very useful as it allows users to share opinions and get feedback themselves from other users. By having this feature it creates a sense of community.  
Having a Categories section was a must for this website as it brings a lot to the table. By allowing users to create posts under a specific category it makes it easier for other users to find the posts that they are interested in.  


<a name="styles"></a>
# Styles

<a name="build"></a>
# Build

<a name="testing"></a>
# Testing

<a name="help"></a>
# Help
Creating this website required a lot of help and a fair amount of external websites were used to guide me on my way. Each one is pointed out below, and any code taken directly from anywhere will be acknowledged above the code itself:  
[Django-Central](https://djangocentral.com/building-a-blog-application-with-django/)  

<a name="bugs"></a>
# Bugs
I encountered a few issues along the way, the issues are all noted below along with how I went about fixing the issue:  
There was a commit issue. Commit number 11 has the wrong message attatched to it. I did try to research how to change the commit message but I was not successful, the messages states "Delete current migrations and remigrate models due to unknown error" The message was supposed to state "Coppied allauth files into templates folder. Remigrate models due to error"  
