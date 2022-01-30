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
Navigation:  
The navigation bar was taken directly from bootstrap and it's features are as follows:  
Falloutinator(Home Button)  
News(Links and informations to all the latest fallout news)  
Categories(Dropdown menu for selecting a category to saerch for)  
Account(This is where all of the user's login/logout items are stored)  
Search-Bar(A search bar for user's to type in what they are looking for)  
Homepage:  
The homepage is the main area, where user's will spend most of their time. This contains all posts created by all users. It is arranged via date, to keep the content fresh. This page also has pagination to prevent there being to much content on any given page. There are six posts per page. If the user is also the creator of a particular post they have added features they can control from the homepage, these are the delete and edit functionality.  
Users are able to click on any post they like and view it in more detail from the homepage. So it is only two web pages a possible viewer has to browse through in order to see the content they like.  

Categories/Search:  
The categories really help to define a post by it's genre and helps to narrow down search time on finding the posts a user wants to find. It is the same with the search bar. It gives users more options to find the posts that they want to find.  

Signup:  
The signup form game from allauth, as did all of the user authentication sections. The form is very simple and only contains Email, Username, Password fields. By keeping the form simple the hope is that it will entice more users to sign up.

Login/Logout:  
I wanted to keep the login/logout ability very simple, so the pages are quite bare minus some basic styling. This is because I feel that if there are too many hoops to jump through to sign in and out then it has the potential to put users off returning.

Create Post:  
The create post form is a self created form, the content can be found in forms.py. This has a few fields, Title, Slug, Category, Content, Image.  
The user must fill in each section or they will receive an error message, With exception of the image field, it that is left blank then there is a placeholder image that will take up the image area. I was unhappy about keeping the slug field in, but I couldn't find a way to auto populate it and keep it hidden!

Edit Post:  
Only the post creator can edit a post. The fields that can be changed are the title, category and the content. I didn't allow for users to change the image because that could end up slowing down the loading speed of the page if it has been through multiple image makeovers.

Delete Post:  
Deleting a post is a single button process. Are you sure you want to delete? Once a user clicks Delete they will be taken back to the homepage and their post will be gone.

News:  
The news section is what helps the website stay current. By giving users access to the most up to date websites they are able to make more accurate posts and comments

The build was difficult as I struggled to work on small sections at a time, and found that I would tweak sections that had nothing to do with the section I was working on. To combat this I wrote out a list of to-do items ontop of the user stories I was following on github. By having a hand written list I found it much easier to stick to an agile method of developing this website as I was able to cross off items as I went along. Once the website was completed I wrote up my to do list so I could paste it in below.
![To-Do](/media/to-do.png)  

<a name="testing"></a>
# Testing
Testing was a critical part of this project. I used a variety of different methods and means, they are all shown below in detail:  
Chrome DevTools was used constantly as it allowed me to find bugs and errors without having to go through code line by line. I had the DevTools open everytime I ran port 8000 as it made it very easy and quick to problem solve. The best feature in DevTools was the lighthouse test. It allowed me to see problem areas on the site as it was in production and increase the website's efficiency by pointing me in the direction of bad practices or loading speed issues. By using the DevTools I was also able to check for responsive issues and make sure that the website worked well across all devices.  
I did install coverage to help with testing but found issues with getting the coverage check html page to display until the end of my development time, meaning I did not have as much time as i'd hoped on running the tests. What I used instead was [Extends-Class](https://extendsclass.com/python.html). This allowed me to check code as I went along to make sure that everything worked as it was supposed to.  
The images below are of validation tests:  
HTML Check  
![HTML Check](/media/html-check.png)  
![CSS Check](/media/css-check.png)  
![Lighthouse Check](/media/lighthouse.png)  
![PEP8 Check](/media/pep8.png)  

<a name="help"></a>
# Help
Creating this website required a lot of help and a fair amount of external websites were used to guide me on my way. Each one is pointed out below, and any code taken directly from anywhere will be acknowledged above the code itself:  
I would like to give a huge thank you as always to my mentor Antonio Rodriguez for going above and beyond to help me understand any issues and better myself as a junior developer!  
[Django-Central](https://djangocentral.com/building-a-blog-application-with-django/)  
[Tiny.png](https://tinypng.com/)  
[BlogTutorial](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)  
The BlogTutorial link above was used mainly when trying to set up the like functionality.  
[StackOverflow](https://stackoverflow.com/)  
[Freepik](www.freepik.com)  
[Slack](https://slack.com/)  
Placeholder photo created by user6702303  
Photo by Scott Webb from Pexels  
To my knowledge the only code that was directly copied was the initial Post model in models.py from django central. Stack overflow and Slack proved very helpful aswell, I had several helpful tips from people posting on those sites, but no code was copied directly from either stack overflow or slack.  
As a side note, the 'Think Before I Blog' videos from Code Institute helped out a lot too.

<a name="bugs"></a>
# Bugs
I encountered a few issues along the way, the issues are all noted below along with how I went about fixing the issue:  
I found a but with liking posts. It took me a few days to sort it out. But even now it's not quite right. The button is supposed to change color when pressed, but it does not. I could fix this issue by having an in depth look at the like view but I wanted to focus my attention onto larger bugs.  
I had an issue with ckeditor, as I wasn't able to risize the text area along with the rest of the input areas on the website. To get around this issue, I added a scroll ability to allow users to have access to the full editor box without it leaving it's container.  
There was a commit issue. Commit number 11 has the wrong message attatched to it. I did try to research how to change the commit message but I was not successful, the messages states "Delete current migrations and remigrate models due to unknown error" The message was supposed to state "Coppied allauth files into templates folder. Remigrate models due to error"  
This one wasn't as much of a bug as it was lack of time, But towards the end of production I realised that I wasn't going to be able to add an edit profile page as intended. This was because I used Allauth for the authentication and didn't realise that it would complicate things for the profile page. So as a temporary measure I changed it so a contact page, with my email address. So user's can contact me to have changed made to their account. Once I have this project graded I will go back and add the edit profile feature.  
I also wasn't able to add comment deletion functionality from the front end as it proved difficult to keep track of who wrote what then they don't have to have an account to comment. This is something that I will go back and look in in the future!  
I found a issue when validating the html with the category names. I did not have time to fix the issue properly before handing in the project so as a fix for now I added - between any spacing in the category names to stop it flagging up as an error. I will slugify the category names in the future

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
User stories were an integral part of the production process as it allowed for me to stick to a mapped out plan. 
I had two lots of user stories, the first one is located in this repo on github, I used github's project feature to create a user story board. However I found that I wasn't sticking to it very well and so I decided to have a hand written one that I kept next to the compuer. I found it much easier that way, once the project was complete I typed it up and it will be pasted below:  
![User Stories Written](/media/user-stories.png)
