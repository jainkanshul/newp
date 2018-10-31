
from flask import Flask
from googletrans import Translator
from flask import request


app = Flask(__name__)
translator = Translator()


@app.route("/")
def hello():
    print(request.args['text'])
    print(request.args['dest'])
    translations = translator.translate(request.args['text'], dest=request.args['dest'])
    return (translations.text)
