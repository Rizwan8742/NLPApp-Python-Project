import paralleldots

class API:
    def __init__(self):

        # Setting your API key
        paralleldots.set_api_key('WfATZU7XULrXOQcQDFftbJqAyIAgEye1Hnw3hUxWoEE')

    def sentiment_anlysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def emotion_prediction(self,text):
        response = paralleldots.emotion(text)
        return response
    
    def abuse_prediction(self,text):
        response = paralleldots.abuse(text)
        return response