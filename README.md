# AgriSense – Agricultural Management System

## Project Overview
AgriSense is a Django-based Agricultural Management System designed to help farmers manage their agricultural activities digitally.

## Technologies Used
- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** MySQL
- **Development Environment:** PyCharm
- **Version Control:** Git and GitHub

## Key Features
- Farmer Registration and Login
- Farmer Dashboard
- Crop Management
- Crop Details and Tracking
- Expense Management
- Crop Sales Management
- Farmer Profile Management

## Database
MySQL database: `agri_sense`

## Project Structure
- `accounts/` – User authentication and account management
- `farm/` – Agricultural and crop management
- `templates/` – HTML templates
- `static/` – Static files
- `AgriSense/` – Django project configuration
- `manage.py` – Django management utility

## Installation and Setup

1. Clone the repository:
   `git clone https://github.com/prathap-08/AgriSense.git`

2. Navigate to the project directory:
   `cd AgriSense`

3. Create a virtual environment:
   `python -m venv .venv`

4. Activate the environment:
   ` .venv\Scripts\activate `

5. Install dependencies:
   `pip install -r requirements.txt`

6. Configure your MySQL database credentials in Django settings.

7. Run migrations:
   `python manage.py migrate`

8. Start the development server:
   `python manage.py runserver`

9. Open `http://127.0.0.1:8000/` in your browser.

## Author
Prathap Otooru

## GitHub Repository
https://github.com/prathap-08/AgriSense