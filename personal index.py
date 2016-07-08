# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

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
        return "rename:woshi" + text
    else:
        return "arg error"


if __name__ == '__main__':
    app.run(port="5551")




