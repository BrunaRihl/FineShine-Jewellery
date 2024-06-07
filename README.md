# FineShine Jewellery

FineShine is an online platform specializing in the sale of unique and elegant jewelry, featuring a wide collection of earrings, necklaces, bracelets, rings, and sets. All pieces are crafted in Ireland and available for shipping. This project was developed as my fifth endeavor in the Code Institute's Full Stack Developer Course, utilizing Django, HTML, CSS, JS, and Python for its creation.

![FineShine website shown on a range of devices](/static/images/docs/responsive.png)  

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

* [Marketing and SEO](#marketing-and-seo)
  * [Business Model - Ecommerce](#business-model---ecommerce)
  * [Marketing](#marketing)
  * [Search Engine Optimization](search-engine-optimization)

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

I have a total of 41 user stories for this project. Here is how I have distributed them across the four categories:

* Must Have: 27 user stories (65%)
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

## Marketing and SEO
### Business Model - Ecommerce
**Fineshine** is a Business to Customer (B2C) e-commerce platform, specializing in the production and sale of high-quality jewelry to individual customers.

### Competitive Advantages:
- **Superior Quality:** Producing and offering high-quality jewelry made with precious materials and unique designs.
- **Ease of Purchase:** Providing an easy and convenient purchasing experience through the online platform.
- **Social Engagement:** Building a community of loyal customers through engagement on social media and loyalty programs.

### Customer Segments:
- **Jewelry Enthusiasts:** Individuals seeking high-quality and exclusive design jewelry.
- **Gift Buyers:** People purchasing jewelry for special occasions like birthdays and weddings.

### Key Assets:
- **Jewelry Inventory:** Diverse inventory of internally produced jewelry to meet customer demand.
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
- **Material Suppliers:** Partnerships with suppliers of precious materials for jewelry production.
- **Delivery Services:** Collaboration with shipping services to ensure efficient order delivery.
- **Fashion Influencers:** Partnerships with fashion influencers to promote products and reach new audiences.
- **Designer Collaborations:** Collaborations with renowned jewelry designers for exclusive collections.

### Seasonal Marketing Campaigns:
- **Festive Promotions:** Creating special promotions for holidays like Christmas, Valentine's Day, and Black Friday.
- **Online Events:** Hosting online events such as collection launches and webinars on jewelry care.

### Competition Analysis:
- **Competitive Analysis:** Studying key competitors in the online jewelry market to identify opportunities and threats.
- **Benchmarking:** Comparing products, prices, and marketing strategies with major competitors.

### Data Analysis and Feedback:
- **Data Analysis:** Using data analytics to understand customer behavior and optimize marketing and sales strategies.
- **Feedback Collection:** Implementing systems to collect and analyze customer feedback for continuous improvement.

## Marketing

A Facebook page was created to promote the jewelry e-commerce due to the platform's wide visibility and engagement potential. Facebook allows for reaching a diverse audience, increasing brand visibility, and attracting new consumers.
To personalize the page, the store's logo was added as the profile picture, and a welcome message with a direct link to the online store was written, making it easy for visitors to access.

![FineShine website shown on a range of devices](/static/images/docs/responsive.png)  

Additionally, a post was created featuring an exclusive jewelry set as the highlight of the week, including a photo of the product and a link for purchase.

![FineShine website shown on a range of devices](/static/images/docs/responsive.png)  

This strategy aims to increase engagement, drive traffic to the website, and boost sales, strengthening the brand's presence on social media.

## Search Engine Optimization
### Keyword Strategy to Increase Online Visibility

To ensure that my website was easily discoverable through online searches, I developed a keyword strategy. This strategy encompassed two main types of keywords:

- **Short-Tail Keywords (Primary Terms):** These were brief and comprehensive terms that captured the essence of my website's offerings in general.

- **Long-Tail Keywords:** These were more specific and detailed phrases that directly aligned with the products and services offered on my site.

To further enhance my keyword strategy, I turned to suggestions provided by Google during searches. I utilized features like "People also search for" and the auto-suggestions provided by Google while typing a keyword. These tools helped me identify popular search trends and related terms actively sought by users.

![FineShine website shown on a range of devices](/static/images/docs/responsive.png)  

Additionally, I utilized resources like Wordtracker.com to conduct keyword research and identify relevant terms that aligned with the content and purpose of my site.

![FineShine website shown on a range of devices](/static/images/docs/responsive.png)  

After the research, my selected keywords were:

![FineShine website shown on a range of devices](/static/images/docs/responsive.png)  


Sitemap: A sitemap.xml file has been created to help search engines index the website more effectively.

Robots.txt: A robots.txt file has been implemented to guide search engine crawlers on which pages to index or avoid, ensuring efficient and controlled crawling of the site.


## Features

### Header

* All pages feature a responsive navigation bar at the top of the screen.

**Logo and Company Name:** A custom logo was created for Fineshine, ensuring instant brand recognition.
![FineShine website shown on a range of devices](/static/images/docs/responsive.png)  

- **Search Bar:** A search bar allows users to easily find specific products directly from the header.

- **Quick Access Links:** On the right side of the header are quick access links, including "My Account," "Contact," and "Shopping Bag." The "Wishlist" link is visible only when the user is logged in.

- **Main Navigation:** Below the header, the main navigation allows users to choose products by categories such as "All Products," "Earrings," "Necklaces," among others.

- **Product Categories:** When clicking on a category such as "Earrings," users have additional options such as "Silver Earrings," "Gold Earrings," or "Full Collection."


### Favicon

A custom favicon has been added to the website's header. The favicon features a diamond with sparkling accents around it, matching the site's color palette of aqua green tones, providing a unique visual identity.

![Fineshine - favicon](/static/images/docs/favicon-docs.webp)

### Footer

### Home Page 

* The main image showcases golden jewelry arranged against a background of aqua green, which inspired the color palette of the site.
* The overlaid message provides a brief introduction to the website's concept, while the high resolution and vibrant colors ensure an inviting presentation to visitors.
* The "Shop Now" button below the main image provides a clear call-to-action, inviting users to explore and shop for jewelry.

![Fineshine - hero image](/static/images/docs/hero-image.webp)

#### Why shop whit us section:

Below the main image, users will find the "Why Shop for Jewellery with FineShine" section.

This section highlights the reasons why customers should choose FineShine for their jewellery purchases. Each reason is presented concisely, providing an overview of the benefits of shopping with FineShine.

![Fineshine - hero image](/static/images/docs/hero-image.webp)

### Products:

Users can explore products by selecting different categories such as earrings, bracelets, necklaces, rings, and sets, available in silver, gold, or the complete collection. This allows for quick and easy navigation through the products of interest.
![Fineshine - hero image](/static/images/docs/hero-image.webp)

When hovering over the products, a zoom effect is applied, accompanied by a subtle shadow to enhance the item preview.

Additionally, users can also sort the products by price, name, or category, offering even more control over the item view.

![Fineshine - hero image](/static/images/docs/hero-image.webp)

Each product displays a representative image, price, category, and rating (if available).

![Fineshine - hero image](/static/images/docs/hero-image.webp)

#### Admin Features:

Administrators have access to additional options such as adding new products or deleting existing ones.

![Fineshine - hero image](/static/images/docs/hero-image.webp)

Admins also have the option to add products directly through the website by accessing "Product Management" in "My Account."

![Fineshine - hero image](/static/images/docs/hero-image.webp)

#### Product details page:

When a product is selected, users are directed to the details page, where they can find comprehensive information about the product, including description, price, an option to add the item to the wishlist, and product reviews.

![Fineshine - hero image](/static/images/docs/hero-image.webp)

#### Reviews:

* All users can view product reviews.
* Each review includes a 5-star rating, the user's name, the date of the review, and the review text.
![Fineshine - hero image](/static/images/docs/hero-image.webp)

* Logged-in users have the option to add reviews.
* Reviews are available only for products they have purchased.
![Fineshine - hero image](/static/images/docs/hero-image.webp)

* Users can edit or delete their own reviews.
![Fineshine - hero image](/static/images/docs/hero-image.webp)


### Bag

The bag page allows users to view and manage the products added to their shopping bag. When a product is added to the bag, a message is displayed with a preview of the bag. Users can see a summary of each product, including the name, image, price, quantity, and subtotal. They have the option to update the quantity of each item or remove items from the bag. The page also displays the total cost of the selected items.

![Fineshine - hero image](/static/images/docs/hero-image.webp)

Users are informed of the amount needed to qualify for free delivery if they haven't met the minimum threshold. From this page, they can proceed to checkout or continue shopping using the "Keep Shopping" button. A toast message is displayed whenever a user adds, updates the quantity, or removes an item from the bag, providing instant feedback on their actions.

![Fineshine - hero image](/static/images/docs/hero-image.webp)


### Checkout

The checkout process at Fineshine is designed to be simple and efficient. When users proceed to checkout from the cart page, they go through the following steps:

Shipping Information: Users enter their payment and shipping address details. If logged in and have previously saved their data, the form is automatically filled with this information.

Payment Information: The payment form accepts user information and notifies if there is an attempt to use an invalid card. Integration with the Stripe API ensures all payment transactions are secure.

To make a test purchase, use the following Stripe test card details:

* Success Card Number: 4242 4242 4242 4242
* Expiration Date: Any future date in the format MM/YY
* CVN: Any 3-digit number
* Postal Code: Any 5-digit combination

Order Review: Before completing the purchase, users have the opportunity to review their cart one last time and make any necessary changes. The total cost of selected items and delivery charge (if applicable) is displayed.

![Fineshine - hero image](/static/images/docs/hero-image.webp)

#### Checkout Success

Upon confirming the order, users finalize their purchase. They are directed to a confirmation page displaying essential details such as the order number and a summary of their purchase. 

![Fineshine - hero image](/static/images/docs/hero-image.webp)

Simultaneously, an email confirmation with identical information is sent to the user's inbox.
This confirmation email ensures that users have a record of their purchase and provides them with all the necessary details regarding their order, including the order number, items purchased, and billing/shipping information.

![Fineshine - hero image](/static/images/docs/hero-image.webp)

### Contact

Fineshine provides a convenient contact form for users to reach out with any questions or inquiries. The form is designed to collect essential information such as the user's name, email address, phone number (optional), and their message. If any fields are not filled out correctly, users will receive prompts and error messages to complete the form accurately.

![Fineshine - hero image](/static/images/docs/hero-image.webp)

After submitting the form, users are directed to a thank you page, where they receive confirmation of their message submission.

![Fineshine - hero image](/static/images/docs/hero-image.webp)

Messages sent through the contact form are directly accessible to the site administrator through their business email service, allowing them to promptly respond to customer queries and feedback.

![Fineshine - hero image](/static/images/docs/hero-image.webp)

### Wishlist

### Sign Up Page

- On the registration page, new users can start their journey on Fineshine by creating a personalized account. Here, users provide essential information such as username, email address and password to establish their identity in the system.
- During the registration process, each user is prompted to choose a unique username and email ensuring uniqueness among all accounts. 
- Upon registration, users receive a confirmation email to verify their email address and activate their account.

![Fineshine sign up](/static/images/docs/signup-error.webp)


### Login Page

- On the login page, registered users can access their existing accounts on Fineshine. Using a simple form, users input their credentials, including username/email and password, to sign into the system. Once authenticated, users have immediate access to the site's personalized features, allowing them to explore and utilize the available functionalities.

![Fineshine login](/static/images/docs/login.webp)

### Logout Page

- The logout page provides users with a convenient way to end their sessions on Fineshine. By clicking the "Logout" button, users are logged out of their accounts, ensuring the privacy and security of their information. Upon logout completion, users are redirected to a confirmation page and then to the homepage, providing a seamless and secure experience.

![Fineshine logout](/static/images/docs/signout.webp)

### Profile

On the profile page, users have access to features to manage their account effectively. This page allows users to update their default shipping details using a form, ensuring they can easily keep their shipping information up to date.

Additionally, users can view their previous order history directly on the profile page. Each order is listed with an order number, which users can click to view more detailed information about past orders. This provides users with easy access to track their order history and review details of their past purchases.

![Fineshine logout](/static/images/docs/signout.webp)

### 404 Page:

A custom 404 error page was developed to properly handle situations where users accessed non-existent pages or encountered broken links. This page provides clear navigation options to assist users in returning to the main site after encountering broken links or non-existent pages.

![Fineshine 404](/static/images/docs/404-page.webp)

### Future Features and Resources to be Added

#### Fashion Articles and Style Tips:
   - Create fashion articles providing inspiration and style tips with your jewelry pieces.
   - Share ideas on how to incorporate your jewelry into different looks for various occasions.

#### Jewelry Customization:
   - Implement customization option, allowing customers to create their own unique pieces.
   - Offer choice of materials, gemstones, and custom engravings.

#### Jewelry Blog:
   - Start a blog section focused on jewelry trends, industry news, and behind-the-scenes stories.
   - Share insights about the production process, new collections, and upcoming events.

#### Loyalty Program:
   - Implement a loyalty program to reward frequent customers with discounts, special offers, or early access to new collections.
   - Encourage customer retention and foster long-term relationships.

## Testing 

### User Story Test: 

| User Story | Expected Result | Actual Result |
|------------|-----------------|---------------|
**`EPIC 1`**
| Early deployment | The application is successfully deployed and accessible on Heroku. | Pass |
| Setting Up Initial Django Project Structure | The Django project is properly configured with the required structure. | Pass |
| Database Integration | Data is successfully stored in the database, and files are uploaded and accessible. | Pass |
**`EPIC 2`**
| Admin Login Functionality | Log in to the admin panel successfully and be able to manage its operations. | Pass |
| Product Management Functionality | Introduce, edit, and delete new products successfully. | Pass |
**`EPIC 3`**
| Register Account | A new user account is successfully created. | Pass |
| User Login | The user is successfully logged in to their account. | Pass |
| User Logout | The user is successfully logged out of their account. | Pass |
| Profile Update | My profile information is successfully updated. | Pass |
| Secure Password Reset | Receive an email with the password reset link and successfully reset the password. | Pass |
| Secure Credential Storage | User's username and password are securely saved and accessible for easy website access. | Pass |
**`EPIC 4`**
| SEO Configuration | As configurações de SEO são configuradas com sucesso para garantir que os usuários possam acessar facilmente o conteúdo desejado. | Pass |
| Newsletter System | Successful utilization of MailChimp for regular communications with customers. | Pass |
| Facebook Marketing Page | Successful creation of a Facebook marketing page. | Pass |
**`EPIC 5`**
| Website Accessibility | Users can navigate the website with ease and access all content, ensuring an inclusive browsing experience and effective access to information. | Pass |
| Intuitive Navigation | Users can navigate through the website/application easily and efficiently, finding what they need without confusion. | Pass |
| Responsive Design | The design adapts seamlessly to different devices (desktop, tablet, mobile), providing a consistent and smooth user experience. | Pass |
| Interaction Messaging | Users receive clear feedback about their actions, helping them understand what is happening and allowing confident navigation and interaction with the product. | Pass |
**`EPIC 6`**
| Intuitive Category Navigation | Users can browse through different product categories intuitively and easily find products that match their preferences. | Pass |
| Product Search by Keywords | Users can search for products by keywords and quickly find what they're looking for. | Pass |
| Search Sorting | Users can sort the search results by price and other options to refine their selection.| Pass |
| Product Details | Users can view a comprehensive product details page including description, price, images, and customer reviews, allowing them to make informed purchasing decisions. | Pass |
| Product Review | Users can leave their review on products they have purchased. | Pass |
**`EPIC 7`**
| Bag Addition | Users can add products to the shopping bag directly from the product details page for a convenient shopping experience. | Pass |
| Product Bag Management | Users can add products to their shopping bag to keep track of items they intend to purchase and have a preview of how their bag looks on the current page. | Pass |
| Bag Item Management | Users can delete and adjust the quantity of items in their shopping bag before proceeding to checkout. | Pass |
| Shopping Bag Overview | Users can view the contents of their shopping bag to review the items added and the total cost, including shipping fees. | Pass |
| Checkout Process | Users can proceed to checkout from their shopping bag to complete their purchase, allowing them to finalize their order. | Pass |
| Checkout Details Entry | Users can enter their personal and delivery details during checkout to ensure delivery of their order. | Pass |
| Secure Payment Processing | Users can securely enter payment details to complete the transaction, with integration with the Stripe API. | Pass |
| Order History | Can view order history in my profile to review past purchases. | Pass |
| Order Confirmation Email | Receive a confirmation email after successfully completing the checkout process, providing details of my order. | Pass |
**`EPIC 8`**
| Contact Option Accessibility | Easily locate the contact option on the website to efficiently reach out to the company for assistance or inquiries. | Pass |
| Contact Form Submission | Fill out a contact form with personal information and message to send an inquiry to the team. Receive a confirmation upon submitting the contact form. | Pass |
| Contact Form Management | Website admin can check whenever a contact form is submitted, enabling prompt responses to visitor inquiries and efficient customer service. | Pass |
**`EPIC 9`**
| Wishlist Management | Customers can add and remove products to/from their wishlist to save items they wish to purchase in the future. | Pass |
| Wishlist Display | Customers can view all the products they've added to their wishlist, allowing them to review their choices and make informed purchasing decisions. | Pass |
**`EPIC 10`**
| User Engagement - Blog | - | Future Features |
| Content Management - Blog | - | Future Features |
**`EPIC 11`**
| README Documentation | The README.md file provides detailed information about the project's purpose, functionality, and usage. | Pass |
| Testing Procedures | Testing procedures are thorough and ensure the quality and usability of the software. | Pass |


### Tested Browsers and Devices: 

* Web Browsers: 

  * Google Chrome;

  * Microsoft Edge; 
 
  * Safari; 

  * Mozilla Firefox.


* Mobile Devices: 

  * iPhone Xr;

  * iPhone 12 Pro; (Google Chrome Inspector) 

  * Samsung Galaxy S20 Ultra. (Google Chrome Inspector) 


* Tablet: 

  * Ipad Air 4, 10.9-inch screen;

  * Nest Hub. (Google Chrome Inspector) 

 
* Laptop: 

  * Macbook Air, 13-inch screen;

  * Asus TUF F15, 15.6-inch screen. 

### Manual Testing

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| **`Navbar`** |
| StarLight Logo | When clicked the user will be redirected to the home page. | Clicked Logo | Redirected to the home page. | Pass |
| Menu-hover | When hovering over the menu items, the text should appear in bold to indicate action.| Hover over menu | text appear in bold. | Pass |
| Navbar links | When clicked the user will be redirected to the correct page.| Clicked link | Redirected to the correct page. | Pass |
| Smaller Screens | The navbar should be displayed in hamburger style on smaller screens to conserve space. | Resized the screen to check the navbar behavior on smaller sizes. | The navbar switched to hamburger style when the screen was resized to a smaller size. | Pass |
| User is Logged In | When the user is logged in, a new menu for booking and the logout option should appear, while the register and login options should disappear. | Logged in with a user account and observed the changes in the navbar. | The booking menu and logout option appeared, and the register and login options disappeared after logging in. | Pass |
| Fixed navbar | The navbar should remain fixed at the top of the page while scrolling through the site content. | Scrolled through the site content and observed the navbar behavior. | The navbar remained fixed at the top of the page while scrolling. | Pass |
| Authentication Status Display | The website displays a message below the navigation bar indicating whether the user is logged in or not. | Verified the message display below the navigation bar while logged in and logged out. | Message displayed correctly indicating the authentication status. | Pass |
| **`Register`** |
| User Registration | After submitting valid data for registration, the user should be prompted to confirm their password, ensuring accuracy. The username must be unique and not already in use, and the optional email field must be in a valid format. | Entered valid registration data and verified the password confirmation request, uniqueness of the username, and valid email format. | The password confirmation request appeared, the unique username was accepted, and the valid email format was enforced. | Pass |
| Registration Redirection | Upon successful registration, the user should be redirected to the home page and receive a notification confirming that they are logged in. | Successfully registered a new account and observed redirection to the home page with a logged-in notification. | Redirected to the home page and received a logged-in notification after successful registration. | Pass |
| Registration with Invalid Data | If the user attempts to register an account with invalid data, such as duplicate information or an incorrect password, the registration will not be completed, and an error message will be displayed in the form. | Attempted registration with duplicate data or incorrect password. | Received error message in the form. | Pass |
| **`Login`** |
| User Login | After entering valid credentials and submitting the login form, the user should be redirected to the homepage and receive a confirmation message indicating successful login. | Entered valid credentials and submitted the login form. | Redirected to the homepage and received confirmation message indicating successful login. | Pass |
| Authenticated User Menus | When logged in, exclusive menus for authenticated users should appear, and the option to schedule an appointment becomes available. | Logged in with valid credentials and observed the appearance of exclusive menus. | Exclusive menus appeared, and appointment scheduling option became available. | Pass |
| **`Log Out`** |
| User Logout | After clicking on the logout, the user should be redirected to a confirmation page. | Clicked on the logout. | Redirected to the confirmation page. | Pass |
| User Logout Redirect | After confirming the logout, the user should be redirected to the home page. | Confirmed logout. | Redirected to the home page after logout confirmation. | Pass |
| **`Booking`** |
| User able to select the service | User should be able to select the desired service when booking a consultation | Selected the desired service on the booking page | Service selected successfully | Pass |
| Select the date | User should be able to choose the desired date for the consultation | Selected a date on the booking page | Date was successfully selected | Pass |
| Select the time | User should be able to choose the preferred time for the consultation | Chose a time slot on the booking page | Time was successfully selected | Pass |
| Book consultation | User should be able to schedule a consultation by selecting a date and time | Attempted to book a consultation on the booking page | Consultation was successfully scheduled | Pass |
| User cannot book in a past date | User should receive an alert when attempting to schedule an appointment for a past date | Tried to book a consultation for a past date on the booking page | Alert message appeared indicating that booking for past dates is not allowed | Pass |
| Unavailable booking slot | When attempting to book a consultation on a date and time that is already booked, the user should receive an alert indicating that the consultant is not available for that date or time. | Attempted to book a consultation on a date and time that is already booked | Alert displayed indicating that the consultant is not available for that date or time | Pass |
| Edit booking | User should have the option to edit their existing bookings | Accessed the edit option for a booked consultation | Booking details were successfully edited | Pass |
| Delete booking | User should be able to remove their bookings if needed | Attempted to delete a booked consultation | Booking was successfully deleted | Pass |
| Save booking in booking page | User's bookings should be saved and displayed on the booking page | Scheduled a consultation and checked if it appeared on the booking page | Booking was saved and appeared on the booking page | Pass |
| **`Home`** |
| Button: Non-Logged-in User | "Login First" message appears, indicating the user needs to log in first to book. | Clicked "Login First" Button | Redirected to the login page. | Pass |
| Button: Logged-in User | "Book Now" button appears, allowing the user to book appointments. | Clicked "Book Now" Button | Redirected to the booking page. | Pass |
| Button: hover | When the mouse hovers over the button, it should change color to indicate action. | Hovered over the button and observed the color change. | The button changed color when hovered over, indicating action. | Pass |
| **`About`** |
| Text Loading  | The text on the "About" page should match the content entered in the admin panel. | Compared displayed text with admin panel content. | Text matched admin panel content. | Pass |
| Image Upload             | The administrator can successfully upload the image through the administration panel.                 | Verification of the image upload process in the administration panel.     | The correct image is displayed on the website.    | Pass |
| Updated Date    | Creation date of the text displayed at the bottom of the page. | Checked if the displayed date matches the creation date of the text. | Date displayed matched the creation date of the text. | Pass |
| Button: Non-Logged-in User | "Login First" message appears, indicating the user needs to log in first to book. | Clicked "Login First" Button | Redirected to the login page. | Pass |
| Button: Logged-in User | "Book Now" button appears, allowing the user to book appointments. | Clicked "Book Now" Button | Redirected to the booking page. | Pass | 
| Button: hover | When the mouse hovers over the button, it should change color to indicate action. | Hovered over the button and observed the color change. | The button changed color when hovered over, indicating action. | Pass |
| **`Admin`** |
| Login to Django Panel | The admin should be able to log in to the Django panel using the provided credentials. | Logged in to the Django panel using admin credentials | Successfully accessed the Django panel | Pass |
| Add, Edit, and Delete Services | The admin should be able to add, edit, and delete services from the website. | Added, edited, and deleted services from the admin panel | Successfully managed services | Pass |
| Edit and Delete Bookings | The admin should be able to edit and delete bookings from the admin panel. | Edited and deleted bookings from the admin panel | Successfully managed bookings | Pass |
| Add, Edit, and Delete Content of About Page | The admin should be able to add, edit, and delete content on the About page from the admin panel. | Added, edited, and deleted content on the About page from the admin panel | Successfully managed About page content | Pass |
| New Menu in Navbar| When logged in as an admin, a new menu should appear in the navbar allowing direct access to the admin control panel, redirecting the admin to the panel. | Logged in as an admin and observed the appearance of a new menu in the navbar | New menu appeared in the navbar, providing access to the admin control panel | Pass |
| **`Notification messages`** |
| Notification messages | Clear and informative messages are displayed upon registration, login, logout, adding, editing, or deleting bookings. | Perform registration, login, logout, adding, editing, or deleting bookings. Verify if clear and informative messages are displayed on the screen confirming the actions taken. | Messages displayed successfully. | Pass      |
| **`Footer`** |
| Icon-clicked | Clicking on social network icons in the footer opens new windows directing users to the respective social networks.| Clicked social networks Icons | Opens the pages in a new window. | Pass |


### Validator Testing  

  * Python

To ensure compliance with coding best practices, I installed Flake8 in my development environment. Flake8 assisted me in identifying and rectifying style and formatting issues throughout the project's source code.

Additionally, I utilized the PEP8 validator to identify and correct any remaining issues in my code. The identified errors were primarily related to improper use of whitespace and exceeding line length. All of these issues were addressed comprehensively, ensuring adherence to coding best practices.

![Pep8 - Python](/static/images/docs/python-check.webp)

  * CSS:  

No errors were found during the validation process using the official Jigsaw validator.


![Jigsaw validator - Css](/static/images/docs/jigsaw-valid.webp)


  * HTML:  

To ensure the validity and compliance of my web pages with web standards, I used the W3C validator. This tool helped me identify and correct any errors highlighted in my pages.

![W3C validator - html](/static/images/docs/html-check.webp)


The corrections were implemented in accordance with the validator's suggestions.

#### Unit Test 

I used unit tests to ensure the proper functioning of different parts of the application. The unit tests were implemented using Python's unittest module.

![unittest - python](/static/images/docs/unittest.png)


### Bugs

#### Solved Bugs
#### Variable Naming Conflict 

  * Bug Description: 

There was an issue in the review rating calculation due to a variable naming conflict. Specifically, the incorrect use of aggregate.total_reviews instead of aggregate.rating in the template caused the calculation for the number of stars to be incorrect. This naming conflict interfered with another existing variable, preventing the correct calculation of the average rating (total stars/number of reviews).
![bug - 1](/static/images/docs/bug3-2.png)

  * Action Taken:

To resolve this issue, the template code was corrected to use the appropriate variable name, aggregate.rating, ensuring that the review ratings are calculated correctly without conflicts.

![bug - 1 solved](/static/images/docs/bug3-2.png)




#### Replace Date Mask with Current Date on Booking

  * Bug Description: 

There was an issue with the contact form where submitting the form without filling in a required field would simply refresh the page without providing any validation error messages to the user. This made it difficult for users to understand why their submission was not processed.

  * Action Taken:

To address this issue, a forms.py file was created to handle the form logic and validation. The new form ensures that all required fields are validated, and appropriate error messages are displayed if any required fields are left empty.
This solution ensures that users are properly informed if they miss any required fields when submitting the contact form, enhancing the overall user experience and ensuring that messages are correctly sent to the admin.

#### Unsolved Bugs

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
