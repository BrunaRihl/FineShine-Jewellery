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
