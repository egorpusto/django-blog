# 📝 Django Blog - Full-Featured Blog Platform

A production-ready blog application built with Django 5.2, PostgreSQL, Redis, Bootstrap 5, and Docker. Started as a learning project from a book and significantly enhanced with modern best practices, REST API, authentication, caching, comprehensive testing, and more.

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue.svg)
![Redis](https://img.shields.io/badge/Redis-7-red.svg)
![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)
![Tests](https://img.shields.io/badge/Tests-24%20passing-brightgreen.svg)
![Coverage](https://img.shields.io/badge/Coverage-95%25-brightgreen.svg)
![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)
![CI](https://github.com/egorpusto/django-blog/actions/workflows/ci.yml/badge.svg)

## 🎯 Project Overview

A full-featured blog platform with Markdown support, tagging system, full-text search, REST API, Redis caching, and user authentication. The project demonstrates Django best practices including Class-Based Views, custom managers, template tags, and a clean project structure.

### Original vs Enhanced

**Original Book Features:**
- Basic Django blog with posts and comments
- SQLite database
- Simple function-based views
- Basic templates without styling
- Tagging with django-taggit
- PostgreSQL trigram search

**My Enhancements:**
- 🔐 **User Authentication** - Registration, login, logout, author profiles
- 📊 **REST API** - Full JSON API with Django REST Framework
- ⚡ **Class-Based Views** - Refactored to ListView, DetailView, FormView
- 🎨 **Bootstrap 5 UI** - Responsive design with sidebar and navigation
- 🔴 **Redis Caching** - Cache for posts, sidebar and template tags with auto-invalidation
- 🐳 **Docker** - PostgreSQL + Redis + Django with health checks
- 🧪 **Comprehensive Testing** - 24 tests, 95% coverage with pytest
- 📝 **Code Quality** - pre-commit hooks with black, isort, flake8
- 🔄 **CI/CD Pipeline** - GitHub Actions with tests, lint and Docker build
- 🔒 **Security** - Environment variables, no hardcoded secrets
- 📋 **Logging** - Structured logging configuration
- 📦 **Clean Structure** - Proper settings, requirements, .env.example

## 🛠️ Tech Stack

### Backend
- **Django** 5.2 - Web framework
- **PostgreSQL** 16 - Primary database with trigram search
- **psycopg** 3 - Modern PostgreSQL adapter
- **django-taggit** - Tagging system
- **Markdown** - Post content rendering
- **python-decouple** - Environment variables management

### API
- **Django REST Framework** - REST API
- **DRF Browsable API** - Interactive API documentation

### Caching
- **Redis** 7 - Caching layer
- **django-redis** - Django Redis integration

### Frontend
- **Bootstrap** 5.3 - Responsive UI
- **Bootstrap Icons** - Icon library

### Testing
- **pytest** - Testing framework
- **pytest-django** - Django integration
- **coverage** - Code coverage reporting

### DevOps
- **Docker** & **Docker Compose** - Containerization
- **GitHub Actions** - CI/CD pipeline
- **pre-commit** - Git hooks for code quality
- **black** - Code formatter
- **isort** - Import sorter
- **flake8** - Linter

## 📋 Features

### Posts
- ✅ Markdown-powered content
- ✅ Draft / Published status
- ✅ Date-based URLs
- ✅ Tag filtering
- ✅ Similar posts (by tags)
- ✅ Share post via email
- ✅ RSS Feed
- ✅ XML Sitemap

### Search
- ✅ PostgreSQL trigram full-text search
- ✅ Similarity ranking

### Comments
- ✅ Comment system with moderation
- ✅ Active/inactive status

### Authentication
- ✅ User registration
- ✅ Login / Logout
- ✅ Author profile pages
- ✅ Posts by author

### REST API
- ✅ Paginated posts list
- ✅ Post detail with comments
- ✅ Read-only for anonymous users
- ✅ Browsable API interface

### Caching
- ✅ Redis cache for post list and detail pages
- ✅ Redis cache for sidebar (latest posts, most commented, total count)
- ✅ Automatic cache invalidation on new comment
- ✅ Configurable TTL per cache type

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose
- Git

### Quick Start with Docker

1. **Clone the repository**
```bash
git clone https://github.com/egorpusto/django-blog.git
cd django-blog
```

2. **Create environment file**
```bash
cp .env.example .env
# Edit .env with your settings
```

3. **Start all services**
```bash
docker-compose up -d
```

4. **Run migrations**
```bash
docker-compose exec web python manage.py migrate
```

5. **Create superuser**
```bash
docker-compose exec web python manage.py createsuperuser
```

6. **Access the application**
- Blog: http://localhost:8000/blog/
- Admin: http://localhost:8000/admin/
- API: http://localhost:8000/api/posts/

### Local Development Setup

1. **Clone & create virtual environment**
```bash
git clone https://github.com/egorpusto/django-blog.git
cd django-blog
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
```bash
cp .env.example .env
# Fill in DB_NAME, DB_USER, DB_PASSWORD, SECRET_KEY
```

4. **Start PostgreSQL and Redis via Docker**
```bash
docker-compose up db redis -d
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/blog/

## 🧪 Testing

### Run all tests
```bash
pytest
```

### Run with coverage
```bash
coverage run -m pytest
coverage report
```

### Run specific file
```bash
pytest blog/tests/test_views.py -v
```

## 📚 API Documentation

### Endpoints
```
GET  /api/posts/       - Paginated list of published posts
GET  /api/posts/{id}/  - Post detail with comments
```

### Example Requests

**Get posts:**
```bash
curl http://localhost:8000/api/posts/
```

**Get post detail:**
```bash
curl http://localhost:8000/api/posts/1/
```

### Example Response
```json
{
    "count": 10,
    "next": "http://localhost:8000/api/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "url": "http://localhost:8000/api/posts/1/",
            "title": "My First Post",
            "author": {
                "id": 1,
                "username": "admin",
                "first_name": "",
                "last_name": ""
            },
            "publish": "2025-01-01T12:00:00Z",
            "tags": ["django", "python"]
        }
    ]
}
```

## 🏗️ Project Structure
```
mysite/
├── blog/                    # Main blog application
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   └── blog/
│   │       ├── base.html
│   │       └── post/
│   ├── templatetags/        # Custom template tags
│   │   └── blog_tags.py
│   ├── tests/               # Test suite
│   │   ├── conftest.py
│   │   ├── test_models.py
│   │   ├── test_views.py
│   │   └── test_forms.py
│   ├── admin.py
│   ├── api_urls.py          # API URL configuration
│   ├── api_views.py         # DRF API views
│   ├── apps.py
│   ├── feeds.py             # RSS feed
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py       # DRF serializers
│   ├── sitemaps.py
│   ├── urls.py
│   └── views.py             # Class-based views
├── accounts/                # Authentication application
│   ├── templates/
│   │   └── accounts/
│   ├── forms.py
│   ├── urls.py
│   └── views.py
├── mysite/                  # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── .env.example             # Environment variables template
├── .flake8                  # Flake8 configuration
├── .gitignore
├── .github/                 # GitHub Actions workflows
│   └── workflows/
│       └── ci.yml
├── .pre-commit-config.yaml  # pre-commit hooks
├── docker-compose.yml       # Docker services
├── .dockerignore
├── Dockerfile
├── manage.py
├── pyproject.toml           # black & isort configuration
├── pytest.ini
├── README.md
└── requirements.txt
```

## ⚙️ Configuration

### Environment Variables
```env
# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=blog_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

# Redis
REDIS_URL=redis://localhost:6379/1

# Email
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=My Blog <noreply@myblog.com>
```

## 🐳 Docker Services
```bash
# Start all services
docker-compose up -d

# Start only db and redis for local dev
docker-compose up db redis -d

# View logs
docker-compose logs -f web

# Run migrations
docker-compose exec web python manage.py migrate

# Stop all services
docker-compose down

# Rebuild
docker-compose up -d --build
```

## 🔄 CI/CD Pipeline

Every push to `main` automatically triggers three parallel jobs:

- **Tests** — spins up PostgreSQL + Redis, runs migrations, pytest with coverage ≥ 90%
- **Lint** — checks black, isort, flake8
- **Docker** — builds image and validates docker-compose config

## 📝 Code Quality
```bash
# Install pre-commit hooks (once)
pre-commit install

# Run manually on all files
pre-commit run --all-files

# Individual tools
black .
isort .
flake8 .
```

## 🔒 Security

- Environment variables via python-decouple
- No secrets in source code
- CSRF protection on all forms
- Password validation
- Debug mode off in production
- Security headers in production settings

## 🚧 Future Improvements

- [ ] Image uploads for posts
- [ ] Like / reaction system
- [ ] Email notifications for comments
- [ ] Deploy to Railway / Render

## 👤 Author

**Egor Anoshin**
- GitHub: [@egorpusto](https://github.com/egorpusto)

## 🙏 Acknowledgments

- Based on "Django 5 By Example" by Antonio Melé
- Enhanced with modern best practices and additional features

---

**Note:** This project started from a book tutorial and was significantly enhanced with authentication, REST API, Redis caching, Docker, CI/CD pipeline, comprehensive testing, and Bootstrap UI as a portfolio piece.
