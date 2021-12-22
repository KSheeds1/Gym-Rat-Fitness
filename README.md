# Gym Rat Fitness

## ***Welcome to the rest of your life!***

Beginning your fitness journey can be an overwhelming experience and it can be difficult to know where or how to begin. From figuring out how to build and structure your workouts, to developing the right nutrition plan for your goals, it’s easy to get stressed or disheartened by the journey ahead. That’s where ***Gym Rat Fitness*** steps in to help! We deliver an all-inclusive app experience for people at every stage of their fitness journey, providing detailed workout programs and nutrition plans tailored to your specific goals.

# Demo

Visit the live site [here](#)
INSERT AM I RESPONSIVE IMG HERE

# Contents

* [UX](#)
  * [User Stories]()
  * [Strategies]()
  * [Scope]()
  * [Structure]()
  * [Skeleton]()
  * [Surface]()
* [Features]()
  * [Existing features]()
  * [Features left to implement]()
* [Technologies Used]()
  * [Languages]()
  * [Frameworks, packages, libraries and toolkits]()
* [Database]()
  * [Schema]()
  * [Breakdown of schema]()
* [Testing]()
* [Deployment]()
  * [Git]()
  * [GitHub]()
  * [Heroku]()
  * [AWS]()
  * [Email]()
* [Credits]()
  * [Code]()
  * [Content]()
  * [Media]()
  * [Acknowledgements]()

# UX

## User Stories

***As a casual unregistered user, I want to be able to:***

* Navigate across the site easily
* Quickly identify any new programs or deals
* Browse the available programs and nutrition plans
* Search for a particular program I’ve heard about
* View my bag and the items added to it
* Add an item to my bag
* Edit the quantity of items from my bag
* Delete or remove an item from my bag
* Make a once-off purchase securely without creating an account
* Have the option to create an account if I like the content of the site
* Have the option to email the company with any questions I have that are not answered on the site

***As a returning user, I want to be able to:***

* Easily login of my account
* Easily logout of my account
* Post updates of my progress to my profile
* Update one of my posts
* Delete one of my posts
* View posts from users that I follow in one place
* ‘Follow’ another user to keep up to date with their journey
* Easily purchase a program, nutrition plan, or merchandise
* Pay a subscription fee for access to Gym Rat Fitness
* Pay for my program or plan in a once-off payment
* Save and/or update my shipping address
* View my order history and the programs I have completed

***As the site owner or admin, I want to be able to:***

* Login to the administration panel
* Add a new program or nutrition plan to the site without logging into the admin panel
* Edit/update any program or nutrition plan on the site without logging into the admin panel
* Delete any program or nutrition plan on the site without logging into the admin panel
* Receive notification of emails sent from users submitted from the contact page

## Strategies

### Purpose & Objectives

* The purpose of this site is to provide a well-structured fitness subscription application where users can purchase a variety of exercise programs, nutritional plans and merchandise. Gym Rat Fitness is a community driven app and provides a 'Community' platform for all registered users to engage with other users to follow each others progress, make new Gym Rat friends, ask questions, and to keep each other accountable. GDF offers a variety of programs catering to all levels of fitness, we've also got nutrition in the bag as well! Each program comes with a built-in nutritional guide to take the hassle out of creating your own meal guides, with thousands of meals to choose from built into the app.

* The objective of this site is to provide the framework necessary for users to purchase exercise programs, nutrition plans, and merchandise securely using Stripe to process card payments. A range of payment options for users has also been included (once-off payments & subscription-based payment model). As a means of encouraging and maintaining user engagement and interaction, a community platform has been established using Stream Django to integrate activity streams for users to interact with one another. The combined use of Django and Bootstrap to build the app provides a user-friendly front-end for users to interact with.

### Owner Goals

* To build an active community based around Gym Rat Fitness exercise programs, nutrition plans and merchandise.
* To build and encourage a community atmosphere through user engagement using Django-streams as the base platform to do so.
* To provide a variety of payment options such as once-off payments and a subscription-based payment model, to cater to all economic demographics.

## Scope

 The functional requirements put in place help aid the user to access the content they are looking for quickly and easily, guide them through the payment and purchasing process smoothly, and encourage further user engagement with the site. The functional requirements provide the framework for users to:

* Create an account
* Log in/out
* Select a payment option that suits the user
* Purchase Gym Rat Fitness exercise programs, nutrition plans and merchandise securely
* Perform CRUD operations on their own information and profile page
* Interact and engage with other users

User feedback is provided throughout the site to aid user actions. This is all combined to present a user-friendly, intuitive, front-end design to maximise UX:

* Django
* Python
* Stream-Django
* Stripe

 The required content for the site is:

* Product/item content for Gym Rat Fitness exercise programs, nutrition plans and merchandise. - THIS NEEDS REWORDING
* Media files for Gym Rat Fitness exercise programs, nutrition plans and merchandise.
* User feedback in the form of toasts
* Tooltips to aid the user

## Structure

* The site is designed to foster intuitive learning; the aim is to provide an intuitive interaction between the user and the website.
* Content is structured logically and grouped categorically.
* Users can quickly identify and access the information they are looking for.

## Skeleton

 **Wireframes:**
Wireframes were created for each HTML file across a variety of viewports (mobile, tablet/iPad, laptop/desktop).
The wireframes for each can be viewed here:
[Home]()
[Programs]()
[Program Details]()
[Nutrition]()
[Nutrition Details]()
[Community]()
[Profile]()
[Bag]()
[Login]()
[Sign Up]()

## Surface

 **Aesthetic:** As the app is orientated towards a fitness demographic, I wanted to keep the feel of the site modern, clean and bright with pops of accent colours.
  
 **Colour Palette:** I chose to use x colours throughout the site, base colours and accent colours.

**Typography:**

**Images:** The images chosen are all fitness orientated and intuitively provide further context to the purpose of the site.

# Features

## Existing features

**Navigation Bar:**
The navigation bar is available in the default position and allows users to quickly identify the different sections of the site. On mobile and table viewports, these sections are available in a collapsible menu to provide a cleaner layout on smaller screens. The sections presented on the nav-bar change depending on the following:

1. Whether the user is logged in.
2. Whether the user logged in is actually a site admin.
3. Whether the user is casually browsing the app.

**If the user is logged in, the navigation bar will display the following:**
INSERT IMAGE OF LOGGED IN USER NAV BAR HERE
**If the user logged in is a site admin:**
INSERT IMG OF LOGGED IN ADMIN NAV BAR HERE
**If the user is casually browsing the app:**
INSERT IMG OF CASUALLY BROWSING USER NAV BAR HERE

The changes in the sections presented in the navigation bar depend solely on the status of the user. Changes will be seen depending on whether you are casually browsing, are registered user, or a site admin. For both the registered user and site admin there is additional functionality made available.
***
**Search Functionality:**
As the app was constructed in a mobile-first approach with user interaction and experience in mind, the choice was made to build the search bar functionality directly below the navigation bar. It is hidden until toggled by the search icons as seen in the navbar, or in the floating action button available on the bottom right hand corner of the screen. The addition of the search functionality minimises the amount of time a user has to spend trying to find what they are looking for.  

INSERT IMG OF THE SEARCH FUNCTIONALITY
***
 **User Accounts:**
To register or create an account with the app, the user is required to provide a unique, validated username and password. To log in, a registered user will be prompted to provide this username and password to gain access to their account. Security measures have been put in place by the site owner to protect user log-in details. Once logged in the user will be redirected to their profile page.
***
**User Profile:**
User profiles are created automatically when a **user registers for the app**. Once a user registers, they are redirected to their profile. The user profile can be found in the 'Community' navbar dropdown. From the profile, a user can:

* Add a profile image
* Post updates of their progress, ask questions etc
* Edit their own posts
* Delete their own posts
* View order history and programs completed in the past
* Save default delivery information to their profile - This information is **only visible to the account owner - not to other users**.
* Update default delivery information from their profile

***
**User registration not required for once-off payments:**
In line with most online stores, the functionality to make once-off purchases and payments ***without*** a registered account was implemented. It was thought that a casual, or first-time browser of the site may be less inclined to make the purchase if they were required to create an account with the site first, and that it would also deter those who chanced across the Gym Rat Fitness and decided to make a impulse purchase.
INSERT IMGS HERE
***
**Bag:**
The user's bag is always available in the navbar, it can be accessed at any time, from any page of the site. From here, the user can perform the following actions:

* Update item quantities
* Remove items from bag
* Access the checkout page

**Note:** Any changes to item quantity or the removal of an item from the bag will be **reflected immediately in the grand total** displayed in the bag.
***
**Checkout:**
From the checkout page:
**Unregistered users can:**

* Add their delivery information
* Pay securely via Stripe

**Newly registered users can:**

* Add their delivery information
* Select the option to save this information as their default delivery info, adding it to their profile for future purchases.
* Pay securely via Stripe

**Return users can:**

* Be redirected to the checkout page and their default delivery information will be populating the form. (Provided they had previously selected the option to save this info.)
* Update the default delivery information populating the form field and save this updated information to their profile also.
* Pay securely via Stripe

***
**Stripe: Individual & subscription-based payment models:**
All card payments are processed securely by Stripe, GRF has also implemented additional safeguards to ensure a successful user payment is always processed and that the order has been received and saved to its database. It was decided to implement **two payment models** within the site to accommodate all economic demographics. Users can choose to make either an:

* Individual payment
* A subscription fee

**Payment flow or process:**
Regardless of the user's status or payment model, the payment flow or process remains the same:

* Delivery information is provided
* Card payment details are input
* A loading screen appears during the processing of the payment to discourage any action by the user that may cause the payment to fail
* Upon a **successful transaction** the user is redirected to the success page which details order confirmation and order summary
* User receives an order confirmation email to the address provided in the delivery details
* In the event of an **unsuccessful transaction**, the user is made aware of the failed attempt and Stripe provides user feedback detailing the issue

**Safeguards:**
Gym Rat Fitness has implemented safeguards in the event of the following scenarios:

* Accidental user action during the processing of the payment eg. closing the browser or tab
* Any issues with submission of the payments form

**Provided that the payment was successful, Stripe will still create the order for the user.**
***
**Individual payment Vs. Subscription fee:**
The only advantage or benefit afforded to users who subscribe to the subscription model of payment is time. Subscription based users will have access to their program or nutrition plan for either:

* Six months
* One year

**This solely depends on which option the user selected when adding the *subscription option* of the program or plan to their bag.**

**Individual payments for programs or plans only provide *access for the stated length of time allotted to the chosen program and/or plan - six weeks or eight weeks.***

Regardless of payment method all users will have access to the same great programs and nutrition plans.
***
**Activity Streams:** - WILL NEED WORK COME IMPLEMENTATION
Stream-Django has been implemented within the 'My Community' section of the app. This feature of the site is **available only to registered users of the app**. It was decided to implement this functionality as a means of encouraging and maintaining user interaction and engagement with the site. The activity stream works in the following manner:

* Users can choose to follow other app users
* From the 'My Community' page users can view posts from other users they follow
* Users can comment on other user's posts
* Users can post from their profile page or from the my community page and their posts will appear in the streams of the those who follow them

The implementation of Stream Django increases user interaction with the site and fosters a sense of community between the users and the brand.
INSERT IMGS HERE
***
**CRUD Operations:**
The following CRUD operations are restricted to registered users of the app only:

* Create
* Update/Edit
* Delete

**Note:** Registered users only have access to perform CRUD operations on their **own profile**.  
INSERT IMGS HERE
Casual or first-time users of the app are able to browse through all areas of the site but, will not be permitted to perform the aforementioned operations. All users will the ability to browse the programs, nutrition plans, and merchandise available on Gym Rat Fitness.
***
**Floating Action Buttons:**
The addition of floating action buttons (Search and Scroll to the top) were added to enhance both UI and UX. On any page where the navigation bar is no longer visible, users can instead use the floating buttons to either search for a program or plan or, to trigger scroll to the top. This was implemented primarily for smaller viewports but was added to all viewports to increase user satisfaction towards the app.
INSERT IMGS HERE
***

#### **Administrative Features:**

**CRUD Operations:**
CRUD operations of **all programs, plans, and merchandise is restricted only to GRF superusers**. Only superusers have the permissions to **create, update, or delete** programs, plans, or merchandise. Upon logging in using admin credentials, superusers will have access to the following site pages from the **'Management' dropdown menu located in the navbar**:

* Program Management
* Nutrition Management
* Merch Management

From these management pages, superusers can perform CRUD operations as necessary to the selected program, plan or merchandise. This reduces the need to sign into the Django admin panel as the operations can be carried out on the site itself.

WILL NEED WORK COME IMPLEMENTATION ->
**Create:**

* To create a program, plan or piece of merchandise, the superuser the superuser can navigate to the appropriate management page, select the 'Add item' button and fill out the form required. Upon submission, the item will be created, both on the site and in the database.

**Update:**
To update a program, plan or piece of merchandise, the superuser can:

1. Navigate to the appropriate management page and search for the item they wish to update and make the necessary edits to the pre-existing form data. Upon submission, the item will be updated, both on the site and in the database.
2. Search for the item using the search functionality, once redirected to the details page of the item, a superuser can click the edit button to redirect them to the edit form. From here the superuser can make the necessary edits to the pre-existing form data. Upon submission, the item will be updated, both on the site and in the database.

**Delete:**
To delete a program, plan, or piece of merchandise, the superuser can:

1. Navigate to the appropriate management page and search for the item they wish to delete. Once located click the 'delete' button, this will trigger a modal prompting confirmation of admin action. To delete the item click the delete button displayed in the modal to remove the item from the site and database.
2. Search for the item using the search functionality, once redirected to the details page of the item, a superuser can click the delete button. this will trigger a modal prompting confirmation of admin action. To delete the item click the delete button displayed in the modal to remove the item from the site and database.

***

## Features left to implement

* Site quiz to choose a program for a user depending on their goals

*
***

# Technologies Used

## Languages

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScipt](https://en.wikipedia.org/wiki/JavaScript)
* [Python3](https://www.python.org/)
  
## Frameworks, packages, libraries and toolkits

* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Pip3](https://pip.pypa.io/)
* [jQuery](https://jquery.com/)
* [Font Awesome](https://fontawesome.com/)
* [Google Fonts](https://fonts.google.com/)

## **Others Technologies**

* [GitHub](https://github.com/) used to host the GRF repository.
* [Git](https://git-scm.com/) used for version control of GRF project.
* [GitPod](https://www.gitpod.io/) used to develop the project.
* [Heroku](https://www.heroku.com/) used to deploy the live site.
* [Stripe](https://stripe.com/ie) used as the once-off and subscription payments system
* [Balsamiq](https://balsamiq.com/) used to create the wireframes for the GRF project.
* [PowerMapper](https://www.powermapper.com/) used to verify cross-browser compatibility.
* [Favicon.io](https://favicon.io/) used to create GRD favicon.
* [RandomKeygen](https://randomkeygen.com/) used to generate a secure password for environment variable `SECRET_KEY`.
* [Miniwebtool](https://miniwebtool.com/django-secret-key-generator/) used to generate a Django `SECRET_KEY`
* [Upsplash](https://unsplash.com/) free images used throughout site found on Upsplash. (Acknowledgments in the credits section)
* [Autoprefixer CSS](https://autoprefixer.github.io/) used to parse CSS and add vendor prefixes to custom CSS file.
* [Am I Responsive](http://ami.responsivedesign.is/) used to create the demo image seen in the README.
* [Lighthouse](https://developers.google.com/web/tools/lighthouse) used to audit the app for improved performance and UI.

# Database

This app utilizes two different databases:

* **Sqlite3** - used for development
* **Postgres** - used for production

## Schema

## Schema breakdown

# Testing

Due to the size of the testing section, you can find all documentation related to the testing of Gym Rat Dictionaries [here]().

# Deployment

## **Git: version control**

**Using Git to add, commit, and push code into a repository:**
Storing files in Git is a two-stage process:
​1. Files must be **added to the staging area** using the `git add` command followed by the specified file name.
​2. Files must be **committed** to the repository using the `git commit -m` command followed by a specified message within double quotation marks:
`git commit -m "Initial commit."`

**Note:** that it is common practice when making your first commit to a repository to provide the message "**Initial commit.**".

**Pushing code to GitHub:**
This is achieved by connecting your local repository with your remote repository and pushing the code from local to remote. Storing your code in a remote repository on a remote server allows it to be backed up and also be accessed by others. Once you have added the files to the storing area, committed the files to the repository, you then push your files to GitHub. Using the `git push` command to push the code from your local repository to the remote repository.

**To commit changes to your local repository and push to your remote repository:**

* Start from the terminal by pressing **CTRL+C** to stop the server.
* Run `ls` to list the files.
* Begin adding and committing the code as outlined in step 1 & 2 of storing files in Git.
* Run `git status` to view all files added to the staging area.
* Run `git commit -m` followed by your message contained in double quotation marks, adding the files to your local repository: `git commit -m "Initial commit."`
* Once the files have been committed, push them to the remote repository using `git push`.

```
ls
git add . # '.' used to add all modified files
git commit -m "Initial commit."
git push
```

For more information on commonly used Git CLI instructions, check out this [cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf)

## **GitHub:**

This repository is hosted by GitHub, but deployed by Heroku.

### **Clone this repository:**

When you clone a repository, you copy the repository from github.com to your local machine. Cloning a repository pulls down a full copy of all the repository data that GitHub.com has at that point in time, including all versions of every file and folder for the project.

 Cloning this repository can be achieved through the following methods:
**Method 1 GitHub CLI:**

* Use the `repo clone` subcommand in the terminal:
`git repo clone repository-name`
* You can also use the GitHub URL to clone a repository:
`git repo clone https://github.com/owner/repo`

**Method 2 Clone from GitHub:**

* Click **Open with GitHub Desktop**.
* Follow the prompts in the GitHub Desktop application or follow the steps outlined in the [GitHub Docs for cloning a repository](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop).

**Method 3 Clone from GitHub:**

* Navigate to the main page of the repository.
* Above the list of files, click the '**Code**' button.
* To clone the repository using **HTTPS**, under '**Clone with HTTPS**', click the **clipboard** symbol.
* Open Git Bash.
* Change the current working directory to the location where you want the cloned directory.
* Type `git clone` and paste in the copied URL
`$ git clone https://https://github.com/KSheeds1/`
* Press **Enter** to create your local clone.
* Run `git remote rm origin` in your terminal to remove the link to this repo.

**When you clone a Django project from GitHub there are some additional *necessary* steps to be taken to run this repo:**

#### 1. Install necessary project dependencies listed in the requirements.txt file

This can be achieved by running the following command in the terminal of your IDE:
`pip3 install -r requirements.txt`

#### 2. Create and store the necessary environment variables

**GitPod:**

* Navigate to your GitPod workspaces dashboard
* Click on '**Settings**' and then select '**Variables**'
* Store the following variables here:

```
| Key               | Value                  | Notes                                                                                   |
|-------------------|------------------------|-----------------------------------------------------------------------------------------|
| DEVELOPMENT       | True                   |                                                                                         |
| SECRET_KEY        | YOUR_SECRET_KEY        | This is a randomly generated string generated by RandomKeygen to keep sessions secure.  |
| DATABSE_URL       | YOUR_DATABASE_URL      |                                                                                         |
| STRIPE_PUBLIC_KEY | YOUR_STRIPE_PUBLIC_KEY | This is the publishable key taken from the Stripe dashboard, developer section          |
| STRIPE_SECRET_KEY | YOUR_STRIPE_SECRET_KEY | This is the secret key taken from the Stripe dashboard, developer section               |
| STRIPE_WH_SECRET  | YOUR_STRIPE_WH_SECRET  | This is the signing secret taken from the Stripe dashboard, developer webhooks section  |
```

**Env file:**
Otherwise you can store your variables in an **env.py** file:

* Create a file named 'env.py', this can be done from the terminal: `touch env.py`
* Add your environment variables to the file
* Add this file to a .gitignore file to prevent these variables from being included in version control

**Create a .gitignore file:**

* Create a .gitignore file in the root directory of the project. (A gitignore file specifies intentionally untracked files that Git should ignore. For more information on gitignore files, check out the [Git documentation for gitignore](https://git-scm.com/docs/gitignore).)
* Add the env.py file to the gitignore file: `env.py`

#### 3. Migrate the database models

Run the following commands in the terminal:

* `python3 manage.py makemigrations`
* `python3 manage.py migrate`

#### 4. Load data

**Note:** The **order** in which the **data is loaded matters**, as the **products are dependent on the categories existence**.
**1.** `python3 manage.py loaddata categories`
**2.** `python3 manage.py loaddata products`

#### 5. Create a superuser

In order to access the Django admin panel, you will need to create a superuser. A superuser is permitted to create, read, update, and delete data in the Django admin. A superuser can have permission to manage all objects.

* In the terminal, run the following command:
`python3 manage.py createsuperuser`
* Enter your username and press enter:
`Username: admin`
* You will then be prompted to enter your email address:
`Email address: admin@example.com`
* Finally, create a password. You will be asked to enter your password **twice**:

```
Password: ********
Password (again): ********
Superuser created successfully.
```

#### 6. Start the development server

* In the terminal of your IDE, type the following command to run the app:
`python3 manage.py runserver`
* Click on option to view the site in the **browser**
* To access the django admin panel add "/admin/" to the end of the URL

To run **locally**, you can clone this repository, or pull the code from this GitHub repository: INSERT GITHUB REPO URL

### **Fork this repository:**

A fork is a copy of a repository that you manage. Forking a repository allows you to freely experiment with changes without affecting the original project.

To fork this repository:

* Log into GitHub and navigate to this repository [here]()
* In the top-right corner of the page, click '**Fork**'.
* From there, you will have a copy of the repository.

#### 1. Install necessary project dependencies listed in the requirements.txt file

This can be achieved by running the following command in the terminal of your IDE:
`pip3 install -r requirements.txt`

#### 2. Create and store the necessary environment variables

**GitPod:**

* Navigate to your GitPod workspaces dashboard
* Click on '**Settings**' and then select '**Variables**'
* Store the following variables here:

```
| Key               | Value                  | Notes                                                                                   |
|-------------------|------------------------|-----------------------------------------------------------------------------------------|
| DEVELOPMENT       | True                   |                                                                                         |
| SECRET_KEY        | YOUR_SECRET_KEY        | This is a randomly generated string generated by RandomKeygen to keep sessions secure.  |
| DATABSE_URL       | YOUR_DATABASE_URL      |                                                                                         |
| STRIPE_PUBLIC_KEY | YOUR_STRIPE_PUBLIC_KEY | This is the publishable key taken from the Stripe dashboard, developer section          |
| STRIPE_SECRET_KEY | YOUR_STRIPE_SECRET_KEY | This is the secret key taken from the Stripe dashboard, developer section               |
| STRIPE_WH_SECRET  | YOUR_STRIPE_WH_SECRET  | This is the signing secret taken from the Stripe dashboard, developer webhooks section  |
```

**Env file:**
Otherwise you can store your variables in an **env.py** file:

* Create a file named 'env.py', this can be done from the terminal: `touch env.py`
* Add your environment variables to the file
* Add this file to a .gitignore file to prevent these variables from being included in version control

**Create a .gitignore file:**

* Create a .gitignore file in the root directory of the project. (A gitignore file specifies intentionally untracked files that Git should ignore. For more information on gitignore files, check out the [Git documentation for gitignore](https://git-scm.com/docs/gitignore).)
* Add the env.py file to the gitignore file: `env.py`

#### 3. Start the development server

* In the terminal of your IDE, type the following command to run the app:
`python3 manage.py runserver`
* Click on option to view the site in the **browser**
* To access the django admin panel add "/admin/" to the end of the URL

## Heroku Deployment

This project was deployed using Heroku. Heroku is a PAAS (platform as a service) that enables developer to build, run and operate applications entirely in the cloud. Heroku integrates with GitHub to make it easy to deploy code living on GitHub to apps running on Heroku.

### Create a Heroku app

Sign in or create an account on heroku.com:

* Click '**New**' on the dashboard and select '**Create new app**'.
* Provide a unique app name including dashes, select your region, and click '**Create App**'.
* On the **resources** tab, provision a new **Postgres** database for the app by searching for it in the search bar.
* Select the **hobby-dev option**.

**Note:** To use Postgres, we need to install **dj_database_url** and **psycopg2-binary**.
In the terminal of the IDE:

```
pip3 install dj_database_url
pip3 install psycopg2-binary
pip3 freeze > requirements.txt
```

Make sure to freeze the requirements to make sure Heroku installs all app requirements.

### Setup the new database

In settings.py, import dj_database_url:

```
import os
from pathlib import Path
import dj_databse_url
```

In the database settings of settings.py, comment out the default configuration and replace the default database with a call to dj_database_url.parse() giving it the **DATABASE_URL** from the Heroku **Config Vars**:

```
# DATABASES = {
#  'default': {
#  'ENGINE': 'django.db.backends.sqlite3',
#  'NAME': BASE_DIR / 'db.sqlite3',
#  }
# }

DATABASES = {
 'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```

With this saved, you're almost ready to connect to the Heroku database, but first you must **run migrations again**:

```
python3 manage.py showmigrations
python3 manage.py migrate  # This will apply all migrations and get the db setup
```

### Import all product data

You can use **fixtures** to do so:
**Note:** The **order** in which the **data is loaded matters**, as the **products are dependent on the categories existence**.
 **1. Load in categories:**
  `python3 manage.py loaddata categories`
 **2. Load in products:**
 `python3 manage.py loaddata products`

### Create a superuser

In order to **access the Django admin panel**, you will need to create a superuser. A superuser is permitted to create, read, update, and delete data in the Django admin. A superuser can have permission to manage all objects.

* In the terminal, run the following command:
`python3 manage.py createsuperuser`
* Enter your username and press enter:
`Username: admin`
* You will then be prompted to enter your email address:
`Email address: admin@example.com`
* Finally, create a password. You will be asked to enter your password **twice**:

 ```
 Password: ********
 Password (again): ********
 Superuser created successfully.
 ```

**BEFORE you commit the changes:** Uncomment the original database configuration and **delete** the dj_database configuration so it won't be added to version control. Add, commit, and push your changes with Git. With this done the Heroku app and database are ready.

### Deploying to Heroku

In the database settings of settings.py, create an if statement to toggle between the two databases depending on whether :

* The app is running on **Herkou**, where the **DATABASE** variable is defined, it **connects to Postgres**.
* Otherwise **connect to sqlite3**.

 ```
 if 'DATABASE_URL' in os.environ:
  DATABASES = {
  'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
  }
 else:
  DATABASES = {
   'default': {
   'ENGINE': 'django.db.backends.sqlite3',
   'NAME': BASE_DIR / 'db.sqlite3',
  }
 }
 ```

A few more **steps are necessary for deployment**:

1. Install **gunicorn** - this will act as the webserver

 ```
 pip3 install gunicorn
 pip3 freeze > requirements.txt
 ```

2. **Create a Procfile** and add the following to **tell Heroku to create a web dyno** which needs **gunicorn to server the django app**:

 ```
 web: gunicorn gym_rat_fitness.wsgi:application 
 ```

3. **Temporarily disable COLLECTSTATIC** - to prevent Heroku from trying to collect the static files when you deploy. To do this use the following command in the terminal of your IDE:
`heroku config:set DISABLE_COLLECTSTATIC=1 --app *add_app_name_here*`
**Note:** The --app flag is only necessary if you have more than one app with Heroku.

4. Add hostname to ALLOWED_HOSTS in settings.py

 ```
 ALLOWED_HOSTS = ['gym-rat-fitness.herokuapp.com', 'localhost']
 ```

 `localhost` allows GitHub to keep working too.

### Attempt First Deployment

* Add files and commit your changes
* Push to **GitHub**
* Push to **Heroku**

 ```
 git add .
 git commit -m "Attempt first deployment."
 git push
 git push heroku main
 ```

**Note:** If you created the app **on the Heroku website**, you will have to **initialize the Heroku git remote** using the following command:
`heroku git:remote -a gym-rat-fitness` and then **run the push to Heroku again**.

### Setup enable automatic deploys

On the Heroku website:

* Navigate to the **deploy** tab
* Click on **Connect to GitHub**
* Search for the repository
* Click **Connect**
* Followed by **Deploy Branch (main)**

Following this when you **push to GitHub**, the code will be **automatically deployed to Heroku**.

### In settings.py make the following changes

1. Replace the old SECRET_KEY with:
`SECRET_KEY = os.environ.get('SECRET_KEY', '')`

 Generate a **Django Secret Key** and add it to the **Heroku Config Vars**. This is the **key for the Heroku app**. You will also need to **generate one for GitPod and save it as 'SECRET_KEY' in your environment variables**.

2. Set DEBUG:
`DEBUG = 'DEVELOPMENT' in os.envrion` - This sets DEBUG to True **only if** the variable DEVELOPEMENT is **in the environment**.

3. Commit and push your changes:

 ```
 git add .
 git commit -m "Removed secret key and set DEBUG."
 git push
 ```

This completes the deployment of your site to Heroku.  You will be able to confirm a successful deployment from the Heroku.
![Heroku Deployment successful]()

Click on **Open App** in the right hand corner of your Heroku account, this will open your live site in another tab.

**Note:**

* You can create a Django Secret Key [here](https://miniwebtool.com/django-secret-key-generator/).
* For more information on GitPod environment variables, watch this [video](https://www.gitpod.io/docs/environment-variables).
* If you need any more information on Heroku Deployment click [here](https://devcenter.heroku.com/start).

## Amazon Web Services

AWS S3 is a cloud-based storage service, this site uses AWS S3 Bucket to store the static files and images for this site.

**To create an S3 Bucket:**

* Sign up or login to the **Amazon management console** under **My Account**
* Open S3 and create a bucket
  * Name your bucket to **match your Heroku app name**
  * Select the region closest to you
* Uncheck '**block all public access**' and acknowledge that the bucket will be public
* Click **Create Bucket**
* In the **Permissions** tab, turn on **static website hosting**
  * Click **Enable**
  * Click **host a static website**
  * Fill in 'index.html' and 'error.html' where asked
  * Click Save
* In the permissions tab, set up the required access between the Heroku app and the S3 Bucket by **adding the following code block into the CORS Configuration**:

```
[
   {
     "AllowedHeaders": [
      "Authorization"
     ],
     "AllowedMethods": [
      "GET"
     ],
     "AllowedOrigins": [
         "*"
     ],
     "ExposeHeaders": []
   }
 ]
```

* Navigate to the 'Bucket Policy', click '**Edit**', and select '**Policy Generator**' to generate a security policy for the bucket
* Select the policy type **S3 Bucket Policy** from the dropdown
* In the policy, add the following settings to 'Statement':

```
"Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::ksheeds1-boutique-ado/*"
        }
    ]
```

* Click 'Add Statement' & then 'Generate Policy'
* Copy the policy from the modal and paste into the bucket policy editor
* Add '/*' on to the end of the **Resource key** and **save**
* Go to the **Access Control List**
* Confirm that the list objects permission is set to **everyone** in the in the **public access section**.

### AWS IAM (Identity and Access Management)

With the S3 Bucket ready to go, you need to **create a user to access it**, this can be done through IAM.

* Access IAM through the search bar on the AWS Management Console
* Select **Users Groups** from the dashboard, click **Create New Group**
* Set the group name - keep it related to the app name
* Click **Create Group**

#### Create policy used to access the bucket

* Select **Policies** from the dashboard & click **Create Policy**
* On the JSON tab select **Import managed policy** - this will allow you to import one from AWS, pre-built for full access to S3
* Search for S3 and **Import 'S3 Full Access Policy**
* Delete the asterisk from the 'Resource key'
* Get the bucket ARN from S3 Permissions and paste it in:

 ```
 "Resource": [
  "arn::aws:s3:::app-name", # The bucket itself
  "arn::aws:s3:::app-name/*" # /* add another rule for all file/folders in the bucket 
 ]
 ```

* Click **Review Policy** and give it a **name** and **description** - Again keep it related to the app and Bucket name. Eg name: manage-gym-rat-fitness description: Access to S3 Bucket for Gym Rat Fitness static files.
* Click **Create Policy**
* This will redirect to the **Policy** page, **attach the policy to the group**:
  * Go to **User Groups**
  * Click on the group and click **Attach Policy**
  * Search for the policy you created, select it and and click **Attach Policy**

#### Create user to put in the group

* Click the **Users** option in the dashboard
* Click **Add Users**
* Add a user name eg., "*gym-rat-fitness-staticfiles-user*"
* Select **Access Key - Programmatic Access**
* Click **Next** through to the end until you reach **Create User** and click that
* Download the CSV file which contains the AWS_SECRET_ACCESS_KEY and the AWS_ACCESS_KEY_ID  - **Add both to your Heroku environment variables**
 **Note: It's important to download and save this file as once you've gone through the process you CANNOT download it again**

### Connect Django to S3

To connect Django to S3, you must first install two packages:

* **Boto3**
* **Django-storages**

 ```
 pip3 install boto3 
 pip3 install django-storages
 pip3 freeze > requirements.txt
 ```

* Add 'storages' to **installed apps** list in settings.py
* Add the variables  **from the CSV file to Heroku Config Vars**
* **Remove** the **DISABLE_COLLECTSTATIC variable from the Config Vars because when you deploy to Heroku this time,**Django will collect static files automatically and upload them to S3.

To connect Django to S3, you need to add the following settings to tell it **which bucket it should be communicating with**.

```
# Check if the environment variable USE_AWS is in the environment & if so define the following:
if 'USE_AWS' in os.environ:  
 # Cache Control
 AWS_S3_OBJECT_PARAMETERS = {
 'Expires': 'Thu, 17 Dec 2099 20:00:00 GMT',
 'CacheControl': 'max-age=94608000',
}

# Bucket Config
AWS_STORAGE_BUCKET_NAME = 'storage-bucket-name'
AWS_S3_REGION_NAME = 'region'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') # Saved to Heroku Config Vars 
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')  # Saved to Heroku Config Vars 
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' # Tell Django where the static files will be coming from in production

# Static and media files
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

# Override static and media URLs in production
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

### Outline production settings for static files and media

This will inform Django that in production you want to **use S3 to store static files whenever someone runs collectstatic and that you want any media files to go there also.**

* Create **custom_storage.py** file
* Import **settings and S3BotoStorage**
* Outline **two classes** telling them to  **store static and media files in location defined in settings.py**:

 ```
 class StaticStorage(S3Boto3Storage):
  location = settings.STATICFILES_LOCATION

 class MediaStorage(S3Boto3Storage):
  location = settings.MEDIAFILES_LOCATION
 ```

* **Add, commit, and push** your changes - triggering an automatic deployment to Heroku

 ```
 git add .
 git commit -m "Connect Django to S3 Bucket."
 git push
 ```

## Email

**Set up Django to send emails:**
**Note:** This procedure will differ depending on which **provider** you use and may change slightly over time due to **changing security policies of email providers.** For this project, Gmail was used as they have a free SMTP server that anyone with a Gmail account can use to send emails.

### Sign up/Login to Gmail

**Sign Up:**

* Navigate to the [create an account page](https://accounts.google.com/SignUp?hl=en) for Gmail.
* Enter your name
* In the "Username" field, enter a username
* Enter and confirm your password
* Click **Next**
  * Optional: Add & Verify a phone number for your account
* Click **Next**

**Login to your account:**

* Go to the [Google Account Sign In page](https://accounts.google.com/signin)
* Enter your email account
* Enter you password
* Click "Sign In"

**Prepare your account:**

* Navigate to the **Account Settings** in the upper right hand corner
* Click on  **Accounts and Imports**
* Then click on **other Google account settings**
* On this screen navigate to the **Security Tab** and under, **signing into Google**
* Turn on **two-step verification** - this will allow us to create an **app password specific to the Django app** that will allow it to **authenticate and use the Gmail account to send emails**.
  * To turn it on, just click **Get Started** and **enter your password**.
  * Select the **verification method of your choice**.
* Once you've verified and turned on two-step verification you will see a new option called **App Passwords** unser the signing into Google heading.
* Click on **App Passwords**
* Enter your password again, if necessary
* On the app password screen, select **mail** from the **Select App Dropdown**
* From the  **Device Type dropdown**, select **Other** and type in **Django**. - (You can set it to the name of your choice)
* With that you'll be given a **16 character password** - **copy it**

**Update Heroku Config Vars:

* On the Heroku dashboard for your project, add the following variables to your Config Vars:

| EMAIL_HOST_PASS | 16_CHARACTER_PASSWORD |
|-----------------|-----------------------|
| EMAIL_HOST_USER | YOUR_GMAIL_EMAIL_ADDRESS   |

### **Add some settings to your Settings.py:**

Use the following procedure to check **which email setup to use:**

```
if 'DEVELOPMENT' in os.environ:
 EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
 DEFAULT_FROM_EMAIL = 'boutiqueado@example.com' # Specify the default from email
else: # for production use:
 EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
 EMAIL_USE_TLS = True
 EMAIL_PORT = 587
 EMAIL_HOST = 'smtp.gmail.com'
 # The following 3 variables will be got from the environment
 EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
 EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
 DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
```

**Deploy to Heroku:**
To complete the set up you need to **deply to Heroku**, which can be done by **committing and pushing all the changes:**

```
git add .
git commit -m "Setup email"
git push
```

**Test the functionality** by navigating to your Heroku app and try to register for an account. If **you receive a confirmation email** this means you have **correctly setup email for your project**.

***
.

# Credits

## Code

## Content

* Majority of the descriptions provided for the products found in the merchandise category on this site were sourced from [HP Nutrition's 'Shakers & Accessories' Category](https://www.hpnutrition.ie/Gym-Gear-Accessories) and [JD Sports 'Accessories Hub'](https://www.jdsports.ie/page/accessories-hub/) - The brand and product names were changed, only the descriptions of the products were used and slightly modified to fit the sites purpose.

## Media

* The images used for each of the products in the merchandise category as sourced from [Adobe Stock Images](https://stock.adobe.com/ie/).

## Acknowledgements
