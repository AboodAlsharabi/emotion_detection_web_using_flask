''' Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Invalid input ! Try again."
    key_value_pairs = [f"'{key}': {value}" for key, value in response.items()]
    key_value_pairs = key_value_pairs[:-1]
    str_representation = ", ".join(key_value_pairs)
    return (
        f"For the given statement, the system response is {str_representation}. "
        f"<br>The dominant emotion is {response['dominant_emotion']}"
        )
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
