# DjangoDevs

## Django / Python

<br>

<div align="center">
  <img
    src="static/images/readme/project-overview.png"
    alt="Project overview"
    width="850"
  >
</div>

<br>

<div>

    DjangoDevs is a web application designed for developers!
    Create your own profile, discover developers from around
    the world, and connect with them to explore new opportunities!

</div>

<br>
<br>

# Index

-   [DjangoDevs](#djangodevs)
    -   [Django / Python](#django--python)
-   [Index](#index)
    -   [Features](#features)
    -   [Technologies and Tools used](#technologies-and-tools-used)
-   [Project Setup](#project-setup)
    -   [Prerequisites](#prerequisites)
    -   [Clone the repository](#clone-the-repository)
    -   [Set up the virtual environment](#set-up-the-virtual-environment)
    -   [Install dependencies](#install-dependencies)
    -   [Set up the database](#set-up-the-database)
    -   [Create a superuser](#create-a-superuser)
    -   [.env file](#env-file)
    -   [Run the development server](#run-the-development-server)
    -   [Access the application](#access-the-application)
    -   [Contribution](#contribution)
    -   [Project Status](#project-status)
    -   [Project Developer](#project-developer)

<br>

## Features

<div>

    ✔️ Share your projects with your own profile

    ✔️ Register and log in users (with JWT)

    ✔️ Message other developers

    ✔️ Rate others projects

    ✔️ Search with pagination

    ✔️ Welcome emails and password reset functionality

    ✔️ CRUD with projects, skills, reviews...

    ✔️ Signals and Flash messages

    ✔️ Responsive design, accessibility and SEO

</div>

<br>

## Technologies and Tools used

<div align="center">
  <br>
    <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="static/images/readme/django.svg" alt="Django" width="60" height="60" style="margin-right: 24px"/></a>
    <a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"> <img src="static/images/readme/postgresql.svg" alt="PostgreSQL" width="60" height="60" style="margin-right: 24px"/></a>
    <a href="https://www.python.org/" target="_blank" rel="noreferrer"> <img src="static/images/readme/python.svg" alt="Python" width="60" height="60" style="margin-right: 24px"/></a>
    <br>
    <br>
    <a href="https://www.django-rest-framework.org/" target="_blank" rel="noreferrer"> <img src="static/images/readme/django-rest-framework.svg" alt="Django REST Framework" width="60" height="60" style="margin-right: 24px"/></a>
    <a href="https://www.djlint.com/" target="_blank" rel="noreferrer"> <img src="static/images/readme/djlint.png" alt="Djlint" width="100" height="60" style="margin-right: 24px"/></a>
  <br>
  <br>
</div>

<br>

# Project Setup

These are the instructions to set up and run the Django project in your local environment.

## Prerequisites

1. **Python**: Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/).
2. **Pip**: Ensure that `pip` is installed. It usually comes pre-installed with Python.
3. **Virtualenv**: It is recommended to use a virtual environment to manage the project dependencies. You can install it with the following command:

    ```sh
    pip install virtualenv
    ```

## Clone the repository

Clone the repository to your local machine using the following command:

```sh
  git clone https://github.com/KevinVanDerSchans/djangodevs-django.git
```

## Set up the virtual environment

Navigate to the project folder and create a virtual environment:

```sh
    cd djangodevs_django
    virtualenv env
```

Activate the virtual environment:

• On Windows:

```sh
    .\env\Scripts\activate
```

• On macOS and Linux:

```sh
    source env/bin/activate
```

## Install dependencies

Install the project dependencies using the requirements.txt file:

```sh
    pip install -r requirements.txt
```

## Set up the database

Apply the migrations to set up the database:

```sh
    python manage.py migrate
```

## Create a superuser

Create a superuser to access the Django admin:

```sh
    python manage.py createsuperuser
```

## .env file

Make sure to create a .env file in the project root for the necessary environment variables.

## Run the development server

Run the development server to verify everything is working correctly:

```sh
    python manage.py runserver
```

## Access the application

Open your browser and navigate to http://127.0.0.1:8000/ to see the application running.

<br>

## Contribution

If you want to contribute to this project, follow these steps:

1. Perform a fork to the repository.

2. Create a branch for your feature or bugfix: `git checkout -b feature/your-feature-name`

3. Make the necessary changes and commits: `git commit -m 'Add some feature'`

4. Push to branch: `git push origin feature/your-feature-name`

5. Send a pull request to the original repository.

<br>

## Project Status

![COMPLETED](https://img.shields.io/badge/COMPLETED-green.svg)

<br>

## Project Developer

| [<img src="https://avatars.githubusercontent.com/u/122877560?v=4" width=115><br><sub>Kevin Schans</sub>](https://github.com/KevinVanDerSchans) |
| :--------------------------------------------------------------------------------------------------------------------------------------------: |
