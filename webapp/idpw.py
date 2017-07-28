import MySQLdb
from flask import Flask
from flask import render_template
from flask import request

#realid = 'a'
#realpw = '1234'
app = Flask(__name__)
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down..'

@app.route('/login_result', methods=['POST'])
def login_result():
    identity = request.form['id']
    passward = request.form['pw']
    idpw={'id':identity ,'pw':passward}
    db=MySQLdb.connect("localhost","root","1234","idpw")
    cur = db.cursor()
    cur.execute("select pw from namedata where id='a'")
    result=cur.fetchone()
    if(str(passward)==str(result)):
        return render_template('success.html')
    else:
        return 'fail'
    cur.close()
    db.close()
    

@app.route('/')
def root():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8886,debug=True)
