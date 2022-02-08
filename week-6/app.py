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
  cursor.execute('SELECT NOT EXISTS(SELECT username from member WHERE username=%s);', (username,))
  is_not_exist = cursor.fetchone()[0]
  if is_not_exist:
    cursor.execute('INSERT INTO member(name, username, password) VALUES (%(name)s, %(username)s, %(password)s);', {'name': name, 'username': username, 'password': password})
    db.commit()
    return redirect('/')
  else:
    return redirect(url_for('err', message='帳號已經被註冊'))
      
  
  # 通常不會把所有資料一次抓出來，然後用程式去檢查，因資料筆數多時效率會不佳
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
  cursor.execute('SELECT EXISTS(SELECT username, password FROM member WHERE username=%s AND password=%s);', (username, password))
  is_member = cursor.fetchall()[0][0]
  if is_member:
    session['logged_in'] = True
    cursor.execute('SELECT name FROM member WHERE username=%s', (username,))
    name = cursor.fetchone()[0]
    session['name'] = name
    return redirect('/member/')
  else:
    session['logged_in'] == False
    return redirect(url_for('err', message='帳號或密碼輸入錯誤'))


@app.route('/signout')
def sign_out():
  session['logged_in'] = False
  return redirect('/')


if __name__ == '__main__':
  app.run(port=3000, debug=True)
