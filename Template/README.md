# **UCNJ Flask Full-Stack Starter Template**

This is a ready-to-use Flask full-stack starter project designed for instructional use at Union College of Union County, NJ. It includes a clean HTML structure using Jinja2 templating, a Flask app starter (`app.py`), and linked static assets (CSS, JS, images). Ideal for beginner to intermediate web application projects in a multi-page format.

---

## **Project Structure**

```
Template (you should rename this folder to your own specific project)/
├── app.py
├── .env # For environment variables (e.g., secret keys)
├── .gitignore # Hides .env and virtual environment from Git
├── requirements.txt # Add Python packages here, you can freeze your environment and pipe the libraries into this file
├── VirtualEnv/ # (Recommended) Virtual environment folder, you can rename it or create a new one: python -m venv MyVenv
│
├── templates/
│ ├── base.html # Main layout used by all pages
│ ├── index.html # Homepage
│ ├── login.html # (Placeholder for specific project instructions)
│ ├── registration.html# (Placeholder for specific project instructions)
│ ├── feedback.html # (Placeholder for specific project instructions)
│ └── about.html # (Placeholder for specific project instructions)
│
├── static/
│ ├── css/
│ │ └── styles.css # Custom styles
│ ├── js/
│ │ └── script.js # JavaScript logic
│ └── images/ # Static image assets
```

## **Setup Instructions**

1. **Clone the repository**

   ```bash
   git clone https://github.com/Emilio-Vasquez/UCNJ-Projects-Template.git
   
   cd UCNJ-Projects-Template
   ```

   - This command will re-create the GitHub's template into your local computer.
   - The `cd UCNJ-Projects-Template` command changes the directory, to go inside of the new folder created named 'UCNJ-Projects-Template'.

2. **Create a virtual environment**

   ```bash
   python -m venv VirtualEnv # or python3 for macOS/Linux
   
   source VirtualEnv/bin/activate  # or VirtualEnv\Scripts\activate on Windows
   ```

   - If you want a full breakdown of virtual environments and their use, go to `Template/VirtualEnv/README.md`

3. **Install dependencies**
    - *Once pakcages are installed, you can populate the requirements.txt using `pip freeze > requirements.txt`*
    - If you want a full breakdown of pip freeze and the requirements.txt file go to the bottom of: `Template/VirtualEnv/README.md`.

4. **Run the app**

   ```bash
   python app.py
   ```
   - Or if you've already set up flask: `flask run`.

## **Understanding HTML, JavaScript, CSS, and Flask**

Flask is a lightweight **Python web framework** used to build web applications. To create a complete and functional website, Flask works alongside:

- **HTML (HyperText Markup Language)**  
  This is the **structure** of your website. It defines the elements you see on the page—text, buttons, forms, etc. HTML files live in the `templates/` folder and use **Jinja2 templating** to dynamically inject Python data from Flask into the HTML.

- **CSS (Cascading Style Sheets)**  
  CSS controls the **appearance** of the HTML elements—fonts, colors, layout, spacing, and responsive design. CSS files go inside `static/css/` and are linked in the HTML `<head>` section.

- **JavaScript (JS)**  
  JavaScript adds **interactivity and behavior** to your page. Things like button clicks, form validation, and dynamic updates without refreshing the page are handled by JS. Scripts live in `static/js/` and are linked at the bottom of HTML files.

- **Flask (Python)**  
  Flask is the **back-end logic**. It receives browser requests, processes them (checking a login), fetches data from a database if needed, and returns HTML pages or JSON responses.

Together:
- Flask renders the HTML (`templates/*.html`)
- HTML loads CSS and JS from the `static/` folder
- JavaScript can send/receive data from Flask using routes (AJAX or form submissions)
- Flask connects to databases and passes that data into templates

---

## **For Databases**

If your project requires storing or retrieving data (users, feedback, products, typically I will only have this section for my database course), you will need a **database**.

### Where Does the Database Go?
- You’ll typically create or connect to a database in your **Flask app (e.g., `app.py`)**.
- Use libraries like `sqlite3`, `SQLAlchemy`, or `PyMySQL` to connect and query your database (Since we'll be working with SQL).
- Flask can read data from the database and pass it into an HTML page via Jinja2 templates.

### How It Connects:
1. A route in `app.py` receives a request (e.g., a user submits a form).
2. Flask processes the input and connects to the database.
3. It runs a SQL query (like INSERT or SELECT).
4. The result is sent to the HTML template and rendered for the user.

**Typical flow**:
```
Browser ⟶ Flask (Python logic) ⟶ Database ⟶ Flask ⟶ HTML (template with data) ⟶ Browser
```

If you’re using SQLite:
- Your `.db` file can live in your project root (same level as `app.py`).
- Example: `mydatabase.db`

We will be using another DBMS (called MySQL), you’ll typically configure it in your `.env` file and use Python code to connect. However, using other DBMS is allowed.

---