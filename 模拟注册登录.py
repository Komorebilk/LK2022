import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='likai',
                     password='@Likai0505', database='stu', charset='utf8')

cur = db.cursor()


def register(user, password):
    # 判断用户名是否重复
    sql = "select * from user where user ='%s';" % user
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return False
    try:
        sql = "insert into user (user,password) values('%s','%s');" % (user, password)
        cur.execute(sql)
        db.commit()
        cur.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print(e)
        return False


def login(user, password):
    sql = "select * from user where user = %s and password = %s;"
    cur.execute(sql, [user, password])
    result = cur.fetchone()
    if result:
        return True



while True:
    print("1>>登录")
    print("2>>注册")
    tmp = input("请输入操作序号>>")
    if tmp == '1':
        user = input("请输入用户名：")
        password = input("请输入密码：")
        if not user or not password:
            print("请正确输入:")
            continue
        else:
            if login(user, password):
                print("登录成功")
                break
            else:
                print("登录失败")


    elif tmp == '2':
        user = input("请输入用户名：")
        password = input("请输入密码：")
        if not user or not password:
            print("请正确输入:")
            continue
        else:
            if register(user, password):
                print("注册成功")
            else:
                print("用户名已经存在")

    else:
        print("输入有误")
