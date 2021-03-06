from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from mysql.connector import pooling
import os

app = Flask(__name__, static_folder='static',
            static_url_path='/', template_folder='templates')
app.secret_key = os.urandom(24)

# 使用 connection pooling
connection_pool = pooling.MySQLConnectionPool(
    pool_name = 'website_db_pool',
    pool_size = 5,
    pool_reset_session = True,
    host='localhost',
    port='3306',
    user='root',
    password='mysqlpassword',
    database='website'
)


@app.route('/', methods=['GET'])
def index():
    session['logged_in'] = False
    return render_template('index.html')


@app.route('/member/', methods=['GET'])
def logged_in():
    if ('logged_in' not in session) or (session['logged_in'] != True):
        return redirect('/')
    elif (session['logged_in'] == True):
        name = session['name']
        return render_template('member.html', name=name)


@app.route('/error', methods=['GET'])
def err():
    message = request.args.get('message')
    return render_template('error.html', message=message)


@app.route('/signup', methods=['POST'])
def sign_up():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    # 避免使用者沒有輸入任一資訊按下註冊鍵，會跳出'帳號已經被註冊'，或是在 member 中加入空字串的資料
    if name == '' or username == '' or password == '':
        return redirect(url_for('err', message='請輸入完整資訊'))
    
    db = connection_pool.get_connection()   # 從 connection_pool 中取得一個連線
    cursor = db.cursor()
    cursor.execute(
        'SELECT username FROM member WHERE username=%s;', (username,))
    exist = cursor.fetchone()
    if exist:
        cursor.close()
        db.close()
        return redirect(url_for('err', message='帳號已經被註冊'))
    else:
        cursor.execute(
            'INSERT INTO member(name, username, password) VALUES (%s, %s, %s);', (name, username, password))
        cursor.close()
        db.commit()
        db.close()
        return render_template('signup_successed.html')


@app.route('/signin', methods=['POST'])
def check_member():
    username = request.form['signin_username']
    password = request.form['signin_password']
    db = connection_pool.get_connection()
    cursor = db.cursor()
    cursor.execute(
        'SELECT name, username, password FROM member WHERE username=%s AND password=%s;', (username, password))
    match = cursor.fetchone()
    cursor.close()
    db.close()
    if match:
        session['logged_in'] = True
        session['name'] = match[0]
        session['username'] = match[1]
        return redirect('/member/')
    else:
        session['logged_in'] = False
        return redirect(url_for('err', message='帳號或密碼輸入錯誤'))


@app.route('/signout', methods=['GET'])
def sign_out():
    session['logged_in'] = False
    return redirect('/')


# 查詢會員姓名 API
@app.route('/api/members', methods=['GET'])
def query_members():
    username = request.args.get('username')
    db = connection_pool.get_connection()
    cursor = db.cursor()
    cursor.execute(
        'SELECT id, name, username FROM member WHERE username=%s;', (username,))
    data = cursor.fetchone()
    cursor.close()
    db.close()
    if data:
        id = data[0]
        name = data[1]
        username = data[2]
        return jsonify(
            {
                "data": {
                    "id": id,
                    "name": name,
                    "username": username
                }
            })
    else:
        return jsonify(
            {
                "data": None
            }
        )


# 更改會員姓名 API
@app.route('/api/member', methods=['POST'])
def update_name():
    username = session['username']
    new_name = request.json.get('name')   # JSON => Python
    if (new_name != '') and (session['logged_in'] == True):
        db = connection_pool.get_connection()
        cursor = db.cursor()
        cursor.execute(
            'UPDATE member SET name=%s WHERE username=%s;', (new_name, username))
        cursor.close()
        db.commit()
        db.close()
        session['name'] = new_name
        return jsonify(   # Python => JSON
            {
                "ok": True
            })
    elif ('logged_in' not in session) or (session['logged_in'] != True):
        return jsonify(
            {
                "error": True
            }
        )


if __name__ == '__main__':
    app.run(port=3000, debug=True)
