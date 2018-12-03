# Tinyflaskblog

Structure:
.
├ app
│   ├ __init__.py
│   ├ main
│   │   ├ __init__.py
│   │   └ routes.py
│   ├ models.py
│   ├ static
│   │   ├ css
│   │   │   ├ materialize.css
│   │   │   └ materialize.min.css
│   │   ├ img
│   │   │   └ logo.png
│   │   └ js
│   │       ├ materialize.js
│   │       └ materialize.min.js
│   └ templates
│       ├ base.html
│       ├ index.html
│       └ page.html
├ blog.py
├ boot.sh
├ config.py
├ content.md
├ docker-compose.yml
├ Dockerfile
├ monolith.py
├ nginx
│   └ blogapp.conf
├ README.md
├ requirements.txt
├ structure
└ tests.py```

```

Running the blog (assumption: docker & docker compose are installed):
```sh
git clone tinyflaskbog
cd tinyflaskbog
docker-compose build
docker-compose up -d
```
