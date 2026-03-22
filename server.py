"""Flask server for emotion detection."""
import json

from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/emotionDetector')
def sent_detector():
    """Detect emotions in the provided text and return a formatted response."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (f"For the given statement, the system response is anger : {anger}, "
            f"disgust : {disgust}, fear : {fear}, joy : {joy} and sadness : {sadness}. "
            f"The dominant emotion is {dominant_emotion}.")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
