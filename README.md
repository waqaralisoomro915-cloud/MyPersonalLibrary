# 📚 Django Book Management System

## 📌 Project Overview

This is a Django-based web application designed to manage book-related data, including:

* User contact messages
* Book requests
* Favorite books updates
* Newly arrived books

The system provides a simple backend structure for storing and managing book information efficiently.


## 🚀 Features

* 📩 Contact form to collect user messages
* 📖 Book request system
* ❤️ Favorite books management
* 🆕 New arrival books listing
* 🗂️ Structured database using Django ORM

## 🛠️ Technologies Used

* Python
* Django
* SQLite (default database)
* HTML/CSS (Frontend)

## 📂 Models Description

### 1. Contact

Stores user contact information:

* First Name
* Last Name
* Email
* Phone
* Subject
* Message

### 2. RequestBook

Stores user book requests:

* Title
* Author

### 3. FavouriteBooksUpdate

Stores favorite book details:

* Title
* Author
* Image (URL)
* About
* Opinion

### 4. ArrivalBooks

Stores newly arrived books:

* Title
* Author
* Description
* Image (URL)


## 📌 Notes

* Ensure all fields are properly validated in forms.
* Use meaningful class naming conventions (e.g., `RequestBook` instead of `requestbook`).

---

## 👨‍💻 Author

Developed as part of a Django learning/project implementation.

---

## 📄 License

This project is open-source and available for educational purposes.
