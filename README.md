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
   
   git clone <https://github.com/ErbetoMiheretab/kuraz-taskmanager-backend>
   cd kuraz-taskmanager-backend
  

2. Create and activate a virtual environment:
   
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
  

3. Install the required packages:
   
   pip install -r requirements.txt
  

4. Apply migrations:
   
   python manage.py migrate
  

5. Create a superuser (optional, for admin access):
   
   python manage.py createsuperuser
  

## Running the Server


python manage.py runserver


The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

- `GET /` - Welcome page
- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/create/` - Create a new task
- `GET /api/tasks/<id>/` - Get a specific task
- `PUT /api/tasks/<id>/update/` - Update a task
- `DELETE /api/tasks/<id>/delete/` - Delete a task
