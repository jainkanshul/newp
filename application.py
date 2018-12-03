
from flask import Flask
from googletrans import Translator
from flask import request


app = Flask(__name__)
translator = Translator()
translations = translator.translate('how are you', dest='hi')
print(translations.text)


@app.route("/")
def hello():
    print(request.args['text'])
    print(request.args['dest'])
    translations = translator.translate(request.args['text'], dest=request.args['dest'])
    print(translations.text)
    return ("hi")
