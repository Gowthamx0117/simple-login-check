# 🔐 Login Check Web App (Flask)

This is a simple **Flask-based login system** that checks credentials (username and password) from an **Excel file**. It's perfect for beginners who want to learn how frontend and backend are connected using Python and Flask.

---

## 📁 Project Structure

```
login_app/
│
├── app.py                  # Main Flask application
├── create_db.py            # Database creation
├── templates/
│   ├── login.html          # Login form
│   ├── success.html        # Shown on successful login
│   └── failure.html        # Shown on login failure
```

---

## 📋 Prerequisites

Make sure Python and pip are installed, then install the required packages:

```bash
pip install flask
```

---

## 📘 How to Use

1. Clone or download this repository
2. Run the app:

```bash
python app.py
```

3. Open your browser and go to:  
   `http://127.0.0.1:5000`

4. Try logging in using credentials stored in `users.xlsx`

---

## 💡 What's Next?

If you'd like to:
- Add registration that updates the Excel file
- Switch to a real database like SQLite or MySQL
- Secure passwords using bcrypt

Just check the issues tab or send a PR!

---

## 🧑‍💻 Author

Built with ❤️ by Gowtham

---
