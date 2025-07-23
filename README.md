# Hostel Management System

-----

This repository contains the source code for a Hostel Management System, a database project built using the Django framework. The system aims to streamline various operations within a hostel, including student management, room allocation, invoice generation, and attendance tracking.

## Features

  * *Student Profiles*: Manage student information including CMS ID, full name, contact details, guardian information, and room assignments.
  * *Manager Profiles*: Administer manager details with contact and hostel-specific information.
  * *Hostel & Room Management*: Define hostels, their blocks, capacity, and manage individual room details like capacity and current occupancy.
  * *Invoice Generation*: Generate and manage invoices for mess and rent bills.
  * *Out-Pass System*: Track student out-passes with details like duration and reason.
  * *Room Change Requests*: Handle requests for room changes between students.
  * *Room Problem Reporting*: Allow students to report problems within their rooms.
  * *Notice Board*: Display important messages and announcements.
  * *Attendance Tracking*: Record student attendance.
  * *PDF Generation*: Generate PDF invoices using Jinja2 templates and wkhtmltopdf.

-----

## Technologies Used

  * *Django*: Web framework for building the application.
  * *SQLite3*: Default database for development.
  * *Jinja2*: Templating engine for PDF generation.
  * *pdfkit*: Python wrapper for wkhtmltopdf to convert HTML to PDF.

-----

## Setup Instructions

To get this project up and running on your local machine, follow these steps:

### 1\. Clone the Repository

bash
git clone https://github.com/prithvirajmotwani/Hostel-Management-System-SemesterProject.git
cd Hostel-Management-System-


### 2\. Set up a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


### 3\. Install Dependencies

Install the required Python packages:

bash
pip install Django djangorestframework django-filter django-crispy-forms viewflow psycopg2-binary
pip install jinja2 pdfkit


### 4\. Install wkhtmltopdf

For PDF generation functionality, you need to install wkhtmltopdf on your system.
Download it from the official website: [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)

*Note*: After installation, make sure to update the path_wkhtmltopdf variable in mysite/basic_form/make_pdf.py to point to the wkhtmltopdf.exe executable on your system. For example:

python
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe' # Windows example
# path_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf' # Linux/macOS example


### 5\. Database Migrations

Navigate into the mysite directory and apply the database migrations:

bash
cd mysite
python manage.py makemigrations basic_form
python manage.py migrate


### 6\. Create a Superuser (Admin)

Create an administrative user to access the Django admin panel:

bash
python manage.py createsuperuser


Follow the prompts to create your superuser.

### 7\. Run the Development Server

Start the Django development server:

bash
python manage.py runserver


The application will now be accessible at http://127.0.0.1:8000/. You can access the admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials you created.

-----

## Project Structure

  * mysite/: The main Django project directory.
      * db.sqlite3: The SQLite database file (development only).
      * manage.py: Django's command-line utility.
      * basic_form/: The core application for the hostel management system.
          * admin.py: Registers models with the Django admin interface.
          * apps.py: Application configuration.
          * forms.py: Defines Django forms for various models.
          * make_pdf.py: Script for generating PDF invoices.
          * models.py: Defines the database models (Student, Manager, Hostel, Room, Invoices, etc.).
          * trial.html: HTML template used for PDF invoice generation.
          * tests.py: Placeholder for application tests.

-----

## Usage

  * *Admin Panel*: Log in to the Django admin panel (/admin) to manage all registered models, including students, managers, hostels, rooms, invoices, and more.
  * *PDF Generation*: The make_pdf.py script demonstrates how to generate a PDF invoice. You can integrate this functionality into your Django views to dynamically create and serve invoices.

-----

## Contributing

If you'd like to contribute to this project, please feel free to fork the repository, make your changes, and submit a pull request.

-----

## License

[No explicit license provided in the initial README.md or file contents. You might want to add one.]

-----

Let me know if you'd like any specific sections expanded or if you have more details to add\!
