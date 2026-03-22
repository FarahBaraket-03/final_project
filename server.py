from flask import Flask , redirect, request, render_template, url_for

from EmotionDetection.emotion_detection import emotion_detector

import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return " Invalid text! Please try again!"
    
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    return "For the given statement, the system response is anger : {}, disgust : {}, fear : {}, joy : {} and sadness : {}. The dominant emotion is {}.".format(anger,disgust,fear,joy,sadness,dominant_emotion)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
