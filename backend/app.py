# -*- coding:utf-8  -*-

# 导入 flask
from flask import Flask
from flask import render_template
from flask import request, jsonify

# 导入中文分词包
import jieba

# 创建 flask 应用
app = Flask(__name__, template_folder="")

# 全局设置
HOST, PORT = "localhost", "5000"
# HOST, PORT = "0.0.0.0", "5000"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/getWordSegmentationResults', methods=["GET"])
def getWordSegmentationResults():
    text = str(request.args["text"])
    return jsonify({'results': jieba.lcut(text)})


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)