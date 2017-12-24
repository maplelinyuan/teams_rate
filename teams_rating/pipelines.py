# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
import datetime
import pdb

nowadays = datetime.datetime.now().strftime('%Y_%m_%d')
nowatime = datetime.datetime.now().strftime('%Y_%m_%d_%H%M')

class TeamsRatingPipeline(object):

    def process_item(self, item, spider):
        if not item and len(item['match_players']) < 11:
            return
        # Connect to the database
        league_id = item['league_id']   # 联赛ID，用来获取连接的数据库名称
        db_name = 'league_'+league_id
        config = {
            'host' : '127.0.0.1',
            'user' : 'root',
            'password' : '19940929',
            'db' : db_name,
            'charset' : 'utf8mb4',
            'cursorclass' : pymysql.cursors.DictCursor
        }
        connection = pymysql.connect(**config)
        print('连接至数据库'+db_name)
        try:
            with connection.cursor() as cursor:
                # 设置当前表名
                tableName = 'team_' + item['team_id']   # 用team_id 辅助建表
                # 建立当前队伍表
                build_table = (
                    "CREATE TABLE IF NOT EXISTS "' %s '""
                    "(league_id VARCHAR(10) NOT NULL,"
                    "match_id VARCHAR(10) NOT NULL PRIMARY KEY,"
                    "team_id VARCHAR(10) NOT NULL,"
                    "home_id VARCHAR(10) NOT NULL,"
                    "home_name VARCHAR(20) NOT NULL,"
                    "away_id VARCHAR(10) NOT NULL,"
                    "away_name VARCHAR(20) NOT NULL,"
                    "match_result INT(4) NOT NULL,"
                    "match_time VARCHAR(20) NOT NULL,"
                    "match_score VARCHAR(20) NOT NULL)"
                )
                cursor.execute(build_table % tableName)

                # 查询一下本表中是否已经保存这场比赛
                search_this_match = ('SELECT match_id FROM %s WHERE match_id=%s'% (tableName,item['match_id']))
                cursor.execute(search_this_match)
                this_match_len = len(cursor.fetchall())
                if this_match_len > 0:
                    return False
                insert_sql = (
                    "INSERT INTO "+tableName+" VALUES "
                    "('%s', '%s', '%s', '%s', '%s','%s','%s', %d, '%s','%s')"
                )
                try:
                    print('insert 数据表'+tableName)
                    cursor.execute(insert_sql % (item['league_id'], item['match_id'], item['team_id'], item['home_id'], item['home_name'],item['away_id'],item['away_name'], item['match_result'], item['match_time'], item['match_score']))
                except Exception as e:
                    print("数据插入表"+tableName+"失败",e)

                # 创建一个该队伍的比赛数据库
                build_database = "CREATE DATABASE IF NOT EXISTS "' %s '""
                database_name = 'matches_'+ item['team_id']
                cursor.execute(build_database % database_name)
                # 在该数据库中建立当前比赛表
                cursor.execute('use '+database_name)
                # 设置比赛表名
                match_table_name = 'match_' + item['match_id']  # 用match_id 辅助建表
                # 建立当前队伍表
                build_match_table = (
                    "CREATE TABLE IF NOT EXISTS "' %s '""
                    "(match_id VARCHAR(10) NOT NULL PRIMARY KEY,"
                    "player_1_id VARCHAR(10) NOT NULL,"
                    "player_1_name VARCHAR(20) NOT NULL,"
                    "player_1_shirtNo VARCHAR(10),"
                    "player_1_currentMarketValue VARCHAR(20) NOT NULL,"
                    "player_1_position VARCHAR(30) NOT NULL,"
                    "player_1_rate VARCHAR(10),"
                    "player_2_id VARCHAR(10) NOT NULL,"
                    "player_2_name VARCHAR(20) NOT NULL,"
                    "player_2_shirtNo VARCHAR(10),"
                    "player_2_currentMarketValue VARCHAR(20) NOT NULL,"
                    "player_2_position VARCHAR(30) NOT NULL,"
                    "player_2_rate VARCHAR(10),"
                    "player_3_id VARCHAR(10) NOT NULL,"
                    "player_3_name VARCHAR(20) NOT NULL,"
                    "player_3_shirtNo VARCHAR(10),"
                    "player_3_currentMarketValue VARCHAR(20) NOT NULL,"
                    "player_3_position VARCHAR(30) NOT NULL,"
                    "player_3_rate VARCHAR(10),"
                    "player_4_id VARCHAR(10) NOT NULL,"
                    "player_4_name VARCHAR(20) NOT NULL,"
                    "player_4_shirtNo VARCHAR(10),"
                    "player_4_currentMarketValue VARCHAR(20) NOT NULL,"
                    "player_4_position VARCHAR(30) NOT NULL,"
                    "player_4_rate VARCHAR(10),"
                    "player_5_id VARCHAR(10) NOT NULL,"
                    "player_5_name VARCHAR(20) NOT NULL,"
                    "player_5_shirtNo VARCHAR(10),"
                    "player_5_currentMarketValue VARCHAR(20) NOT NULL,"
                    "player_5_position VARCHAR(30) NOT NULL,"
                    "player_5_rate VARCHAR(10),"
                    "player_6_id VARCHAR(10) NOT NULL,"
                    "player_6_name VARCHAR(20) NOT NULL,"
                    "player_6_shirtNo VARCHAR(10),"
                    "player_6_currentMarketValue VARCHAR(20) NOT NULL,"
                    "player_6_position VARCHAR(30) NOT NULL,"
                    "player_6_rate VARCHAR(10),"
                    "player_7_id VARCHAR(10) NOT NULL,"
                    "player_7_name VARCHAR(20) NOT NULL,"
                    "player_7_shirtNo VARCHAR(10),"
                    "player_7_currentMarketValue VARCHAR(20) NOT NULL,"
                    "player_7_position VARCHAR(30) NOT NULL,"
                    "player_7_rate VARCHAR(10),"
                    "player_8_id VARCHAR(10) NOT NULL,"
                    "player_8_name VARCHAR(20) NOT NULL,"
                    "player_8_shirtNo VARCHAR(10),"
                    "player_8_currentMarketValue VARCHAR(20) NOT NULL,"
                    "player_8_position VARCHAR(30) NOT NULL,"
                    "player_8_rate VARCHAR(10),"
                    "player_9_id VARCHAR(10) NOT NULL,"
                    "player_9_name VARCHAR(20) NOT NULL,"
                    "player_9_shirtNo VARCHAR(10),"
                    "player_9_currentMarketValue VARCHAR(20) NOT NULL,"
                    "player_9_position VARCHAR(30) NOT NULL,"
                    "player_9_rate VARCHAR(10),"
                    "player_10_id VARCHAR(10) NOT NULL,"
                    "player_10_name VARCHAR(20) NOT NULL,"
                    "player_10_shirtNo VARCHAR(10),"
                    "player_10_currentMarketValue VARCHAR(20) NOT NULL,"
                    "player_10_position VARCHAR(30) NOT NULL,"
                    "player_10_rate VARCHAR(10),"
                    "player_11_id VARCHAR(10) NOT NULL,"
                    "player_11_name VARCHAR(20) NOT NULL,"
                    "player_11_shirtNo VARCHAR(10),"
                    "player_11_currentMarketValue VARCHAR(20) NOT NULL,"
                    "player_11_position VARCHAR(30) NOT NULL,"
                    "player_11_rate VARCHAR(10))"
                )
                cursor.execute(build_match_table % match_table_name)
                insert_match_sql = (
                        "INSERT INTO " + match_table_name + " VALUES "
                        "('%s', '%s', '%s', '%s', '%s','%s','%s',"
                        "'%s', '%s', '%s', '%s', '%s','%s',"
                        "'%s', '%s', '%s', '%s', '%s','%s',"
                        "'%s', '%s', '%s', '%s', '%s','%s',"
                        "'%s', '%s', '%s', '%s', '%s','%s',"
                        "'%s', '%s', '%s', '%s', '%s','%s',"
                        "'%s', '%s', '%s', '%s', '%s','%s',"
                        "'%s', '%s', '%s', '%s', '%s','%s',"
                        "'%s', '%s', '%s', '%s', '%s','%s',"
                        "'%s', '%s', '%s', '%s', '%s','%s',"
                        "'%s', '%s', '%s', '%s', '%s','%s')"
                )
                try:
                    print('insert 数据表 '+match_table_name)
                    cursor.execute(insert_match_sql % (
                        item['match_id'],
                        item['match_players'][0]['playerId'], item['match_players'][0]['playerName'],item['match_players'][0]['shirtNo'], item['match_players'][0]['currentMarketValue'],item['match_players'][0]['position'], item['match_players'][0]['rate'],
                        item['match_players'][1]['playerId'], item['match_players'][1]['playerName'],item['match_players'][1]['shirtNo'], item['match_players'][1]['currentMarketValue'],item['match_players'][1]['position'], item['match_players'][1]['rate'],
                        item['match_players'][2]['playerId'], item['match_players'][2]['playerName'],item['match_players'][2]['shirtNo'], item['match_players'][2]['currentMarketValue'],item['match_players'][2]['position'], item['match_players'][2]['rate'],
                        item['match_players'][3]['playerId'], item['match_players'][3]['playerName'],item['match_players'][3]['shirtNo'], item['match_players'][3]['currentMarketValue'],item['match_players'][3]['position'], item['match_players'][3]['rate'],
                        item['match_players'][4]['playerId'], item['match_players'][4]['playerName'],item['match_players'][4]['shirtNo'], item['match_players'][4]['currentMarketValue'],item['match_players'][4]['position'], item['match_players'][4]['rate'],
                        item['match_players'][5]['playerId'], item['match_players'][5]['playerName'],item['match_players'][5]['shirtNo'], item['match_players'][5]['currentMarketValue'],item['match_players'][5]['position'], item['match_players'][5]['rate'],
                        item['match_players'][6]['playerId'], item['match_players'][6]['playerName'],item['match_players'][6]['shirtNo'], item['match_players'][6]['currentMarketValue'],item['match_players'][6]['position'], item['match_players'][6]['rate'],
                        item['match_players'][7]['playerId'], item['match_players'][7]['playerName'],item['match_players'][7]['shirtNo'], item['match_players'][7]['currentMarketValue'],item['match_players'][7]['position'], item['match_players'][7]['rate'],
                        item['match_players'][8]['playerId'], item['match_players'][8]['playerName'],item['match_players'][8]['shirtNo'], item['match_players'][8]['currentMarketValue'],item['match_players'][8]['position'], item['match_players'][8]['rate'],
                        item['match_players'][9]['playerId'], item['match_players'][9]['playerName'],item['match_players'][9]['shirtNo'], item['match_players'][9]['currentMarketValue'],item['match_players'][9]['position'], item['match_players'][9]['rate'],
                        item['match_players'][10]['playerId'], item['match_players'][10]['playerName'],item['match_players'][10]['shirtNo'], item['match_players'][10]['currentMarketValue'],item['match_players'][10]['position'], item['match_players'][10]['rate']
                    ))
                    print('1的位置：',item['match_players'][0]['position'])
                except Exception as e:
                    print("数据插入表"+match_table_name+"失败",e)
                    pdb.set_trace()

            # connection is not autocommit by default. So you must commit to save your changes.
            cursor.close()
            if not connection.commit():
                connection.rollback()
        finally:
            connection.close()

        return item
