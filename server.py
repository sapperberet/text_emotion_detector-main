from flask import *
from Flask_EmotionDetection.emotion_detection import *

app = Flask("__name__",template_folder="templates")

@app.route("/detector")
def emotion_detect():
    text = request.args.get('textToAnalyze')
    response =emotion_detector(text)
    anger = response['anger']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    disgust = response['disgust']
    emotion = response['dominant_emotion']
    if emotion is not None:
        return(
        f"For the given statement, the system response is 'anger':"
        f"{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}." 
        f"The dominant emotion is {emotion}"


        )
    return "enter a valid text"


@app.route("/")
def renderpages():
    return render_template('index.html')

if __name__ == "__main__":
    app.run( debug=True  , host="0.0.0.0" , port = 5001)