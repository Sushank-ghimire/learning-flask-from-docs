# Flask User Authentication App

This is a simple web application built using Flask to demonstrate basic user authentication features, including registration, login, and user dashboards. Users can register, log in, and view their dashboard once authenticated.

## Features

- **User Registration**: Allows users to sign up by providing a username, email, and password.
- **User Login**: Allows registered users to log in using their email and password.
- **Dashboard**: After successful login, users are redirected to their personalized dashboard.
- **Session Management**: Uses Flask's session to manage logged-in users and maintain their authentication status across pages.
- **User Management**: Admin users can view a list of all registered users in the admin dashboard.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **HTML/CSS**: Basic structure and styling of the web pages.
- **TailwindCSS**: A utility-first CSS framework for styling.
- **Flask Sessions**: Used to store the current user's login state.
- **Flash Messages**: For displaying success, error, and informational messages.

## File Structure

```
flask_user_app/
│
├── app.py                # Main Flask application file
├── users.txt             # File that stores registered user data (username, email, password)
├── templates/
│   ├── index.html        # Home page
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── dashboard.html    # User dashboard page
│   ├── about.html        # About page
│   └── contact.html      # Contact page
└── static/
    └── styles.css        # Custom styles (optional, Tailwind used for most styles)
```

## Setup

### 1. Install Dependencies

Make sure you have Python 3.x installed, then install Flask and other required dependencies using `pip`:

```bash
pip install flask
```

### 2. Run the Application

After installing the required dependencies, you can run the application using the following command:

```bash
python app.py
```

This will start a local development server at `http://127.0.0.1:5000/`.

### 3. Access the App

Once the server is running, you can access the app by navigating to the following URLs in your browser:

- **Home page**: `http://127.0.0.1:5000/`
- **Login page**: `http://127.0.0.1:5000/login`
- **Register page**: `http://127.0.0.1:5000/register`
- **Dashboard page**: `http://127.0.0.1:5000/dashboard` (requires login)
- **About page**: `http://127.0.0.1:5000/about`
- **Contact page**: `http://127.0.0.1:5000/contact`

### 4. Register a New User

To register, go to the **Register** page, fill in your details, and submit the form. Once you’re registered, you can log in with the credentials you just created.

### 5. Logging In

After registration, go to the **Login** page and use your credentials to log in. If the login is successful, you will be redirected to your dashboard.

### 6. User Logout

To log out, go to the **Logout** route, which will log the user out and redirect them to the home page.

## Routes

- **`/`**: Home page
- **`/login`**: User login page (GET and POST methods)
- **`/register`**: User registration page (GET and POST methods)
- **`/dashboard`**: Admin dashboard to view all registered users (Requires login)
- **`/about`**: About page
- **`/contact`**: Contact form page
- **`/logout`**: Logs out the current user

## Error Handling

- **Login Errors**: If the email or password is incorrect, a flash message will inform the user.
- **Duplicate User Registration**: If the email is already in the database, the user will be notified.
- **Unauthorized Access**: If the user tries to access the dashboard without logging in, they will be redirected to the login page.

## Customization

You can customize the app by:

- Updating the HTML templates inside the `templates/` folder.
- Modifying the design with TailwindCSS or custom CSS.
- Adding more functionality like email verification, password reset, etc.

## Contributing

Feel free to fork the project, make changes, and create pull requests. Contributions are always welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).