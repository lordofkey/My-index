# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from db import Mydblib

app = Flask(__name__)



@app.route('/map')
def map():
    return render_template("map.html")


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/resume')
def resume():
    photourl = url_for("static",filename = "photo1.jpg");
    return render_template("resume.html",photourl = photourl)

@app.route('/geturl')
def geturl():
    return  render_template("geturl.html")

@app.route('/ajax/bookmark', methods=['GET', 'POST'])
def getbook():
    if request.method == 'POST':
        text = request.form["book"]
        title = request.form["title"]
        db = Mydblib.Mydblib()
        db.addbookmark(title,text)
        db.save()
        return "已经成功加入书签：" + title
    else:
        return "arg error"
@app.route('/ajax/getbookmarks', methods=['GET'])
def getbookmarks():
    db = Mydblib.Mydblib()
    redict = str(db.getbookmarks())
    return redict

if __name__ == '__main__':
    app.run(port="5551")




