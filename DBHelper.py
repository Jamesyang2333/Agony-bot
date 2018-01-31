import python_mysql_connect2
from mysql.connector import Error
import random

class DBHelper:

    # Instantiate a DBHelper object with the configured connection information
    def __init__(self, conn = python_mysql_connect2.connect()):
        self.conn = conn
    # Add a new user input record
    def add_log(self, content, sender, msgid):
        query = "INSERT INTO log(content, sender, id) " \
            "VALUES(%s, %s, %s)"
        args = (content, sender, msgid)
        try:
            print("inserting a new message...")
            cursor = self.conn.cursor()
            cursor.execute(query,args)
            self.conn.commit()
        except Error as err:
            print(err.msg)
        cursor.close()
    # Add a new message sharing record       
    def add_message(self, description, sender, msgid):
        query = "INSERT INTO agony(description, sender, num_like, id) " \
            "VALUES(%s, %s, %s, %s)"
        args = (description, sender, 0, msgid)
        try:
            print("inserting a new message...")
            cursor = self.conn.cursor()
            cursor.execute(query,args)
            self.conn.commit()
        except Error as err:
            print(err.msg)
        cursor.close()
    # Add a new message receiving record
    def add_reply(self, message, reply, msgid, sender, replyid):
        query = "INSERT INTO aunt(message, reply, msgid, sender, replyid) " \
            "VALUES(%s, %s, %s, %s, %s)"
        args = (message, reply, msgid, sender, replyid)
        try:
            print("inserting a new reply..")
            cursor = self.conn.cursor()
            cursor.execute(query,args)
            self.conn.commit()
        except Error as err:
            print(err.msg)
        cursor.close()
    # Get information of the user's last input
    def get_last_message(self, sender):
        query = "select content from log where sender = %s order by id desc"
        args = (sender, )
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            result = cursor.fetchall()
        except Error as err:
            print(err)
        cursor.close()
        return result[0][0]
    # Get information of a random message shared by other users
    def get_message(self, sender):
        query = "select description, sender, id from agony where sender != %s;"
        args = (sender, )
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            row = cursor.fetchall()
            n = random.randint(0, cursor.rowcount-1)
            result = row[n]
        except Error as err:
            print(err)
        cursor.close()
        return result
    # Get information of the last message shared by the user
    def last_sent_message(self, sender):
        query = "select id from agony where sender = %s;"
        args = (sender, )
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            row = cursor.fetchall()
            n = cursor.rowcount - 1
            result = row[n][0]
        except Error as err:
            print(err)
        cursor.close()
        return result
    # Delete a specific message sharing record identified by msgid
    def delete_message(self, msgid):
        query = "delete from agony where id = %s;"
        args = (msgid, )
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            self.conn.commit()
        except Error as err:
            print(err)
        cursor.close()
    # Get information of the last message receiving record of the user
    def get_reply(self, sender):
        query = "select sender, message, msgid from aunt where replyid = %s;"
        args = (sender, )
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            result = cursor.fetchall()
        except Error as err:
            print(err)
        cursor.close()
        return result[-1]
    # Increase the number of 'like' by one for a specific message sharing record identified by msgid 
    def increase_like(self, msgid):
        query = """ UPDATE agony
                SET num_like = num_like+1
                WHERE id = %s """
        args = (msgid, )
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            self.conn.commit()
        except Error as err:
            print(err)
        cursor.close()
    # Update the 'spamming' state of a specific message sharing record identified by msgid as true
    def mark_as_spam(self, msgid):
        query = """UPDATE agony
                SET spam = true
                where id = %s """
        args = (msgid, )
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            self.conn.commit()
        except Error as err:
            print(err)
        cursor.close()
    # Get the number of 'like' for a specific message sharing record identified by msgid
    def get_like(self, msgid):
        query = "select num_like from agony where id = %s"
        args = (msgid, )
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            result = cursor.fetchall()
        except Error as err:
            print(err)
        cursor.close()
        return result[0][0]
    # Get a list of all users who ever had a conversation with Agony Bot
    def get_all_user(self):
        query = "select distinct sender from log;"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
        except Error as err:
            print(err)
        cursor.close()
        return row
