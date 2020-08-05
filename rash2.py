import json
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys
from time import sleep
import re
import json
from difflib import get_close_matches
import regex
import random
import time
import requests
from bs4 import BeautifulSoup as bs
from newsapi import NewsApiClient as nac

#data = json.load(open("dictionary.json"))
hi=["janu hi","janu hello","janu hey","janu yo","janu hola","janu heyy","janu hui","janu hi there"]
greetings=["hi","hello","hey","hola","hi !\ngreetings from janu✋️","hey there"]
about=["janu who made you","janu who is your father","janu who is your creator","janu who created you","janu who created you?","janu who is your father","janu what is your name","janu who are you","janu who invented you","janu who made you?","janu who is your father?","janu who is your creator?","janu who is your father?","janu what is your name?","janu who are you?","janu who invented you?"]
abtans=["Iam the whatsapp bot- *JANU* 👧️\n -created by great Sidharth and the magnificent Bejoy\n😎️😅️","Iam the whatsapp bot- *JANU* 👧️\nMy creators are the great Sidharth and the magnificent Bejoy\n😎️😅️"]
us=["sidharth","bejoy"]
usa=["he is my god-my creator.🤗️","He is my dad.\nHe made me. iam his child","He is everything for me.🤗️\nMy dad\n My creator\nJust everything" ]
watch_spell=["wach","wacht","wathc","wath"]
repeat = ''
sleep(1)
browser = webdriver.Firefox(executable_path=r'/root/Downloads/geckodriver')
browser.get('https://web.whatsapp.com')
def fn(query):
	url="https://www.google.com/search?client=firefox-b-e&biw=772&bih=646&tbs=sbd%3A1&tbm=nws&ei=OYoqX47bH8uxggfs6JSwBQ&q="+query
	content = requests.get(url.encode()).content
	soup=bs(content,"html.parser")

	newss=soup.find_all('div', attrs={'class':'kCrYT'})

	for news in newss:
		#send(news.get_text()+"\n")
		link= (news.find("a").get("href"))
		link=re.sub("/url\?q=","",link)
		link=re.sub("&usg.*","",link)
		#send("Read More:: "+link+"\n")
		send(news.get_text()+"\n"+"Read More:: "+link+"\n")
def yt(query):


	import requests
	from bs4 import BeautifulSoup as bs
	import re
	import urllib.parse




	count=0
	counts=0
	dic=dict()
	link_list=[]
	vdo_list=[]
	#query=input("Enter search term : ")
	url ="https://www.google.com/search?q="+query+"&tbm=vid&source=lnt&tbs=srcf:H4sIAAAAAAAAAEWLQQ6AIAwEf-PF6J_1W0iAJUNMCBl-v6cXjzGTWKb31g3eSsowkisLBgc5EiEKileEmw1hxYzohDFTiQGKFWyLrGlnnZuTZkNtzfcuf3L9b4CUHcQAAAA&sa=X&ved=0ahUKEwiv1IaUyYHrAhVwRN8KHZEqBwMQpwUIIQ&biw=1366&bih=646&dpr=1"

	content = requests.get(url.encode()).content
	soup=bs(content,"html.parser")
	links=soup.find_all("a")
	vids=soup.find_all("h3")
	for link in links:
		if "https://www.youtube.com/" in (link.get("href")):
			x=link.get("href")
			x=re.sub("\/url\?q=","",x)
			x=re.sub("&sa=.*","",x)
			x=urllib.parse.unquote(x)
			if x not in link_list:
				link_list.append(x)

				print(x)
				count+=1
	print(count)
	for vid in vids:
		print(vid.get_text())
		vdo_list.append(vid.get_text())

		counts+=1
	print(counts)
	for i in range(5):
		send(vdo_list[i]+">>>>"+link_list[i])

def kuki(mess):
	url="https://miapi.pandorabots.com/talk"
	Data={"input":mess,
	"sessionid":"404559097",
	"channel":"6",
	"botkey":"jUmYHOGnr2Irfq4jE2qdKOlApIfuE8eJ8WF1RXAnnL-2BdStk_EfhShoEEpqDr71crA8qiW6zIxp9rI_1dsWOQ~~",
	"client_name":"cw173858f5f22"
	}

	headers={"Host":"miapi.pandorabots.com",
		"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",

		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://home.pandorabots.com/home.html",
		"Content-type": "application/x-www-form-urlencoded",
		"Content-Length": "161",
		"Origin": "https://home.pandorabots.com",
		"Connection": "close"
		}





	data=requests.post(url ,headers=headers,data=Data).json()
	response=data["responses"][0]
	def remove_html_tags(text):
		import re
		clean = re.compile('<.*?>')
		return re.sub(clean, '', text)
	tag_less_response = remove_html_tags(response).lower()
	if ".or go back to main menubeginwidgetbotshall we get back on topic? we were talking about our social media channels." in tag_less_response.lower():
		tag_less_response=re.sub("or go back to main menubeginwidgetbotshall we get back on topic? we were talking about our social media channels.",'',tag_less_response)
	if "talking about getting to know us better." in tag_less_response.lower():
		tag_less_response=re.sub("or go back to main menubeginwidgetbotshall we get back on topic? we were talking about getting to know us better.",'',tag_less_response)
	if "yesagentnonothanks" in tag_less_response.lower():
		tag_less_response=re.sub("yesagentnonothanks",'',tag_less_response)
	if "pandora" in tag_less_response.lower():
		tag_less_response=re.sub("pandora",'Janu',tag_less_response)
	if "do you want to check us" in tag_less_response.lower():
		garb = "Pandorabots is all over the internet! Do you want to check us out?Youtubehttps://www.youtube.com/channel/UCGsqke8OySdZEkTgNFeUeSQFacebookhttps://www.facebook.com/chatbots.io/Twitterhttps://twitter.com/pandorabotsOur Bloghttps://medium.com/pandorabots-blogInstagramhttps://www.instagram.com/pandorabotsMaybe laternothanks"
		tag_less_response=re.sub(garb.lower(),"Sorry ! i dont have access to social media sites due to privacy statements🤧️",tag_less_response)
	return(tag_less_response)
	print(tag_less_response)
def find(mesg):

	op=open("memory.json","r")
	data=json.load(op)
	flist=list()
	for i in list(data):
		if mesg in i.lower():
			resp=i+"\n"+"dealer: "+data[i][0]+"  model: "+data[i][1]+"  price: "+data[i][2]+"  Unique_id: "+data[i][3]
			flist.append(resp)
		else:
			print("not found")
	return flist

def save(mesg,dlr,model,price):
	if "." in mesg.lower():
		mesg=re.sub('\.','.\n',mesg)
	op=open("memory.json","r")
	full="abcdefghijklmnopqrstuvwxyz"
	id="".join(random.sample(full,6))
	data=json.load(op)
	data[mesg]=data.get(mesg, [dlr,model,price,id])
	os.remove("memory.json")
	print(data)
	f=open("memory.json","w")
	json.dump(data,f, indent=4)

def change(id,price,newprice):
	op=open("memory.json","r")
	data=json.load(op)
	for x,y in data.items():
		if y[3] == id:
			x=re.sub(price,newprice,x)

			send(x)

	os.remove("memory.json")
	print(data)
	f=open("memory.json","w")
	json.dump(data,f, indent=4)




def elbot(mess):
	url1 = "http://elbot-e.artificial-solutions.com/cgi-bin/elbot.cgi"
	indent_value=""
	userlog_value=""
	Data={
	"IDENT":indent_value,
	"USERLOGID":userlog_value,
	"ENTRY":mess,
	"EXTRAINPUT":14,
	"send.x":0,
	"send.y":0,
	}

	data=requests.post(url1 ,data=Data).content
	soup=bs(data ,"html.parser")
	tags=soup.find_all("td")
	indent_tag = soup.find_all(attrs={"name" : "IDENT"})
	indent_value=indent_tag[0]['value']
	user_tag=soup.find_all(attrs={"name" : "USERLOGID"})
	userlog_value=user_tag[0]["value"]

	response=tags[4].text
	if "elbot" in response.lower():
		return(re.sub("Elbot",'Jaanu',response))
	else:
		return(response)


def retrive_definition(word):
#Removing the case-sensitivity from the program
#For example 'Rain' and 'rain' will give same output
	#Converting all letters to lower because out data is in that format
	word = word.lower()

	#Check for non existing words
	#1st elif: To make sure the program return the definition of words that start with a capital letter (e.g. Delhi, Texas)
	#2nd elif: To make sure the program return the definition of acronyms (e.g. USA, NATO)
	#3rd elif: To find a similar word
	#-- len > 0 because we can print only when the word has 1 or more close matches
	#-- In the return statement, the last [0] represents the first element from the list of close matches
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		action =("Oops ! there seems to be a spelling mistake.🤦‍♀️️🤦‍♀️️\nDid you mean %s instead😅️" % get_close_matches(word, data.keys())[0])
		send(action)
		sleep(.5)
		return data[get_close_matches(word, data.keys())[0]]
def send(x):
	print("reached inside send function")
	text_box = browser.find_elements_by_xpath(
		'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]


	text_box.send_keys(x)
	sleep(5)
	text_box.send_keys(Keys.ENTER)

def prefix(x):
	URL = "https://en.wikipedia.org/w/api.php"
	PARAMS = {
	"action": "query",
	"format": "json",
	"list": "prefixsearch",
	"pssearch":x
	}
	S = requests.Session()
	R = S.get(url=URL, params=PARAMS)
	DATA = R.json()

	PAGES = DATA['query']['prefixsearch']
	for page in PAGES:

		msg=page["title"]
		send(msg)

def weather():
	city="trivandrum"
	url="https://api.openweathermap.org/data/2.5/weather?q=trivandrum&appid=c609fd28e059f9b4b8a5388682af0eb4"
	response=requests.get(url)
	data=response.json()

	descr=data["weather"][0]["main"]
	temp=str(int(int(data["main"]["temp"])-273.15))
	feels_like=str(int(int(data["main"]["feels_like"])-273.15))
	humidity=data["main"]["humidity"]


	msg="Today's Weather in kerala::"+descr+"\nTemperature::"+temp+"°C\nFeels Like::"+feels_like+"°C\nHumidity::"+str(humidity)+"\n"

	send(msg)

def news(search):
	print(search)
	from newsapi import NewsApiClient as nac


	newsapi = nac(api_key='a7ad3c210edc417699e9ef55f83e6df2')

	# /v2/top-headlines
	top_headlines = newsapi.get_top_headlines(sources='the-hindu,the-times-of-india,google-news-in',
											  language='en',
											  )

	# /v2/everything
	articles = newsapi.get_everything(q=search,
									  sources='the-hindu,the-times-of-india,google-news-in',

									  from_param='2020-07-20',
									  to='2020-07-31',
									  language='en',
									  sort_by="publishedAt"
									  )


	for i in range(5):

		send("*"+articles["articles"][i]["title"].upper()+"*"+"\n"+articles["articles"][i]["description"])
		send("Read more: "+articles["articles"][i]["url"] )

def top_lines():
	from newsapi import NewsApiClient as nac
	newsapi = nac(api_key='a7ad3c210edc417699e9ef55f83e6df2')
	top_headlines = newsapi.get_top_headlines(sources='the-hindu,the-times-of-india,google-news-in',
											  language='en',
											  )
	for i in range(5):
		send("*"+top_headlines["articles"][i]["title"].upper()+"*"+"\n"+top_headlines["articles"][i]["description"])
		#send(top_headlines["articles"][i]["description"]+"\n")
		send("Read more: "+top_headlines["articles"][i]["url"])

while True:
	n=5
	# The green dot tells us that the message is new
	unread = browser.find_elements_by_class_name("_31gEB")

	name, message = '', ''
	if len(unread) > 0:
		ele = unread[-1]
		action = webdriver.common.action_chains.ActionChains(browser)
		action.move_to_element_with_offset(ele, 0, -20)

		try:
			action.click()
			action.perform()
			action.click()
			action.perform()
		except Exception as e:
			pass


	try:
		#test=0
		#timeout=2
		#timeout_start=time.time()
		while n>0:#time.time() < timeout_start + timeout:

			name = browser.find_element_by_class_name("DP7CM").text  # Contact name

			message = browser.find_elements_by_class_name("eRacY")[-1]
			if "hey" in message.text.lower():
				heyy = "Hey✋️\n Iam your personal assistant bot- *JANAKI* 👧️\nType the following to access my functions\n--Type 'janu(space)xxx' to chat with me[eg : janu how are you]\n--Type 'janu weather' to know the present weather in kerala.\n--Type 'janu find(space)xxx' to search wiki.[eg : janu find corona]\n--Type 'janu def(space)xxx' to get the definition of words[eg : janu def apple\nLet's start human !🤙️"
				send(heyy)
			elif message.text.lower() in about:
				greet = random.choice(abtans)
				send(greet)
			elif message.text.lower() in hi:
				greet = random.choice(greetings)
				send(greet)
			elif "abuf " in message.text.lower():
				slist=message.text.split()
				del slist[0]
				if len(slist)>1:
					filtered_search='_'.join(slist)
				else :
					filtered_search=slist[0]
				result = find(filtered_search)
				print(result)
				if len(result) > 1:
					print("if is working")
					mul="There are multiple inputs !!🤧️"
					send(mul)
					for item in result:
						send(item)
				#For words having single definition
				else:
					print("else is working")
					send(result[0])
			elif "abus " in message.text.lower():
				word_user=message.text.lower().split()

				if len(word_user)>1:


					dealer=word_user[1]
					model=word_user[2]
					price=word_user[3]
					mess = browser.find_elements_by_class_name("eRacY")[-2].text.lower()
					save(mess,dealer,model,price)
				print(mess)
			elif "abuc" in message.text.lower():
				word= message.text.lower().split()
				id,price,newprice=word[1],word[2],word[3]
				change(id,price,newprice)





			elif "weather" in message.text.lower():
				weather()
			elif "news" in message.text.lower():
				if len(message.text.split())>1:
					terms=message.text.split()
					del terms[0]
					search_term=' '.join(terms)
					news(search_term)
				else:
					top_lines()
			elif "yt" in message.text.lower():
				terms=message.text.split()
				del terms[0]
				search_term=' '.join(terms)
				yt(search_term)
			elif "fnws" in message.text.lower():
				terms=message.text.split()
				del terms[0]
				search_term=' '.join(terms)
				fn(search_term)
	except Exception as e:

		print(e)
		pass
	repeat= message
	sleep(2) # A 2 second pause so that the program doesn't run too fast
