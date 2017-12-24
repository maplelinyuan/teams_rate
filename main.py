from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import time
import datetime
import json
import pdb

team_name_dict = {
    '英超':1,
    '西甲':2,
    '意甲':5,
    '德甲':4,
    '法甲':6,
    '巴甲':10,
    '荷甲':8,
    '葡超':7,
    '英冠':12,
    '俄超':9,
    '土超':13,
    '阿甲':11,
    '中超':3
}


class Ui_MainWindow(object):
    home_player_info_list = []
    away_player_info_list = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(MainWindow)  # 绑定label到窗口
        self.label1.setText("总场次：")  # 设置label标签的文字内容
        self.label1.setGeometry(260, 10, 60, 20)  # 设置控件相对父窗口位置宽高 参数(x,y,w,h)
        self.label2 = QtWidgets.QLabel(MainWindow)  # 绑定label到窗口
        self.label2.setText("")  # 设置label标签的文字内容
        self.label2.setGeometry(330, 10, 30, 20)  # 设置控件相对父窗口位置宽高 参数(x,y,w,h)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 10, 131, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.currentTextChanged.connect(self.on_combobox2_changed)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 720, 600))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        # 第二个表格
        self.label3 = QtWidgets.QLabel(MainWindow)  # 绑定label到窗口
        self.label3.setText("总场次：")  # 设置label标签的文字内容
        self.label3.setGeometry(1000, 10, 60, 20)  # 设置控件相对父窗口位置宽高 参数(x,y,w,h)
        self.label4 = QtWidgets.QLabel(MainWindow)  # 绑定label到窗口
        self.label4.setText("")  # 设置label标签的文字内容
        self.label4.setGeometry(1070, 10, 30, 20)  # 设置控件相对父窗口位置宽高 参数(x,y,w,h)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(750, 10, 91, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.currentTextChanged.connect(self.on_combobox3_changed)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(860, 10, 131, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.currentTextChanged.connect(self.on_combobox4_changed)
        self.tableWidget2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget2.setGeometry(QtCore.QRect(750, 60, 720, 600))
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(10)
        self.tableWidget2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(9, item)

        # 输入首发单行编辑和按钮
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(40, 670, 361, 25))
        self.lineEdit1.setObjectName("lineEdit1")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(420, 670, 81, 25))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.enterHomeLineUp)  # 用来输入主队首发

        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(740, 670, 361, 25))
        self.lineEdit2.setObjectName("lineEdit2")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(1120, 670, 81, 25))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.enterAwayLineUp)  # 用来输入客队首发

        self.textBrowser1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser1.setGeometry(QtCore.QRect(40, 700, 411, 101))
        self.textBrowser1.setObjectName("textBrowser1")

        self.textBrowser2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser2.setGeometry(QtCore.QRect(760, 700, 411, 101))
        self.textBrowser2.setObjectName("textBrowser2")

        # 自定义界面结束

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "球队具体信息"))
        self.comboBox.setItemText(0, _translate("MainWindow", "选择联赛"))
        self.comboBox.setItemText(1, _translate("MainWindow", "英超"))
        self.comboBox.setItemText(2, _translate("MainWindow", "西甲"))
        self.comboBox.setItemText(3, _translate("MainWindow", "意甲"))
        self.comboBox.setItemText(4, _translate("MainWindow", "德甲"))
        self.comboBox.setItemText(5, _translate("MainWindow", "法甲"))
        self.comboBox.setItemText(6, _translate("MainWindow", "巴甲"))
        self.comboBox.setItemText(7, _translate("MainWindow", "荷甲"))
        self.comboBox.setItemText(8, _translate("MainWindow", "葡超"))
        self.comboBox.setItemText(9, _translate("MainWindow", "英冠"))
        self.comboBox.setItemText(10, _translate("MainWindow", "俄超"))
        self.comboBox.setItemText(11, _translate("MainWindow", "土超"))
        self.comboBox.setItemText(12, _translate("MainWindow", "阿甲"))
        self.comboBox.setItemText(13, _translate("MainWindow", "中超"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "选择球队"))

        self.comboBox_3.setItemText(0, _translate("MainWindow", "选择联赛"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "英超"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "西甲"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "意甲"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "德甲"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "法甲"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "巴甲"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "荷甲"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "葡超"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "英冠"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "俄超"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "土超"))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "阿甲"))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "中超"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "选择球队"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "球员ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "球员姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "球员号码"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "球员身价"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "球员位置"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "球员评分"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "球员首发"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "首发win"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "首发draw"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "首发lose"))

        item = self.tableWidget2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "球员ID"))
        item = self.tableWidget2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "球员姓名"))
        item = self.tableWidget2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "球员号码"))
        item = self.tableWidget2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "球员身价"))
        item = self.tableWidget2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "球员位置"))
        item = self.tableWidget2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "球员评分"))
        item = self.tableWidget2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "球员首发"))
        item = self.tableWidget2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "首发win"))
        item = self.tableWidget2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "首发draw"))
        item = self.tableWidget2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "首发lose"))

        self.pushButton1.setText(_translate("MainWindow", "主队首发"))
        self.pushButton2.setText(_translate("MainWindow", "客队首发"))

    def on_combobox_changed(self):
        curent_text = self.comboBox.currentText()
        if curent_text == '选择联赛':
            return False
        current_league_id = team_name_dict[curent_text]
        current_league_name = "league_"+str(current_league_id)
        # 先连接至分析数据库获取该联赛球队列表
        db = QtSql.QSqlDatabase().addDatabase("QMYSQL")
        db.setDatabaseName(current_league_name)
        db.setHostName("127.0.0.1")  # set address
        db.setUserName("root")  # set user name
        db.setPassword("19940929")  # set user pwd
        if not db.open():
            # 打开失败
            print('打开数据库失败！')
            return db.lastError()
        print("连接数据库"'%s'"成功!" % curent_text)
        # 创建QsqlQuery对象，用于执行sql语句
        query = QtSql.QSqlQuery(db)
        query.exec('SHOW TABLES LIKE "team_all"') # 查看当前数据库是否存在全体队伍信息表
        team_all_len = query.size()
        # 如果没有全体队伍信息表就去建立
        teams_list = []
        if team_all_len < 1:
            query.exec('SHOW TABLES')
            query.next()
            for i in range(query.size()):
                team_table_name = query.value(0)
                search_name = current_league_name + '.' + team_table_name
                sub_query = QtSql.QSqlQuery(db)
                sub_query.exec('SELECT team_id,home_id,home_name,away_id,away_name FROM %s' % search_name)
                sub_query.next()
                if sub_query.value(0) == sub_query.value(1):
                    team_name = sub_query.value(2)
                else:
                    team_name = sub_query.value(4)
                team_dict = {}
                team_dict['team_id'] = sub_query.value(0)
                team_dict['team_name'] = team_name
                teams_list.append(team_dict)
                query.next()
            # 建立全体队伍信息表
            build_table = (
                "CREATE TABLE IF NOT EXISTS "' %s '""
                "(team_id VARCHAR(10) NOT NULL PRIMARY KEY,"
                "team_name VARCHAR(20) NOT NULL)"
            )
            tableName = 'team_all'
            query.exec(build_table % tableName)
            # 插入信息
            insert_sql = (
                    "INSERT INTO " + tableName + " VALUES "
                    "('%s', '%s')"
            )
            for team in teams_list:
                try:
                    query.exec(insert_sql % (team['team_id'], team['team_name']))
                except Exception as e:
                    print("数据插入表" + tableName + "失败", e)

        # 如果已经有全体队伍表或者已经建立，则读取该表，将所有队伍名写到conboBox_2中
        query.exec('SELECT * FROM team_all')
        query.next()
        combobox_teams_list = ['选择球队']
        for i in range(query.size()):
            combobox_team_name = query.value(1) + '_' +query.value(0)   # 队伍名_id
            combobox_teams_list.append(combobox_team_name)
            query.next()
        self.comboBox_2.clear()
        self.comboBox_2.addItems(combobox_teams_list)
        db.close()
        print('断开数据库')
        return

    def on_combobox3_changed(self):
        curent_text = self.comboBox_3.currentText()
        if curent_text == '选择联赛':
            return False
        current_league_id = team_name_dict[curent_text]
        current_league_name = "league_"+str(current_league_id)
        # 先连接至分析数据库获取该联赛球队列表
        db = QtSql.QSqlDatabase().addDatabase("QMYSQL")
        db.setDatabaseName(current_league_name)
        db.setHostName("127.0.0.1")  # set address
        db.setUserName("root")  # set user name
        db.setPassword("19940929")  # set user pwd
        if not db.open():
            # 打开失败
            print('打开数据库失败！')
            return db.lastError()
        print("连接数据库"'%s'"成功!" % curent_text)
        # 创建QsqlQuery对象，用于执行sql语句
        query = QtSql.QSqlQuery(db)
        query.exec('SHOW TABLES LIKE "team_all"') # 查看当前数据库是否存在全体队伍信息表
        team_all_len = query.size()
        # 如果没有全体队伍信息表就去建立
        teams_list = []
        if team_all_len < 1:
            query.exec('SHOW TABLES')
            query.next()
            for i in range(query.size()):
                team_table_name = query.value(0)
                search_name = current_league_name + '.' + team_table_name
                sub_query = QtSql.QSqlQuery(db)
                sub_query.exec('SELECT team_id,home_id,home_name,away_id,away_name FROM %s' % search_name)
                sub_query.next()
                if sub_query.value(0) == sub_query.value(1):
                    team_name = sub_query.value(2)
                else:
                    team_name = sub_query.value(4)
                team_dict = {}
                team_dict['team_id'] = sub_query.value(0)
                team_dict['team_name'] = team_name
                teams_list.append(team_dict)
                query.next()
            # 建立全体队伍信息表
            build_table = (
                "CREATE TABLE IF NOT EXISTS "' %s '""
                "(team_id VARCHAR(10) NOT NULL PRIMARY KEY,"
                "team_name VARCHAR(20) NOT NULL)"
            )
            tableName = 'team_all'
            query.exec(build_table % tableName)
            # 插入信息
            insert_sql = (
                    "INSERT INTO " + tableName + " VALUES "
                    "('%s', '%s')"
            )
            for team in teams_list:
                try:
                    query.exec(insert_sql % (team['team_id'], team['team_name']))
                except Exception as e:
                    print("数据插入表" + tableName + "失败", e)

        # 如果已经有全体队伍表或者已经建立，则读取该表，将所有队伍名写到conboBox_2中
        query.exec('SELECT * FROM team_all')
        query.next()
        combobox_teams_list = ['选择球队']
        for i in range(query.size()):
            combobox_team_name = query.value(1) + '_' +query.value(0)   # 队伍名_id
            combobox_teams_list.append(combobox_team_name)
            query.next()
        self.comboBox_4.clear()
        self.comboBox_4.addItems(combobox_teams_list)
        db.close()
        print('断开数据库')
        return

    def on_combobox2_changed(self):
        # 获取到联赛名称
        curent_league_text = self.comboBox.currentText()
        if curent_league_text == '选择联赛':
            return False
        current_league_id = str(team_name_dict[curent_league_text])
        current_league_name = "league_" + current_league_id
        # 获取到本队伍名称
        current_text = self.comboBox_2.currentText()
        if current_text == '选择球队' or current_text == '':
            return False
        print('combobox2_changed:',current_text)
        current_team_id = current_text.split('_')[1]    # 当前选中的球队ID
        current_team_scheme = 'team_' + current_team_id
        db = QtSql.QSqlDatabase().addDatabase("QMYSQL","combobox2_db")
        db.setDatabaseName(current_league_name)
        db.setHostName("127.0.0.1")  # set address
        db.setUserName("root")  # set user name
        db.setPassword("19940929")  # set user pwd
        if not db.open():
            # 打开失败
            print('打开数据库失败！')
            return db.lastError()
        print("连接数据库"'%s'"成功!" % current_team_scheme)
        query = QtSql.QSqlQuery(db)
        query.exec('SELECT match_id,home_id,away_id,match_result FROM '+current_team_scheme)  # 查看本队本赛季比赛信息
        query.next()
        # 使用列表保存比赛信息，之后遍历列表统计球员信息
        match_list = []
        for i in range(query.size()):
            match_dict = {}
            match_dict['match_id'] = query.value(0)
            match_dict['home_id'] = query.value(1)
            match_dict['away_id'] = query.value(2)
            match_dict['match_result'] = query.value(3)
            match_list.append(match_dict)
            query.next()

        # 遍历比赛列表
        db.exec('use matches_' + current_team_id)  # 切换到当前球队的比赛数据库
        # 获取本队伍球员信息表，如果没有就建表
        query.exec('SELECT * FROM player_info')
        if query.size() < 1:
            print('新建球员信息表')
            self.new_player_table(current_league_id,current_team_id,match_list)    # 还不存在，收集球员信息建立
        else:
            query.next()
            update_time = query.value(1)    # 获取更新时间，如果超过一天就更新该表
            update_time_stamp = time.mktime(time.strptime(update_time, '%Y-%m-%d %H:%M:%S'))
            now_time_stamp = time.time()
            if now_time_stamp-update_time_stamp > 86400:
                print('更新球员信息表')
                # self.update_player_table(current_league_id,current_team_id,match_list)
                # 目前是删除原有表，重新建
                query.exec('DROP TABLE player_info')
                self.new_player_table(current_league_id,current_team_id,match_list)
            else:
                print('直接读取球员信息表')  # 否则就直接读取该表
        db.close()
        print('断开数据库')
        # 读取球员信息表 player_info, 将相关信息填入表格
        self.print_form_info('matches_'+current_team_id)
        return

    def on_combobox4_changed(self):
        # 获取到联赛名称
        curent_league_text = self.comboBox_3.currentText()
        if curent_league_text == '选择联赛':
            return False
        current_league_id = str(team_name_dict[curent_league_text])
        current_league_name = "league_" + current_league_id
        # 获取到本队伍名称
        current_text = self.comboBox_4.currentText()
        if current_text == '选择球队' or current_text == '':
            return False
        print('combobox2_changed:',current_text)
        current_team_id = current_text.split('_')[1]    # 当前选中的球队ID
        current_team_scheme = 'team_' + current_team_id
        db = QtSql.QSqlDatabase().addDatabase("QMYSQL","combobox2_db")
        db.setDatabaseName(current_league_name)
        db.setHostName("127.0.0.1")  # set address
        db.setUserName("root")  # set user name
        db.setPassword("19940929")  # set user pwd
        if not db.open():
            # 打开失败
            print('打开数据库失败！')
            return db.lastError()
        print("连接数据库"'%s'"成功!" % current_team_scheme)
        query = QtSql.QSqlQuery(db)
        query.exec('SELECT match_id,home_id,away_id,match_result FROM '+current_team_scheme)  # 查看本队本赛季比赛信息
        query.next()
        # 使用列表保存比赛信息，之后遍历列表统计球员信息
        match_list = []
        for i in range(query.size()):
            match_dict = {}
            match_dict['match_id'] = query.value(0)
            match_dict['home_id'] = query.value(1)
            match_dict['away_id'] = query.value(2)
            match_dict['match_result'] = query.value(3)
            match_list.append(match_dict)
            query.next()

        # 遍历比赛列表
        db.exec('use matches_' + current_team_id)  # 切换到当前球队的比赛数据库
        # 获取本队伍球员信息表，如果没有就建表
        query.exec('SELECT * FROM player_info')
        if query.size() < 1:
            print('新建球员信息表')
            self.new_player_table(current_league_id,current_team_id,match_list)    # 还不存在，收集球员信息建立
        else:
            query.next()
            update_time = query.value(1)    # 获取更新时间，如果超过一天就更新该表
            update_time_stamp = time.mktime(time.strptime(update_time, '%Y-%m-%d %H:%M:%S'))
            now_time_stamp = time.time()
            if now_time_stamp-update_time_stamp > 86400:
                print('更新球员信息表')
                # self.update_player_table(current_league_id,current_team_id,match_list)
                # 目前是删除原有表，重新建
                query.exec('DROP TABLE player_info')
                self.new_player_table(current_league_id,current_team_id,match_list)
            else:
                print('直接读取球员信息表')  # 否则就直接读取该表
        db.close()
        print('断开数据库')
        # 读取球员信息表 player_info, 将相关信息填入表格
        self.print_form_2_info('matches_'+current_team_id)
        return


    # 根据主客场id及赛果判断该球队本场比赛胜负
    def judge_winORlose(self,teamId,match):
        result = ''
        home_id = match['home_id']
        away_id = match['away_id']
        match_result = match['match_result']
        if teamId == home_id:
            result = match_result
        elif teamId == away_id:
            if match_result == 3:
                result = 0
            elif match_result == 0:
                result = 3
            else:
                result = 1
        if result == '':
            pdb.set_trace()
        return result

    # 更新单场比赛的球员数据
    def new_player_info(self,player_dict,player_id,player_name,player_shirtNo,player_marketValue,player_position,player_rate,team_result):
        # 如果该player的id已经存在于dict中，就直接更新数据，否则新加一个key
        if player_id in player_dict.keys():
            player_dict[player_id]['name'] = player_name
            player_dict[player_id]['shirtNo'] = player_shirtNo
            player_dict[player_id]['marketValue'] = player_marketValue
            # 处理位置
            if player_position in player_dict[player_id]['position'].keys():
                player_dict[player_id]['position'][player_position] += 1
            else:
                player_dict[player_id]['position'][player_position] = 1
            # 处理位置结束
            # 处理赛果
            if team_result == 3:
                result_text = 'win'
            elif team_result == 1:
                result_text = 'draw'
            elif team_result == 0:
                result_text = 'lose'
            if result_text in player_dict[player_id]['result'].keys():
                player_dict[player_id]['result'][result_text] += 1
            else:
                player_dict[player_id]['result'][result_text] = 1
            # 处理赛果结束
            player_dict[player_id]['rate'] = str((float(player_dict[player_id]['rate']) + float(player_rate))/2)
            player_dict[player_id]['firstEleven'] += 1  # 记录首发次数
        else:
            detail_info = {}
            # 一个球员可能会踢多个位置，记录每个位置的首发次数
            player_position_info = {}
            player_position_info[player_position] = 1
            # 记录一个球员参加比赛的胜平负赛果数
            player_result = {}
            if team_result == 3:
                player_result['win'] = 1
            elif team_result == 1:
                player_result['draw'] = 1
            elif team_result == 0:
                player_result['lose'] = 1
            detail_info['name'] = player_name
            detail_info['shirtNo'] = player_shirtNo
            detail_info['marketValue'] = player_marketValue
            detail_info['position'] = player_position_info
            detail_info['rate'] = player_rate
            detail_info['firstEleven'] = 1
            detail_info['result'] = player_result
            player_dict[player_id] = detail_info
        return player_dict

    # 新建球员信息表
    def new_player_table(self,leagueId,teamId,matchList):
        match_database_name = 'matches_' + teamId
        match_db = QtSql.QSqlDatabase().addDatabase("QMYSQL","match_db")
        match_db.setDatabaseName(match_database_name)
        match_db.setHostName("127.0.0.1")  # set address
        match_db.setUserName("root")  # set user name
        match_db.setPassword("19940929")  # set user pwd
        if not match_db.open():
            # 打开失败
            print('打开数据库失败！')
            return match_db.lastError()
        print("连接数据库"'%s'"成功!" % match_database_name)
        query = QtSql.QSqlQuery(match_db)
        # 建立本队伍球员字典：
        player_dict = {}
        match_total = len(matchList)  # 比赛总轮数
        for match in matchList:
            match_id = match['match_id']
            query.exec('SELECT * FROM match_%s' % match_id)
            query.next()
            # 调用函数
            team_result = self.judge_winORlose(teamId,match)
            player_dict = self.new_player_info(player_dict,query.value(1),query.value(2),query.value(3),query.value(4),query.value(5),query.value(6),team_result)
            player_dict = self.new_player_info(player_dict,query.value(7),query.value(8),query.value(9),query.value(10),query.value(11),query.value(12),team_result)
            player_dict = self.new_player_info(player_dict,query.value(13),query.value(14),query.value(15),query.value(16),query.value(17),query.value(18),team_result)
            player_dict = self.new_player_info(player_dict,query.value(19),query.value(20),query.value(21),query.value(22),query.value(23),query.value(24),team_result)
            player_dict = self.new_player_info(player_dict,query.value(25),query.value(26),query.value(27),query.value(28),query.value(29),query.value(30),team_result)
            player_dict = self.new_player_info(player_dict,query.value(31),query.value(32),query.value(33),query.value(34),query.value(35),query.value(36),team_result)
            player_dict = self.new_player_info(player_dict,query.value(37),query.value(38),query.value(39),query.value(40),query.value(41),query.value(42),team_result)
            player_dict = self.new_player_info(player_dict,query.value(43),query.value(44),query.value(45),query.value(46),query.value(47),query.value(48),team_result)
            player_dict = self.new_player_info(player_dict,query.value(49),query.value(50),query.value(51),query.value(52),query.value(53),query.value(54),team_result)
            player_dict = self.new_player_info(player_dict,query.value(55),query.value(56),query.value(57),query.value(58),query.value(59),query.value(60),team_result)
            player_dict = self.new_player_info(player_dict,query.value(61),query.value(62),query.value(63),query.value(64),query.value(65),query.value(66),team_result)
        now_time_stamp = time.time()
        timestruct = time.localtime(now_time_stamp)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', timestruct)
        # 建立队伍信息表
        build_table = (
            "CREATE TABLE IF NOT EXISTS "' %s '""
            "(player_id VARCHAR(10) NOT NULL PRIMARY KEY,"
            "update_time VARCHAR(20) NOT NULL,"
            "player_name VARCHAR(20) NOT NULL,"
            "player_shirtNo VARCHAR(20) NOT NULL,"
            "player_marketValue VARCHAR(20) NOT NULL,"
            "player_position VARCHAR(50) NOT NULL,"
            "player_rate VARCHAR(20) NOT NULL,"
            "player_firstEleven INT(6) NOT NULL,"
            "match_total INT(6) NOT NULL,"
            "player_result VARCHAR(50) NOT NULL)"
        )
        tableName = 'player_info'
        query.exec(build_table % tableName)
        # 插入信息
        insert_sql = (
                "INSERT INTO " + tableName + " VALUES "
                 "('%s','%s','%s','%s','%s','%s','%s',%d,%d,'%s')"
        )
        for playerId in player_dict.keys():
            single_player_info = player_dict[playerId]
            # 遍历球员位置字典
            single_player_position_text = ''
            for player_position in single_player_info['position'].keys():
                player_position_name = player_position
                player_position_total = single_player_info['position'][player_position]
                single_player_position_text += player_position_name+'_'+str(player_position_total)+' '
            single_player_position_text = single_player_position_text.strip()
            # 遍历球员赛果字典
            single_player_result_text = ''
            for player_result in single_player_info['result'].keys():
                player_result_name = player_result
                player_result_total = single_player_info['result'][player_result]
                single_player_result_text += player_result_name+'_'+str(player_result_total)+' '
            single_player_result_text = single_player_result_text.strip()
            try:
                query.exec(insert_sql % (playerId,now_time,single_player_info['name'],single_player_info['shirtNo'],single_player_info['marketValue'],single_player_position_text,single_player_info['rate'],single_player_info['firstEleven'],match_total,single_player_result_text))
            except Exception as e:
                print("数据插入表" + tableName + "失败", e)

        match_db.close()
        print('new_table 断开match_db')
        return

    # 打印表格信息
    def print_form_info(self, matches_name):
        print('开始获取球员信息')
        db = QtSql.QSqlDatabase().addDatabase("QMYSQL","print_db")
        db.setDatabaseName(matches_name)
        db.setHostName("127.0.0.1")  # set address
        db.setUserName("root")  # set user name
        db.setPassword("19940929")  # set user pwd
        if not db.open():
            # 打开失败
            print('打开数据库失败！')
            return db.lastError()
        print("连接数据库"'%s'"成功!" % matches_name)
        query = QtSql.QSqlQuery(db)
        query.exec('SELECT * FROM player_info')  # 查看本队球员信息
        query.next()
        # 使用列表保存球员信息，之后遍历列表打印球员信息
        print('开始整理球员信息')
        player_info_list = []
        total_competition = '' # 本队伍本赛季比赛总场次
        for i in range(query.size()):
            print('球员信息更新时间：',query.value(1))
            player_info_dict = {}
            player_info_dict['id'] = query.value(0)
            player_info_dict['name'] = query.value(2)
            player_info_dict['shirtNo'] = query.value(3)
            player_info_dict['marketValue'] = query.value(4)
            player_info_dict['position'] = query.value(5)
            player_info_dict['rate'] = query.value(6)
            player_info_dict['firstEleven'] = str(query.value(7))
            result_text = query.value(9)
            result_list = result_text.split(' ')
            result_win_total = 0
            result_draw_total = 0
            result_lose_total = 0
            for single_result in result_list:
                result_text = single_result.split('_')[0]
                result_total = single_result.split('_')[1]
                if result_text == 'win':
                    result_win_total = result_total
                elif result_text == 'draw':
                    result_draw_total = result_total
                else:
                    result_lose_total = result_total
            player_info_dict['player_result_win'] = result_win_total
            player_info_dict['player_result_draw'] = result_draw_total
            player_info_dict['player_result_lose'] = result_lose_total
            player_info_list.append(player_info_dict)
            total_competition = str(query.value(8))
            query.next()

        db.close()
        print('断开player_info数据库')
        print('开始打印球员信息')
        self.label2.setText(total_competition)  # 设置本赛季比赛总场次
        # 先清空所有表项
        self.tableWidget.clearContents()
        # 设置行数
        self.tableWidget.setRowCount(len(player_info_list))
        row_count = 0
        # 将当前主队球员信息保存到全局
        self.home_player_info_list = player_info_list
        for i in range(len(player_info_list)):
            # 循环填入数据
            col_count = 0
            for j in range(self.tableWidget.columnCount()):
                if col_count == 0:
                    cnt = '%s' % (
                        player_info_list[i]['id']
                    )
                elif col_count == 1:
                    cnt = '%s' % (
                        player_info_list[i]['name']
                    )
                elif col_count == 2:
                    cnt = '%s' % (
                        player_info_list[i]['shirtNo']
                    )
                elif col_count == 3:
                    cnt = '%s' % (
                        player_info_list[i]['marketValue']
                    )
                elif col_count == 4:
                    cnt = '%s' % (
                        player_info_list[i]['position']
                    )
                elif col_count == 5:
                    cnt = '%.2f' % (
                        round(float(player_info_list[i]['rate']),2)
                    )
                elif col_count == 6:
                    cnt = '%d' % (
                        int(player_info_list[i]['firstEleven'])
                    )
                elif col_count == 7:
                    cnt = '%d' % (
                        int(player_info_list[i]['player_result_win'])
                    )
                elif col_count == 8:
                    cnt = '%d' % (
                        int(player_info_list[i]['player_result_draw'])
                    )
                elif col_count == 9:
                    cnt = '%d' % (
                        int(player_info_list[i]['player_result_lose'])
                    )
                newItem = QtWidgets.QTableWidgetItem(cnt)
                self.tableWidget.setItem(row_count, col_count, newItem)
                col_count += 1
            row_count += 1
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setSortingEnabled(True)
        return

    # 打印表格2信息
    def print_form_2_info(self, matches_name):
        print('开始获取球员信息')
        db = QtSql.QSqlDatabase().addDatabase("QMYSQL", "print_db")
        db.setDatabaseName(matches_name)
        db.setHostName("127.0.0.1")  # set address
        db.setUserName("root")  # set user name
        db.setPassword("19940929")  # set user pwd
        if not db.open():
            # 打开失败
            print('打开数据库失败！')
            return db.lastError()
        print("连接数据库"'%s'"成功!" % matches_name)
        query = QtSql.QSqlQuery(db)
        query.exec('SELECT * FROM player_info')  # 查看本队球员信息
        query.next()
        # 使用列表保存球员信息，之后遍历列表打印球员信息
        print('开始整理球员信息')
        player_info_list = []
        total_competition = ''  # 本队伍本赛季比赛总场次
        for i in range(query.size()):
            print('球员信息更新时间：', query.value(1))
            player_info_dict = {}
            player_info_dict['id'] = query.value(0)
            player_info_dict['name'] = query.value(2)
            player_info_dict['shirtNo'] = query.value(3)
            player_info_dict['marketValue'] = query.value(4)
            player_info_dict['position'] = query.value(5)
            player_info_dict['rate'] = query.value(6)
            player_info_dict['firstEleven'] = str(query.value(7))
            result_text = query.value(9)
            result_list = result_text.split(' ')
            result_win_total = 0
            result_draw_total = 0
            result_lose_total = 0
            for single_result in result_list:
                result_text = single_result.split('_')[0]
                result_total = single_result.split('_')[1]
                if result_text == 'win':
                    result_win_total = result_total
                elif result_text == 'draw':
                    result_draw_total = result_total
                else:
                    result_lose_total = result_total
            player_info_dict['player_result_win'] = result_win_total
            player_info_dict['player_result_draw'] = result_draw_total
            player_info_dict['player_result_lose'] = result_lose_total
            player_info_list.append(player_info_dict)
            total_competition = str(query.value(8))
            query.next()

        db.close()
        print('断开player_info数据库')
        print('开始打印球员信息')
        self.label4.setText(total_competition)  # 设置本赛季比赛总场次
        # 先清空所有表项
        self.tableWidget2.clearContents()
        # 设置行数
        self.tableWidget2.setRowCount(len(player_info_list))
        row_count = 0
        # 将当前主队球员信息保存到全局
        self.away_player_info_list = player_info_list
        for i in range(len(player_info_list)):
            # 循环填入数据
            col_count = 0
            for j in range(self.tableWidget2.columnCount()):
                if col_count == 0:
                    cnt = '%s' % (
                        player_info_list[i]['id']
                    )
                elif col_count == 1:
                    cnt = '%s' % (
                        player_info_list[i]['name']
                    )
                elif col_count == 2:
                    cnt = '%s' % (
                        player_info_list[i]['shirtNo']
                    )
                elif col_count == 3:
                    cnt = '%s' % (
                        player_info_list[i]['marketValue']
                    )
                elif col_count == 4:
                    cnt = '%s' % (
                        player_info_list[i]['position']
                    )
                elif col_count == 5:
                    cnt = '%.2f' % (
                        round(float(player_info_list[i]['rate']), 2)
                    )
                elif col_count == 6:
                    cnt = '%d' % (
                        int(player_info_list[i]['firstEleven'])
                    )
                elif col_count == 7:
                    cnt = '%d' % (
                        int(player_info_list[i]['player_result_win'])
                    )
                elif col_count == 8:
                    cnt = '%d' % (
                        int(player_info_list[i]['player_result_draw'])
                    )
                elif col_count == 9:
                    cnt = '%d' % (
                        int(player_info_list[i]['player_result_lose'])
                    )
                newItem = QtWidgets.QTableWidgetItem(cnt)
                self.tableWidget2.setItem(row_count, col_count, newItem)
                col_count += 1
            row_count += 1
        self.tableWidget2.resizeColumnsToContents()
        self.tableWidget2.setSortingEnabled(True)
        return

    def enterHomeLineUp(self):
        lineup = self.lineEdit1.text().strip()
        const_lineup_list = lineup.split(',')   # 不变的输入list
        lineup_list = lineup.split(',')
        if len(lineup_list) != 11:
            print('请用逗号分隔，输入11位首发球员号码')
            return False
        # 遍历保存下来的主队球员信息利列表
        lineup_player_list = []
        competition_total = int(self.label2.text())  # 主队总场数
        for player in self.home_player_info_list:
            lineup_player_info = {}
            if player['shirtNo'] in lineup_list:
                lineup_player_info['rate'] = player['rate']
                lineup_player_info['firstEleven'] = player['firstEleven']
                lineup_player_info['win'] = player['player_result_win']
                lineup_player_info['draw'] = player['player_result_draw']
                lineup_player_info['lose'] = player['player_result_draw']
                lineup_player_info['marketValue'] = player['marketValue']
                lineup_player_list.append(lineup_player_info)
                lineup_list.remove(player['shirtNo'])  # 移除已经查找到的球员
            # # 如果不在所有球员列表中，就全部设为0
            # elif not player['shirtNo'] in const_lineup_list:
            #     lineup_player_info['rate'] = 6.0
            #     lineup_player_info['firstEleven'] = 0
            #     lineup_player_info['win'] = 0
            #     lineup_player_info['draw'] = 0
            #     lineup_player_info['lose'] = 0
            #     lineup_player_info['marketValue'] = 0
            #     lineup_player_list.append(lineup_player_info)
            # 计算首发平均分，平均首发率，平均win,平均draw,平均lose
        # 将之前没参加过比赛本轮新加入的人添加默认数据信息
        need_player_list_len = 11 - len(lineup_player_list)
        for i in range(need_player_list_len):
            lineup_player_info = {}
            lineup_player_info['rate'] = 6.0
            lineup_player_info['firstEleven'] = 0
            lineup_player_info['win'] = 0
            lineup_player_info['draw'] = 0
            lineup_player_info['lose'] = 0
            lineup_player_info['marketValue'] = 0
            lineup_player_list.append(lineup_player_info)

        total_rate = 0
        total_firstEleven = 0
        total_win = 0
        total_draw = 0
        total_lose = 0
        total_marketValue = 0
        for player in lineup_player_list:
            total_rate += float(player['rate'])
            total_firstEleven += int(player['firstEleven'])
            total_win += int(player['win'])
            total_draw += int(player['draw'])
            total_lose += int(player['lose'])
            total_marketValue += int(player['marketValue'])
        avarage_rate = round(total_rate / 11, 2)
        avarage_firstEleven = round(total_firstEleven / 11, 2)
        firstEleven_ratio = round(total_firstEleven / (11 * competition_total), 2)
        win_ratio = round(total_win / (11 * competition_total), 2)
        draw_ratio = round(total_draw / (11 * competition_total), 2)
        lose_ratio = round(total_lose / (11 * competition_total), 2)
        avarage_marketValue = round(total_marketValue / 11, 2)
        print_text = '平均分：' + str(avarage_rate) + ' 平均首发：' + str(avarage_firstEleven) + ' 首发率：' + str(
            firstEleven_ratio) + ' 平均身价：' + str(avarage_marketValue) + ' 胜率：' + str(win_ratio) + ' 平率：' + str(
            draw_ratio) + ' 负率：' + str(lose_ratio)
        self.textBrowser1.setText(print_text)


    def enterAwayLineUp(self):
        lineup = self.lineEdit2.text().strip()
        const_lineup_list = lineup.split(',')  # 不变的输入list
        lineup_list = lineup.split(',')
        if len(lineup_list) != 11:
            print('请用逗号分隔，输入11位首发球员号码')
            return False
        # 遍历保存下来的主队球员信息利列表
        lineup_player_list = []
        competition_total = int(self.label4.text())  # 客队总场数
        for player in self.away_player_info_list:
            lineup_player_info = {}
            if player['shirtNo'] in lineup_list:
                lineup_player_info['rate'] = player['rate']
                lineup_player_info['firstEleven'] = player['firstEleven']
                lineup_player_info['win'] = player['player_result_win']
                lineup_player_info['draw'] = player['player_result_draw']
                lineup_player_info['lose'] = player['player_result_draw']
                lineup_player_info['marketValue'] = player['marketValue']
                lineup_player_list.append(lineup_player_info)
                lineup_list.remove(player['shirtNo'])  # 移除已经查找到的球员
            # # 如果不在所有球员列表中，就全部设为0
            # elif not player['shirtNo'] in const_lineup_list:
            #     lineup_player_info['rate'] = 6.0
            #     lineup_player_info['firstEleven'] = 0
            #     lineup_player_info['win'] = 0
            #     lineup_player_info['draw'] = 0
            #     lineup_player_info['lose'] = 0
            #     lineup_player_info['marketValue'] = 0
            #     lineup_player_list.append(lineup_player_info)
        # 将之前没参加过比赛本轮新加入的人添加默认数据信息
        need_player_list_len = 11 - len(lineup_player_list)
        for i in range(need_player_list_len):
            lineup_player_info = {}
            lineup_player_info['rate'] = 6.0
            lineup_player_info['firstEleven'] = 0
            lineup_player_info['win'] = 0
            lineup_player_info['draw'] = 0
            lineup_player_info['lose'] = 0
            lineup_player_info['marketValue'] = 0
            lineup_player_list.append(lineup_player_info)

        # 计算首发平均分，平均首发率，平均win,平均draw,平均lose
        total_rate = 0
        total_firstEleven = 0
        total_win = 0
        total_draw = 0
        total_lose = 0
        total_marketValue = 0
        for player in lineup_player_list:
            total_rate += float(player['rate'])
            total_firstEleven += int(player['firstEleven'])
            total_win += int(player['win'])
            total_draw += int(player['draw'])
            total_lose += int(player['lose'])
            total_marketValue += int(player['marketValue'])
        avarage_rate = round(total_rate / 11, 2)
        avarage_firstEleven = round(total_firstEleven / 11, 2)
        firstEleven_ratio = round(total_firstEleven / (11 * competition_total), 2)
        win_ratio = round(total_win / (11 * competition_total), 2)
        draw_ratio = round(total_draw / (11 * competition_total), 2)
        lose_ratio = round(total_lose / (11 * competition_total), 2)
        avarage_marketValue = round(total_marketValue / 11, 2)
        print_text = '平均分：' + str(avarage_rate) + ' 平均首发：' + str(avarage_firstEleven) + ' 首发率：' + str(
            firstEleven_ratio) + ' 平均身价：'+str(avarage_marketValue) + ' 胜率：' + str(win_ratio) + ' 平率：' + str(draw_ratio) + ' 负率：' + str(lose_ratio)
        self.textBrowser2.setText(print_text)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
