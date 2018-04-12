# Elder Scrolls Online Website
 
## Overview
 
### What is this website for?
 
This is a fan site for those who have played the Elder Scrolls Online. 
 
### What does it do?
 
This site provides players with a chance to recreate their characters from ESO while also seeing other player creations. It also provides the purchase of extra content for the game. Along with messaging between other users on the site. 
 
### How does it work
 
This site uses HTML and CSS to display pages. The site is also styled with **Bootstrap**. **Django** was used to create the site, with **SQLite** used to store info. The site can be viewed [HERE](https://becca-elderscrollsonline.herokuapp.com)

## Features
 
### Existing Features

- Vertical Navbar
- Index page with login and register buttons
    - Login form
    - Registtation form
    - On submit redirect to profile page
- Profile app with username
- Characters app
    - compose form link
        - Char fields
        - Text Boxes
        - Drop Downs Menus
        - Checkbox lists
    - Individual Character options
        - Creator can edit the character details
        - Creator can delete character
        - All details listed out on seperate page, with back to list button
    - Image determined by which race is selected
- Store app with 12 unique exapnsion packs with varying prices, pictures, and descriptions
    - Add to cart buttons
- Cart app with a table showing product image, name, quantity, price, and total.
    - Checkout button, links to checkout page
- Checkout app
    - Cart table with same info
    - Buyer shipping info
    - Credit Card Details
    - Submit Payment button
        - Redirects user to store page
        - Clears cart
- Messaging app
    - Inbox
        - compose button link
        - inbox/sent items links
        - list of messages (sender, subject, part of message, date/time sent), click to view
    - Sent
        - Same layout as inbox except messages are the users sent files
    - Compose
        - Form with subject, body, and recipient inputs
    - View Message
        - Message with all info for message
        - Back to inbox button
- Logout option


## Tech Used

### Some the tech used includes:

- **Django Framework**
    - Used to create site and all associated apps
    - Used for testing purposes
- **SQLite**
    - Used to store info:
        - Characters
        - DLCs
        - Messages
- **HTML**, **CSS** and **Javascript**
  - Base languages used to create webpages
- [Bootstrap](http://getbootstrap.com/)
    - We use **Bootstrap** to give our project a simple, responsive layout
- [JQuery](https://jquery.com)
    - Use **JQuery** for boostrap and displaying modal
- **Stripe**
 - Used to process credit card payments

## Testing
- All code used on the site has been tested to ensure everything is working as expected
- Django Testing Framework used
- Site viewed and tested in the following browsers:
  - Google Chrome
  - Microsoft Edge
  - Mozilla Firefox
- Site link sent to and tested on multiple machines on different continents

## Contributing
 

## Credits

### Media
The photos used in this site were obtained from various locations over google and screen shots of the game
All game info and names developed by ZeniMax Online Studios and published by Bethesda Softworks and ZeniMax Online Studios.




