from gtts import gTTS
from flask import Flask
from flask import request
from flask import send_file

app = Flask(__name__)

@app.route('/speak')
def hello_world():
    print(request.args.get('text', ''))
    text = request.args.get('text', '')
    tts = gTTS(text)
    tts.lang = "en"
    tts.save("speak.mp3")
    path = "./speak.mp3"
    return send_file(path, as_attachment=True)