# Blog Web Application

A Django-based blog web application that allows users to create, display, and manage blog posts. The app features pagination, email notifications, a comment system, tagging, and post recommendations. Additionally, it includes an RSS feed for the latest posts and a full-text search engine built using PostgreSQL.

## ✨ Features

- Blog Post Management: Create and display blog posts with content and images.
- Pagination: Breaks down blog posts into pages for easy navigation.
- Comment System: Users can leave comments on blog posts.
- Tagging System: Posts can be tagged with multiple keywords for easy categorization and searching.
- Post Recommendations: Similar posts are recommended to readers based on tags.
- Email Notifications: Sends notifications about new posts and comments.
- RSS Feed: A news feed for blog posts, allowing users to follow updates.
- Full-Text Search: A search engine powered by PostgreSQL's full-text search capabilities for searching through blog posts.

## 🛠 Technologies

- Python 3.x
- Django 5.x
- PostgreSQL (for full-text search)
- SQLite (for development)
- HTML
- CSS
- RSS (for the feed)

## 🚀 Getting Started

### 1. Clone the project

git clone https://github.com/egorpusto/django-blog.git
cd django-blog

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
  - `blog/` — Django app for managing blog posts 
    - `migrations/` — database migrations for the blog app
    - `templates/` —  HTML templates for blog-related pages
    - `forms.py` — forms for blog post creation and editing
    - `models.py` — blog post model
    - `urls.py` —  URL configuration for blog-related views
    - `views.py` — views for blog post operations (create, list, update, delete)
  - `mysite/` — project settings  
    - `settings.py` — Django settings  
    - `urls.py` — project-level URL routing  
    - `wsgi.py` — WSGI application  
  - `manage.py` — Django management script  
  - `requirements.txt` — project dependencies  

---

Made with ❤️ by egorpusto