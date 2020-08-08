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
import regex
import random
import time
import requests
from bs4 import BeautifulSoup as bs
from newsapi import NewsApiClient as nac
import schedule
try:
	import autoit
except ModuleNotFoundError:
	pass

repeat = ''

browser = webdriver.Firefox(executable_path=r'/root/Downloads/geckodriver')
browser.get('https://web.whatsapp.com')
wait = WebDriverWait(browser, 3)


def send_message(message):
	global  wait, browser
	print(message,"reached send")
	for i in range(4):
		target="Bot"+str(i)
		try:
			x_arg = '//span[contains(@title,' + target + ')]' #/html/body/div[1]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div/span
			ct = 0
			while ct != 10:
				try:
					# group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
					# group_title.click()
					browser.find_element_by_css_selector("span[title='" + target + "']").click()
					print("found target")
					break
				except:
					ct += 1
					time.sleep(1)
					print(" notfound target")
			input_box = browser.find_elements_by_xpath(
				'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
			for ch in message:
				if ch == "\n":
					ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
				else:
					input_box.send_keys(ch)
			time.sleep(4)
			input_box.send_keys(Keys.ENTER)
			print("Message sent successfuly")

		except Exception as e :#NoSuchElementException:
			print(e)
			return



def fn(query):
	print("reached here")
	url="https://www.google.com/search?client=firefox-b-e&biw=772&bih=646&tbs=sbd%3A1&tbm=nws&ei=OYoqX47bH8uxggfs6JSwBQ&q="+query
	content = requests.get(url.encode()).content
	soup=bs(content,"html.parser")

	newss=soup.find_all('div', attrs={'class':'kCrYT'})

	for news in newss:
		#send(news.get_text()+"\n")
		link= (news.find("a").get("href"))
		link=re.sub("/url\?q=","",link)
		link=re.sub("&.*","",link)
		#send("Read More:: "+link+"\n")
		send_message(news.get_text()+"\n"+"Read More:: "+link+"\n")


def youtube():
	from youtube_search import YoutubeSearch
	search_terms=["malayalam funny","malayalam trending" ,"comedy malayalam", "fun"]
	search_term=random.choice(search_terms)
	results = YoutubeSearch(search_term, max_results=10).to_dict()

	for i in range(2):
		title=results[i]["title"]
		channel=results[i]["channel"]
		views=results[i]["views"]
		duration=results[i]["duration"]
		link="https://www.youtube.com"+results[i]["url_suffix"]
		send_message(title+"\nChanel: "+channel+"\nViews: "+str(views)+"\nDuration: "+str(duration)+"\nLink: "+link)



def send(x):
	print("reached inside send function")
	text_box = browser.find_elements_by_xpath(
		'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]


	text_box.send_keys(x)
	sleep(5)
	text_box.send_keys(Keys.ENTER)

def image_downloader_and_sender(url,file_type):
	if file_type=="GraphImage":
		response = requests.get(url)
		file = open("test.jpg", "wb")
		file.write(response.content)
		file.close()
		sleep(2)
		docPath = os.getcwd() + "/test.jpg"
	elif file_type=="GraphVideo":
		response = requests.get(url)
		file = open("test.mp4", "wb")
		file.write(response.content)
		file.close()
		docPath = os.getcwd() + "/test.mp4"

	# Attachment Drop Down Menu
	for i in range(4):
		target=("Bot"+str(i))
		try:
			x_arg = '//span[contains(@title,' + target + ')]' #/html/body/div[1]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div/span
			ct = 0
			while ct != 10:
				try:
					# group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
					# group_title.click()
					browser.find_element_by_css_selector("span[title='" + target + "']").click()
					print("found target")
					break
				except:
					ct += 1
					time.sleep(1)
					print(" notfound target")
		except Exception as e:
			print(e)
		clipButton = browser.find_elements_by_class_name("PVMjB")[-2]
		clipButton.click()
		time.sleep(2)
		# To send a Document(PDF, Word file, PPT)
		browser.find_element_by_css_selector("input[type=file]").send_keys(docPath)
		time.sleep(2)
		whatsapp_send_button = browser.find_element_by_css_selector("span[data-icon=send]")
		whatsapp_send_button.click()

def insta_scraper(insta_account):

	r = requests.get('https://www.instagram.com/'+insta_account+'/')
	soup = bs(r.text, 'lxml')
	script = soup.find('script', text=lambda t: t.startswith('window._sharedData'))
	page_json = script.string.split(' = ', 1)[1].rstrip(';')
	data = json.loads(page_json)
	non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
	post = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
	for i in range(2):
		display_url=post[i]["node"]["display_url"]
		type=post[i]["node"]["__typename"]
		if type=="GraphImage":
			image_likes=post[i]["node"]["edge_liked_by"]["count"]
			image_downloader_and_sender(display_url,type)
		elif type=="GraphVideo":
			video_url=post[i]["node"]["video_url"]
			video_views=post[i]["node"]["video_view_count"]
			video_likes=post[i]["node"]["edge_liked_by"]["count"]
			image_downloader_and_sender(video_url,"GraphVideo")



def news(search="kerala"):

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

		send("*"+articles["articles"][i]["title"].upper()+"*"+"\n"+articles["articles"][i]["description"]+"\nRead more: "+articles["articles"][i]["url"])
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

def morning():
	print("1 min")
	fn("funny news malayalam")
	print("1 min")
def insta():
	accounts=["criticscut","9gag","ffc.trolls","trollmovies","ar._beatz"]
	account=random.choice(accounts)
	insta_scraper(account)

schedule.every(3).hours.do(youtube)
schedule.every(2).hours.do(insta)
schedule.every().day.at("07:30").do(news)




while True:
	schedule.run_pending()
	time.sleep(4)
