--Schema start--
CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT);

CREATE TABLE helpdesk (username TEXT PRIMARY KEY, position TEXT);

CREATE TABLE Requests (
    request_id INTEGER PRIMARY KEY,
    sender_email TEXT,
    helpdesk_staff_email TEXT,
    request_type TEXT,
    request_desc TEXT,
    request_status INTEGER
);

CREATE TABLE Address (
    address_id HEX PRIMARY KEY,
    zipcode TEXT,
    street_num TEXT,
    street_name TEXT
);

CREATE TABLE Bidder (
    email TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    age INTEGER,
    home_address_id HEX,
    major TEXT,
    FOREIGN KEY(home_address_id) REFERENCES Address(address_id)
);

CREATE TABLE Zipcode_Info (
    zipcode TEXT PRIMARY KEY,
    city TEXT,
    state TEXT
);

CREATE TABLE Credit_Cards (
    credit_card_num TEXT PRIMARY KEY,
    card_type TEXT,
    expire_month INTEGER,
    expire_year INTEGER,
    security_code TEXT,
    Owner_email TEXT,
    FOREIGN KEY(Owner_email) REFERENCES Bidder(email)
);

CREATE TABLE Seller (
    email TEXT PRIMARY KEY,
    bank_routing_number TEXT,
    bank_account_number TEXT,
    balance REAL,
    FOREIGN KEY(email) REFERENCES Bidder(email)
);

CREATE TABLE Local_Vendors (
    email TEXT PRIMARY KEY,
    business_name TEXT,
    business_address_id HEX,
    customer_service_phone_number TEXT,
    FOREIGN KEY(email) REFERENCES Seller(email),
    FOREIGN KEY(business_address_id) REFERENCES Address(address_id)
);

CREATE TABLE Categories (
    parent_category TEXT,
    category_name TEXT,
    PRIMARY KEY(parent_category, category_name),
    FOREIGN KEY(parent_category) REFERENCES Categories(category_name)
);

CREATE TABLE Auction_Listings (
    Seller_Email TEXT NOT NULL,
    Listing_ID INTEGER NOT NULL,
    Category TEXT,
    Auction_Title TEXT,
    Product_Name TEXT,
    Product_Description TEXT,
    Quantity INTEGER,
    Reserve_Price TEXT,
    Max_bids INTEGER,
    Status INTEGER DEFAULT 1,
    PRIMARY KEY (Seller_Email, Listing_ID),
    FOREIGN KEY (Seller_Email) REFERENCES Seller(Email)
);

CREATE TABLE Bids (
  Bid_ID INTEGER PRIMARY KEY,
  Seller_Email TEXT NOT NULL,
  Listing_ID INTEGER NOT NULL,
  Bidder_email TEXT NOT NULL,
  Bid_price REAL NOT NULL,
  FOREIGN KEY (Seller_Email, Listing_ID) REFERENCES Auction_Listings (Seller_Email, Listing_ID)
);

CREATE TABLE Transactions (
    Transaction_ID INTEGER PRIMARY KEY,
    Seller_Email TEXT NOT NULL,
    Listing_ID INTEGER NOT NULL,
    Bidder_Email TEXT NOT NULL,
    Date TEXT NOT NULL,
    Payment REAL NOT NULL,
    FOREIGN KEY (Seller_Email, Listing_ID) REFERENCES Auction_Listings(Seller_Email, Listing_ID)
);

CREATE TABLE Rating (
    Bidder_Email TEXT NOT NULL,
    Seller_Email TEXT NOT NULL,
    Date TEXT NOT NULL,
    Rating INTEGER NOT NULL,
    Rating_Desc TEXT NOT NULL,
    PRIMARY KEY (Bidder_Email, Seller_Email, Date),
    FOREIGN KEY (Bidder_Email) REFERENCES Bidder(email),
    FOREIGN KEY (Seller_Email) REFERENCES Seller(email)
);