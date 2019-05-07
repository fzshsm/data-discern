# -*- coding: utf-8 -*-

from collections import OrderedDict
import mysql.connector
import config



class DataProcess :

    def __init__(self):
        self.conn = mysql.connector.connect(**config.MYSQL)

    def getOneGame(self):
        sql = "SELECT * FROM `hh_game` WHERE `discern` = 'no' ORDER BY `gid` ASC LIMIT 1"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def saveData(self , gameId , *forecastData):
        try:
            self.cursor = self.conn.cursor()
            self._updateGameDiscern(gameId)
            self._saveDiscernData(*forecastData)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self.cursor.close()

    def _updateGameDiscern(self ,  gameId):
        sql = "UPDATE `hh_game` SET `discern` = 'yes' WHERE `gid` = '%s' AND `discern` = 'no'" % gameId
        if self.cursor.execute(sql) == False :
            raise Exception('update %s  discern fail' % gameId)

    def _saveDiscernData(self , *forecastData):
        forecastData = OrderedDict(forecastData)
        fields = ','.join( "`%s`" % n for n in forecastData.keys())
        values = ','.join( "'%s'" % v for v in forecastData.values())
        sql = "INSERT INTO `hh_game_discern` (%s) VALUES (%s)" % (fields , values)
        if self.cursor.execute(sql) == False:
            raise Exception('save discern data fail')





mysqConn = DataProcess()
print(mysqConn.getOneGame())

try:
    raise Exception('aaaaaa')
except Exception as e:
    print(e)

