import pymysql  # 连接Mysql
from sys import exit  # 退出
from os import system  # 清空控制台


def conn():  # 连接Mysql的函数
    db = pymysql.connect(host='localhost', user='root', passwd='233233', db='名片', charset='utf8')
    return db


def close(self):  # 关闭连接的函数
    self.cursor.close()  # 关闭游标
    self.db.close()  # 关闭连接


def f1():  # 实现功能1
    system('cls')  # 清空控制台
    print("**" * 20)
    db = conn()
    try:
        new_name = input("请输入姓名：")
        new_sex = input("请输入性别：")
        new_age = int(input("请输入年龄："))
        cursor = db.cursor()  # 创建游标
        sql_insert = "insert into Namecard values('%s','%s',%d)" % (new_name, new_sex, new_age)  # T-SQL语句
        cursor.execute(sql_insert)  # 执行语句
        db.commit()  # 保存
        print("添加成功！")
    except Exception as e:
        db.rollback()  # 出现异常回滚
        print("失败！", e)
    db.close()  # 关闭连接
    xuan_ze()  # 继续运行


def f2():  # 实现功能2
    system('cls')
    print("**" * 20)
    db = conn()
    try:
        cname = input("请输入删除人姓名：")
        cursor = db.cursor()
        sql_delete = "delete from Namecard where 姓名='%s'" % cname  # T-SQL语句
        cursor.execute(sql_delete)
        db.commit()
    except Exception as e:
        db.rollback()
        print("失败！", e)
    db.close()
    xuan_ze()


def f3():  # 实现功能3
    system('cls')
    print("**" * 20)
    db = conn()
    try:
        cname = input("请输入修改姓名：")
        new_name = input("请输入姓名：")
        new_sex = input("请输入性别：")
        new_age = int(input("请输入年龄："))
        cursor = db.cursor()
        sql = "update Namecard set 姓名='%s',性别='%s',年龄=%d where 姓名='%s'" % (new_name, new_sex, new_age, cname)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print("失败！", e)
    db.close()
    xuan_ze()


def f4():  # 实现功能4
    system('cls')
    print("**" * 20)
    db = conn()
    try:
        cname = input("请输入查询姓名：")
        cursor = db.cursor()
        sql = "select * from Namecard where 姓名='%s'" % cname  # T-SQL语句 查询时不需要 commit()
        cursor.execute(sql)
        result = cursor.fetchone()
        print("姓名：",result[0],"\t性别：",result[1],"\t年龄：",result[2])
    except Exception as e:
        print("失败！", e)
    db.close()
    xuan_ze()


def f5():  # 实现功能5
    system('cls')
    print("**" * 20)
    db = conn()
    try:
        print("姓名\t性别\t年龄")
        cursor = db.cursor()
        sql = "select * from Namecard"  # T-SQL语句
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], "\t", data[1], "\t", data[2])
    except Exception as e:
        print("失败！", e)
    db.close()
    xuan_ze()


def f6():  # 实现功能6
    exit()  # 退出函数


def xuan_ze():  # 实现选择
    print("**" * 20)
    print("1.添加名片", "\t"*3, "2.删除名片", "\t"*3, "3.修改名片")
    print("4.查询名片", "\t"*3, "5.获取所有名片信息", "\t"*2, "6.退出系统")
    # 打印
    c = int(input("选择："))
    # 获取选项
    if c == 1:
        f1()
    elif c == 2:
        f2()
    elif c == 3:
        f3()
    elif c == 4:
        f4()
    elif c == 5:
        f5()
    elif c == 6:
        f6()
    else:
        print("请选择数字1~6")
        xuan_ze()
    # 判断选项


xuan_ze()
# 执行