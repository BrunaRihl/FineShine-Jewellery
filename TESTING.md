
  * [Accessibility](#accessibility)
  * [User Story Test](#user-story-test)
  * [Tested Browsers and Devices](#tested-browsers-and-devices)
  * [Manual Testing](#manual-testing)
  * [Validator Testing](#validator-testing)


## Testing 

### Accessibility

From the project's inception, the website's design has been planned with a focus on accessibility. Special attention has been given to ensuring good color contrast, an easily understandable structure, and intuitive navigation, establishing a solid foundation for the user experience.

### LightHouse 

The accessibility, performance, best practices, and SEO (Search Engine Optimization) of the website were analyzed using the Lighthouse tool available in Google Chrome's DevTools.Lighthouse was utilized to address issues and I made changes as per its recommendations. I aimed to achieve 100% on all pages in terms of accessibility and SEO.

![Fineshine Lighthouse](/media/docs/lighthouse1.jpg)


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
| SEO Configuration | The SEO settings have been successfully configured to ensure that users can easily access the desired content. | Pass |
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
| FineShine Logo | When clicked the user will be redirected to the home page. | Clicked Logo | Redirected to the home page. | Pass |
| Navbar links | When clicked the user will be redirected to the correct page. | Clicked link | Redirected to the correct page. | Pass |
| Smaller Screens | The navbar should be displayed in hamburger style on smaller screens to conserve space. | Resized the screen to check the navbar behavior on smaller sizes. | The navbar switched to hamburger style when the screen was resized to a smaller size. | Pass |
| User is Logged In   | Wishlist icon becomes clickable for logged-in users and disabled for non-logged-in users. | Logged in and checked navbar changes. | Wishlist icon became clickable for logged-in users. | Pass |
| Fixed navbar | The navbar should remain fixed at the top of the page while scrolling through the site content. | Scrolled through the site content and observed the navbar behavior. | The navbar remained fixed at the top of the page while scrolling. | Pass |
| **`Register`** |
| User Registration | User should be able to register by providing valid data. User receives a confirmation email after registration. | Entered valid registration data and submitted the form. Verified email confirmation process. | Registration and email confirmation process successful. | Pass |
| Registration with Invalid Data | If the user attempts to register an account with invalid data, such as duplicate information, an incorrect password, or an existing email/username, the registration will not be completed, and an error message will be displayed in the form. | Attempted registration with duplicate data, incorrect password, or existing email/username. | Received error message in the form. | Pass |
| **`Login`** |
| User Login | After entering valid credentials and submitting the login form, the user should be redirected to the homepage and receive a confirmation message indicating successful login. | Entered valid credentials and submitted the login form. | Redirected to the homepage and received confirmation message indicating successful login. | Pass |
| **`Log Out`** |
| User Logout | After clicking on the logout, the user should be redirected to a confirmation page. | Clicked on the logout. | Redirected to the confirmation page. | Pass |
| User Logout Redirect | After confirming the logout, the user should be redirected to the home page. | Confirmed logout. | Redirected to the home page after logout confirmation. | Pass |
| **`Profile`** |
| Update Shipping Details | Users can update their default shipping information using a form. | Updated the shipping details on the profile page. | Shipping information updated successfully. | Pass |
| View Order History | Users can view their previous orders, each listed with an order number. | Checked the order history section in the profile. | Previous orders displayed with clickable order numbers for detailed view. | Pass |
| **`Header`** |
| Responsive Navigation Bar | Navigation bar adjusts on all devices. | Checked on different devices. | Navigation bar adjusts correctly on all devices. | Pass |
| Logo and Company Name | Custom logo displayed, website responsive. | Verified logo and website on various devices. | Custom logo displayed correctly, website responsive on different devices. | Pass |
| Search Bar | Search functionality for finding products. | Tested search by entering keywords. | Search functionality works as expected. | Pass |
| Quick Access Links  | Quick links visible, Wishlist for logged-in users.| Checked visibility and functionality. | Links visible and functional, Wishlist link is clickable only for logged-in users. | Pass |
| Main Navigation | Navigation links functional for categories. | Verified navigation to correct categories. | Navigation links directs to correct categories. | Pass |
| Product Categories | Additional options under each category. | Checked available options. | Additional options displayed under each category. | Pass |
| Favicon | Custom favicon displayed in browser tab. | Verified presence in browser tab. | Custom favicon displayed in browser tab. | Pass |
| **`Products`** |
| Product Categories | Users can explore products by category (earrings, bracelets, etc.). | Checked category navigation. | Navigation by category functional. | Pass |
| Product Hover Effect | Products show zoom effect and shadow on hover. | Tested hover effect on products. | Hover effect applied correctly. | Pass |
| Product Sorting | Users can sort products by price, name, or category. | Tested sorting functionality. | Sorting works as expected. | Pass |
| Product Information | Each product displays image, price, category, and rating. | Reviewed product display. | Product information displayed correctly. | Pass |
| **`Products Details`** |
| Product Details Page | Users find comprehensive product information: description, price, add to wishlist option, and product reviews. | Checked details page layout and information. | Product details page shows all expected information. | Pass |
| Product Reviews | All users can view reviews with 5-star rating, user's name, review date, and text. | Reviewed display of reviews. | Reviews displayed with all required information. | Pass |
| Adding Reviews | Logged-in users can add reviews for products they have purchased. | Tested adding reviews as logged-in user. | Adding reviews functional for logged-in users. | Pass |
| Editing/Deleting Reviews | Users can edit or delete their own reviews. | Tested editing/deleting reviews. | Editing/deleting reviews functional. | Pass |
| **`Admin`** |
| Login to Django Panel | The admin should be able to log in to the Django panel using the provided credentials. | Logged in to the Django panel using admin credentials | Successfully accessed the Django panel | Pass |
| Add, Edit, and Delete Products | The admin should be able to add, edit, and delete products both from the admin panel and through the website. | Added, edited, and deleted products from both admin panel and website interface | Products were successfully managed | Pass |
| **`Bag`** |
| View Bag | Users can view and manage products in their shopping bag, including name, image, price, quantity, and subtotal. | Added products to the bag and viewed bag contents. | All product details are correctly displayed. | Pass |
| Update Quantity | Users can update the quantity of each item in the bag. | Updated product quantities in the bag. | Quantities updated successfully. | Pass |
| Remove Items | Users can remove items from the bag. | Removed items from the bag. | Items removed successfully. | Pass |
| Total Cost Display | The total cost of selected items is displayed. | Verified total cost calculation. | Total cost is displayed correctly. | Pass |
| Free Delivery Info | Users are informed about the amount needed to qualify for free delivery. | Checked free delivery message with different total amounts. | Free delivery message displayed correctly. | Pass |
| Proceed to Checkout | Users can proceed to checkout from the bag page. | Clicked "Proceed to Checkout" button. | Redirected to checkout page successfully. | Pass |
| Continue Shopping | Users can continue shopping using the "Keep Shopping" button. | Clicked "Keep Shopping" button. | Redirected back to shopping page successfully. | Pass |
| Toast Messages | Toast messages are displayed when adding, updating, or removing items from the bag. | Added, updated, and removed items to observe toast messages. | Toast messages displayed correctly for each action. | Pass |
| **`Checkout`** |
| Shipping Information | Users enter payment and shipping address details; form pre-filled if logged in and data saved. | Entered shipping information, logged in and verified pre-filled data. | Form correctly pre-filled and accepted shipping details. | Pass |
| Payment Information | The payment form accepts valid card details, notifies invalid card attempts, and integrates with Stripe for secure transactions. | Tested with Stripe test card, checked for invalid card notification. | Payment processed securely, invalid card notification displayed. | Pass |
| Order Review | Users can review and edit their cart before finalizing the purchase, with total cost and delivery charges displayed. | Reviewed and edited cart before finalizing. | Cart review and edits functioned correctly, total cost displayed accurately. | Pass |
| Checkout Success | Users are directed to a confirmation page with order number and summary; confirmation email sent with order details. | Completed checkout, observed confirmation page, and checked email. | Confirmation page displayed correctly, email received with correct order details. | Pass |
| **`Wishlist`** |
| Add to Wishlist Button | When clicked, the product should be added to the user's wishlist. | Clicked "Add to Wishlist" button for a product. | Product was successfully added to the wishlist. | Pass |
| View Wishlist | Users should be able to view all products added to their wishlist. | Navigated to the wishlist page. | All products in the wishlist were displayed correctly. | Pass |
| Remove from Wishlist | Users should be able to remove products from their wishlist. | Clicked "Remove" button for a product in the wishlist. | Product was successfully removed from the wishlist. | Pass |
| View Product Details  | Users can click on a product to view more details. | Clicked on a product in the Wishlist. | Product details were displayed correctly. | Pass |
| Wishlist Sorting | Wishlist items should be sorted by  favorites. | Viewed the Wishlist. | Items are sorted correctly. | Pass |
| Wishlist Notifications | Users should receive a notification upon login if a product remains in the Wishlist for more than five days. | Product remained in Wishlist for more than five days. | User receives a notification upon login with link to the Wishlist. | Pass |
| **`Contact`** |
| Contact Form Submission | Users can submit their name, email, phone number (optional), and message; prompts and errors for incorrect fields. | Filled out and submitted the contact form with valid and invalid data. | Form submission successful with valid data; error messages displayed for incorrect fields. | Pass |
| Thank You Page | After form submission, users are directed to a thank you page confirming submission. | Submitted the contact form and observed the redirection. | Thank you page displayed confirming submission. | Pass |
| Admin Access to Messages | Messages are sent to the site admin's business email for prompt response. | Submitted a message and checked the admin email. | Message received in admin's email. | Pass |
| **`Notification messages`** |
| Notification messages | Clear and informative messages are displayed upon registration, login, logout, adding, editing, or deleting bookings. | Perform registration, login, logout, adding, editing, or deleting... Verify if clear and informative messages are displayed on the screen confirming the actions taken. | Messages displayed successfully. | Pass |
| **`Footer`** |
| Newsletter Signup | Submitting the newsletter signup form with a valid email address adds the user to the mailing list. | Submitted valid email address to newsletter signup form | User is successfully added to the mailing list. | Pass |
| Newsletter Validation | Submitting the newsletter signup form with an invalid email address displays an error message. | Submitted invalid email address to newsletter signup form | Error message is displayed. | Pass  |
| Useful Links | Useful links in the footer section direct users to the respective pages. | Clicked on useful links in the footer. | User is directed to the respective pages. | Pass |
| Icon Clicked | Clicking on social network icons in the footer opens new windows directing users to the respective social networks. | Clicked social network icons | Opens the pages in a new window. | Pass |

| **`404 Page`** |
| Custom 404 Page | A custom 404 page appears when users access non-existent pages, offering clear navigation back to the main site. | Accessed a non-existent page to trigger the 404 error. | Custom 404 page displayed with navigation options. | Pass |


### Validator Testing  

  * HTML:  

To ensure the validity and compliance of my web pages with web standards, I used the W3C validator. This tool helped me identify and correct any errors highlighted in my pages.

![W3C validator - html](/media/docs/html-check.jpg)  


The corrections were implemented in accordance with the validator's suggestions.

  * CSS:  

No errors were found during the validation process using the official Jigsaw validator.


![Jigsaw validator - Css](/media/docs/css-check.jpg)  


  * Python

To ensure compliance with the best coding practices, I integrated Black (an automatic code formatter) into my workflow. Black helped maintain consistent code style and formatting throughout the project, ensuring readability and adherence to PEP8 guidelines. Additionally, to identify and fix style and formatting issues throughout the project's source code, I installed Flake8 in my development environment.

![Black - Python](/media/docs/blak2.jpg) 

I also used the PEP8 validator to identify and correct any remaining issues in my code. The identified errors were primarily related to improper use of whitespace and exceeding the line length.

![Pep8 - Python](/media/docs/pythonlinter.jpg) 



