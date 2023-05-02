from baseObject import baseObject
import hashlib

class user(baseObject):
     def __init__(self):
       self.setup('transaction')
       self.roles = {}


    # def establishConnection(self):

    #     self.conn = pymysql.connect(host=mysecrets.db_host, port=3306, user=mysecrets.db_user,
    #                    passwd=mysecrets.db_passwd, db=mysecrets.db_name, autocommit=True)
    #     self.cur = self.conn.cursor(pymysql.cursors.DictCursor)