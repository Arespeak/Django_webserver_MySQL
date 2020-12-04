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
        return render(request, 'cli1/login.html')
    else:
        admin_name = request.POST.get('admin_name')
        admin_id = request.POST.get('admin_id')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT WORK_ID FROM adminors WHERE NAME=%s", [admin_name])
            result = cursor.fetchall()
        if not result or admin_id != result[0]["WORK_ID"]:
            mesg = '用户名或工号输入错误！请重新输入!'
            return render(request, 'cli1/login.html', {'message': mesg})
        else:
            return render(request, 'cli1/content.html')


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
            cursor.execute("SELECT * FROM users")
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
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
        return render(request, 'cli1/index.html', {'users': users})

#删除用户信息
def delete(request):
    id = request.GET.get("ID")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM users WHERE ID = %s", [id])
        # cursor.execute("CALL USERDELECT(%s)", [id])
        conn.commit()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    return render(request, 'cli1/index.html', {'users': users})

    # return redirect('cli1/index.html')


#更改用户信息
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("ID")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform",
                               charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM users WHERE ID = %s", [id])
            users = cursor.fetchone()
        print(users)
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
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
        return render(request, 'cli1/index.html', {'users': users})

        # return redirect('cl1/index.html')

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
            return render(request, 'cli1/index.html', {'users':result})

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
        return render(request, 'cli1/v_index.html', {'users': users})

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
    return render(request, 'cli1/v_index.html', {'users': users})

    # return redirect('cli1/index.html')


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
            cursor.execute("SELECT * FROM videos")
            users = cursor.fetchall()
        return render(request, 'cli1/v_index.html', {'users': users})

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
            return render(request, 'cli1/v_index.html', {'users':result})