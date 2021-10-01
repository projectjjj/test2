
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock

import datetime



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def save_post():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    now = datetime.datetime.now()
    doc = {'제목': title_receive, '내용': content_receive, '날짜' : now}
    db.lists.insert_one(doc)
    return jsonify({'result': '포스팅 성공!'})

@app.route('/post', methods=['GET'])
def get_post():
    lists = list(db.lists.find({},{'_id':False}))
    return jsonify({'lists': lists})


@app.route('/post', methods=['DELETE'])
def delete_post():
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
