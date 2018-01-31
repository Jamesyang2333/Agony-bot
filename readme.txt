All scripts for the implementation of Agony Bot are listed below:
config.ini
python_mysql_dbconfig.py
python_mysql_connect2.py
DBHelper.py
user.py
quote.py
Admin_script.py
database_operation.sql

config.ini : Configuration of Agony Bot's mysql database connection, including username, host, password and name of the database.

python_mysql_dbconfig.py : Python script that reads the mysql database configuration information from config.ini.

python_mysql_connect2.py : Python scipt that make the mysql database connection using the configuration information returned from functions in python_mysql_dbconfig.py.

DBHelper.py : Python script of the DBHelper class. A instance of the DBHelper class could access the mysql database connection return from python_mysql_connect2.py and has various methods to perform mysql database manipulations necessary for the operation of Agony Bot.

user.py : Main python script that implements Agony Bot. A DBHelper object is instantiated to coordinate the database manipulation with the operation of Agony Bot. The script contains a main non-stoping loop that processes one user input within each iteration according to the chronological order multiple users enter their input.

quote.py : Python script that scraps a ever-updating motto from the Internet which would be sent to users who share their thoughts with Agony Bot.

Admin_script.py : Python script that contains basic Agony Bot administer operations, including to send an announcement to all users and to send a specific message to a specific list of users.

database_operation.sql : SQL script that contains SQL statements which wouldn't be executed automatically during the operation of Agony Bot. The statements perform database manipulations of creating a database schema containing three tables that store records of user input, message sharing and message receiving respectively, creating each of the three tables, checking all reportedly spamming message and deleting a spamming message sharing record identified by msgid.
