'''
作者：桑忠人 18281160
时间：2020.11
描述：本server版权为 北京交通大学计算机学院 桑忠人 18281160 所有！
'''

from django.shortcuts import render, redirect
import MySQLdb


# Create your views here.
#登录界面
def login(request):
    if request.method == 'GET':
        print("get login.html")
        return render(request, 'cli1/login.html')
    else:
        admin_name = request.POST.get('admin_name', '')
        admin_id = request.POST.get('admin_id', '')
        user_id = request.POST.get('u_id', '')
        user_password = request.POST.get('u_password', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT WORK_ID FROM adminors WHERE NAME=%s", [admin_name])
            result = cursor.fetchall()
            cursor.execute("SELECT * FROM users WHERE ID = %s", [user_id])
            u_result = cursor.fetchall()
        if len(admin_name) != 0 or len(admin_id) != 0:
            if not result or admin_id != result[0]["WORK_ID"]:
                print(len(admin_name), admin_id)
                print(result)
                mesg = '用户名或工号输入错误！请重新输入!'
                return render(request, 'cli1/login.html', {'message': mesg})
            else:
                print(admin_name, admin_id)
                return render(request, 'cli1/content.html')
        else:
            if not u_result or user_password != u_result[0]["U_PASSWORD"]:
                mesg = "用户名或密码输入错误！请重新输入!"
                return render(request, 'cli1/login.html', {'message': mesg})
            else:
                print(u_result)
                u_name = u_result[0]["NAME"]
                with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
                    cursor.execute("SELECT * FROM videos WHERE AUTHOR = %s", [u_name])
                    videos = cursor.fetchall()
                    print(not videos)
                    print(len(videos))
                if videos:
                    video0 = videos[0]
                    # mesg = '登陆成功！'
                    return render(request, 'cli1/u_index.html',
                                  {'users': u_result, 'videos': videos, 'video0': video0, 'u_v_name':u_name})
                else:
                    # mesg = '登录成功！'
                    return render(request, 'cli1/u_index.html',
                                  {'users': u_result, 'videos': videos, 'u_v_name':u_name})

def login_1(request):
    if request.method == 'GET':
        print("get login.html")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT MAX(ID) FROM users")
            users_id = cursor.fetchall()[0]['MAX(ID)']
        mesg = '注册成功！账号为：' + str(users_id)
        return render(request, 'cli1/login_1.html', {'message':mesg})
    else:
        admin_name = request.POST.get('admin_name', '')
        admin_id = request.POST.get('admin_id', '')
        user_id = request.POST.get('u_id', '')
        user_password = request.POST.get('u_password', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT WORK_ID FROM adminors WHERE NAME=%s", [admin_name])
            result = cursor.fetchall()
            cursor.execute("SELECT * FROM users WHERE ID = %s", [user_id])
            u_result = cursor.fetchall()
        if len(admin_name) != 0 or len(admin_id) != 0:
            if not result or admin_id != result[0]["WORK_ID"]:
                print(len(admin_name), admin_id)
                print(result)
                mesg = '用户名或工号输入错误！请重新输入!'
                return render(request, 'cli1/login_1.html', {'message': mesg})
            else:
                print(admin_name, admin_id)
                return render(request, 'cli1/content.html')
        else:
            if not u_result or user_password != u_result[0]["U_PASSWORD"]:
                mesg = "用户名或密码输入错误！请重新输入!"
                return render(request, 'cli1/login.html', {'message': mesg})
            else:
                print(u_result)
                u_name = u_result[0]["NAME"]
                with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
                    cursor.execute("SELECT * FROM videos WHERE AUTHOR = %s", [u_name])
                    videos = cursor.fetchall()
                    print(not videos)
                    print(len(videos))
                if videos:
                    video0 = videos[0]
                    # mesg = '登陆成功！'
                    return render(request, 'cli1/u_index.html',
                                  {'users': u_result, 'videos': videos, 'video0': video0, 'u_v_name':u_name})
                else:
                    # mesg = '登录成功！'
                    return render(request, 'cli1/u_index.html',
                                  {'users': u_result, 'videos': videos, 'u_v_name':u_name})

def u_index(request):
    if request.method == 'GET':
        u_name = request.POST.get("u_name")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM users WHERE NAME = %s", [u_name])
            users = cursor.fetchall()
            cursor.execute("SELECT * FROM videos WHERE AUTHOR = %s", [u_name])
            videos = cursor.fetchall()
        if videos:
            video0 = videos[0]
            mesg = '添加成功'
            return render(request, 'cli1/u_index.html',
                          {'users': users, 'videos': videos, 'video0': video0, 'message': mesg, 'u_v_name':u_name})
        else:
            mesg = '添加成功'
            return render(request, 'cli1/u_index.html',
                          {'users': users, 'videos': videos, 'message': mesg, 'u_v_name':u_name})

def u_v_add(request):
    if request.method == 'GET':
        u_name = request.GET.get("v_u_name")
        print(u_name)
        return render(request, 'cli1/u_v_add.html', {'u_name':u_name})
    else:
        video_author = request.POST.get('video_author', '')
        video_intro = request.POST.get('video_intro', '')
        video_loca = request.POST.get('video_loca', '')
        print(video_loca)
        # user_age = request.POST.get('user_age', '')
        # user_age = int(user_age)
        conn = MySQLdb.connect(host='localhost', user='root', passwd="000606", db="short_video_platform", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO videos (AUTHOR,INTRO,LOCATION)"
                           "VALUES (%s, %s, %s)", [video_author, video_intro, video_loca])
            conn.commit()
            cursor.execute("SELECT * FROM videos WHERE AUTHOR = %s", [video_author])
            videos = cursor.fetchall()
            cursor.execute("SELECT * FROM users WHERE NAME = %s", [video_author])
            users = cursor.fetchall()
        if videos:
            video0 = videos[0]
            mesg = '添加成功'
            return render(request, 'cli1/u_index.html',
                          {'users': users, 'videos': videos, 'video0': video0, 'message': mesg, 'u_v_name':video_author})
        else:
            mesg = '添加成功'
            return render(request, 'cli1/u_index.html',
                          {'users': users, 'videos': videos, 'message': mesg, 'u_v_name':video_author})


def u_delete(request):
    # u_name = request.GET.get("u_name")
    v_id = request.GET.get("v_id")
    print(v_id)
    conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("SELECT AUTHOR FROM videos WHERE NO = %s", [v_id])
        u_name = cursor.fetchall()
        print(u_name)
        cursor.execute("DELETE FROM videos WHERE NO = %s", [v_id])
        # cursor.execute("CALL USERDELECT(%s)", [id])
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE NAME = %s", [u_name[0]['AUTHOR']])
        users = cursor.fetchall()
        cursor.execute("SELECT * FROM videos WHERE AUTHOR = %s", [u_name[0]['AUTHOR']])
        videos = cursor.fetchall()
    if videos:
        video0 = videos[0]
        mesg = '删除成功'
        return render(request, 'cli1/u_index.html',
                      {'users': users, 'videos': videos, 'video0': video0, 'message': mesg, 'u_v_name':u_name})
    else:
        mesg = '删除成功'
        return render(request, 'cli1/u_index.html',
                      {'users': users, 'videos': videos, 'message': mesg, 'u_v_name':u_name})

def u_edit(request):
    if request.method == 'GET':
        id = request.GET.get("ID")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM users WHERE ID = %s", [id])
            users = cursor.fetchone()
        return render(request, 'cli1/u_edit.html', {'users':users})
    else:
        id = request.POST.get("ID")
        user_name = request.POST.get('user_name', '')
        user_age = request.POST.get('user_age', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
            conn.commit()
            cursor.execute("UPDATE users SET NAME=%s,AGE=%s WHERE ID=%s",
                           [user_name, user_age, id])
            conn.commit()
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
            conn.commit()
            cursor.execute("SELECT * FROM users WHERE ID = %s", [id])
            users = cursor.fetchall()
            cursor.execute("SELECT * FROM videos WHERE AUTHOR = %s", [user_name])
            videos = cursor.fetchall()
        if videos:
            video0 = videos[0]
            mesg = '修改成功'
            return render(request, 'cli1/u_index.html',
                          {'users': users, 'videos': videos, 'video0': video0, 'message': mesg, 'u_v_name': user_name})
        else:
            mesg = '修改成功'
            return render(request, 'cli1/u_index.html',
                          {'users': users, 'videos': videos, 'message': mesg, 'u_v_name': user_name})


#注册界面
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'cli1/sign_up.html')
    else:
        user_name = request.POST.get('u_name', '')
        user_sex = request.POST.get('u_sex', '')
        user_age = request.POST.get('u_age', '')
        user_password = request.POST.get('u_password', '')
        print(user_password)
        h_password = hash(user_password)
        h_password = str(h_password)
        print(h_password)
        conn = MySQLdb.connect(host='localhost', user='root', passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO users (NAME,SEX,AGE,U_PASSWORD)"
                           "VALUES (%s, %s, %s, %s)", [user_name, user_sex, user_age, user_password])
            conn.commit()
            cursor.execute("SELECT MAX(ID) FROM users")
            users_id = cursor.fetchall()[0]['MAX(ID)']
        mesg = '注册成功！账号为：' + str(users_id)
        # return render(request, 'cli1/login_1.html', {'message': mesg})
        return redirect('/sim/login_1/', mesg)

#目录网页
def content(request):
    if request.method == 'GET':
        return render(request, 'cli1/content.html')


#建立查询的操作函数
def index(request):
    if request.method == 'GET':
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM users WHERE ID<1001")
            users = cursor.fetchall()
        return render(request, 'cli1/index.html', {'users': users})


#添加用户信息
def add(request):
    if request.method == 'GET':
        return render(request, 'cli1/add.html')
    else:
        user_name = request.POST.get('user_name', '')
        user_sex = request.POST.get('user_sex', '')
        user_age = request.POST.get('user_age', '')
        # user_age = int(user_age)
        conn = MySQLdb.connect(host='localhost', user='root', passwd="000606", db="short_video_platform", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO users (NAME,SEX,AGE)"
                           "VALUES (%s, %s, %s)", [user_name,user_sex,user_age])
            conn.commit()
            cursor.execute("SELECT MAX(ID) FROM users")
            users_id = cursor.fetchall()[0]['MAX(ID)']
            print(users_id)
            cursor.execute("SELECT * from users WHERE ID = %s", [users_id])
            users = cursor.fetchall()
        mesg = '添加成功！ID为:'+str(users_id)
        return render(request, 'cli1/index.html', {'users': users, 'message':mesg})

#删除用户信息
def delete(request):
    id = request.GET.get("ID")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM users WHERE ID = %s", [id])
        # cursor.execute("CALL USERDELECT(%s)", [id])
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE ID<1001")
        users = cursor.fetchall()
    mesg = '删除成功！'
    return render(request, 'cli1/index.html', {'users': users, 'message':mesg})



#更改用户信息
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("ID")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM users WHERE ID = %s", [id])
            users = cursor.fetchone()
        return render(request, 'cli1/edit.html', {'users':users})
    else:
        id = request.POST.get("ID")
        user_name = request.POST.get('user_name', '')
        # user_sex = request.POST.get('user_sex', '')
        user_age = request.POST.get('user_age', '')
        user_fans = request.POST.get('user_fans', '')
        user_follows = request.POST.get('user_follows', '')
        user_pub = request.POST.get('user_pub', '')
        user_favorites = request.POST.get('user_favorites', '')
        print(user_name, user_age, user_fans, user_follows, user_pub, user_favorites, id)
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE users SET NAME=%s,AGE=%s,FANS=%s,FOLLOWS=%s,PUBLISHED=%s,FAVORITES=%s WHERE ID=%s",
                           [user_name, user_age, user_fans, user_follows, user_pub, user_favorites, id])
            conn.commit()
            cursor.execute("SELECT * FROM users WHERE ID = %s", [id])
            users = cursor.fetchall()
        mesg = '修改成功！'
        return render(request, 'cli1/index.html', {'users': users, 'message':mesg})


def find(request):
    if request.method == 'GET':
        return render(request, 'cli1/find.html')
    else:
        user_id = request.POST.get('user_id', '')
        conn = MySQLdb.connect(host='localhost', user='root', passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM users WHERE ID=%s", [user_id])
            result = cursor.fetchall()
        if len(result) == 0:
            # return HttpResponse("查无此人！请输入正确的用户ID！")
            message = '查无此人！请输入正确的用户ID！'
            return render(request, 'cli1/find.html', {'message':message})
        else:
            mesg = '查询成功！'
            return render(request, 'cli1/index.html', {'users':result, 'message':mesg})

#建立视频表查询的操作函数
def v_index(request):
    if request.method == 'GET':
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM videos")
            users = cursor.fetchall()
        return render(request, 'cli1/v_index.html', {'users': users})


#添加用户信息
def v_add(request):
    if request.method == 'GET':
        return render(request, 'cli1/v_add.html')
    else:
        video_author = request.POST.get('video_author', '')
        video_intro = request.POST.get('video_intro', '')
        # user_age = request.POST.get('user_age', '')
        # user_age = int(user_age)
        conn = MySQLdb.connect(host='localhost', user='root', passwd="000606", db="short_video_platform", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO videos (AUTHOR,INTRO)"
                           "VALUES (%s, %s)", [video_author, video_intro])
            conn.commit()
            cursor.execute("SELECT * FROM videos")
            users = cursor.fetchall()
        mesg = '添加成功'
        return render(request, 'cli1/v_index.html', {'users': users, 'message':mesg})

#删除视频信息
def v_delete(request):
    id = request.GET.get("ID")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM videos WHERE ID = %s", [id])
        # cursor.execute("CALL USERDELECT(%s)", [id])
        conn.commit()
        cursor.execute("SELECT * FROM videos")
        users = cursor.fetchall()
    mesg = '删除成功！'
    return render(request, 'cli1/v_index.html', {'users': users, 'message':mesg})



#更改视频信息
def v_edit(request):
    if request.method == 'GET':
        no = request.GET.get("NO")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM videos WHERE NO = %s", [no])
            users = cursor.fetchone()
        print(users)
        return render(request, 'cli1/v_edit.html', {'users':users})
    else:
        no = request.POST.get("NO")
        video_author = request.POST.get('video_author', '')
        # user_sex = request.POST.get('user_sex', '')
        video_likes = request.POST.get('video_likes', '')
        video_performed = request.POST.get('video_performed', '')
        video_comment = request.POST.get('video_comment', '')
        video_intro = request.POST.get('video_intro', '')
        # print(user_name, user_age, user_fans, user_follows, user_pub, user_favorites, id)
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE videos SET AUTHOR=%s,LIKES=%s,PERFORMED=%s,COMMENT=%s,INTRO=%s WHERE NO=%s",
                           [video_author, video_likes, video_performed, video_comment, video_intro, no])
            conn.commit()
            cursor.execute("SELECT * FROM videos WHERE NO = %s", [no])
            users = cursor.fetchall()
        mesg = '修改成功！'
        return render(request, 'cli1/v_index.html', {'users': users, 'message':mesg})

def v_find(request):
    if request.method == 'GET':
        return render(request, 'cli1/v_find.html')
    else:
        video_no = request.POST.get('video_no', '')
        conn = MySQLdb.connect(host='localhost', user='root', passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM videos WHERE NO=%s", [video_no])
            result = cursor.fetchall()
        if len(result) == 0:
            message = '没有此视频信息！请输入正确的视频序号！'
            return render(request, 'cli1/v_find.html', {'message':message})
        else:
            mesg = '查找成功！'
            return render(request, 'cli1/v_index.html', {'users':result, 'message':mesg})