# <img src = "travelBlog/static/Files/Logo/TravelBlogLogo.png" width = "150" height = "150"></img> 
## A Django frontend project intergrated with PostgreSQL backend 
### Developed by Fabliha Hossain


**Project Objective:** After implementing websites with Python Flask, I wanted to see how it compares to the Django Web Framework. This particular site allows users to share their travel journeys with other travelors around the world. 

**Login Demo:** The following gif shows the initial welcome page that provides routes to the login and register pages. Once the site validates a user's credentials, the welcome page is updated to show a menu of options that the user can engage in. In a (potentia) future version of this site, the user could be able to have a page dedicated to their own entries to view, edit, delete, etc.
![Login Demo](travelBlog/static/Files/VideoDemos/login.gif)

**Homepage:** The homepage of the site showcases all the uploaded entries in the database. It is currently in chronological order, where the latest entry is shown at the beginning. In a potential future version, the entry card could include the date and time of when it has been uploaded.
![Entry Cards Demo](travelBlog/static/Files/VideoDemos/entryCards.gif)

**Entry Display Demo:** This next gif shows a closer example of a travel entry. It utilizes a carousel to display the images and their respective descriptions. The user can either click the previous and next arrow buttons to go through the images, or let the carousel automatically scroll through them.
![Entry Example Demo](travelBlog/static/Files/VideoDemos/fullEntryExample.gif)

**Registration Page:** The below screenshot show a standard register page. It simply asks for name, email, username, and password. Error handling has been implemented to prevent multiple users having the same username.
![Register Page](travelBlog/static/Files/Screenshots/RegisterPage.png)

**New Entry Page:** This final screenshot shows the form that a user must fill out in order to submit their entry to the site. In this devleopmental environment, the user can upload up to 5 images per entry. Proper error handling is implemented to ensure that the number of descriptions match the number of images uploaded (and vice versa).
![New Entry Page](travelBlog/static/Files/Screenshots/AddEntryPage.png)


###### Technology Decisions:
* Django
* PostgreSQL 
* Javascript
	* Bootstrap 4.5
* HTML

**License Info:** This work is licensed under a *Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License*
https://creativecommons.org/licenses/by-nc-nd/4.0/