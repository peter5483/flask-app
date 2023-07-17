# import os

# dir_path = os.chdir("C:\\Users\\peter\\Desktop\\novel\\JP\\")
# # dir_path2 = os.chdir("C:\\Users\\peter\\Desktop\\novel\\TL\\")
# all_file_name = os.listdir(dir_path)
# # all_file_name2 = os.listdir(dir_path)

# os.system("echo 99 | translate zh-TW")

import json
from flask import Flask, render_template, request, after_this_request
from flask_socketio import SocketIO
from googletrans import Translator
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

  
# @socketio.on("ESP")
# def ESP(data):
  

# @socketio.on("JS")
# def JS(data):
  


@app.route('/')
def control():
  return "HI"

  
@app.route("/t")
def tt():
  # socketio.emit("ESP", "嗨".encode())
  return render_template("t.html")

if __name__ == '__main__':
  socketio.run(app, host='0.0.0.0', port=443, debug=True)
#   socketio.run(app, debug=True)