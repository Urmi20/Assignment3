import boto3


class TextAi():
    @staticmethod
    def get_key_phrases(text):
        comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
        key_phrases = comprehend.detect_key_phrases(Text=text, LanguageCode='en')

        return key_phrases

    @staticmethod
    def get_sentiment(text):
        comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
        sentiment = comprehend.detect_sentiment(Text=text, LanguageCode='en')

        return sentiment
