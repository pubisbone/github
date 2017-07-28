from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
def shutdown():
  func = request.environ.get('werkzeug.server.shutdown')
  if func is None:
    raise RuntimeError('Not runnint with the Werkzeug Server')
  func()

@app.route('shutdown')
def shutdown(): #콜백함수
  shutdown_server()
  return 'Server shutting down..'
