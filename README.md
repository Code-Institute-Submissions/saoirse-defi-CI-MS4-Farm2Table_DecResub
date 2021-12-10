![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Code Institute, Milestone 4: Farm2Table

## Introduction

Over the past decade, the world has truly become a global economy. Global supply chain expansion has provided unparalleled choice for the consumer. In relation to the food industry, the term 'out of season' has become a thing of the past. No longer do we have to wait until the summer months to enjoy berries or winter for citrus fruits. With the popularity of grocery chains such as Lidl & Aldi, locally sourced fruit & vegetables are being phased out for cheaper produce which is normally shipped halfway across the globe. To endure this expedition, the produce is harvested well before it has reached maturity and ripened in shipping containers by the use of 'controlled environments'. This produce tends to turn bad very quickly due to this unnatural journey, sometimes within 48 hours of purchase causing massive food wastage. Most of us have lost the connection to the food we eat.

With my final milestone project for Code Institute, I will attempt to tackle this problem within our society. My goals is to get Ireland eating locally & in season again by creating a marketplace to connect local producers with consumers. My project Farm2Table aims to reduce the friction associated with sourcing local produce by having all local producers of fruit & veg in one marketplace. This environment will inspire competition between producers, allowing the consumers to easily find the best price for their local fruit & veg.

### Notes for Assessment Team

#### PEP8 Validation Errors

The codebase has been written to comply with the PEP8 validation standard. Unfortunately certain validation errors couldn't be corrected.

##### Line Too Long

Only a handful of these validation errors are still present. The remaining lines of code that are recieving this error couldn't be shortened any further without introducing new validation errors.


### Future Features

This section will outline potential features which I would like to implement in the future.

* Loyalty point system through a native cryptocurrency

## UX

### Project Goals

The goal of this project is to get Ireland eating locally again by creating a marketplace where fruit & vegetable producers will post listings of their produce. This format will increase competition between the farmers as consumers can compare prices directly. Payment will be taken through the application in order to reduce friction once the customer goes to collect their order or has it delivered.

## User Stories

### User Goals

Potential users for this application can be split into 2 groups listed below. It is essential to be mindful of specific needs of both of these user types.

1. Producers
2. Consumers

#### User Needs (Producers)

For this application to be successful we will need to onboard as many fruit & vegetable producers across the country in order to create a competitive marketplace for the consumer. We need to make the registration process as easy as possible.

In order for a seller to be willing to join our app, they will need:

* Access to a phone/computer to maintain their store's dashboard.
* A European Bank Account in order to receive card payments via Stripe.

##### Producer Goals

* To expand my customer base.
* Cultivate an online presence, the benefit of free online advertising.

#### User Needs (Consumers)

The target audience for this application will be users over the age of 25. This is due to the fact that they are generally more concerned about the source/quality of their produce & have access to more discretionary income. Users of the application will be in search of the highest quality fruit & vegetables at the most affordable price.

As a user of this application, I need:

* A central marketplace where I can browse different producers and compare pricing.
* The ability to filter the marketplace to only show sellers within my vicinity.
* Ways to identify how local producers compare to one another in order to make an informed purchase.
* A clean UX that is easy to navigate while also remaining fresh and exciting.
* A quick and simple way to create an account with little to no friction.
* The ability to make purchases using my credit/debit card.
* To be able to quickly identify which sellers can deliver to my area.

##### Consumer Goals

* To eat the best quality produce sourced close to me.
* To find the best price for locally grown produce.
* To support local business.


### Developer & Business Goals

This section will outline my goals as the developer of the project, what the future of the website holds & how to generate revenue from the application.

#### Developer Goals

My goals as the developer of this project are:

1. To provide a neutral platform that will allow grocers to sell directly to the consumer.
2. Provide Stripe integration which will allow payment's to be sent directly to the merchant's bank account.
3. Create a clean and intuitive UI which keeps users.
4. Allow merchant's goods to be in full focus by cultivating an immersive UX for the user that keeps them coming back to shop with us.
5. Once a robust marketplace has been formed within Ireland, the application can be launched in localised foreign markets.


#### Business Goals

Currently, I have identified 3 possible streams of income this project would be able to generate. 

1. A small fee will be applied to each purchase made within the application for connecting the producer with the consumer & processing payment between the 2 parties.
2. Producers will have the ability to purchase premium Farm2Table memberships giving them access to additional features, such as being highlighted on the front page of the website, ad-free storefronts.
3. Advertising revenue will be generated from the web traffic on the application.


### User Stories

|User Type |I want to be able to...  | So that I can... |
| :--- | :--- | :--- |
|Seller|Add my listing to a marketplace|I can attract orders from a larger number of customers|
|Seller|Display product information|Allow the consumer to make an informed purchase|
|Seller|Post a photo of the produce|Entice customers to purchase my produce|
|Seller|Update listings|Change product descriptions, quantities, availability or pricing|
|Seller|Delete listings|Remove items that are no longer for sale|
|Seller|Receive reviews from consumers|See areas at which I can improve upon|
|Seller|Display my reviews to the end user|Encourage new users to choose me over my competitors|
|Seller|See the pricing of other producers|Regulate my pricing accordingly|
|Seller|Update listings|Change product descriptions, availability or pricing|
|Seller|Provide delivery options to the customer|Avoid the customer having to collect the order|
|Seller|Take electronic payment|Reach a larger customer base|
|Seller|Views all of my orders in one place|Keep track of the business at a granular level|
|Seller|Secure Authentication|Have peace of mind in relation to the security of the account|
|  |  |  |
|Buyer|To view all listings in one marketplace|Find the best price or closest producer|
|Buyer|View individual product details|Make an informed purchase|
|Buyer|Easily view the total of my purchases|Control how much I am spending|
|Buyer|To view my previous orders|Compare current pricing or to review my spending|
|Buyer|Sort marketplace listings by category|Search for exactly the type of product I want|
|Buyer|Sort marketplace listings by price|Find the best price|
|Buyer|Sort marketplace listings by a number of categories simultaneously|Exclude product types that I'm not searching for|
|Buyer|Pay for my order within the application|Avoid payment upon collection|
|Buyer|Adjust the quantity of items within my shopping bag|Change my mind before proceeding to checkout|
|Buyer|View order confirmation after checkout|Review my shipping & billing details|
|Buyer|View the seller location before checkout|Make an informed commercial decision|
|  |  |  |
|Site User|Easily register an account|Have a profile in order to start placing orders|
|Site User|Easily log in/logout|Access my profile|
|Site User|Change my password|Recover access to my account in case I get locked out|
|Site User|Receive an email confirmation after registration|Verify that my registration was successful|
|Site User|Have a personalised user profile|View my previous orders|
|Site User|Easily make or receive secure payments|Place orders within the application|
|Site User|Navigate through the website easily|Increase my productivity|
|  |  |  |


1. As a user of this web application I want:
    * A clean and enjoyable UX, everything should be where I want it.
    * Fonts that are legible but something a bit different to the norm.
    * Little to no load times when the website first starts or has to complete a process.

2. As somebody looking to advertise on this website I would like:
    * Content that is family friendly and not provocative, so our brand doesn't become tarnished.
    * Heavy user traffic in order to get our brand in front of as many eyeballs as possible.
    * Fast load times to ensure impatient users don't leave the site.


### Design Choices

#### Favicon

I really enjoy this favicon which was sourced from [Favicon.cc](https://www.favicon.cc/?action=icon&file_id=636006)

![Favicon](media/favicon/favicon.ico)

#### Responsive Front-End Framework

For this project, I decided to use the Materialize framework which is build on the principles of material design. I have previous experience with this framework as I incorporated it into my third milestone project. Throughout the course of this project, the lack of thorough documentation & package support for this framework have turned me off using it in future.

#### Icons

All icons for this application have been sourced from [Google Fonts](https://fonts.google.com/icons) collected from the Material Icons library. As the designer of the web application, the selection of the icons must be done in line with other successful applications. 

##### Favourite Outline Icon

This icon is present on the product_details page when you are logged in to the application. By pressing the button linked to it, the user has the ability to add products to their wishlist.

##### Favourite Icon

Present on the product_details page, if a user's wishlist already contains this specific product, the empty heart icon will be replaced by the full heart.


#### Fonts

The impact that font choice can have on a web application cannot be understated. Web design trends over the past decade have shown that clear and extremely legible sans-serif fonts leads to a dramatic reduction in the user bounce rate. All fonts used within this application have been sourced from [Google Fonts](https://fonts.google.com/icons).

##### Logo Font

The extreme legibility of a font can be sacrificed in the case that is to be displaying the company's logo. For THEVEGTABLE.ie, I have chosen a font named Fjalla One, a sans-serif font that catches the eye while still remaining fully legible to the user.

##### Content Font

The font chosen for the rest of the application's content should be lightweight and extremely legible. This allows the user to relax while browsing through the website as they are not having to strain their eyes when moving from one piece of content to the other. The Lato font was chosen for this task due to its sharp and clean look.


#### Colours

During the design process, I wanted to colour pallet of the application to take inspiration from nature. Greens & Beige have been used to remind the user that purchasing produce locally has a massive effect on the environment and that they're making a 'green' choice.


##### Materialize Button



## Key Frontend Design Elements

This section will outline the key elements within this application giving descriptions on the purpose of each element.


#### Lottie Player Animations

Lottie provides lightweight animation hosting which provides significantly smaller footprint than conventional animations.

## Django App Structure

This section of the documentation will outline the function behind each self-contained Django application.

##### Farm2Table App

This app is responsible for the Django configuration of the entire project as well as organising the URL paths for each sub-application.

##### Profile App

This application controls information in relation to the UserProfile model such as contact details & their order history. It also contains authentication features such as login & signup.

##### Store App

Once a UserProfile is created, the application user can establish a sales organisation and connect it to their UserProfile. Once on the store page, store owners can edit their store's contact details. This is also where the County model resides.

##### Products App

This Django application gives the ability to store owners so that they can create, edit & delete products. Each product is connected to a Category model in order to enable product filtering.

##### Wishlist App

This app keeps track of a list of products favourited by the user. Favourited items can be removed at any time.

##### Bag App

The bag application hosts the shopping cart, allowing the user to gather products before proceeding to the checkout. The size & quantity of each item within the bag can be updated.

##### Checkout App

In the checkout, the user submits their shipping details and card information. Here is where the order is processed and where the Stripe payment is established.

## User Interaction

### Implementation

This section will outline the technologies & processes used in the design & implementation of this application.

### Materialize Framework

For this project, the frontend framework I decided to use was Materialize. In my previous 2 milestone projects, I chose Bootstrap for the frontend, but I can now safely say that I much prefer the look of Materialize.
As it is based on the principles of material design, all elements just seem that little sharper and current.

### Error Handling

#### Django Messages

This section outlined the technology used to pass the user information without refreshing the page. These notifications appear when:

* Adding/Removing/Adjusting products to/from the bag
* Adding/Removing products to/from the user's watch list
* Adding/Updating/Removing a product to/from the store
* A user updates their profile
* A store owner updates their store profile


##### Custom Django Message Tags

Django messages allows developers to create custom message tags to allow for more granular UX notifications. As you can see from the image below, two new message tags have been created for this project. 

* Checkout[50] - In charge of displaying the shopping cart modal to the user whenever they add an item to the cart
* Wishlist[60] - Allow for a custom modal when the adds/removes items from their wish list.


#### Other Low Level Exceptions

Other low level exceptions such as client-side errors (4xx) or server-side errors (5xx) will also be handled, describing to the user which error occurred. The user will also have an option to either return to their homepage or the login page depending on their credentials. 

#### CRUD Operations

One of the main goals of this milestone project was to integrate a database within our application and use it to its full potential. CRUD in computer programming is an acronym which stands for create, read, update & delete. This covers the 4 main operations of a database. Within this section I will go over how I implemented each of these operations.

## Performance

#### Lottie Player Animations

By using the Lottie animation player, we can bring beautiful animations into our application without having to worry about file size and hence performance. I have used a single hosted Lottie animation on the error.html page.


###### Autoprefixing

The CSS style rules have been [Autoprefixed](https://autoprefixer.github.io/) to maintain uniformity of style rules across all browsers.


## Testing

### Security features

#### Decorator Functions

##### loginrequired()

This decorator function was supplied by the Django auth package. This decorator is attached to specific views where it essential to be authenicated.

##### storerequired()

This is a custom decorator that check whether the user has created a sales organisation. On pages where is would be insecure to allow access to unauthenticated users or authenticaed users without a Store.

##### Custom Django Security

When writing a view in Django which has CRUD functionality it is essential to ensure that only the data's owner & admin have the access to do so. 

### User Testing

As the application began to take shape with all major components in place, the user testing could commence. This was done by reviewing each component line by line to ensure that the code works as intended. If an edit was to be made, the developer made sure to the changes were reflected correctly on the frontend.

### Manual Testing

| Test Description | Expectation | Outcome | Result |
|---|---|---|---|
| Hero Logo | The logo link should take you back to the home page. | When the user clicks the logo, they should be redirected to the home page. | pass |
| Navigation Links | All links should direct the user as outlined. | The user should be redirected to the URL outlined by the button description. | pass |
| County Search | Should return all stores within the county selected | User see filtered results for their selected county | pass |
| Local Producers | Displays stores that are within the user's county.  If a county hasn't been set, the user will be asked to update their profile | Users should see store within their county. If their county isn't set, they should be redirect to their profile. | pass |
| All Stores | Displays all stores to the user | All stores should be displayed. | pass |
| Register | Potential users should be able to create an account using a username, email & password | Users are registered after providing the details requested. | pass |
| Register | Users shouldn't be able to create an account with an email that has already been registered | User receives error if they use a pre-registered email | pass |
| Register | All links should work as intended | The user is taken to the intended path | pass |
| Register | Once an account has been created, users are taken to their profile | Users are directed to their profile after registration | pass |
| Login | Users should be able to access their profile by logging in with their pre-registered credentials. | Users can log into their profile if the correct credentials are provided. | pass |
| Login | Users shouldn't be able to log into an account with the incorrect password | User gets a form error if the incorrect password is provided | pass |
| Logout | Logged in users can sign out of their account. | Active users can log out successfully. | pass |
| Profile | All links should work as intended.  | Clicking links redirects the user as described. | pass |
| Edit Profile | Users are able to edit their profile details using the form provided with the correct form validation being applied. | The profile edit form allows users to edit  their profile details with the correct validation being applied. | pass |
| Create Store | Users with a profile should be able to create a  sales organisation. | A store is created which is linked to the user's profile. | pass |
| Create Store | User shouldn't be able to create a store if the form validation hasn't been passed | The form reloads to show the form validation error to the user | pass |
| Edit Store | Store owners can edit their contact details,  IBAN & organic status with the correct form  validation being applied. | The store profile can be edited by it's owner using the store edit form with the correct validation being applied. | pass |
| Create Product | Store owners should have the ability to create products within  their organisation and attach a product image. | Store owners can create products under their sales organisation. | pass |
| Edit Product | Product creators can update details and image on products which they have created. | Store owners can edit products they have created. | pass |
| Delete Product | Product creators should only be able to delete their own products. | Store owners can delete products they have created. | pass |
| Add to Wishlist | Users with an account can add products to their  personalised wishlist. | Users with a profile can add products to a wishlist. | pass |
| Remove From Wishlist | Profile users should be able to delete items  from their own wishlist. | Users with a profile can remove items from their wishlist. | pass |
| Add to Bag | Users can add items to their shopping bag | Items of varying sizes and quantities can be added to the users shopping bag. | pass |
| Bag Nav Link | This link should take the user to their shopping bag | User is directed to their shopping bag | pass |
| Adjust Product Size | If the product has size, the user should have the ability to select one using the dropdown provided | The user can change the size of the required product. | pass |
| Adjust Product Quantity | The user can select how many of each specific item they want. | The quantity of an item can be changed before checkout. | pass |
| Remove from Bag | Users can remove items from their shopping bag | Items existing in the shopping bag can be removed. |  |
| Checkout Success | Supplies the customer with necessary order information | The information in relation to the order matches what was provided | pass |
| Place Order | After entering their shipping details and card information, user should be able to place their order & pay using their card. | The order has been placed if all provided details are valid. | pass |
| Stripe | After an order has been placed, the payment should be confirmed. | A payment is processed whenever an order is placed. | pass |


### Testing Screenshots

#### All Stores

![All Stores](readme-files/testing-screenshots/allStores.JPG)

#### County Search

![County Search](readme-files/testing-screenshots/countySearch.JPG)

#### Email Already Registered

![Email Already Registered](readme-files/testing-screenshots/emailAlreadyRegistered.JPG)

#### Local Store Page with Location Set

![#### Local Store Page with Location Set](readme-files/testing-screenshots/localCountySet.JPG)

#### Local Store Page with Location Not Set

![Local Store Page with Location Not Set](readme-files/testing-screenshots/localNoCountySet.JPG)

#### Valid Password

![Valid Password](readme-files/testing-screenshots/validPassword.JPG)

#### Valid User

![Valid User](readme-files/testing-screenshots/validUser.JPG)

#### Order Confirmed

![Order Confirmed](readme-files/testing-screenshots/orderConfirmed.JPG)

#### Order Appears On Profile

![Order Appears On Profile](readme-files/testing-screenshots/orderAppearsOnProfile.JPG)

## Bugs Discovered

### Unsolved Bugs

##### Frontend Framework Unsupported by Crispy Forms

Unfortunately due to the lack of Materialize support for Crispy Forms, the placeholder fields for the Materialize dropdowns within forms could not be removed.

### Solved Bugs

There were a few bugs during development but they were mainly due to a lack of Django understanding.

##### CSS Grid Leaving Gaps

This specific bug I believe was caused due to the use of Materialize within the project. By surrounding the entire product card in an anchor tag, it caused Materialize to put the anchor tag in the 1st slot & the product card in the 2nd slot. Once the anchor tag was placed within the outer product-card div, the bug resolved itself.

## Deployment

### Github Pages Deployment Procedure

This project was developed using Gitpod, committed to git and pushed to Github using the built-in function with Gitpod.

To deploy this page from Github pages from its Github repository, the following steps were taken.

1. Log into Github.
2. From the list of repositories on the screen, select saoirse-defi/milestone1-bad-arts-1.0.
3. From the menu items near the top of the page, select Settings.
4. Scroll down to the Github Pages section.
5. Under source click the drop-down menu labelled None and select Master Branch.
6. On selecting Master Branch, the page is automatically refreshed, the website is now deployed.
   
At the moment of submitting this milestone project, the default branch is version1.2 which is the latest version.


#### How to run this project locally:

To clone this project into Gitpod you will need:
1. A Github account
2. Use the Chrome browser

Then follow these steps:
1. Install the Gitpod browser extensions for Chrome
2. After installation, restart the browser
3. Log into Gitpod with your Gitpod account
4. Navigate to the Github project repository
5. Click the green 'Gitpod' button in the top right corner of the repository
6. This will trigger a new Gitpod workspace to be created from the code in Github where you can work locally


To work on the code within a local IDE such as VScode:
1. Follow this link to the Github repository
2. Under the repository name, click 'clone' or 'download'
3. In the clone with the https section, copy the clone URL for the repository
4. In your local IDE, open the terminal
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type 'git clone', and then paste the URL copied in step 3

git clone https://www.Github.com/USERNAME/REPOSITORY

7. Press enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository can be found here [Github](https://docs.Github.com/en/free-pro-team@latest/Github/creating-cloning-and-archiving-repositories/cloning-a-repository).


### Django Deployment Procedure

#### Requirements.txt

This file is responsible for keeping track of the required Django packages needed to run our application successfully. Once a new package has been installed, update the file by typing

```
    pip freeze > requirements.txt
```

#### Procfile

Heroku apps use a Procfile in order to specify the commands which have to be executed upon each startup. This has no file extension and is stored in your application's root directory.

#### WSGI

The web service gateway interface is a standard that allows the web server to be interoperable with our Django application. During the implementation, I stuck with Gunicorn as it was familiar from the last milestone project.

#### Static Files

The static files for this application are being hosted via an Amazon S3 bucket for which I have outlined the deployment below.

#### Environment Variables

There variables are stored in such a way that they cannot be accessed by reading through the code. They are stored either within the Gitpod or Heroku settings tab behind password authentication. Variables of this nature would include Secret Keys & the Heroku database URL.

#### Settings.py

This file contains all the information in order to configure your Django application. I have created a variable called OS_ENVIRON_NAME which denotes for which environment to use. This allows me as a developer to customise the settings.py file depending on the circumstances as you can see in the example below.

```
    if os.environ.get('OS_ENVIRON_NAME') == 'gitpod':
        DEBUG = True
        ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    else:
        DEBUG = os.environ.get('DEBUG')
        ALLOWED_HOSTS = ['thevegtable.herokuapp.com']
```

##### Base Dir

Whatever file paths we created in future all inherit from Base Dir. Initiate Base Dir with the following command.

```
    BASE_DIR = Path(__file__).resolve().parent.parent
```

##### Debug

When this variable is set to it's True default setting, the developer will get a lot more feedback when an error occurs within the application. It is essential to note that this setting should only be True in the development phase, you do not want your end user to see the Django development error page but the custom error page you have created.

##### Allowed Hosts

This array refers to the list of domains that are allowed run your Django application. In order for Heroku to be able to run your app, it needs to be set to the following:

```
    ALLOWED_HOSTS = ['appname.herokuapp.com']
```

##### Installed Apps

Here is where we outlined all the apps used within our project.

##### Databases

Depending on the environment selected, the Django application will either choose SQLite (local) or Postgres (Heroku).

```
    if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

### Heroku Deployment Procedure

1. Create an account on Heroku and sign in
2. Click the 'new' button at the top right of the dashboard and select 'create new app'
3. Select your payment plan, region and dyno tier
4. Click 'Create App'
5. You can now add your config variables in the 'settings' tab of your dashboard
6. On your IDE terminal, download the Heroku CLI and type

```
    heroku stack:set container -a <app name>
```

7. Once git is connected through the Heroku CLI, a new build will be deployed each time new code is committed

```
    git push heroku main
```

#### AWS S3 Bucket

1. Create an account with AWS [here](https://www.aws.amazon.com)
2. Navigate to the S3 bucket console using the search bar
3. Create an S3 bucket using thoughtful naming conventions
4. Navigate to the IAM (Identity & Access Management) console in order to create a user group
5. Create a user policy for this group outlining the permission allowed
6. Create and attach a user to this user group
7. Design a bucket policy containing the access required and attach it to the bucket
8. In 'My Security Credentials' you will find the AWS access keys & secrets
9. Add AWS access key and secret to Heroku config variables


## Credit

[Settings.py](https://www.geeksforgeeks.org/django-settings-file-step-by-step-explanation/)

[1st Django App](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)

[WSGI](https://medium.com/analytics-vidhya/what-is-wsgi-web-server-gateway-interface-ed2d290449e)

[Heroku Documentation](https://devcenter.heroku.com/articles/)

[Postgres Backend Article](https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43)

[Materialize Framework Documentation](https://materializecss.com/)

[HTML Element fade-out](https://stackoverflow.com/questions/1911290/make-div-text-disappear-after-5-seconds-using-jquery#1911308)

[Jinja Documentation](https://jinja.palletsprojects.com/en/3.0.x/)

[Python Docstrings](https://www.geeksforgeeks.org/python-docstrings/)

[Pylint Error Help](https://learn.adafruit.com/improve-your-code-with-pylint/pylint-errors)

[Heroku Documentation](https://devcenter.heroku.com/categories/python-support)

[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet)

## Database Schema

![DB Schema](readme-files/schema/thevegtable-db.png)

## Wireframes

### Desktop Wireframes

![Index](/readme-files/wireframes/index.html.png)
![Login](readme-files/wireframes/Login.png)
![Product Detail](readme-files/wireframes/Product-Detail.png)
![Profile](readme-files/wireframes/profile.png)
![Signup](readme-files/wireframes/Signup.png)
![Store](readme-files/wireframes/Store.png)

### Mobile Wireframes

![Mobile Index](readme-files/wireframes/Mobile-Homepage.png)
![Mobile Product Detail](readme-files/wireframes/Mobile-Product-Detail.png)
![Mobile Profile](readme-files/wireframes/Mobile-Profile.png)
![Mobile Store](readme-files/wireframes/Store.png)
![Mobile Wishlist](readme-files/wireframes/Mobile-Wishlist.png)



