import boto3
import json

# Comprehend constant
REGION = 'us-east-1'


# Function for detecting the dominant language
def detect_dominant_language(text):
    comprehend = boto3.client('comprehend', region_name=REGION)
    response = comprehend.detect_dominant_language(Text=text)
    return response


# Function for detecting named entities
def detect_entities(text, language_code):
    comprehend = boto3.client('comprehend', region_name=REGION)
    response = comprehend.detect_entities(Text=text, LanguageCode=language_code)
    return response


# Function for detecting key phrases
def detect_key_phraes(text, language_code):
    comprehend = boto3.client('comprehend', region_name=REGION)
    response = comprehend.detect_key_phrases(Text=text, LanguageCode=language_code)
    return response


# Function for detecting sentiment
def detect_sentiment(text, language_code):
    comprehend = boto3.client('comprehend', region_name=REGION)
    response = comprehend.detect_sentiment(Text=text, LanguageCode=language_code)
    return response


def main():
    # text
    text = "Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to find insights and relationships in text."

    # language code
    language_code = 'en'

    # detecting the dominant language
    result = detect_dominant_language(text)
    print("Starting detecting the dominant language")
    print(json.dumps(result, sort_keys=True, indent=4))
    print("End of detecting the dominant language\n")

    # detecting named entities
    result = detect_entities(text, language_code)
    print("Starting detecting named entities")
    print(json.dumps(result, sort_keys=True, indent=4))
    print("End of detecting named entities\n")

    # detecting key phrases
    result = detect_key_phraes(text, language_code)
    print("Starting detecting key phrases")
    print(json.dumps(result, sort_keys=True, indent=4))
    print("End of detecting key phrases\n")

    # detecting sentiment
    result = detect_sentiment(text, language_code)
    print("Starting detecting sentiment")
    print(json.dumps(result, sort_keys=True, indent=4))
    print("End of detecting sentiment\n")


if __name__ == '__main__':
    main()