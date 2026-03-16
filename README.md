# Tourism Management System

A Django-based web application for managing tourism trips, bookings, and informational pages. This project demonstrates a full-stack Django application with models, views, templates, static files, and user interaction.

## 🛠️ Features

- **Trip Management:** Add, view, and manage trips and destinations.
- **Booking System:** Users can book trips and view booking details.
- **Static Pages:** Home, About, and Contact pages using a separate `pages` app.
- **User Interaction:** Forms for booking and contact.
- **Media & Static Files:** Handles images and CSS/JS for frontend styling.
- **Database:** SQLite used for development; models for trips, bookings, and users.

## 📂 Project Structure
tourism_managment_system/
├── myproject/ # Django project folder (settings, urls, wsgi/asgi)
├── pages/ # Static informational pages
├── trips/ # Core app for trip management
├── templates/ # HTML templates for all apps
├── static/ # CSS, JS, images
├── media/ # Uploaded media files
├── manage.py # Django command-line utility
├── db.sqlite3 # Development database
└── README.md # Project documentation


## ⚡ Installation & Running the Project

1. **Clone the repository:**
```bash
git clone https://github.com/ibad1103/tourism_managment_system.git
cd tourism_managment_system

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver


Open http://127.0.0.1:8000 in your browser.
