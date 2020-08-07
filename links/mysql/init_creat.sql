CREATE USER IF NOT EXISTS 'flask'@'%' IDENTIFIED BY 'flask';

GRANT ALL ON *.* TO 'flask'@'%';


CREATE DATABASE 'microblog_db' default character set utf8 collate utf8_general_ci;


