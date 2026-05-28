The Secure Login Web Application is developed using Python Flask, SQLite, HTML, and CSS to provide a safe and user-friendly authentication system. The application allows users to register by creating a username and password through the registration page. Before storing the password in the database, the system encrypts it using Flask-Bcrypt hashing, ensuring that passwords are never stored in plain text. 
This improves security and protects user credentials from unauthorized access.
After registration, users can log in through the login page by entering their credentials. 
The application securely verifies the entered password with the hashed password stored in the SQLite database. 
If the authentication is successful, Flask session management is used to create a secure user session, allowing access to the protected home page.
The home page displays a personalized welcome message and provides a logout option to safely end the session.
The application also includes protection against SQL injection attacks by using parameterized SQL queries instead of directly inserting user inputs into database commands. 
Input validation ensures that required fields are properly filled before submission.
The frontend is designed using HTML and CSS with a clean, responsive, and visually appealing interface for better user experience.
Overall, the project demonstrates a complete secure login system with user registration, encrypted password storage, authentication, session management, logout functionality, and basic web security practices to protect user accounts and sensitive information from common cyber threats.
