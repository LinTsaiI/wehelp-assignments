from flask import Flask, request, render_template, redirect, url_for, session
import os
app = Flask(__name__, static_folder='static', static_url_path='/')
app.secret_key = os.urandom(24)
app.url_map.strict_slashes = False

@app.route('/')
def index():
  session['logged_in'] = False
  return render_template('index.html')


@app.route('/member/')
def logged_in():
  if ('logged_in' not in session) or (session['logged_in'] != True):
    return redirect('/')
  elif (session['logged_in'] == True):
    return render_template('member.html')


@app.route('/error')
def err():
  message = request.args.get('message')
  return render_template('error.html', message=message)


@app.route('/signin', methods=['POST'])
def check_user():
  account = request.form['account']
  password = request.form['password']
  if (account == 'test' and password == 'test'):
    session['logged_in'] = True
    return redirect('/member/')
  elif(account == '' or password == ''):
    session['logged_in'] == False
    return redirect(url_for('err', message='請輸入帳號、密碼'))
  else:
    session['logged_in'] == False
    return redirect(url_for('err', message='帳號、或密碼輸入錯誤'))


@app.route('/signout')
def sign_out():
  session['logged_in'] = False
  return redirect('/')


app.run(port=3000)
