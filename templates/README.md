# 📘 Expense Tracker Web App

## 👥 Team Members
- Rathnanjali, Abdulah Parveen, Sakthi, Swathi (Final-year MCA Students) 

---

## 📝 Project Overview
**Expense Tracker** is a lightweight web application built with **Flask** that helps users record and manage their daily expenses.  
Instead of using a database or cloud storage, this project stores data locally in **CSV files**, making it simple, fast, and ideal for offline use.  

The app provides:
- A **signup form** to register users (stored in `users.csv`)
- An **expense submission form/API** to record expenses (stored in `expenses.csv`)
- A **viewer** to display stored expenses
- Multiple categorized pages for navigation (Start, Category, Accounts, Currency, Disclaimer)

---

## ⚙️ Technologies Used
- **Python 3.14.2**
- **Flask (Web Framework)**
- **HTML/CSS (Frontend Templates)**
- **CSV (Data Storage)**

---

## 📁 Project Structure
Expense Tracker/
│
├── app.py                   # Main Flask application
├── connectsheet.py          # CSV utility functions
├── storeexcel.py            # Signup data storage
├── expenses.csv             # Expense records
├── users.csv                # Signup records
├── templates/              # HTML templates
│   ├── demo.html
│   ├── start.html
│   ├── category.html
│   ├── accounts.html
│   ├── currency.html
│   └── dis.html
└── static/      
    |-  📁 images
    |- demo.css
    |- demo.js          # CSS or JS files

