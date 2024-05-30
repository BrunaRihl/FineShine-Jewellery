# FineShine Jewellery

FineShine is an online platform specializing in the sale of unique and elegant jewelry, featuring a wide collection of earrings, necklaces, bracelets, rings, and sets. All pieces are crafted in Ireland and available for shipping. This project was developed as my fifth endeavor in the Code Institute's Full Stack Developer Course, utilizing Django, HTML, CSS, JS, and Python for its creation.

![FineShine website shown on a range of devices](/static/images/docs/responsive.png)  

If you'd like to make a test purchase, feel free to use the following Stripe test card details:

Success Card Number: 4242 4242 4242 4242
Expiration Date: Any future date in the format MM/YY
CVN: Any 3-digit number
Postal Code: Any 5-digit combination

## Demo
The live demo is available [here](https://fineshine-jewellery-07c9a5f5519c.herokuapp.com/)!

## Contents

* [User Experience](#user-experience)
  * [Website Overview](#website-overview)
  * [User base](#user-base)
  * [Website Goals](#website-goals)
  * [Flowchart](#flowchart)
  * [ERD](#erd)

* [User Stories](#user-stories)
  * [Epics and User Stories](#epics-and-user-stories)
  * [Agile development](#agile-development)

* [Design](#design)
  * [Color Palette](#color-palette)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
    
* [Features](#features)
  * [General Features on Page](#features)
  * [Features and resources to be added in the future](#features-and-resources-to-be-added-in-the-future)
  * [Accessibility](#accessibility)

* [Testing](#testing)
  * [User Story Test](#user-story-test)
  * [Tested Browsers and Devices](#tested-browsers-and-devices)
  * [Manual Testing](#manual-testing)
  * [Validator Testing](#validator-testing)
  * [Bugs](#bugs)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment](#deployment)

* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)


## User Experience

### Website overview 

FineShine is a fictional platform I created to offer an online shopping experience for exclusive and elegant jewelry. It was developed with the intention of providing an engaging and informative experience for users interested in acquiring high-quality and stylish jewelry pieces. Every aspect of the site, from design to content, has been planned to ensure easy and intuitive navigation.

### User base

FineShine caters to individuals interested in acquiring exclusive and elegant jewelry pieces, seeking to enhance their personal style and adorn themselves with distinction. Our user base consists of those who value high-quality craftsmanship, appreciate unique designs, and seek exceptional beauty in their jewelry choices. Whether for special occasions or daily wear, FineShine offers a curated collection to satisfy the diverse tastes and preferences of jewelry enthusiasts.

### Website Goals  

The primary goal of the FineShine platform is to provide a seamless and enjoyable shopping experience for jewelry enthusiasts. The website aims to achieve the following objectives:


Users:

* Provide intuitive navigation to explore our wide range of jewelry offerings, including earrings, necklaces, bracelets, rings, and sets.
* Facilitate navigation and offer filtering options to find the perfect pieces based on individual preferences, such as product type, material, and price range.
* Present detailed product descriptions and high-quality images to assist in informed purchasing decisions.
* Ensure a secure and convenient checkout process, with payment options and efficient shipping services for a smooth transaction experience.

Administrators:

* Maintain an efficient and updated categorization system to organize products clearly and accessibly for users.
* Ensure the security of user data by implementing robust protection and privacy measures.
* Implement effective customer support channels to respond to inquiries, feedback, and newsletter subscriptions.
* Regularly update site content to inform users about the available products from the brand.


### Flowchart

In the planning stage, I drafted a basic structure that depicted the desired functionality and interaction for the project.

As development progressed, I identified elements that needed to be included and others that required a different order of operation. These changes were gradually incorporated into the initial outline. The outline was conceived using the Lucidchart tool.

![FineShine Flowchart](/static/images/docs/flow.png)

### ERD

In order to provide a clear visual representation of the database structure, an Entity-Relationship Diagram (ERD) was developed using a Database Designer tool.

![FineShine ERD](/static/images/docs/erd.jpg)


## User Stories

### Epics and User Stories
During the project development, the creation of epics, user stories, acceptance criteria, and tasks was crucial in guiding and successfully concluding the project. These elements provided a clear and detailed framework for planning and executing activities, ensuring alignment with the project's objectives and expectations. Among them were:

#### EPIC 1: Set Up
The 'Set up' epic encompasses the activities required to establish the initial development environment of the project, including installing tools, configuring version control systems, and organizing the project structure.

* As a developer, I can deploy a version of the application on Heroku to verify the functionality of the configuration and continue testing the application during development.

* As a developer I can establish database connectivity and media storage so that user data is successfully stored.

#### EPIC 2: Admin Dashboard

The Admin Panel epic aims to create a interface for administrators to efficiently manage various aspects of the website or application. This includes functionalities such as user management, content moderation, and configuration.

* As an admin, I can log in to the admin panel so that I can manage and oversee its operations.

* As an admin, I can introduce, edit, and delete new products, so that the catalog can be continually expanded, keeping the offerings current and relevant for our customers.


#### EPIC 3: User Authentication

The User Authentication epic deals with implementing a system for user registration, login, and logout on the website. This enables users to create accounts, log in to access exclusive features, and log out when they wish to exit.

* As a registered user, I can to be able to log in to my account so that I can access personalized features and services and save my preferences.

* As a user, I can register an account so that I can establish a profile, save my information, become a customer, and access stored data.

* As a logged-in user, I can to be able to log out of my account so that I can securely end my session on the website.

* As a logged-in user, I can update my profile so that I can keep my personal information up to date.

* As a registered user, I can securely reset my password in case I forget it, so that I can regain access to my account.

* As a registered user, I can securely save my username and password so that I can easily access the website whenever necessary.


#### EPIC 4: SEO

The 'SEO' epic aims to optimize website visibility on search engines and enhance promotion through strategies such as configuring SEO details and creating a Facebook marketing page.

* As a developer, I can set up SEO details for the website to ensure that users can effortlessly reach the content they seek.

* As a user, I can subscribe to the newsletter so that I can stay informed about the latest news and offerings.

* As a developer, I can create a Facebook marketing page to display the store, so that potential customers are directed to the website.


#### EPIC 5: Enhanced User Experience

* As a user, I can navigate the website with ease and access all content so that I can have an inclusive browsing experience and access information effectively.

* As a user, I can have an intuitive interface to easily navigate through the website/application, so that I can find what I need efficiently.

* As a user, I can have a responsive design to access the product on different devices (desktop, tablet, mobile), so that I can have a seamless experience regardless of the device I'm using.

* As a user, I can receive clear feedback about my actions to better understand what is happening, so that I can navigate and interact with the product confidently.


#### EPIC 6: Product Discovery and Features

Product Discovery and Features focuses on enhancing the user's ability to explore and interact with available products effectively.

* As a user, I can browse through different product categories intuitively to explore the available options, so that I can find products that match my preferences.

* As a user, I can search for products by keywords to quickly find what I'm looking for, so that I can save time and effort in the shopping process.

* As a user, I can sort the search results by price and other options to refine my selection, so that I can easily locate the products that meet my criteria.

* As a user, I can view a comprehensive product details page, including description, price, images, and customer reviews, so that I can make informed purchasing decisions.

* As a user, I can add products to the shopping bag directly from the product details page for a convenient shopping experience, so that I can proceed to checkout seamlessly.

* As a logged-in user, I can leave my review on products I have purchased, so that I can share my feedback with other users.

#### EPIC 7: Shopping bag and checkout

Shopping Bag and Checkout enables users to seamlessly manage their shopping experience from adding items to the bag to completing the checkout process.

* As a user, I can add products to my shopping bag to keep track of items I intend to purchase and have a preview of how my bag looks on the current page, so that I can easily manage my shopping selections.

* As a user, I can delete and adjust the quantity of items in my shopping bag before proceeding to checkout, so that I can ensure my order reflects my desired purchases accurately.

* As a user, I can view the contents of my shopping bag to review the items I've added and the total cost of the items in my shopping bag, including shipping fees, so that I can make informed decisions and proceed with checkout confidently.

* As a user, I can proceed to checkout from my shopping bag to complete my purchase, so that I can finalize my order.

* As a logged-in user, I can enter my personal and delivery details during checkout to ensure delivery of my order, so that my items are shipped to the correct address.

* As a user, I can securely enter my payment details to complete the transaction, so that my purchase is successfully processed.

* As a user, I receive a confirmation email after successfully completing the checkout process, providing details of my order, so that I have a record of my purchase.

* As a logged-in user, I can view my order history in my profile to review my past purchases, so that I can track my shopping activity and access details of previous orders.
 

#### Epic 8: Contact Management and Customer Support

Contact Management and Customer Support streamlines user interaction by offering easy access to contact options, enabling users to submit inquiries efficiently.

* As a user, I can easily locate the contact option on the website, so that I can efficiently reach out to the company for assistance or inquiries.

* As a user, I can fill out a contact form with my personal information and message to send an inquiry to the team, so that I can easily get in touch with the company and receive a confirmation upon submitting the contact form.

* As a website admin, I can check whenever a contact form is submitted, enabling me to promptly respond to visitor inquiries and provide efficient customer service.

#### Epic 9: Wishlist

The Epic 9 focuses on implementing Wishlist functionality, allowing customers to easily manage desired products by adding, removing, and viewing items to facilitate future purchases.

* As a logged-in user, I can add and remove products to my wishlist so that I can save items I wish to purchase in the future.

* As a logged-in user, I can view all the products I've added to my wishlist so that I can review my choices and make informed purchasing decisions.

#### Epic 10: Posts

The Epic 10 focuses on post management, allowing users to access and interact with updated content on topics such as fashion trends and jewelry.

* As a user, I can access a "Posts" section to read about the latest trends, style tips, and information about the materials used in jewelry, so that I stay updated and inspired.

* As a site administrator, I can manage articles directly from the frontend, including deleting, editing, and creating them using a form, so that I have full control over the content displayed on the site and can share relevant and timely information with users.

#### Epic 11: Project Documentation and Testing

This epic focuses on both comprehensive testing procedures and creating detailed project documentation. The goal is to ensure high-quality software and easy access to project details for understanding.

* As a developer, I can thoroughly test the project so that I can ensure its quality and usability.

* As a developer, I can create a README.md file to document and present the project, ensuring that everyone can easily understand the purpose, functionality, and usage of the project.

### Agile development

Throughout the project development, I adopted an agile methodology, utilizing Kanban to manage my activities and projects. Kanban provided a clear view of the workflow, allowing me to track task progress visually and in real time. I organized my project on GitHub, using a Kanban board to divide tasks into columns such as "To Do," "In Progress," and "Done."

![FineShine Agile development](/static/images/docs/agile.png)


For more details on the project management process, you can access the link [here](https://github.com/users/BrunaRihl/projects/8).

#### User Story Prioritization

In my agile project, I prioritize user stories to ensure that I focus on delivering the most critical features first. I categorize my user stories into four main groups:

* Must Have: These are essential for the project's success. Without these features, the project cannot be considered complete. They represent the core functionalities that need to be delivered in the first release.

* Should Have: These are important but not critical. While the project can be launched without these features, they are high-priority items that add significant value and should be included if possible.

* Could Have: These are desirable features that enhance the user experience but are not essential. They are lower in priority and can be included if time and resources allow.

* Won't Have: These features will not be included in the current iteration or release. They may be considered for future development but are not a focus for the current project timeline.

#### Distribution of User Stories

I have a total of 40 user stories for this project. Here is how I have distributed them across the four categories:

* Must Have: 26 user stories (65%)
* Should Have: 8 user stories (20%)
* Could Have: 4 user stories (10%)
* Won't Have: 2 user stories (5%)

For more details on the categorization, distribution of user stories, and project prioritization, you can access the link [here](https://github.com/BrunaRihl/FineShine-Jewellery/issues).

## Design

### Color palette

The website's color palette was inspired by the hero image on the homepage, featuring shades of aqua green, gold, black, and white. This choice not only reflects the sophistication of the jewelry but also creates an atmosphere of freshness and elegance for users. Additionally, the sharp contrast between black and white was carefully considered to ensure excellent readability and ease of navigation for visitors.

![FineShine website color palette](/static/images/docs/palette.png)

### Typography 

Google Fonts were used to incorporate the selected font styles into the website. 

I chose 'Raleway' for the body text due to its modern and elegant appearance, characterized by clean lines and versatility, making it suitable for a wide range of content types. This contributes to a cohesive and polished design aesthetic. Its legibility ensures a comfortable reading experience for users, while its balanced proportions and distinct letterforms add a touch of sophistication to the site, enhancing the overall user experience and reinforcing its brand identity.

![FineShine fonts](/static/media/docs/fonts.jpg)  

### Imagery 

The images selected for the website were carefully chosen to showcase the variety of products available, including earrings, rings, necklaces, bracelets, and sets. High-resolution images that present the products clearly and attractively were prioritized. Each image was chosen to complement the overall design of the site, ensuring a visually cohesive experience for users. The goal was to provide an engaging and inspiring experience, inviting visitors to explore the diversity of products available in the e-commerce catalog.

### Wireframes

I developed a simple wireframe, aiming to ensure a consistent experience across mobile devices and computers.

I made some adjustments in relation to what I had planned for positioning and added some buttons to enhance functionality and user experience, aiming to ensure the website is accessible and enjoyable on any platform.

#### Desktop
<details>
  <summary>Home
</summary>

![FineShine wireframe](/static/images/docs/home-desk.webp)  

</details>
<details>
  <summary>Products
</summary>

![FineShine wireframe](/static/images/docs/products-desk.webp)  

</details>
<details>
  <summary>Products Details
</summary>

![FineShine wireframe](/static/images/docs/details-desk.webp)  

</details>

</details>
<details>
  <summary>Wishlist
</summary>

![FineShine wireframe](/static/images/docs/wish-desk.webp)  

</details>
<details>
  <summary>Contact
</summary>

![FineShine wireframe](/static/images/docs/contact-desk.webp)  

</details>


#### Mobile
<details>
  <summary>Home
</summary>

![FineShine wireframe](/static/images/docs/home-mob.webp)  

</details>
<details>
  <summary>Products
</summary>

![FineShine wireframe](/static/images/docs/products-mob.webp)  

</details>
<details>
  <summary>Products Details
</summary>

![FineShine wireframe](/static/images/docs/details-mob.webp)  

</details>

</details>
<details>
  <summary>Wishlist
</summary>

![FineShine wireframe](/static/images/docs/wish-mob.webp)  

</details>
<details>
  <summary>Contact
</summary>

![FineShine wireframe](/static/images/docs/contact-mob.webp)  

</details>
</details>







## Technologies Used
### Languages

* Python 3, Html, Css, JavaScript.

### Frameworks, Libraries & Programs

Visual Studio Code (VS Code): Utilized as a source code editor.

[Django](https://www.djangoproject.com/): Used as a web framework for building the application.

[Bootstrap](https://getbootstrap.com/): Utilized for responsive and mobile-first front-end web development.

[ElephantSQL](https://www.elephantsql.com/): Utilized for managing PostgreSQL databases in the cloud.

[Google Fonts](https://fonts.google.com/): Imported to integrate font styles into the website. 

[Font Awesome](https://fontawesome.com/): Incorporated to easily add icons across the website.

[Lucidchart](https://lucid.app/): employed in the planning phase for crafting flowcharts

[Heroku Platform](https://dashboard.heroku.com/apps): for deploying the application in a live environment.

[Stripe](https://stripe.com/): Integrated for handling payment processing within the Django application.

[AWS](https://aws.amazon.com/):Utilized for cloud computing services, such as hosting and managing the application's database and storage.

Google Dev Tools: Leveraged for debugging and testing features, as well as resolving issues related to responsiveness and styling. 

[Pep8 online](https://pep8ci.herokuapp.com/): Used to identify issues in my Python code.

[The W3C Markup Validation Service](https://validator.w3.org/): Used to validate the accuracy and validity of HTML code.

[The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/): Employed to validate the correctness and compliance of CSS code.

[GitHub](https://github.com/): Used to save and store the website files.


#### Python Libraries and Modules

* **os:** Used for interacting with the operating system, including file system operations and environment variables.

* **sys:** Provides access to interpreter variables and functions for interacting with the Python interpreter.

* **pathlib:** Allows for easy and platform-independent manipulation of file paths, representing files and directories in the file system.

* **uuid**: Generates and manages universally unique identifiers (UUIDs) in Python.

* **stripe**: used for integrating Stripe payment processing into Django applications.

* **time**: used for handling time-related functionalities such as pausing program execution, calculating the duration of operations / scheduling actions to occur at specific times.

* **datetime**: Used for date and time manipulation.

## Deployment

<details>
  <summary> Deploying Your Project on Heroku</summary>

* To get your project up and running on Heroku, follow these steps:

1. **Create a List of Dependencies:**
   - In the terminal, run the command `pip3 freeze > requirements.txt` to generate a list of dependencies needed for Heroku deployment.

2. **Heroku Account Setup:**
   - Log in to your Heroku account or create a new one if needed.

3. **Create a New App:**
   - Click on "New" in the top-right corner of your Heroku Dashboard, and select "Create new app" from the dropdown menu.
   - Enter a unique app name and choose a region (EU or USA) closest to you.
   - Click on "Create App".

4. **Config Var**:
   - In your new app’s settings tab, ensure the Config Var DISABLE_COLLECTSTATIC key has a value of 1.

5. **Update Your Code for Deployment**:
   - Use pip3 to install gunicorn and freeze it to the requirements.txt file.
   - In the Procfile, add a command using gunicorn and your project wsgi file to start the webserver.
     ```bash
     web: gunicorn <your project>.wsgi
     ```
   - In thensettings.py file, set the DEBUG constant to False and append the '.herokuapp.com' hostname to the ALLOWED_HOSTS list.
     ```python
     DEBUG = False
     ALLOWED_HOSTS = ['.herokuapp.com']
     ```

6. **Connect to GitHub:**
   - Go to the "Deploy" tab and select "GitHub" as the deployment method.
   - Click "Connect to GitHub" and search for your repository name.
   - Click "Connect" to link the repository to Heroku.
  - In your new app’s resources tab delete any Postgres database Add-on.

7. **Deploy the App:**
   - Scroll down to "Manual deploy" and click "Deploy Branch". This allows you to view the build logs as the app is being constructed.
   - After the initial deployment, you can enable "Enable Automatic Deploys" to keep the app up-to-date with your GitHub repository.

8. **Finalize Deployment:**
   - Wait for the app to build. Once ready, you will see the "App was successfully deployed" message and a 'View' button to take you to your deployed link.


You can access the live project by clicking [here](https://starlight-consultations-2b1105ac431c.herokuapp.com/).

</details>

<details>
  <summary>Setting up ElephantSQL PostgreSQL Database
</summary>

Steps to create an instance of a cloud-based PostgreSQL database using ElephantSQL and connect it to our Django project.

**Steps**

1. **Create PostgreSQL Instance:**
   - Log into your ElephantSQL dashboard.
   - Click on "Create New Instance".
   - Set up your plan
   - Select a data center near you.
   - Click "Review".
   - Verify your details and click "Create instance".

2. **Copy Database URL:**
   - Click on "DETAILS" and copy the URL.

   
3. **Create `env.py` File:**
   - Create a file named `env.py` at the top level of your project.
   - Add the following code to `env.py`, replacing `<your-database-URL>` with the URL copied from ElephantSQL:
     ```python
     import os

     os.environ.setdefault(
         "DATABASE_URL", "<your-database-URL>"
     )
     ```

4. **Update `.gitignore` File:**
   - Open `.gitignore` file and add `env.py` to prevent secret data from being pushed to GitHub.

5. **Install Database Packages:**
   - Install the required packages to connect to your PostgreSQL database:

6. **Update `settings.py`:**
   - Import required packages in `settings.py`:
     ```python
     import os
     import dj_database_url

     if os.path.isfile('env.py'):
         import env
     ```
   - Connect to the environment variable `DATABASE_URL`:
     ```python
     DATABASES = {
         'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
     }
     ```

7. **Migrate Database Tables:**
   - Run migrations to create database tables

8. **Create Superuser:**
    - Create a superuser for admin access to the database:
      ```bash
      python manage.py createsuperuser
      ```
    - Follow the prompts to choose a username, email, and password.

9. **Deploy the Project:**
    - Change DEBUG value to False in `settings.py`.
    - Push your updated code to GitHub.
    - Go to the Heroku dashboard and deploy your project.

10. **Connect Heroku to PostgreSQL Database:**
    - Go to the Heroku app's Settings tab and click "Reveal Config Vars".
    - Add a new config var with a key of `DATABASE_URL` and the value of the ElephantSQL URL.

</details>

<details>
  <summary>Setting up Amazon AWS</summary>

To store media and static files online, this project leverages AWS, a cloud computing platform. Since Heroku does not retain this type of data, AWS provides a reliable solution.

Here's a step-by-step guide to connect your project to AWS:

## S3 Bucket

**Steps:**

1. Search for S3.
2. Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
3. Uncheck "Block all public access" and confirm that the bucket will be public (required for it to work on Heroku).
4. From Properties, enable static website hosting, and enter index.html and error.html in their respective fields, then click Save.
5. In the Permissions tab, paste the following CORS configuration:

```json
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
6. Copy your ARN.
7. In the Bucket Policy tab, select the Policy Generator link, and use the following steps:
* Policy Type: S3 Bucket Policy
* Effect: Allow
* Principal: *
* Actions: GetObject
* Amazon Resource Name (ARN): paste-your-ARN-here
* Click Add Statement
* Click Generate Policy
8. Copy the entire Policy and paste it into the * Bucket Policy Editor:
```json
{
    "Id": "Policy1234567890",
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1234567890",
            "Action": [
                "s3:GetObject"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::your-bucket-name/*",
            "Principal": "*"
        }
    ]
}

```

9. Before clicking "Save", add "/*" to the end of the Resource key in the Bucket Policy Editor (like above).
10. Click Save.
11. In the Access Control List (ACL) section, click "Edit" and enable List for Everyone (public access), and accept the warning box.
12. If the edit button is disabled, you need to change the Object Ownership section above to ACLs enabled (mentioned above).

### AWS - IAM Setup

To set up IAM (Identity and Access Management) in AWS, follow these simplified steps:

Steps:

1. Create a New Group: Navigate to the AWS Services Menu and create a new group, giving it a name relevant to your project, like 'group-project-name'.

2. Assign Policies to the Group: Once the group is created, navigate to the Review Policy page. Under User Groups, select the newly named group. Then, move to the Permissions tab, click on Add Permissions, and select the policies you want to attach. Click on the Add Permissions button at the bottom to finish.

3. Import Managed Policy: From the JSON tab, click on the Import Managed Policy link. Search for 'S3' and select the 'AmazonS3FullAccess' policy. Import it into your policy.
* Copy ARN from S3 Bucket
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::bucket-name",
        "arn:aws:s3:::bucket-name/*"
      ]
    }
  ]
}

```

4. Review and Create Policy: Review the policy settings, give it a name (e.g., 'policy-everneed'), enter a description, and create the policy.

5. Attach Policy to User Groups: Search for the newly created policy and attach it to the desired user groups.

6. Create a New User: Under User Groups, add a new user, providing a name like 'user-everneed'. For Select AWS Access Type, choose Programmatic Access. Add the group 'user-everneed' to this user.

7. Review and Create User: Review the user settings and create the user.

8. Download Access Credentials: After creating the user, find the Download.csv button to download the user's access credentials immediately. Save a copy of this file. It contains the user's Access Key ID and Secret Access Key, which you'll need for authentication.
* AWS_ACCESS_KEY_ID = Access key ID
* AWS_SECRET_ACCESS_KEY = Secret access key

### Final AWS Setup

1. If the Heroku Config Vars still includes DISABLE_COLLECTSTATIC, it can now be removed. This allows AWS to manage the static files.

2. In the S3 dashboard, create a new folder named "media".

3. Choose the media images you want to upload into this new folder.

4. Grant public read access to these objects by selecting "Manage Public Permissions".

5. Click "Upload" to complete the process. There are no further settings required.

</details>

</details>
<details>
  <summary>Stripe API</summary>
Stripe Integration: This project uses Stripe to manage ecommerce payments. Follow these steps to integrate Stripe with your project:


**Steps:**

1. Go to your Stripe dashboard and locate "Get your test API keys". You'll find two keys:
* STRIPE_PUBLIC_KEY: Publishable Key (starts with pk)
* STRIPE_SECRET_KEY: Secret Key (starts with sk)
2. Additionally, for backup purposes, set up Stripe Webhooks:
* Navigate to Developers > Webhooks in your Stripe dashboard.
Add an endpoint using the URL: https://your-website/checkout/wh/.
3. Select "receive all events".
4. Click "Add Endpoint" to complete the process.
5. After setting up Webhooks, you'll receive a new key:
* STRIPE_WH_SECRET: Signing Secret (Webhook) Key (starts with wh)

</details>


<details>
  <summary>Gmail API</summary>
Gmail Integration: This project uses Gmail to send emails for account verification and purchase order confirmations. 

**Steps:**

1. Click on the Account Settings (cog icon) in the top-right corner of Gmail and go to the Accounts and Import tab.
2. Under "Change account settings", select Other Google Account settings.
Choose Security from the left sidebar and turn on 2-Step Verification (verify your password and account).
3. After verification, enable 2FA.
4. Return to the Security page and find App passwords. Confirm your password and account again if prompted.
5. Select Mail for the app type and choose Other (Custom name) for the device type.
6. Use any custom name (e.g., "Django").
7. You'll receive a 16-character password (API key). Save this securely, as it can't be accessed later!
* EMAIL_HOST_PASS: User's 16-character API key
* EMAIL_HOST_USER: User's personal Gmail email address

</details>

<details>
  <summary>Forking the Repository</summary>
Forking the repository allows you to create a copy of the original repository in your GitHub profile. This enables you to view and edit the code without affecting the original repository.

**Steps:**

1. In the "starlight-consultations" repository, click on "Fork" in the top right corner.
2. Confirm the creation of the fork.

</details>

<details>
  <summary>Cloning the Repository</summary>
Cloning a repository means obtaining a local copy to work on in your own development environment.

**Steps:**

1. In the repository, click on "Code" above the file list.
2. Copy the URL.
3. Open Git Bash.
4. Navigate to the directory where you want to clone the repository.
5. Type `git clone` followed by the URL and press "enter".









