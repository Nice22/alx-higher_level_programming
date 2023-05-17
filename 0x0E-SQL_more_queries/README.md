# 0x0E. SQL - More queries

<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg" alt="" loading="lazy" style="">

## Resources

<ul>
<li><a href="/rltoken/RniBKj48bnIN8xpXhGl1yA" title="How To Create a New User and Grant Permissions in MySQL" target="_blank">How To Create a New User and Grant Permissions in MySQL</a> </li>
<li><a href="/rltoken/FIiEIvA6IN_hSKM5TvgyxQ" title="How To Use MySQL GRANT Statement To Grant Privileges To a User" target="_blank">How To Use MySQL GRANT Statement To Grant Privileges To a User</a> </li>
<li><a href="/rltoken/LrovGa6N-OE2ID_tpWZRaQ" title="MySQL constraints" target="_blank">MySQL constraints</a> </li>
<li><a href="/rltoken/kR71h5zjkPtx4kBoVf7q0g" title="SQL technique: subqueries" target="_blank">SQL technique: subqueries</a> </li>
<li><a href="/rltoken/rNMJeQ1jbNTCljbvCSjf6w" title="Basic query operation: the join" target="_blank">Basic query operation: the join</a> </li>
<li><a href="/rltoken/HhZ6TJ1q5S0aR4lhfpKdOQ" title="SQL technique: multiple joins and the distinct keyword" target="_blank">SQL technique: multiple joins and the distinct keyword</a> </li>
<li><a href="/rltoken/T6FZUQdsMzr8hgNInBzudA" title="SQL technique: join types" target="_blank">SQL technique: join types</a> </li>
<li><a href="/rltoken/Nd-sdM8QUpf0YKIlXzVv4w" title="SQL technique: union and minus" target="_blank">SQL technique: union and minus</a> </li>
<li><a href="/rltoken/iSNyinU6SPWTGDUWMmcRkg" title="MySQL Cheat Sheet" target="_blank">MySQL Cheat Sheet</a> </li>
<li><a href="/rltoken/-plhBsra0N7BOuFoEg--zg" title="The Seven Types of SQL Joins" target="_blank">The Seven Types of SQL Joins</a> </li>
<li><a href="/rltoken/I4Lws_eQrIrNTbkZvvk-oQ" title="MySQL Tutorial" target="_blank">MySQL Tutorial</a> </li>
<li><a href="/rltoken/051eAEP_rePBU7jeh879GA" title="SQL Style Guide" target="_blank">SQL Style Guide</a> </li>
<li><a href="/rltoken/YavbYiraYFr8oTukT_N6eQ" title="MySQL 8.0 SQL Statement Syntax" target="_blank">MySQL 8.0 SQL Statement Syntax</a> </li>
</ul>

Extra resources around relational database model design:

<ul>
<li><a href="/rltoken/EWLRPeqr5sQ9AqfoG_KXxw" title="Design" target="_blank">Design</a></li>
<li><a href="/rltoken/mqBhYoSYbhH5ZZrhDcY0kA" title="Normalization" target="_blank">Normalization</a></li>
<li><a href="/rltoken/R0exkJmf-2ddKjGfa8D0dA" title="ER Modeling" target="_blank">ER Modeling</a></li>
</ul>

## General
How to create a new MySQL user
How to manage privileges for a user to a database or table
What’s a PRIMARY KEY
What’s a FOREIGN KEY
How to use NOT NULL and UNIQUE constraints
How to retrieve datas from multiple tables in one request
What are subqueries
What are JOIN and UNION


# Requirements

## General
Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
All your files should end with a new line
All your SQL queries should have a comment just before (i.e. syntax above)
All your files should start by a comment describing the task
All SQL keywords should be in uppercase (SELECT, WHERE…)
A README.md file, at the root of the folder of the project, is mandatory
The length of your files will be tested using wc
## More Info
### Comments for your SQL file:
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
### Install MySQL 8.0 on Ubuntu 20.04 LTS
$ sudo apt update
$ sudo apt install mysql-server
...
$ my8sql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
## Use “container-on-demand” to run MySQL
In the container, credentials are root/root

Ask for container Ubuntu 20.04
Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
#### In the container, credentials are root/root

## How to import a SQL dump
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$


<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230517%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20230517T150956Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=c8f0cdd9093173c9331a1c0cd4b04d599f7182d4518c5518e0b4020ad46677ca" alt="" loading="lazy" style="">
