# FastAPI Expense Tracker

This project is an Expense Tracker API built using FastAPI. It allows users to register, log in, and manage their expenses. The API provides endpoints for creating, retrieving, updating, and deleting expenses, as well as analytics on spending.

## Project Structure

```
expense-tracker
├── src
│   ├── main.py          # Entry point for the FastAPI application
│   ├── models.py        # SQLAlchemy models for User and Expense
│   ├── schemas.py       # Pydantic models for data validation
│   ├── database.py      # Database connection setup
│   ├── auth.py          # Authentication functions
│   └── tests
│       └── test_main.py # Unit tests for the application
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables
├── .gitignore            # Files to ignore in Git
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd expense-tracker
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables

Create a `.env` file in the root directory and add the following variables:

```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./expenses.db  # Change to your database URL
```

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn src.main:app --reload
```

## API Endpoints

- **POST /register**: Register a new user.
- **POST /login**: Log in and receive a JWT token.
- **POST /expenses**: Create a new expense.
- **GET /expenses**: Retrieve a list of expenses.
- **GET /expenses/{expense_id}**: Retrieve a specific expense by ID.
- **PUT /expenses/{expense_id}**: Update an existing expense.
- **DELETE /expenses/{expense_id}**: Delete an expense.
- **GET /analytics/summary**: Get a summary of expenses by category.

## Testing

To run the tests, navigate to the `src/tests` directory and run:

```bash
pytest test_main.py
```

## License

This project is licensed under the MIT License.