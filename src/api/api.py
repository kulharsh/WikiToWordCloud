import flask
from flask import send_file, request 
from ..processor import wordcloud_processor
import os

from elasticsearch import Elasticsearch
#from elasticsearch import Elasticsearch

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/get_wordcloud', methods=['GET'])
def home():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    word = request.args.get("word")
    path = os.path.dirname(os.path.abspath(__file__))                      
    path = path + "/../static/"+word+".png"
    wordcloud_processor.get_wordCloud(es, word, path)	
    return send_file(path, mimetype='image/gif')
app.run()
