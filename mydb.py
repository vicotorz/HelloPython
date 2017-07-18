#!/usr/bin/python
# -*- coding:UTF-8-*-
#mysql连接操作
import MySQLdb
import random

if __name__=='__main__':
    db=MySQLdb.connect('localhost','root','','wenda',charset='utf8')
    try:
        cursor=db.cursor()

        sql='insert into question(title,content,user_id,created_date,comment_count) values ("xx","rx",1,now(),0)'
        cursor.execute(sql)
        qid=cursor.lastrowid
        db.commit()


        sql='select * from question order by id desc limit 2'
        cursor.execute(sql)

        for each in cursor.fetchall():
            for row in each:
                print row

        db.commit()

    except Exception, e:
        print e
        db.rollback()
    db.close()

