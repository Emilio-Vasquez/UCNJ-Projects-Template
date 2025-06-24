**Python Project**

**Backend:** Python (Flask/Django)  
**Frontend:** JavaScript (Simple JS is fine, no need for react or Node.js)  
**Database:** MySQL works \- Make sure your local DBMS are the same to avoid version errors  
**Email Sender:** Google SMTP

**User Registration & Email Verification (20 points):**

* User register by entering:  
  * Username (5+ characters long, checked for availability with JS and Python)  
  * Password (8+ characters, 1 uppercase, 1 lowercase and 1 symbol is required, checked if legitimate or not through JS and Python again)  
  * Email (Must be unique, logic is done though JS and Python checks with the database)  
  * Users must also be given a member ID.  
  * All of these things will be stored inside of your database for each unique user, and you have to encrypt the password.  
* If the username, password and email is valid, send a link to verify they want to sign up.  
  * If user is not verified, they will NOT be permitted to login, tell them to verify their login.  
  * If the user is verified, then they can login, make sure to keep track of who’s verified and who’s not.

**Customer Dashboard & Search System (50 points):**

* Display all available products or services relevant to the project theme.  
* Provide filters and search functionality: search by name, category, or identifier (i.e. the product ID for the specific item, you’ll have multiple items)  
* Filters should allow you to filter by attribute (i.e. price, rating, availability)  
* Customers should be able to view and interact with what your website has to offer

**Transaction & Purchase System (20 points):**

* Users can interact with system content to purchase items, book services or submit orders (specific to your project theme).  
* Each user should get a certain amount of money generated from $50 to $1500. This will be their balance.  
* Each time the user purchases something, take away that much money from their balance, if they’re going to go below $0 on a purchase, then the purchase CAN NOT go through. There shouldn’t be any person owing money.  
* Upon successful purchase, there must be a confirmation email generated and sent to the user.

**Additional Features (20 points):**

* Some websites aren’t primarily created for business purposes. So everyone should add at least 3 additional pages specific to your project theme.

**Presentation (30 points):**

* **You MUST describe what your code is doing, and it’s functionality, specifically the Python, and JavaScript**

**The group must divide the work amongst yourselves, and use GitHub as a way to merge your work.**

**There is a total of 140 points.**

**AI Policy:**

**You’re allowed to use AI. I do not recommend you become over-reliant on AI, but it can be very useful to you, as long as you’re using it correctly.**

**REMEMBER, you will need to present your code, and I will grade the last portion ‘Presentation’ harshly, if you don’t know what your code is doing, how it’s being linked and how each function you create works, I will take off points.**

**This is your chance to create something unique, if you didn’t implement somethings but you explained your code well and gave a thorough presentation and a concrete flow on your implementation process I will be forgiving. Because what I truly care about, is how much and what you are learning.**

**This project, and this whole course as a matter of fact is just a grade. A grade that doesn’t mean anything to employers. What they care about is what you know and how you can apply what you know, into real life.**

**Work hard, learn, apply yourself and your efforts will be recognized.**