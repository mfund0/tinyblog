docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=pages -e MYSQL_USER=blog \
    -e MYSQL_PASSWORD=<your_password>\
    mysql/mysql-server:5.7

docker build -t tinyflaskblog:latest .

docker run --name blogapp -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://blog:<database-password>@dbserver/pages \
    tinyflaskblog:latest