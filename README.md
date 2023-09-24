Django Email Authentication System with Password Reset and Account Activation


This is a Django project that offers email-based account activation and password reset functionalities using Gmail as the email provider. It provides a secure and user-friendly way to manage user accounts in your web application.

Features
User registration with email verification.
Account activation via email link.
Password reset via email link.
User profile management (optional).
Easy integration into existing Django projects.
Installation
To use this Django Email Authentication System in your project, follow these steps:

Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/shahpankaj123/OTP-based-Authentication-System-in-Django 
Change into the project directory:

bash
Copy code
cd OTP-based-Authentication-System-in-Django 
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate
Install the project dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file in the project root and set your Gmail SMTP email and password as environment variables:

env
Copy code
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password
Apply database migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Access the web application at http://localhost:8000 in your browser.

Usage
Register a new user account by providing your email address and a password.

Verify your email address by clicking the link sent to your Gmail account. Check your spam folder if you don't see the email.

Log in with your registered email and password.

If you forget your password, use the "Forgot Password?" link on the login page. You will receive an email with instructions on how to reset your password.

After successfully logging in, you can manage your user profile (if applicable).

Configuration
You can customize and extend this Django Email Authentication System to suit your project's requirements. Some configuration options include:

Adding more user profile fields.
Modifying email templates for account activation and password reset.
Implementing Two-Factor Authentication (2FA).
Integrating with other email providers.
Please refer to the Django documentation for further details on customization.

Contributing
Contributions to this project are welcome! To contribute:

Fork the repository.

Create a new branch for your feature or bug fix:

bash
Copy code
git checkout -b feature-name
Make your changes and commit them:

bash
Copy code
git commit -m "Add feature/fix"
Push your branch to your fork:

bash
Copy code
git push origin feature-name
Create a pull request on the original repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to open issues if you have any questions or encounter any problems while using this Django Email Authentication System. Enjoy enhancing your project's security and user experience!
