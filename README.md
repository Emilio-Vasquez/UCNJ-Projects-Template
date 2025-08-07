# **UCNJ Projects Template**

This repository provides a **starter template** for full-stack Python Flask projects, along with a folder containing **instructional documents** used for Computer Science and Database classes at Union College of Union County, NJ.

---

## **Folder Structure**

```
UCNJ-Projects-Template/
├── Template/
|   ├── app/
|   |   ├── __init__.py
|   |   ├── db.py
│   |   ├── login.py
│   |   ├── register.py
│   |   ├── routes.py
│   │   ├── VirtualEnv/
│   │   │   └── README.md # Placeholder file to give instructions on virtual Environments
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   └── ucnj_style.css
│   │   │   ├── images/
│   │   │   │   └── favicon.ico
│   │   │   ├── js/
│   │   │   │   ├── flash.js
│   │   │   │   ├── login.js
│   │   │   │   ├── register.js
│   │   │   │   └── reset_password.js
│   │   ├── templates/
│   │   │   ├── base.html # Main layout used by all pages
│   │   │   ├── index.html # Homepage
│   │   │   ├── login.html
│   │   │   ├── registration.html
│   │   │   ├── feedback.html
│   │   │   └── about.html
│   ├── database/
│   │   └── schema.sql
│   ├── .env
│   ├── .gitignore
│   ├── config.py
│   ├── README.md
│   ├── requirements.txt
│   └── run.py
├── Tutorials/ 
├── docs/
└── README.md
```

## **How to Use**

- Use the `Template/` folder to **kickstart your web project** — it includes base HTML, routing, static files, and a virtual environment guide.
- Refer to the `docs/` folder for **project instructions and guides** related to Python, Flask, SQL, and full-stack development.
- Clone the repository and duplicate or rename the `Template/` folder for each new project.

---

## **Notes**

- The `Template/VirtualEnv` folder includes a `README.md` with setup instructions for creating and managing virtual environments.
- `.gitignore` is already configured to skip virtual environments and sensitive `.env` files.
- You’re free to customize the starter files and instructional documents as needed for your class or project.

---

Created for educational use at **Union College of Union County, NJ**.

Developed and maintained by **Prof. Emilio Vasquez**.