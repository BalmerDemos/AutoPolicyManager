# AutoPolicyManager

**Description**
Auto Policy Manager is a web application built with Django that provides an interface to manage car-related information, insurance policies, and car models. This project includes features like displaying car details, updating car information, and managing insurance policies.

It also includes an **admin interface** for easy management of car makes, models, and insurance policies, as well as a **user-friendly front-end** for displaying a list of cars and details with dynamic data fetching. The project is backed by a PostgreSQL database and is designed to help users manage car and insurance data in a structured and scalable way.

While currently focusing on core functionality, this project lays the groundwork for potential future enhancements, such as adding more complex features or integrating with other systems.

---

### Table of Contents
1.  [Installation](#installation)
2.  [Usage](#usage)
3.  [Features](#Features)
4.  [Endpoints](#Endpoints)
5.  [Available Endpoints](#AvailableEndpoints)
6.  [Folder Structure](#FolderStructure)
7.  [Database](#Database)
8.  [License](#License)
9.  [Contributing](#contributing)
10. [Disclaimer](#disclaimer)

--- License

### Installation

1. Clone the repository:
    ```bash
   https://github.com/BalmerDemos/AutoPolicyManager


    ```

2. Install the required dependencies: YOU NEED TO HAVE PYTHON PRE-INSTALLED.
    ```bash
    pip install -r requirements.txt
    ```

   **Current Dependencies**:
    - asgiref==3.8.1
    - Django==5.1.4
    - psycopg2==2.9.10
    - sqlparse==0.5.3
    - tzdata==2024.2
---

### Usage

# Create a virtual environment - option to run the project.
- python -m venv manager_env
- manager_env\Scripts\activate
- pip install -r requirements.txt

# Install package in the virtual environment.
- pip install django
- pip install psycopg2
- python.exe -m pip install --upgrade pip - just if needed.
- pip install -r requirements.txt

1. **Use the AutoPolicyManager project**:
   Clone the repository using the following command:
   ```bash
   git clone https://github.com/your-username/AutoPolicy.git
   cd AutoPolicy

2. **Run the application**:
Start the Django development server using:
- python manage.py runserver <port_number>
- Replace <port_number> with the desired port (e.g., 5000).

# Application Pages
1. **Index Carousel**:
URL: http://127.0.0.1:5000/
Displays a static list of cars defined in index.html using a carousel.
Technologies used: Python, Django, PostgreSQL.

2. **Car Details**:
URL: http://127.0.0.1:5000/cars
Displays a dynamic list of cars fetched from the "Car" table using raw SQL statements.

3. **Car Details by ID (Join Query Across Tables)**:
URL: http://127.0.0.1:5000/car-detail/2/
Displays detailed information for a selected car. Data is fetched using a SQL JOIN across the "Make," "Model," "Car," and "InsurancePolicy" tables.

4. **Car Update**:
URL: http://127.0.0.1:5000/update-details/2/
Displays a form to update the car's details, where only the "color" field is editable.

5. **Car Update Success**:
URL: http://127.0.0.1:5000/update-success/2/
Shows the updated field for the selected car. The updated information is passed using a session variable.

6. **Delete Successful**:
URL: http://127.0.0.1:5000/delete-success/8/
Displays the ID of the successfully deleted car.

# Features
**Static and Dynamic Car Displays**:
Static list of cars on the index page.
Dynamic list of cars fetched from the database using raw SQL statements.

**Detailed Car Information**:
View details of a selected car with a SQL JOIN query across multiple tables.

**Car Update Functionality**:
Update specific details (e.g., color) of a car.

**Session-Based Success Messages**:
Session variables are used to display update success messages.

**Car Deletion**:
Successfully delete a car and display its ID.

# Endpoints
- Endpoints
- Index Page: /
- Car List: /cars
- Car Details by ID: /car-detail/<id>/
- Car Update: /update-details/<id>/
- Update Success: /update-success/<id>/

# Available Endpoints

**GET /cars/**
Retrieves a list of all cars.

**GET /car-detail/<id>/**
Fetches detailed information for a specific car by ID.

**POST /update-details/<id>/**
Updates the "color" field for a specific car.

**GET /update-success/<id>/**
Displays a confirmation message for a successful update.

**DELETE /delete-success/<id>/**
Deletes a specific car by ID and confirms deletion.
Removes an item from the database.

# Folder Structure
AutoPolicyManager/
static/app.css
templates/base and 404 html
car_app/
    __init__.py
    admin.py      # Admin interface configuration
    forms.py
    models.py
    urls.py
    views.py
    static/images/
    templatees/car_app/

AutoPolicyManager/
# Root project folder
static/ # Static assets folder
app.css # Global styles for the application
templates/
# Global templates folder
base.html
# Base template for consistent layout
404.html # Custom 404 error page
car_app/ # Main Django app for managing cars and policies
init.py
# Python package initializer
admin.py
# Admin interface configuration
forms.py
# Form definitions for the app
models.py
# Models representing database tables
urls.py
# URL routes for the app
views.py
# Application views (business logic)
static/
# App-specific static assets
images/
# Images specific to the app
templates/
# App-specific templates
car_app/
# Templates specific to the car_app
manage.py
# Django's command-line utility for administrative tasks

# Database Configuration

The application uses **PostgreSQL** as the database engine. Configure the `DATABASES` setting in your `settings.py` file as follows:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'YOUR_DATABASE_NAME',   # Replace with your database name
        'USER': 'postgres',             # PostgreSQL username
        'PASSWORD': 'YOUR_POSTGRESQL_PWD',  # Replace with your PostgreSQL password
        'HOST': 'localhost',           # Address of your PostgreSQL server
        'PORT': '5432',                # Default PostgreSQL port
    }
}

# Dummy data - Use Admin
Make table
1	"Toyota"
2	"Honda"
3	"Ford"
4	"Chevrolet"
5	"Tesla"

Model Table
1	"Corolla"	2022	1
2	"Camry"	    2021	1
3	"Civic"	    2023	2
4	"Accord"	2022	2
5	"Mustang"	2021	3

Car Table
3	"2FTRX18W1XCA12345"	"Black"	3
4	"4FTRX18W1XCA42365"	"Black"	4
5	"1FAFP4048WF123456"	"Blue"	5
2	"1HGBH56JXMN109198"	"White"	2
1	"1HGBH41JXMN109186"	"White"	1

Insurancepolicy Table
1	"POL123456789"	"Allstate Insurance"	"Full Coverage"	"2025-12-31"	1
2	"POL987654321"	"Geico Insurance"	"Liability Only"	"2026-06-30"	2
3	"POL457654321"	"Geico Insurance"	"Liability Only"	"2025-06-30"	3
4	"POL657654321"	"Geico Insurance"	"Liability Only"	"2025-06-30"	4
5	"POL757654321"	"Geico Insurance"	"Liability Only"	"2025-06-30"	5

# Notes:
- Ensure PostgreSQL is installed and running on your system.
- Replace placeholders like YOUR_DATABASE_NAME and YOUR_POSTGRESQL_PWD with actual values
- Run migrations after setting up the database configuration to create the necessary tables

# Create Admin User
- Open a terminal or command prompt and run:
- python manage.py createsuperuser
- Username: demos
- Email: demos@test.com
- Password: admin12345 After this, you can log in at http://127.0.0.1:5000/admin/.

# Add Dummy Data Using Admin Interface
- Once you've logged into the Django admin interface, you can manually add the dummy data into the respective tables:

# Make table
1	"Toyota"
2	"Honda"
3	"Ford"
4	"Chevrolet"
5	"Tesla"

# Model Table (relates to Make):
1	"Corolla"	2022	1
2	"Camry"	    2021	1
3	"Civic"	    2023	2
4	"Accord"	2022	2
5	"Mustang"	2021	3

# Car Table (relates to Model):
3	"2FTRX18W1XCA12345"	"Black"	3
4	"4FTRX18W1XCA42365"	"Black"	4
5	"1FAFP4048WF123456"	"Blue"	5
2	"1HGBH56JXMN109198"	"White"	2
1	"1HGBH41JXMN109186"	"White"	1

# InsurancePolicy Table
1	"POL123456789"	"Allstate Insurance"	"Full Coverage"	"2025-12-31"	1
2	"POL987654321"	"Geico Insurance"	"Liability Only"	"2026-06-30"	2
3	"POL457654321"	"Geico Insurance"	"Liability Only"	"2025-06-30"	3
4	"POL657654321"	"Geico Insurance"	"Liability Only"	"2025-06-30"	4
5	"POL757654321"	"Geico Insurance"	"Liability Only"	"2025-06-30"	5

After completing these steps, your dummy data will be ready for testing in the admin interface.


**SECURITY WARNING**: keep the secret key used in production secret!
# For this demo project, the SECRET_KEY is included for convenience.
# In a real-world project, replace 'YOUR_SECRET_KEY_SHOULD_BE_HERE' with an actual secret key,
# and store it securely using environment variables or a .env file.


# License

MIT License

Copyright (c) 2024 [Developed by user Balmer Valencia]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Contributing
Feel free to clone the repository for your own enhancements or bug fixes! Cloning allows you to create a local copy of the project, where you can experiment and make changes without affecting the original repository. If you're unsure how to clone a repository, you can follow a simple guide on the process

# Disclaimer
Please note that this project is for educational purposes only. Any use of the code or information provided is at your own risk.
--------------------------------------------------------------------------------------------------------------
Hey everyone! To all my amazing peers in the second year at Universidad Autónoma De Occidente, I’m excited to share this project with you! I hope you find it super useful and that it sparks some inspiration for your own work. Let’s learn and grow together!

If you have any questions or need assistance, feel free to reach out. Happy coding!

