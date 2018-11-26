docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=pages -e MYSQL_USER=blog \
    -e MYSQL_PASSWORD=<your_password>\
    mysql/mysql-server:5.7