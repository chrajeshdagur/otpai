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
	webtext=text_from_html(html)
	print (type(webtext))
	print (webtext)
	myList = webtext.rstrip().split()
	
	print(len(myList))
	
	
	tem = []
	
	#for i in range(len(myList)):
	#	myList[i] = temp
	#	temp = myList[i].rstrip()
	#length = len(myList)	
	#new_list = []
	#new_list.append(myList[:])
		
		
	#lis_len = len(myList)
	#factor = lis_len/4000
	#print(lis_len)
	#mod = lis_len % 4000
	#initial_index= 0
	#last_index = 0
	#lisTemp = []
	#for i in range(1,factor+1):
	#	last_index = 4000+i
	#	lisTemp.append(myList[initial_index:last_index])
	#
	
	#then = " ".join(myList[:400])
	#list_str.append(then)
	#then = " ".join(myList[400:800])
	#list_str.append(then)
	#print(list_str)
	
	
	
	
	#alldata=re.split('\s{4,}',webtext)
		
	
	#for line in alldata:
	#	print (line)
	
	#bigdata = text.split(' ')
	#text=text_from_html(html).strip()	
	#lines = (line.strip() for line in text.splitlines())	
	#chunks = (phrase.strip() for line in lines for phrase in line.split("  "))	
	#for chunk in chunks:
	#	print (chunk)
	
	#print(chunks)
	
	#text = ' '.join(chunk for chunk in chunks if chunk)
    
	#print (text)
	
	#bigdata = text.split(' ')
	#print (bigdata)
	#print(text.encode('utf-8').split('\'))
	
	
	#print(lines)

	# text
	#text = "Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to find insights and relationships in text."
    
	# language code
	#language_code = 'en'
    
	# detecting key phrases
	#result = detect_key_phraes(text, language_code)
	#print("Starting detecting key phrases")
	#print(json.dumps(result, sort_keys=True, indent=4))
	#print("End of detecting key phrases\n")	
	
	#for line in alldata:
	#	if (len(line) != 0):
	#		text=re.sub(' +', ' ',line)
	#		result = detect_key_phraes(text, language_code)
	#		print("Starting detecting key phrases")
	#		print(json.dumps(result, sort_keys=True, indent=4))
	#		print("End of detecting key phrases\n")	

		
	
if __name__ == '__main__':
    main()
	
	
	
	
