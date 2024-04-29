<h1 align="center">
  <img
    width="400"
    alt="django"
    src="https://live.staticflickr.com/65535/53658854827_c1c359e276_z.jpg">
</h1>

---

<h3 align="center">
  <strong>
🗓 Django Todo List API 🗓

  </strong>
</h3>

---

<p align="center">
  <img 
    width="1000"
    alt="home"
    src="https://live.staticflickr.com/65535/53658852452_9cdf4a53c8_b.jpg"/>
</p>

---

## Todo List App - Django REST API (DRF)
### Description

This is a Django REST Framework (DRF) project for managing todo items. The API allows users to register, log in, create, update, delete todos, and retrieve todo details.

The project is Dockerized for easy deployment and development environment setup.


---


## Features

- **User Authentication (Dockerized):** Users can register, login, and logout. JWT authentication is used to secure the API endpoints.
- **Todo Management (Dockerized):** Users can create, retrieve, update, and delete todos. Todos have attributes such as title, description, due date, priority, and completion status.
- **Pagination and Filtering (Dockerized):** Todos are paginated to improve performance, and filtering options are available based on various attributes such as title, completion status, priority, and due date.
- **Swagger Documentation (Dockerized):** API documentation is generated using Swagger, providing an interactive interface for exploring the endpoints.

<p align="center">
  <img 
    width="600"
    alt="home"
    src="https://live.staticflickr.com/65535/53660176654_0da75ec9eb_b.jpg"/>
</p>
<p align="center">
  <img 
    width="600"
    alt="home"
    src="https://live.staticflickr.com/65535/53659711436_0fca697c35_c.jpg"/>
         
</p>


---


## Technologies Used
- **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework (DRF):** A powerful and flexible toolkit for building Web APIs in Django, providing serializers, views, authentication, and more.
- **PostgreSQL:** A powerful open-source relational database management system used for storing and managing data in the application.
- **DRF-YASG:** DRF-YASG is a library for generating OpenAPI/Swagger specifications for Django REST Framework APIs.
- **django-filter:** django-filter provides a simple way to filter down data based on parameters passed in the URL.
- **PyJWT:** PyJWT is a Python library to work with JSON Web Tokens (JWT), which are used for user authentication.
- **psycopg2:** psycopg2 is a PostgreSQL adapter for Python, enabling interaction with PostgreSQL databases.
- **python-decouple:** python-decouple is a Python library for separating settings from code, allowing configuration via environment variables or separate configuration files.
- **Docker:** A platform for developing, shipping, and running applications in containers, providing a consistent environment across different systems.
- **Docker Compose:** A tool for defining and running multi-container Docker applications, simplifying the process of managing complex containerized environments.

 <p align="left">
  <img src="https://img.shields.io/badge/django-00008B?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/django rest framework-acace6?style=for-the-badge&logo=DRF&logoColor=white"/>
  <img src="https://img.shields.io/badge/postgresql-800000?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white"/>
  <img src="https://img.shields.io/badge/pyjwt-ffa500?style=for-the-badge&logo=pyjwt&logoColor=white"/>
  <img src="https://img.shields.io/badge/docker-0000FF?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/docker compose-4682B4?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

---

## API Endpoints
### Authentication

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/auth/login/``` | _Login user_| _All users_|
| *POST* | ```/auth/logout/``` | _Logout user_|_All users_|
| *POST* | ```/auth/register/``` | _Register new user_|_All users_|
| *DELETE* | ```/auth/user/<int:user_id>/``` | _Delete a specific user_|_All users_|
| *PUT*  | ```/auth/user/<int:user_id>/``` | Edit a specific user |_All users_|
| *PATCH*  | ```/auth/user/<int:user_id>/``` | Edit a specific user |_All users_|
| *GET* | ```/auth/users/<int:user_id>/``` | Get a specific user |_All users_|
| *GET* | ```/auth/users/``` | Get all users | _All users_ |

### Todo

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/todos/``` | _Get all todos_|_All users_|
| *POST* | ```/todos/``` | _Create a new todo_|_All users_|
| *GET* | ```/todos/<int:id>/``` | _Retrieve an todo by id_|_All users_|
| *PUT* | ```/todos/<int:id>/``` | _Update an todo_|_All users_|
| *PATCH* | ```/todos/<int:id>/``` | _Update an todo_|_All users_|
| *DELETE* | ```/todos/<int:id>/``` | _Delete/Remove an todo_ |_All users_|

---

## Installation

1- **Clone the repository:**
```
git clone https://github.com/PayamAnari/todo-django.git
cd todo-django

```
2- **Create your virtualenv and activate it:**
```
Pipenv or virtualenv
```
3- **Install dependencies:**
```
pip install -r requirements.txt
```
4- **Set up environment variables:**
Create a .env file in the project root and add the following variables:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<your_database_name>
DB_USER=<your_database_user>
DB_PASSWORD=<your_database_password>
DB_HOST=db
DB_PORT=5432
POSTGRES_PASSWORD=<your_postgresql_password>

```
5- **Apply database migrations:**
```
python manage.py migrate
```

6- **Run Docker Compose:**
```
docker-compose up

```

---

## Example Requests
### User Register
### Request

```
POST /auth/register/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json

}
data = {
    "username": "john_doe",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "password": "securepassword"
}
```

### Response

```
{
    "message": "User created successfully!",
    "data": {
        "username": "john_doe",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com"
    }
}

```
### Get user by ID
### request

```
GET /users/<int:id>/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Authorization: Bearer <your_access_token>

```

### response

```
{
    "id": 1,
    "username": "john_doe",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "is_active": true,
    "is_superuser": false,
    "created_at": "2024-04-17T12:00:00Z",
    "email_verified": false,
    "todo_count": 5  
}
```

### Get Todo by ID
### request

```
GET /todos/<int:id>/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Authorization: Bearer <your_access_token>

```

### response

```

{
    "id": 1,
    "title": "Example Todo",
    "description": "This is an example todo",
    "due_date": "2024-04-20T00:00:00Z",
    "is_completed": false,
    "priority": "High",
    "owner": {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com"
    }
}
```

---

## License
This project is licensed under the [MIT License](LICENSE).

---
### Built with ❤️ by Payam Anari

Thank you for exploring the Gym Fitness app! If you have any questions, feedback, or just want to say hi, feel free to [reach out](mailto:anari.p62@gmail.com). Happy fitness journey!

---
