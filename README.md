# Lion Auction
As an e-commerce website, Lion Auction will allow both buyers and sellers to interact through the bidding on various goods.


In login.html, the user is asked to input their username and password, and will notify them if given an invalid login.
When the user inputs their password, it is compared against using the hashed password in the data base. 
This is done using the passlib.hash library, and the SHA-256 algorithm is used for the hashing.
Upon successful login, the user is taken to the homepage of LionAuction.

A successful login is dependent on also selecting the correct role: bidder, seller, or helpdesk. The priveldes of each 
user time is dependent upon the user.

From the home page, a navigation bar is used to route to other portions of the website. This includes
an account information page, a page of categories which lists several items available to be bid on, and a page to submit 
tickets to helpdesk or view tickets if user is helpdesk

Account displays all the users information, and is dependent on the type of user. Sellers will have their bank account included,
whereas helpdesk will have their position listed. All users will have their general information listed including name, address, etc.
Additionally, one is able to switch roles from the account page. We maintain not only the current user, but their current role using
session in flask. 

In categories, one is able to look through from parent categories to subcategories to individual listings. From the individual listings,
We keep track relevant bidding information that is displayed on the page. Bidding has not been implemented.

Styling on the front end of the website was accomplished using a combination of Bootstrap and css.
