# Django Blog Project

This is a simple blog application built while studying **"Django 5 By Example" by Antonio Mele**.  
It demonstrates creating models, views, templates, and adding pagination and comment functionality.

## ✨ Features

- List of blog posts
- Post detail pages
- Add comments to posts
- Pagination support
- Post sharing via email
- Admin panel management

## 🛠 Technologies

- Python 3.x
- Django 5.x
- SQLite (default)
- HTML
- CSS

## 🚀 Getting Started

### 1. Clone the project

git clone https://github.com/egorpusto/django-barter.git
cd django-barter

### 2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run migrations

python manage.py migrate

### 5. Create a superuser (for admin panel)

python manage.py createsuperuser

### 6. Start the development server

python manage.py runserver

Visit:

- http://127.0.0.1:8000/ — main interface
- http://127.0.0.1:8000/admin/ — admin panel

## 🗂 Project Structure

- `mysite/` — project root  
  - `blog/` — Django app for the blog  
  - `static/` — static CSS files  
  - `templates/` — templates for the blog and pagination  
  - `db.sqlite3` — project database  
  - `manage.py` — Django management script  

---

Made with ❤️ by egorpusto