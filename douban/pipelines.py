# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from douban.settings import mysql_host, mysql_user, mysql_password, mysql_db_name


class DoubanPipeline(object):
    # def __init__(self):
        # host = mysql_host
        # user = mysql_user
        # password = mysql_password
        # dbName = mysql_db_name
        # self.connect = pymysql.Connect(host, user, password, dbName)
        # self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            # 插入数据
            # self.cursor.execute(
            #     """insert into doubanmovie(serial_number, movie_name_main, movie_name_sub,
            #     movie_name_other, actor, `date`, star, rate_num, `desc`)
            #     value (%s, %s, %s,
            #     %s, %s, %s,
            #     %s, %s, %s)""",
            #     (item['serial_number'],
            #      item['movie_name_main'],
            #      item['movie_name_sub'],
            #      item['movie_name_other'],
            #      item['actor'],
            #      item['date'],
            #      item['star'],
            #      item['rate_num'],
            #      item['desc']
            #      ))

            print("process_item-->" + item['serial_number'])

            # 提交sql语句
            # self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            print(error)
        return item
