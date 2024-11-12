# drf-api

---
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white)![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON-web-tokens&logoColor=white)


This is a simple Django REST framework project with user authentication, post creation, liking functionality, and analytics. It provides a basic CRUD operations, liking posts, and viewing analytics based on likes over a date range.

## Features

- **User registration** and JWT-based authentication.
- **Post management** with the ability to create, update, delete posts.
- **Like functionality** for posts.
- **Analytics** showing the number of likes on posts within a specific date range.

## Requirements

- Python 3.11.0
- Django 5.1.3
- Django REST Framework
- Simple JWT
- SQLite (default database)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/barabarinov/drf-api.git
   
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3.	Install dependencies:

   ```bash
   pip install -r requirements.txt
   
4.  Set up environment variables:

   Create a `.env` file in the project root and add your `SECRET_KEY`:

   ```bash
   SECRET_KEY=<your-secret-key>
   
5.	Run migrations to set up the database:

   ```bash
   python manage.py makemigrations
   ```
   ```bash
   python manage.py migrate

6.	Create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   
7.	Start the development server:

   ```bash
   python manage.py runserver

## API Endpoints

### User Registration and Authentication

- `POST /api/users/register/`: Register a new user.
- `POST /api/users/token/`: Get JWT access token.
- `POST /api/users/token/refresh/`: Refresh the JWT access token.
- `POST /api/users/token/verify/`: Verify the validity of a given JWT access token.

### Post Endpoints

- `GET /api/posts/`: List all posts.
- `POST /api/posts/`: Create a new post (requires authentication).
- `GET /api/posts/<post_id>/`: Retrieve a single post.
- `PUT /api/posts/<post_id>/`: Update a post's content (requires authentication).
- `PATCH /api/posts/<post_id>/`: Partially update a post's content (requires authentication).
- `DELETE /api/posts/<post_id>/`: Delete a post (requires authentication).
- `POST /api/posts/<post_id>/like/`: Like a post (requires authentication).

### Analytics

- `GET /api/posts/analytics/`: Get analytics on likes within a date range. Example: `/api/posts/analytics/?date_from=2024-01-01&date_to=2024-12-31`.
