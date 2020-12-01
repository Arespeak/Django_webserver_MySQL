'''
作者：桑忠人 18281160
时间：2020.11
描述：本server版权为 北京交通大学计算机学院 桑忠人 18281160 所有！
'''


from django.shortcuts import render, redirect
import MySQLdb

# Create your views here.
#建立查询的操作函数
def index(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform", charset='utf8')
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
        return redirect('../')

#删除用户信息
def delete(request):
    id = request.GET.get("ID")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="000606", db="short_video_platform", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM users WHERE ID = %s", [id])
        # cursor.execute("CALL USERDELECT(%s)", [id])
        conn.commit()
    return redirect('../')


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
        return redirect('../')
