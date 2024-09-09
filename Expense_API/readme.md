# Expense Tracker API

The Expense Tracker API is a Flask-based application that allows users to manage their expenses. It provides features for user authentication, creating, reading, updating, and deleting expenses, as well as filtering expenses by time frame.

## Features

- User registration and authentication using JWT tokens.
- CRUD (Create, Read, Update, Delete) operations for expenses.
- Filtering expenses by time frame (past week, past month, last 3 months, custom date range).
- Expense categories (Groceries, Leisure, Electronics, Utilities, Clothing, Health, Others).

## Installation

1. Ensure you have Python 3 and the required dependencies installed:

   - Flask
   - Flask-SQLAlchemy
   - Flask-JWT-Extended

2. Clone the repository and navigate to the project directory:

   ```
   git clone https://github.com/LucaGini/Projects/Expense_API.git
   cd expense-tracker-api
   ```

3. Set the `JWT_SECRET_KEY` environment variable to a secret key of your choice:

   ```
   # Windows
   set JWT_SECRET_KEY=your_secret_key

   # macOS/Linux
   export JWT_SECRET_KEY=your_secret_key
   ```

4. Run the Flask application:

   ```
   python expense_api.py
   ```

   The API will be available at `http://localhost:5000`.

## API Endpoints

- `POST /register`: Register a new user.
- `POST /login`: Login an existing user and obtain an access token.
- `GET /expenses`: Fetch the user's expenses, with optional filtering by time frame.
- `POST /expenses`: Create a new expense.
- `PUT /expenses/<int:expense_id>`: Update an existing expense.
- `DELETE /expenses/<int:expense_id>`: Delete an existing expense.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
