# Task Manager API

A RESTful API for managing tasks, built with Django REST Framework.

## Features

- Create, read, update, and delete tasks
- Mark tasks as completed
- Input validation
- RESTful endpoints

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd kuraz-taskmanager-backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

## Running the Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

- `GET /` - Welcome page
- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/create/` - Create a new task
- `GET /api/tasks/<id>/` - Get a specific task
- `PUT /api/tasks/<id>/update/` - Update a task
- `DELETE /api/tasks/<id>/delete/` - Delete a task

## Request/Response Examples

### Create a Task

**Request:**
```http
POST /api/tasks/create/
Content-Type: application/json

{
    "title": "Complete project",
    "completed": false
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "title": "Complete project",
    "completed": false,
    "created_at": "2025-06-05T11:30:00Z"
}
```

### Validation Errors

**Request:**
```http
POST /api/tasks/create/
Content-Type: application/json

{
    "title": "",
    "completed": false
}
```

**Response (400 Bad Request):**
```json
{
    "title": ["Title cannot be empty"]
}
```

## Validations

- Title is required and cannot be empty
- Title must be at least 3 characters long
- Completed field is optional (defaults to false)

## Testing

To run tests:
```bash
python manage.py test
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
