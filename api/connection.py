import pymysql
from api.config import cfg
import json


my_conn = None

try:
    my_conn = pymysql.connect(
        host = cfg.MYSQL_HOST, 
        user = cfg.MYSQL_USER, 
        passwd = cfg.MYSQL_PASSWORD, 
        db = cfg.MYSQL_DATABASE, 
        charset = 'utf8',
        autocommit = True
    )
except:
    print("ERROR: Can't connect to MySQL database.")
    quit()

