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
11. [ Wireframes ](#wireframes)
12. [ User-Stories ](#userstories)

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
[ck-editor](https://ckeditor.com/)
[Coverage](https://coverage.readthedocs.io/en/6.3/)


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
For my final deployment, I had to make sure I had changed the DEBUG=True to false, and also update my installed items.

<a name="admin"></a>
# Admin
The admin section of this website allows for complete control over the website and it's users. This helps keep the website clean and free from harm. The admin section has several sections inside it:  
Email addresses:  
This is where all of the user's email addresses will be stored. All email accounts that are given during the sign up proccess will stay there AND NOT BE USED ANYWHERE ELSE!  
Groups/Users:  
These came as standard with django. The groups one remained empty and the users one contains all of the website's registered users. From here it's possible to remove accounts is users no longer with to have their account or have done something bad to have their account removed.  
Categorys/Comments/Posts:  
These are the additions I made to the admin section, they are written about in detail in the models section of this read me file.  
Sites/Social Accounts:  
I made no changes inside those as I didn't feel it was within the scope of this project. I was hoping to play around with the social accounts section but I ran out of time. I hope to edit these features in the future.  
![Admin Section](/media/admin-view.png)

<a name="models"></a>
# Models
The models were the center piece of the project. This is where the whole project stems from, so it was very important to get them right. Each time a change was made to anything in the models.py file it was very important to type the following two commands into the terminal:  
```bash
pip3 manage.py makemigrations
```  
```bash
pip3 manage.py migrate
```  
Without these commands the models wouldn't work properly.  
In order to complete this project I used three models. The three models are detailed below:
Post:  
This model came directly from Django central, although I made changes to suit my needs. This was the primary model. It gave users the ability to create their own blog posts. It also is connected to both the category model and comment model via a foreign key to allow for smooth functionality between the three models.  
I also added a postmanager section to this model. I found this on stack overflow, and it helped as an overall control for calling this model.  
This model also contains a likes field, giving users the ability to like/unlike blog posts (Provided they have an account!)  
Category:  
This allowed me to create categories that are connected to the Post model. It only had one field and that was a name field. Although it only had one field it was very useful. It was used in creating the category dropdown menu (The categories were written in the backend and displayed in the front). It also gave users the ability to select a category that suits their post content. Allowing users to find posts that they are interested in easily.  
Comment:
This model gave users the ability to comment on their own posts and also the posts of others too. Instead of it being linked to the user's account I built it so that all that is needed is a name and email address. This is risky as it allows for non registered users to create comments and therefor runs the risk of harmful content. But that is what the Admin section is for!  


<a name="styles"></a>
# Styles
For the most part, this project was styled using bootstrap classes. Mainly the primary class. This class was applied to navigation and all buttons across the website. I feel it gives the site a warm but professional (like Facebook). Click the link for bootstrap colors detail [Bootstrap-Colors](https://getbootstrap.com/docs/5.1/utilities/colors/#how-it-works). For the background I used the same image throughout the website  
![Backgound](/media/background-texture.png)  
It was very simple but also looked very sleek across the pages. Plus by using the same background for all webpages it kept a level of continuity that users will find appealing.  The other big styling option I went with was with all containers. To keep things from getting lost against the background I added some colors that would be subtle but also clearly divide the background from the content  
![Container Backgound](/media/container-background.png)  
When all was put together I think it worked very well, below is an image of the post creation page:  
![Create Post View](/media/create-post.png)  
The fonts for the website were taken from google fonts. I went with Merriweather for all Titles/Headers, and for Times New Roman for everything else (You can't beat an old classic!).

<a name="build"></a>
# Build

<a name="testing"></a>
# Testing
Testing was a critical part of this project. I used a variety of different methods and means, they are all shown below in detail:  
Chrome DevTools was used constantly as it allowed me to find bugs and errors without having to go through code line by line. I had the DevTools open everytime I ran port 8000 as it made it very easy and quick to problem solve. The best feature in DevTools was the lighthouse test. It allowed me to see problem areas on the site as it was in production and increase the website's efficiency by pointing me in the direction of bad practices or loading speed issues.

<a name="help"></a>
# Help
Creating this website required a lot of help and a fair amount of external websites were used to guide me on my way. Each one is pointed out below, and any code taken directly from anywhere will be acknowledged above the code itself:  
I would like to give a huge thank you as always to my mentor Antonio Rodriguez for going above and beyond to help me understand any issues and better myself as a junior developer!  
[Django-Central](https://djangocentral.com/building-a-blog-application-with-django/)  
[Freepik](www.freepik.com)  
Placeholder photo created by user6702303  
Photo by Scott Webb from Pexels  
[Tiny.png](https://tinypng.com/)  


<a name="bugs"></a>
# Bugs
I encountered a few issues along the way, the issues are all noted below along with how I went about fixing the issue:  
I found a but with liking posts. It took me a few days to sort it out. But even now it's not quite right. The button is supposed to change color when pressed, but it does not. I could fix this issue by having an in depth look at the like view but I wanted to focus my attention onto larger bugs.  
I had an issue with ckeditor, as I wasn't able to risize the text area along with the rest of the input areas on the website. To get around this issue, I added a scroll ability to allow users to have access to the full editor box without it leaving it's container.  
There was a commit issue. Commit number 11 has the wrong message attatched to it. I did try to research how to change the commit message but I was not successful, the messages states "Delete current migrations and remigrate models due to unknown error" The message was supposed to state "Coppied allauth files into templates folder. Remigrate models due to error"  
This one wasn't as much of a bug as it was lack of time, But towards the end of production I realised that I wasn't going to be able to add an edit profile page as intended. This was because I used Allauth for the authentication and didn't realise that it would complicate things for the profile page. So as a temporary measure I changed it so a contact page, with my email address. So user's can contact me to have changed made to their account. Once I have this project graded I will go back and add the edit profile feature.  


<a name="wireframes"></a>
# Wireframes
Prior to creating this project, and along side creating this project I made good use of wireframes. They proved to be very helpful as it allowed me to stay focused on what needed to be done without getting too lost in the moment:  
![Homepage Wireframe](/media/wire-1.png)
![Register Wireframe](/media/wire-2.png)
![Category/Search View Wireframe](/media/wire-3.png)
![Commenting Wireframe](/media/wire-4.png)
![Creating Posts Wireframe](/media/wire-5.png)
![Post Detail Wireframe](/media/wire-6.png)
![News Wireframe](/media/wire-7.png)

<a name="userstories"></a>
# User-stories
