Overview
:

This project is a Django-based login page that captures user login details and saves the username, password, and cookies (while excluding the email) to a login_file.txt file. This README provides instructions on how to start the project, run the server, and customize the log file location if needed.

Table of Contents

1. Getting Started

2. Project Structure
3. 
Setup and Installation
4. 
Running the Project

5. Customizing the Log File Directory
6. 
Testing the Login Functionality
7. 
Project Notes

Getting Started
:

Ensure you have Python 3 and Django installed. We recommend creating a virtual environment to manage project dependencies.

Project Structure:


1. The main components of this project include:

 * home/ - Contains views, templates, and static files for the login page.
 * 
login_file.txt - This file logs the username, password, and cookies from user login. This file’s location can be customized (see instructions below).


Setup and Installation
:

 * Install Required Libraries:
Install the libraries needed for this project by running:
 - pip install django

 *Apply Migrations:
  -python manage.py migrate

Running the Project:


 To start the Django development server, use the following command:
 - python manage.py runserver
The server will run at http://127.0.0.1:8000/. You can access the login page by navigating to this URL in your web browser.

Customizing the Log File Directory
:

 * The login information is saved to login_file.txt in the home directory by default. To change this:
1. Open views.py in the home app.
2. Modify the file_path variable as follows:

 - file_path = os.path.join("your/custom/path", "login_file.txt")
3. Replace "your/custom/path" with the desired directory path.
Ensure the Django application has write permissions to the specified directory.

Testing the Login Functionality:


1. Enter a username, password, and email on the login form.
2. Click Next.
3. 
If the login is successful, your details will be logged in login_file.txt, excluding the email.
4. 
You will be redirected to the specified project URL: https://myproject-finals.edu.ph/.


Project Notes:


  * CSRF Protection: 
Ensure CSRF tokens are included in forms for secure submissions.

  * Cookie Handling: 
Cookies are recorded from the user’s session for potential security and tracking purposes.


Contact:

 * If you have any questions or need further assistance, please feel free to reach out.

Enjoy working with the Django Login Project!