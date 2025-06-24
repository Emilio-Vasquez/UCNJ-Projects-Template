**Library Database Project**

**Backend:** Python (Flask/Django)  
**Frontend:** JavaScript (Simple JS is fine, no need for react or Node.js)  
**Database:** Cloud-hosted SQL (Research to find a free cloud host provider)  
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

**Admin Request & Appeal Page (15 points):**

* Users can request to become an admin (if user becomes admin, they must get an admin ID)  
* The request is stored in the ‘Admin\_Requests’ table. There should be a page dedicated to this, once the user has inputted a request a message should be displayed as “Your request has been submitted”. And you guys should be able to review the process and enroll the person as an admin or not. Consider the ‘admins’ to be your ‘librarians’ because they’ll have to the power to remove books from the library dashboard or put in a request for a specific book (you should change these permissions specifically for those who are considered ‘admin’ compared to regular members).  
* Admin’s should also have another page visible to them (members shouldn’t be able to see this page). That page would be the ‘Request book’ page, where they can put in a request to get a specific book, by providing the ISBN number, the price, the title of the book and the authors

**Library Dashboard & Search System (50 points):**

* Shows all Available books (There should be a ‘Books’ table to extract this information)  
* Checked-out books (This should be only visible to the ‘admins’, and this would be information taken from your ‘Transaction’ table).  
* Overdue books (marked red, and again this should only be visible by the ‘admins’)  
* Filters (Title, author, ISBN, categories, years, available (i.e. there’s still a copy left for them to take))  
* Search books by the title, author, isbn, or category.  
* Admins should also be able to see a list of Library Members (by name and ID)  
* Admins should also be able to see a list of transactions (by member/book)  
* And you should use the MySQL ‘LIKE’ Operator for flexible keyword matching.

**Book Borrowing & Returning (20 points):**

* User can select a book to borrow, if available then the book is assigned to their member ID  
* If the book is already checked out by that specific member ID then tell them they can’t take out two copies of the same book (they can get another copy of the book once they’ve returned it).  
* Set a due date automatically as soon as they take it out, maximum 14 days.  
* Set the number of that specific book available to be \-1. If it’s at 0 copies available, leave it still on display but make the ‘0’ red. If the number of copies available hits 0, then a user cannot take out this specific book.  
* You need to put at least 25 different books on display. The number of copies available can vary.  
* If an admin wants to take out a book because there are 0 copies available, they should have a button that ONLY they can see, and be able to press it to take the book out of the library dashboard.  
* When a member returns a book, the number of this specific book available should be increased by 1\.  
* Members CAN NOT borrow more than 5 books at once.  
* Once a member has borrowed a book, an email should be sent to their email confirming that they’ve borrowed this book and is expected to be returned at a certain date (14 days).  
* Late returns are flagged, and an email should be sent to the users who failed to return the book, telling them that their return is late.

**SQL Queries at end (20 points):**

* I want to see all the books available in the library  
* Find all the books written by a specific author  
* Get the total number of books in the library that are sci-fi  
* Show all members who have borrowed at least one book  
* Get a list of overdue books  
* I want to see how many members are admin.  
* Find the most borrowed book  
* Find members who borrowed more than 3 books  
* Get a list of books that have never been borrowed  
* Find the member who has borrowed the most books and is considered an ‘admin’  
* Find the average number of books borrowed per member.

**Share the screenshots of your queries, and the results.**

**The group must divide the work amongst yourselves, and use GitHub as a way to merge your work.**

**There is a total of 125 points.**

**This project is due May 8th, you will present the project in class. You MUST describe what your code is doing, and it’s functionality, specifically the Python, SQL, and JavaScript statements.**