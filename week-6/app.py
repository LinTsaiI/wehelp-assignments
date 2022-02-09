from flask import Flask, request, render_template, redirect, url_for, session
import mysql.connector
import os
app = Flask(__name__, static_folder='static', static_url_path='/')
app.secret_key = os.urandom(24)
app.url_map.strict_slashes = False

db = mysql.connector.connect(
  host='localhost',
  port='3306',
  user='root',
  password='mysqlpassword',
  database='website'
)
cursor = db.cursor()

@app.route('/')
def index():
  session['logged_in'] = False
  return render_template('index.html')


@app.route('/member/')
def logged_in():
  if ('logged_in' not in session) or (session['logged_in'] != True):
    return redirect('/')
  elif (session['logged_in'] == True):
    name = session['name']
    return render_template('member.html', name=name)


@app.route('/error')
def err():
  message = request.args.get('message')
  return render_template('error.html', message=message)


@app.route('/signup', methods=['POST'])
def sign_up():
  name = request.form['name']
  username = request.form['username']
  password = request.form['password']
  # 利用 SQL 查詢 username 是否存在 member 中
  if name == '' or username == '' or password == '':   # 避免使用者沒有輸入任一資訊按下註冊鍵，會跳出'帳號已經被註冊'，或是在 member 中加入空字串的資料
    return redirect(url_for('err', message='請輸入完整資訊'))
  cursor.execute('SELECT username FROM member WHERE username=%s;', (username,))
  exist = cursor.fetchone()
  if exist:   # 若有找到結果表已存在
    return redirect(url_for('err', message='帳號已經被註冊'))
  else:   # 若結果為None表不存在，將輸入的資料加入member
    cursor.execute('INSERT INTO member(name, username, password) VALUES (%s, %s, %s);', (name, username, password))
    db.commit()
    return render_template('signup_successed.html')

  # 額外使用 NOT EXISTS 確認 username 是否存在 member 中 (比較麻煩的做法)
  # cursor.execute('SELECT NOT EXISTS(SELECT username from member WHERE username=%s);', (username,))
  # not_exist = cursor.fetchone()[0]
  # if not_exist:
  #   cursor.execute('INSERT INTO member(name, username, password) VALUES (%(name)s, %(username)s, %(password)s);', {'name': name, 'username': username, 'password': password})
  #   db.commit()
  #   return redirect('/')
  # else:
  #   return redirect(url_for('err', message='帳號已經被註冊'))
      
  
  # 通常不會把所有資料一次抓出來，然後用程式去檢查，因資料筆數多時效率會不佳，以下範例
  # cursor.execute('SELECT username from member;')
  # username_list = cursor.fetchall()
  # if (username,) not in username_list:
  #   cursor.execute(
  #     'INSERT INTO member(name, username, password) VALUES (%s, %s, %s)', (name, username, password))
  #   cursor.close()
  #   db.commit()
  #   return redirect('/')
  # else:
  #   return redirect(url_for('err', message='帳號已經被註冊'))
  

@app.route('/signin', methods=['POST'])
def check_member():
  username = request.form['signin_username']
  password = request.form['signin_password']
  cursor.execute('SELECT name, username, password FROM member WHERE username=%s AND password=%s;', (username, password))
  match = cursor.fetchone()
  if match:
    session['logged_in'] = True
    session['name'] = match[0]  # fetchone() 的[0]個位置為name
    return redirect('/member/')
  else:   # 若結果為None表沒有對應的(username, password)
    session['logged_in'] = False
    return redirect(url_for('err', message='帳號或密碼輸入錯誤'))

  # 額外使用 EXISTS 確認 username 與 password 是否已經存在 member 中 (比較麻煩的做法)
  # cursor.execute('SELECT EXISTS(SELECT username, password FROM member WHERE username=%s AND password=%s);', (username, password))
  # is_member = cursor.fetchall()[0][0]
  # if is_member:
  #   session['logged_in'] = True
  #   cursor.execute('SELECT name FROM member WHERE username=%s', (username,))
  #   name = cursor.fetchone()[0]
  #   session['name'] = name
  #   return redirect('/member/')
  # else:
  #   session['logged_in'] = False
  #   return redirect(url_for('err', message='帳號或密碼輸入錯誤'))


@app.route('/signout')
def sign_out():
  session['logged_in'] = False
  return redirect('/')


if __name__ == '__main__':
  app.run(port=3000, debug=True)
