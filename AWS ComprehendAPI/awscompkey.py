# Once you Done with the code read and understand each keyword of code for explanation.	

import boto3
import json
import urllib.request
import re
from bs4 import BeautifulSoup
from bs4.element import Comment


def main():	
	# Comprehend constant
	REGION = 'us-east-1'
	
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
	
	def tag_visible(element):
		if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
			return False
		if isinstance(element, Comment):
			return False
		return True
	
	def text_from_html(body):
		soup = BeautifulSoup(body, 'html.parser')
		texts = soup.findAll(text=True)
		visible_texts = filter(tag_visible, texts)  
		return u" ".join(t.strip() for t in visible_texts)
	
	#HTML Text
	html = urllib.request.urlopen('https://blogs.wsj.com/cio/2018/06/18/software-microservices-open-up-new-business-models-for-companies/').read()		
	webtext=text_from_html(html).split()
	
	def divide_chunks(l, n):       
		# looping till length l 
		for i in range(0, len(l), n):  
			yield l[i:i + n] 

	x = list(divide_chunks(webtext, 500)) 

	# language code
	language_code = 'en'
    
	for i in range(len(x)):
		print (' '.join(x[i]))
		print ("\n")
		
		text=' '.join(x[i])
	
		# detecting key phrases
		result1 = detect_key_phraes(text, language_code)		
		#print(json.dumps(result, sort_keys=True, indent=4))		
		with open('data_key'+str(i)+'.json', 'w') as outfile:
			json.dump(result1, outfile)
		
		
		# detecting named entities
		result2 = detect_entities(text, language_code)
		with open('data_named'+str(i)+'.json', 'w') as outfile:
			json.dump(result2, outfile)
	
	
if __name__ == '__main__':
    main()
	
	
	
	
