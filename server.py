''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_measurement():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    emotions = emotion_detector(text_to_analyze)

    # Examine the dominant emotion and its score from the response
    if emotions['dominant_emotion'] is None:
        return "Invalid input! Try again."

    return_result = f"For the given statement, the system response is 'anger': \
                {emotions['anger']}, 'disgust': {emotions['disgust']}, \
                'fear': {emotions['fear']}, 'joy': {emotions['joy']}, \
                'sadness': {emotions['sadness']}. The dominant emotion is \
                {emotions['dominant_emotion']}."
    return return_result

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''

    return render_template('index.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
