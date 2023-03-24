# LionAuction is an e-commerce web application
It will allow both buyers and sellers to interact through the bidding on various goods.
So far, the logic for user login and database population for users has been implemented. 
Additionally, the original passwords have been removed and replaced with the hashes of the passwords. 
Currently, the website routes initially to index.html, which will prompt the user to login. 
Then, in login.html, the user is asked to input their username and password, and will notify them if given an invalid login.
When the user inputs their password, it is compared against using the hashed password in the data base. 
This is done using the passlib.hash library, and the SHA-256 algorithm is used for the hashing.
Upon successful login, the user is taken to the homepage of LionAuction.
