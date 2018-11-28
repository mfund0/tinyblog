# Tinyflaskblog

Structure:
```
.
├── app
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   ├── materialize.css
│   │   │   └── materialize.min.css
│   │   ├── img
│   │   │   └── logo.png
│   │   └── js
│   │       ├── materialize.js
│   │       └── materialize.min.js
│   └── templates
│       ├── base.html
│       ├── index.html
│       └── page.html
├── blog.py
├── boot.sh
├── config.py
├── test_content.md
├── Dockerfile
├── monolith.py
├── README.md
├── requirements.txt
├── tests.py
└── venv/
```

Running the blog (assumption: docker & docker compose are installed):
```sh
git clone tinyflaskbog
cd tinyflaskbog
docker-compose build
docker-compose up -d
```