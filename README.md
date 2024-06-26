# FineShine Jewellery

FineShine is an online platform specializing in the sale of unique and elegant jewellery, featuring a wide collection of earrings, necklaces, bracelets, rings, and sets. All pieces are crafted in Ireland and available for shipping. This project was developed as my fifth project in the Code Institute's Full Stack Developer Course, using Django, HTML, CSS, JS, and Python for its creation.

![FineShine website shown on a range of devices](/media/docs/responsive.jpg)  

## Demo
The live demo is available [here](https://fineshine-jewellery-07c9a5f5519c.herokuapp.com/)!

## Contents

* [User Experience](#user-experience)
  * [Website Overview](#website-overview)
  * [User base](#user-base)
  * [Website Goals](#website-goals)
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
  * [Future Features](#future-features)

* [Marketing and SEO](#marketing-and-seo)
  * [Business Model - Ecommerce](#business-model---ecommerce)
  * [Marketing](#marketing)
  * [Search Engine Optimization](#search-engine-optimization)

* [Testing](#testing)
  * [Bugs](#bugs)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used)

* [Deployment](#deployment)

* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)


## User Experience

### Website overview 

FineShine is a fictional platform I created to offer an online shopping experience for exclusive and elegant jewellery. It was developed with the intention of providing an engaging and informative experience for users interested in acquiring high-quality and stylish jewellery pieces. Every aspect of the website, from design to content, has been planned to ensure easy and intuitive navigation.

### User base

FineShine caters to individuals interested in acquiring exclusive and elegant jewellery pieces, seeking to enhance their personal style and adorn themselves with distinction. Our user base consists of those who value high-quality craftsmanship, appreciate unique designs, and seek exceptional beauty in their jewellery choices. Whether for special occasions or daily wear, FineShine offers a curated collection to satisfy the diverse tastes and preferences of jewellery enthusiasts.

### Website Goals  

The primary goal of the FineShine platform is to provide a seamless and enjoyable shopping experience for jewellery enthusiasts. The website aims to achieve the following objectives:


**Users:**

- Provide intuitive navigation to explore the wide range of jewellery offerings, including earrings, necklaces, bracelets, rings, and sets.
- Facilitate navigation and offer filtering options to find the perfect pieces based on individual preferences.
- Present detailed product descriptions and high-quality images to assist in informed purchasing decisions.
- Ensure a secure and convenient checkout process, with payment options and efficient shipping services for a smooth transaction experience.
- Offer an engaging and responsive user experience on all devices, from desktops to mobile devices.
- Provide clear and accessible contact channels for users to ask questions or get additional support.

**Administrators:**

- Maintain an efficient and updated categorization system to organize products clearly and accessibly for users.
- Ensure the security of user data by implementing robust protection and privacy measures.
- Implement effective customer support channels to respond to questions, feedback, and newsletter subscriptions.
- Regularly update site content to inform users about the available products from the brand.
- Facilitate the user registration and login process, ensuring security and ease of use.


### ERD

In order to provide a clear visual representation of the database structure, an Entity-Relationship Diagram (ERD) was developed using a Database Designer tool.

![FineShine ERD](/media/docs/erd.jpg)  


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

The Epic 10 focuses on post management, allowing users to access and interact with updated content on topics such as fashion trends and jewellery.

* As a user, I can access a "Posts" section to read about the latest trends, style tips, and information about the materials used in jewellery, so that I stay updated and inspired.

* As a site administrator, I can manage articles directly from the frontend, including deleting, editing, and creating them using a form, so that I have full control over the content displayed on the site and can share relevant and timely information with users.

#### Epic 11: Project Documentation and Testing

This epic focuses on both comprehensive testing procedures and creating detailed project documentation. The goal is to ensure high-quality software and easy access to project details for understanding.

* As a developer, I can thoroughly test the project so that I can ensure its quality and usability.

* As a developer, I can create a README.md file to document and present the project, ensuring that everyone can easily understand the purpose, functionality, and usage of the project.

### Agile development

Throughout the project development, I adopted an agile methodology, utilizing Kanban to manage my activities and projects. Kanban provided a clear view of the workflow, allowing me to track task progress visually and in real time. I organized my project on GitHub, using a Kanban board to divide tasks into columns such as "To Do", "In Progress", "Done" and "Future Features"

![FineShine Agile development](/media/docs/project.jpg)

For more details on the project management process, you can access the link [here](https://github.com/users/BrunaRihl/projects/8).

#### User Story Prioritization

In my agile project, I prioritize user stories to ensure that I focus on delivering the most critical features first. I categorize my user stories into four main groups:

* Must Have: These are essential for the project's success. Without these features, the project cannot be considered complete. They represent the core functionalities that need to be delivered in the first release.

* Should Have: These are important but not critical. While the project can be launched without these features, they are high-priority items that add significant value and should be included if possible.

* Could Have: These are desirable features that enhance the user experience but are not essential. They are lower in priority and can be included if time and resources allow.

* Won't Have: These features will not be included in the current iteration or release. They may be considered for future development but are not a focus for the current project timeline.

#### Distribution of User Stories

I have a total of 41 user stories for this project. Here is how I have distributed them across the four categories:

* Must Have: 27 user stories (65%)
* Should Have: 8 user stories (20%)
* Could Have: 4 user stories (10%)
* Won't Have: 2 user stories (5%)

For more details on the categorization, distribution of user stories, and project prioritization, you can access the link [here](https://github.com/BrunaRihl/FineShine-Jewellery/issues).

## Design

### Color palette

The website's color palette was inspired by the hero image on the homepage, featuring shades of aqua green, gold, black, and white. This choice not only reflects the sophistication of the jewellery but also creates an atmosphere of freshness and elegance for users. Additionally, the sharp contrast between black and white was carefully considered to ensure excellent readability and ease of navigation for visitors.

![FineShine website color palette](/media/docs/palette.png)

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

![FineShine wireframe](/media/docs/home-desktop.png)

</details>
<details>
  <summary>Products
</summary>

![FineShine wireframe](/media/docs/products-desktop.png)

</details>
<details>
  <summary>Products Details
</summary>

![FineShine wireframe](/media/docs/products-d-desktop.png)

</details>

</details>
<details>
  <summary>Wishlist
</summary>

![FineShine wireframe](/media/docs/wishlist-desktop.png)

</details>
<details>
  <summary>Contact
</summary>

![FineShine wireframe](/media/docs/contact-desktop.png)

</details>


#### Mobile
<details>
  <summary>Home
</summary>

![FineShine wireframe](/media/docs/Home-mobile.png)

</details>
<details>
  <summary>Products
</summary>

![FineShine wireframe](/media/docs/products-mobile.png)

</details>
<details>
  <summary>Products Details
</summary>

![FineShine wireframe](/media/docs/products-d-mobile%20.png)

</details>

</details>
<details>
  <summary>Wishlist
</summary>

![FineShine wireframe](/media/docs/wishlist-mobile%20.png)

</details>
<details>
  <summary>Contact
</summary>

![FineShine wireframe](/media/docs/contact-mobile.png)

</details>
</details>

## Marketing and SEO
### Business Model - Ecommerce
**Fineshine** is a Business to Customer (B2C) e-commerce platform, specializing in the production and sale of high-quality jewellery to individual customers.

### Competitive Advantages:
- **Superior Quality:** Producing and offering high-quality jewellery made with precious materials and unique designs.
- **Ease of Purchase:** Providing an easy and convenient purchasing experience through the online platform.
- **Social Engagement:** Building a community of loyal customers through engagement on social media and loyalty programs.

### Customer Segments:
- **Jewellery Enthusiasts:** Individuals seeking high-quality and exclusive design jewellery.
- **Gift Buyers:** People purchasing jewellery for special occasions like birthdays and weddings.

### Key Assets:
- **Jewellery Inventory:** Diverse inventory of internally produced jewellery to meet customer demand.
- **E-commerce Platform:** Robust and user-friendly website for sales and transactions.
- **Social Media Engagement:** Active presence on social media to attract and engage customers.
- **Newsletter System:** Utilization of MailChimp for regular communications with customers.

### Channels:
- **E-commerce Website:** Primary platform for displaying products, processing orders, and facilitating transactions.
- **Social Media:** Utilization of platforms like Facebook for marketing and customer interaction.
- **Newsletter (MailChimp):** Sending updates, promotions, and regular announcements to subscribers via email.

### Customer Relationships:
- **Personalized Support:** Customer support for inquiries and issue resolution.
- **Wishlist:** Tool for customers to save favorite products for future purchases, enhancing personalized experience.
- **Product Reviews:** Option for customers to leave reviews, aiding other buyers in making informed decisions.
- **Facebook Presence:** Using Facebook to interact with customers, answer queries, and build a sense of community.

### Strategic Collaborations:
- **Material Suppliers:** Partnerships with suppliers of precious materials for jewellery production.
- **Delivery Services:** Collaboration with shipping services to ensure efficient order delivery.
- **Fashion Influencers:** Partnerships with fashion influencers to promote products and reach new audiences.
- **Designer Collaborations:** Collaborations with renowned jewellery designers for exclusive collections.

### Seasonal Marketing Campaigns:
- **Festive Promotions:** Creating special promotions for holidays like Christmas, Valentine's Day, and Black Friday.
- **Online Events:** Hosting online events such as collection launches and webinars on jewellery care.

### Competition Analysis:
- **Competitive Analysis:** Studying key competitors in the online jewellery market to identify opportunities and threats.
- **Benchmarking:** Comparing products, prices, and marketing strategies with major competitors.

### Data Analysis and Feedback:
- **Data Analysis:** Using data analytics to understand customer behavior and optimize marketing and sales strategies.
- **Feedback Collection:** Implementing systems to collect and analyze customer feedback for continuous improvement.

## Marketing

### Facebook Page
A Facebook page was created to promote the jewellery e-commerce due to the platform's wide visibility and engagement potential. Facebook allows for reaching a diverse audience, increasing brand visibility, and attracting new consumers.
To personalize the page, the store's logo was added as the profile picture, and a welcome message with a direct link to the online store was written, making it easy for visitors to access.

![FineShine Facebook](/media/docs/facebook.jpg)

Additionally, a post was created featuring an exclusive jewellery set as the highlight of the week, including a photo of the product and a link for purchase.

![FineShine facebook](/media/docs/facebook2.jpg)

This strategy aims to increase engagement, drive traffic to the website, and boost sales, strengthening the brand's presence on social media.
Click [here](https://www.facebook.com/profile.php?id=61560858680361) to visit the FineShine Facebook Business Page.

### Newsletter Signup

The website features a Mailchimp newsletter signup form, designed to collect email addresses for marketing and promotional purposes. This allows customers to stay informed about the latest products, special offers, and updates. The newsletter form is accessible and can be found below:

![FineShine newsletter](/media/docs/news.jpg)

## Search Engine Optimization
### Keyword Strategy to Increase Online Visibility

To ensure that my website was easily discoverable through online searches, I developed a keyword strategy. This strategy encompassed two main types of keywords:

- **Short-Tail Keywords (Primary Terms):** These were brief and comprehensive terms that captured the essence of my website's offerings in general.

- **Long-Tail Keywords:** These were more specific and detailed phrases that directly aligned with the products and services offered on my site.

To further enhance my keyword strategy, I turned to suggestions provided by Google during searches. I utilized features like "People also search for" and the auto-suggestions provided by Google while typing a keyword. These tools helped me identify popular search trends and related terms actively sought by users.

![FineShine keywords](/media/docs/keys1.jpg)
![FineShine keywords](/media/docs/keys2.jpg)
![FineShine keywords](/media/docs/keys3.jpg)


Additionally, I utilized resources like Wordtracker.com to conduct keyword research and identify relevant terms that aligned with the content and purpose of my site.

![FineShine wordtracker](/media/docs/keys4.jpg)

After the research, my selected keywords were:

![FineShine keywords meta](/media/docs/keywords.jpg)

Sitemap: A sitemap.xml file has been created to help search engines index the website more effectively.

Robots.txt: A robots.txt file has been implemented to guide search engine crawlers on which pages to index or avoid, ensuring efficient and controlled crawling of the site.


## Features

### Header

* All pages feature a responsive navigation bar at the top of the screen.

![FineShine navbar](/media/docs/nav.jpg)

**Logo and Company Name:** A custom logo was created for Fineshine, ensuring instant brand recognition.

![FineShine logo](/media/docs/logofs.jpg)

- **Search Bar:** A search bar allows users to easily find specific products directly from the header.

- **Quick Access Links:** Quick Access Links: On the right side of the header are quick access links, including "My Account," "Contact," and "Shopping Bag." The "Wishlist" link is visible but not clickable unless the user is logged in.

- **Main Navigation:** Below the header, the main navigation allows users to choose products by categories such as "All Products," "Earrings," "Necklaces," among others.

- **Product Categories:** When clicking on a category such as "Earrings," users have additional options such as "Silver Earrings," "Gold Earrings," or "Full Collection."

- **Highlighting Free Delivery:** A highlighted line emphasizes free delivery for purchases over €200, using a gold glitter effect to match the website theme and draw attention.


### Favicon

A custom favicon has been added to the website's header. The favicon features a diamond with sparkling accents around it, matching the site's color palette of aqua green tones, providing a unique visual identity.

![Fineshine - favicon](/media/docs/fav.jpg)

## Footer

The footer of the website is structured into three main sections. The first section features a Mailchimp newsletter signup form, which collects email addresses for marketing purposes. The second section includes store information, useful links, and contact details. The third section, "Follow Us," contains icons and links to the store's social media profiles, including Facebook, Instagram, and YouTube.

![Fineshine - favicon](/media/docs/footer.jpg)

## Home Page 

* The main image showcases golden jewellery arranged against a background of aqua green, which inspired the color palette of the site.
* The overlaid message provides a brief introduction to the website's concept, while the high resolution and vibrant colors ensure an inviting presentation to visitors.
* The "Shop Now" button below the main image provides a clear call-to-action, inviting users to explore and shop for jewellery.

![Fineshine - home](/media/docs/homepage.jpg)

### Why shop with us section:

Below the main image, users will find the "Why Shop for Jewellery with FineShine" section.

This section highlights the reasons why customers should choose FineShine for their jewellery purchases. Each reason is presented concisely, providing an overview of the benefits of shopping with FineShine.

![Fineshine - Why shop whit us](/media/docs/why-shop.jpg)

## Products:

Users can explore products by selecting different categories such as earrings, bracelets, necklaces, rings, and sets, available in silver, gold, or the complete collection. This allows for quick and easy navigation through the products of interest.
![Fineshine - products page](/media/docs/products.jpg)

When hovering over the products, a zoom effect is applied, accompanied by a subtle shadow to enhance the item preview.

Additionally, users can also sort the products by price, name, or category, offering even more control over the item view.

Each product displays a representative image, price, category, and rating (if available).

![Fineshine - products](/media/docs/products2.jpg)

### Admin Features:

Administrators have access to additional options such as adding new products or deleting existing ones.

![Fineshine - admin](/media/docs/admin1.jpg)

Admins also have the option to add products directly through the website by accessing "Product Management" in "My Account."

![Fineshine - admin](/media/docs/admin2.jpg)

## Product details page:

When a product is selected, users are directed to the details page, where they can find comprehensive information about the product, including description, price, an option to add the item to the wishlist, and product reviews.

![Fineshine - hero image](/media/docs/product-d.jpg)

## Reviews:

* All users can view product reviews.
* Each review includes a 5-star rating, the user's name, the date of the review, and the review text.
![Fineshine - reviews](/media/docs/reviews.jpg)

* Logged-in users have the option to add reviews.
![Fineshine - add review](/media/docs/review-add.jpg)

* Reviews are available only for products they have purchased.
![Fineshine - error](/media/docs/review-error.jpg)

* Users can edit or delete their own reviews.
![Fineshine - edit/delete review](/media/docs/review-edits.jpg)
![Fineshine - edit/delete review](/media/docs/reviews-manage.jpg)


## Bag

The bag page allows users to view and manage the products added to their shopping bag. When a product is added to the bag, a message is displayed with a preview of the bag. Users can see a summary of each product, including the name, image, price, quantity, and subtotal. They have the option to update the quantity of each item or remove items from the bag. The page also displays the total cost of the selected items.

![Fineshine - hero image](/media/docs/bag.jpg)

Users are informed of the amount needed to qualify for free delivery if they haven't met the minimum amount. From this page, they can proceed to checkout or continue shopping using the "Keep Shopping" button. A toast message is displayed whenever a user adds, updates the quantity, or removes an item from the bag, providing instant feedback on their actions.

![Fineshine - hero image](/media/docs/bag-toast.jpg)


## Checkout

The checkout process at Fineshine is designed to be simple and efficient. When users proceed to checkout from the cart page, they go through the following steps:

Shipping Information: Users enter their payment and shipping address details. If logged in and have previously saved their data, the form is automatically filled with this information.

Payment Information: The payment form accepts user information and notifies if there is an attempt to use an invalid card. Integration with the Stripe API ensures all payment transactions are secure.

To make a test purchase, use the following Stripe test card details:

* Success Card Number: 4242 4242 4242 4242
* Expiration Date: Any future date in the format MM/YY
* CVN: Any 3-digit number
* Postal Code: Any 5-digit combination

Order Review: Before completing the purchase, users have the opportunity to review their cart one last time and make any necessary changes. The total cost of selected items and delivery charge (if applicable) is displayed.

![Fineshine - checkout](/media/docs/checkout.jpg)

### Checkout Success

Upon confirming the order, users finalize their purchase. They are directed to a confirmation page displaying essential details such as the order number and a summary of their purchase. 

![Fineshine -checkout success](/media/docs/checkout-s.jpg)

Simultaneously, an email confirmation with identical information is sent to the user's inbox.
This confirmation email ensures that users have a record of their purchase and provides them with all the necessary details regarding their order, including the order number and items purchased.

![Fineshine - hero image](/media/docs/check-email.jpg)

## Contact

Fineshine provides a convenient contact form for users to reach out with any questions or inquiries. The form is designed to collect essential information such as the user's name, email address, phone number (optional), and their message. If any fields are not filled out correctly, users will receive prompts and error messages to complete the form accurately.

![Fineshine - contact](/media/docs/contact.jpg)

After submitting the form, users are directed to a thank you page, where they receive confirmation of their message submission.

![Fineshine - contact-thankyou page](/media/docs/contact-s.jpg)

Messages sent through the contact form are directly accessible to the site administrator through their business email service, allowing them to promptly respond to customer queries and feedback.

![Fineshine - contact email](/media/docs/contact-email.jpg)

## Wishlist

The Wishlist page allows users to view and manage the products they wish to purchase in the future. When a product is added to the wishlist, users can see a summary of each product, including the name, image and the date it was added.

![Fineshine sign up](/media/docs/wishlist.jpg)

### Features and Functionalities:

**Product Summary:**

Name: Displays the name of the product in the wishlist.

Image: Shows an image of the product.

Date Added: Shows the date when the product was added to the wishlist.

**Manage Wishlist:**

Users can remove items from the wishlist when they are no longer interested in them.

**Favorite Items:**

Users can mark items as favorites. Favorited items are moved to the top of the wishlist for easy access.

![Fineshine sign up](/media/docs/wishlist-fav.jpg)

**Notifications:**

If a product remains in the wishlist for more than five days, the user receives a notification upon logging in, reminding them that the product is still in their wishlist with a link to the wishlist page.

![Fineshine sign up](/media/docs/wishlist-alert.jpg)

### Sign Up Page

- On the registration page, new users can start their journey on Fineshine by creating a personalized account. Here, users provide essential information such as username, email address and password to establish their identity in the system.
- During the registration process, each user is prompted to choose a unique username and email ensuring uniqueness among all accounts.

![Fineshine sign up](/media/docs/resgister.jpg)

- Upon registration, users receive a confirmation email to verify their email address and activate their account.

![Fineshine sign up](/media/docs/register-email.jpg)


### Login Page

- On the login page, registered users can access their existing accounts on Fineshine. Using a simple form, users input their credentials, including username/email and password, to sign into the system. Once authenticated, users have immediate access to the site's personalized features, allowing them to explore and utilize the available functionalities.

![Fineshine login](/media/docs/signin.jpg)

### Logout Page

- The logout page provides users with a convenient way to end their sessions on Fineshine. By clicking the "Logout" button, users are logged out of their accounts, ensuring the privacy and security of their information. Upon logout completion, users are redirected to a confirmation page and then to the homepage, providing a seamless and secure experience.

![Fineshine logout](/media/docs/signout.jpg)

### Profile

On the profile page, users have access to features to manage their account effectively. This page allows users to update their default shipping details using a form, ensuring they can easily keep their shipping information up to date.

Additionally, users can view their previous order history directly on the profile page. Each order is listed with an order number, which users can click to view more detailed information about past orders. This provides users with easy access to track their order history and review details of their past purchases.

![Fineshine logout](/media/docs/profile.jpg)

### 404 Page:

A custom 404 error page was developed to properly handle situations where users accessed non-existent pages or encountered broken links. This page provides clear navigation options to assist users in returning to the main site after encountering broken links or non-existent pages.

![Fineshine 404](/media/docs/404.jpg)

### Future Features

#### Fashion Articles and Style Tips:
   - Create fashion articles providing inspiration and style tips with your jewellery pieces.
   - Share ideas on how to incorporate your jewellery into different looks for various occasions.

#### Jewellery Customization:
   - Implement customization option, allowing customers to create their own unique pieces.
   - Offer choice of materials, gemstones, and custom engravings.

#### Jewellery Blog:
   - Start a blog section focused on jewellery trends, industry news, and behind-the-scenes stories.
   - Share insights about the production process, new collections, and upcoming events.

#### Loyalty Program:
   - Implement a loyalty program to reward frequent customers with discounts, special offers, or early access to new collections.
   - Encourage customer retention and foster long-term relationships.

## Testing 

For detailed testing documentation, refer to the [TESTING.md](TESTING.md) file.

## Bugs

### Solved Bugs
### Variable Naming Conflict 

  * Bug Description: 

There was an issue in the review rating calculation due to a variable naming conflict. Specifically, the incorrect use of aggregate.total_reviews instead of aggregate.rating in the template caused the calculation for the number of stars to be incorrect. This naming conflict interfered with another existing variable, preventing the correct calculation of the average rating (total stars/number of reviews).

![bug - 1](/media/docs/bug1.jpg)


  * Action Taken:

To resolve this issue, the template code was corrected to use the appropriate variable name, aggregate.rating, ensuring that the review ratings are calculated correctly without conflicts.

![bug - 1 solved](/media/docs/bug1-solved.jpg)


### HTML escaping in messages.info not rendering HTML correctly

  * Bug Description: 

HTML inside the messages.info was not being rendered correctly in the template, appearing as plain text.

![bug - 2 ](/media/docs/bug4.png)

  * Action Taken:

Used mark_safe to mark the message as safe before passing it to messages.info(), allowing the HTML inside the message to be rendered correctly in the template.

![bug - 2 solved](/media/docs/bug4.solved.jpg)

![bug - 2 solved](/media/docs/bug4-solves.png)

### Newsletter signup form layout issue.

  * Bug Description: 

The newsletter signup form was displaying incorrectly, cutting off some information and making it difficult to input email on mobile devices.

![bug - 3](/media/docs/bug5.png)

  * Action Taken:

 Removed the width: 600px; property from the form container style, allowing the form to dynamically adjust to the screen size, thereby fixing the issue of information cutoff and email input box.

![bug - 3 solved](/media/docs/bug5-solved.jpg)

### Lack of Timezone Support Causes Wishlist Reminders Issue

  * Bug Description: 

The bug was caused by the lack of timezone support when filtering wishlist reminders. Without timezone support, the system was not correctly considering the time differences between users, resulting in issues such as reminders not being displayed when they should.

  * Action Taken:

To fix the bug, it was necessary to add timezone support using the pytz library. This ensures that wishlist reminders are filtered correctly based on the timezone configured for each user.


![bug - 4 solved](/media/docs/bug3.png)

### Missing Validation Feedback

  * Bug Description: 

There was an issue with the contact form where submitting the form without filling in a required field would simply refresh the page without providing any validation error messages to the user. This made it difficult for users to understand why their submission was not processed.

  * Action Taken:

To address this issue, a forms.py file was created to handle the form logic and validation. The new form ensures that all required fields are validated, and appropriate error messages are displayed if any required fields are left empty.

![bug - 5 solved](/media/docs/bug6.jpg)

### Unsolved Bugs

No unfixed bugs.

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

[Wordtracker](https://www.wordtracker.com/): Used to conduct keyword research.

[Mailchimp](https://mailchimp.com/): Used to set up Email marketing.

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

* **pytz**: Used for accurate and cross-platform timezone calculations. It helps in converting and working with different timezones.

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


You can access the live project by clicking [here](https://fineshine-jewellery-07c9a5f5519c.herokuapp.com/).

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

1. In the "fineshine-jewellery" repository, click on "Fork" in the top right corner.
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

</details>

## Credits

### Code

During the development of my Django project, there were a few times when I needed to explore topics beyond the course material or conduct in-depth reviews. Below are some of the links to the sources I consulted:

* [Scrum & Kanban - Theme, Epic, Story, Task](https://scrumandkanban.co.uk/theme-epic-story-task/)

* [Django-allauth - Quickstart](https://docs.allauth.org/en/latest/installation/quickstart.html)

* [Bootstrap - Introduction](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

* [Djangoproject - Aggregation](https://docs.djangoproject.com/en/5.0/topics/db/aggregation/)

* [Djangoproject - Making queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/)

* [Bootstrap - Spacing](https://getbootstrap.com/docs/5.0/utilities/spacing/#margin-and-padding)

* [w3schools - HTTP Request Methods](https://www.w3schools.com/tags/ref_httpmethods.asp)

* [Stackoverflow - Date formatting in Django templates](https://stackoverflow.com/questions/3663046/date-formatting-in-django-templates)

* [Stackoverflow - Adding days to a date in Python](https://stackoverflow.com/questions/6871016/adding-days-to-a-date-in-python)

* [Visual Studio Code - Formatting Python in VS Code](https://code.visualstudio.com/docs/python/formatting)

* [AskPython - Python pytz Module: Mastering Timezones in Python](https://www.askpython.com/python-modules/python-pytz-module)

* [Fontawesome - Accessibility](https://fontawesome.com/docs/web/dig-deeper/accessibility)

* [README Example](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md): To write the README file, I followed the structure and table format (testing section) from the readme-examples repository by Kera Cudmore.

* The foundation of the project was established using the CI I Think Therefore I Blog project example as a starting point.

### Content

I created  the content for my application.

ChatGPT: used to assist in write the product descriptions.

### Media

[Favicon.io](https://favicon.io/favicon-converter/): utilized to convert the image from the logo into a favicon.

[CloudConvert](https://cloudconvert.com/png-to-webp): utilized for image format conversion.

[Adobe Express](https://www.adobe.com/br/express/feature/image/resize): utilized for image manipulation and resizing.

MS Paint: used to edit the images. 

[Balsamiq](https://balsamiq.com/): utilized for wireframing purposes.

[Coolors](https://coolors.co/f08080-f4978e-f8ad9d-fbc4ab-ffdab9): utilized to create the color palette. 

[Unsplash](https://unsplash.com/) and [Freepik](https://br.freepik.com/): used to source images for the website. 

[Am I Responsive?](https://ui.dev/amiresponsive) and [Morckup Generator](https://techsini.com/multi-mockup/index.php): utilized to view the website's appearance and responsiveness across a range of devices.

### Acknowledgments

I would like to extend my sincere gratitude to the individuals who offered their assistance and support throughout the entirety of this project:

Jubril Akolade, my mentor, for his guidance and constructive feedback.

Laura Mayock, the Cohort Facilitator at Code Institute, for consistently steering our studies in the most effective direction.

My husband Jasser, for always believing in my abilities, for continuously motivating me, and for his unwavering support.

My family and friends for standing by my side throughout this journey. All the support meant a lot to me, and I couldn't have done it without them.

My friends Ivan Frezza and Bruna Andelieri, providing valuable insights and clarifying uncertainties about my code. Thank you for always supporting me.
