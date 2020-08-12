
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
from time import sleep
import json
import os
import sys
import re
import random
import time
import requests
import schedule
from datetime import datetime
def date_now():
	# datetime object containing current date and time
	now = datetime.now()
	dt_string = now.strftime("%b-%d-%Y")
	return str("\n🌄️ *"+dt_string+"*\n")
contacts = ['Bot1','Bot2','Bot3','Bot0'] #Bejoy Jiofi','Sandeep','Abu EC','sidhu',
browser = webdriver.Firefox(executable_path=r'/root/Desktop/geckodriver')
browser.get('https://web.whatsapp.com')
wait = WebDriverWait(browser, 3)


def close_json(data):
	os.remove("verify.json")
	print(data)
	f=open("verify.json","w")
	json.dump(data,f, indent=4)

def admin(id,media,message):

	op=open("verify.json","r")
	print(message)
	print(message.split())
	data=json.load(op)

	if media.lower()=="yt" or media.lower()=="news":


		message="⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️\n*വിട്ട് കളയണം 1.0*"+" 🌀️"+date_now()+"\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n*"+message+"\n➖➖➖➖➖➖➖➖➖➖\n\nto advertise here contact angel peter\n\n"
		data[id]={}
		data[id]["payload"]=data.get("payload", message)
		send_message((message+"UNIQUE_ID: "+str(id)),"admin")

		close_json(data)

	elif media.lower()=="instapic":

		url=message.split()[0]
		caption="*"+str(message.split()[1])+"*"+" *K*"+" 👍️\n⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️\n*വിട്ട് കളയണം 1.0*"+" 🌀️"+date_now()+"©️ *2020*\n"
		data[id]={}
		data[id]["link"]=data.get("link", url)
		data[id]["payload"]=data.get("payload",caption )
		image_downloader_and_sender(url,"GraphImage","admin",caption+str(id))

		close_json(data)

	elif media.lower()=="instavideo":


		url=message.split()[0]
		caption="*"+str(message.split()[1])+"*"+" *K*"+" 👍️\n⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️\n*വിട്ട് കളയണം 1.0*"+" 🌀️"+date_now()+"©️ *2020*\n"
		#send_message((message+"UNIQUE_ID"+id),"admin")
		data[id]={}
		data[id]["link"]=data.get("link", url)
		data[id]["payload"]=data.get("payload",caption )
		image_downloader_and_sender(url,"GraphVideo","admin",caption+str(id))
		close_json(data)

	elif id=="end":#or media=="end" or message="end":
		while True:

			target="Admins"
			try:

				x_arg = '//span[contains(@title,' + target + ')]' #/html/body/div[1]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div/span
				ct = 0
				try:
					op=open("verify.json","r")

					data=json.load(op)
					# group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
					# group_title.click()
					browser.find_element_by_css_selector("span[title='" + target + "']").click()
					print("found target")
					admin_message=browser.find_elements_by_class_name("eRacY")[-1]
					print(admin_message.text)
					if "approve" in admin_message.text.lower():
						id=admin_message.text.lower().split()[1]
						print("message approved")
						print(id)
						print(data)
						if "insv" in id:
							link=data[id]["link"]
							caption=data[id]["payload"]
							send("sending "+id+" to all groups")
							image_downloader_and_sender(link,"GraphVideo","verified",caption)
						if "insi" in id:
							link=data[id]["link"]
							caption=data[id]["payload"]
							send("sending "+id+" to all groups")
							image_downloader_and_sender(link,"GraphImage","verified",caption)
						elif "yt" in id or "nws" in id:
							message=data[id]["payload"]
							send("sending "+id+" to all groups")
							send_message(message,"verified")
						return False
					elif "edit" in admin_message.text.lower():
						id=admin_message.text.lower().split()[1]
						while True:
							admin_message=browser.find_elements_by_class_name("eRacY")[-1]
							if "edited" in admin_message.text.lower() or "":
								payload=re.sub("edited","",admin_message.text)
								payload=re.sub("Edited","",admin_message.text)
								data[id]["payload"]=payload

								if "insi" in id:

									link=data[id]["link"]
									caption=data[id]["payload"]
									send("sending"+id+" to all groups")
									image_downloader_and_sender(link,"GraphImage","verified",caption)

								elif "insv" in id:
									link=data[id]["link"]
									caption=data[id]["payload"]
									send("sending"+id+" to all groups")
									image_downloader_and_sender(link,"GraphVideo","verified",caption)
								elif "yt" in id or "nws" in id:
									message=data[id]["payload"]
									send("sending"+id+" to all groups")
									send_message(message,"verified")



								break
						return False
					elif "ok" in admin_message.text.lower():
						return False
						break

					# elif "nope" in admin_message.text.lower():
					# 	return True
					# 	break

				except:
					ct += 1
					sleep(1)
					print("")
			except Exception as e:
				print(e)

def send_message(message,user):
	global  wait, browser
	print(message,"reached send")
	if user=="verified":

		for i in contacts:
			target=i
			search_box = input_box = browser.find_elements_by_xpath(
					'/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')[0] #/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]
			search_box.send_keys(target + Keys.ENTER)
			sleep(2)
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
						sleep(1)
						print(" notfound target")

				input_box = browser.find_elements_by_xpath(
					'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
				if "\n" in message:
					for part in message.split('\n'):
						 input_box.send_keys(part)
						 ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
					input_box.send_keys(Keys.ENTER)
				else:
					input_box.send_keys(message + Keys.ENTER)
					print("Message sent successfuly")

			except Exception as e :#NoSuchElementException:
				print(e)
				return
	elif user=="admin":

		target="Admins"
		try:
			x_arg = '//span[contains(@title,' + target + ')]' #/html/body/div[1]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div/span
			ct = 0
			while ct!=10:
				try:
					# group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
					# group_title.click()
					browser.find_element_by_css_selector("span[title='" + target + "']").click()
					print("found target")
					break
				except:
					ct += 1
					sleep(1)
					print(" notfound target")

			input_box = browser.find_elements_by_xpath(
				'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
			if "\n" in message:
				for part in message.split('\n'):
					 input_box.send_keys(part)
					 ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
				input_box.send_keys(Keys.ENTER)
			else:
				input_box.send_keys(message + Keys.ENTER)
				print("Message sent successfuly")

		except Exception as e :#NoSuchElementException:
			print(e)
			return

def fn(query):

	from googletrans import Translator
	translator = Translator()

	url="https://www.google.com/search?client=firefox-b-e&biw=772&bih=646&tbs=sbd%3A1&tbm=nws&ei=OYoqX47bH8uxggfs6JSwBQ&q="+query
	content = requests.get(url.encode()).content
	soup=bs(content,"html.parser")

	newss=soup.find_all('div', attrs={'class':'BNeawe s3v9rd AP7Wnd'})
	links=soup.find_all('div', attrs={'class':'kCrYT'})
	heads=newss=soup.find_all('div', attrs={'class':'BNeawe vvjwJb AP7Wnd'})
	# print(newss)
	# print(heads)
	for i in range(0,20,2):
		#send(news.get_text()+"\n")
		head=heads[int(i/2)].get_text()
		head=translator.translate(head, dest='ml').text
		#news=newss[i].get_text()
		news="\n"+links[i+1].get_text()
		news=translator.translate(news, dest='ml').text
		link= (links[i].find("a").get("href"))
		# print(link)
		link=re.sub("/url\?q=","",link)
		link=re.sub("&.*","",link)
		link_to_shorten="https://tinyurl.com/create.php?source=indexpage&url="+link
		tiny_url=requests.get(link_to_shorten).content
		tiny_soup=bs(tiny_url,"html.parser")

		shrt_link=tiny_soup.find_all('b')[1].get_text()
		print(shrt_link)
		full="1234567890"
		id="".join(random.sample(full,3))
		# send_message(head+"\n"+news+"\nRead more at: "+shrt_link+"\n
		message=head+"*\n\n"+news+"\nRead more at: "+shrt_link+"\n"
		admin("nws"+id,"news",message)
		#rint("Read More:: "+link+"\n")
def random_id():

	full="1234567890"
	id="".join(random.sample(full,3))
	return id
		#print("Read More:: "+link)
def youtube():
	from youtube_search import YoutubeSearch
	# search_terms=["malayalam funny","malayalam trending" ,"comedy malayalam", "fun"]
	# search_term=random.choice(search_terms)
	# results = YoutubeSearch(search_term, max_results=10).to_dict()
	count=0
	for i in range(10):
		search_terms=["malayalam trending", "fun","laugh","corona updates",]
		search_term=random.choice(search_terms)
		results = YoutubeSearch(search_term, max_results=10).to_dict()
		title=results[i]["title"]
		channel=results[i]["channel"]
		views=results[i]["views"]
		print(type(views))
		views = str(views)
		if ',' in views.lower() or 'views' in views.lower():
			views=re.sub(",","",views)
			views=re.sub(" views","",views)
		print(views)
		views=(int(views)/1000000)
		format(views, '.2f')
		views=(str(views)+" M")
		duration=results[i]["duration"]
		id=results[i]["id"]
		link="https://www.youtube.com"+results[i]["url_suffix"]
		if verify("youtube",id) ==False:
			message=title+"*\n➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️\nChannel: "+channel+"\nViews: "+str(views)+"\nDuration: "+str(duration)+"\nLink: "+link
			admin("yt"+random_id(),"yt",message)
			# send_message(title+"\nChannel: "+channel+"\nViews: "+str(views)+"\nDuration: "+str(duration)+"\nLink: "+link)
			count+=1
			# if admin("yt"+random_id(),"yt",message):
			# 	print("reached nope")
			# 	count=0
			# 	continue
		else:
			continue
		if count==3:
			msg="end"
			admin(msg,msg,msg)
			break

def verify(media,url):
	op=open("memory.json","r")

	data=json.load(op)
	if url in data[media]:
		return True
	else:
		data[media].append(url)
		os.remove("memory.json")
		print(data)
		f=open("memory.json","w")
		json.dump(data,f, indent=4)
		return False

def send(x):
	print("reached inside send function")
	text_box = browser.find_elements_by_xpath(
		'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]


	text_box.send_keys(x+Keys.ENTER)

def image_downloader_and_sender(url,file_type,user,caption):
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
	if user=="verified":
		for i in contacts:
			target=i
			search_box = input_box = browser.find_elements_by_xpath(
					'/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')[0] #/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]
			search_box.send_keys(target + Keys.ENTER)
			sleep(2)
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
						sleep(1)
						print(" notfound target")
			except Exception as e:
				print(e)
			clipButton = browser.find_elements_by_class_name("PVMjB")[-2]
			clipButton.click()
			sleep(2)
			# To send a Document(PDF, Word file, PPT)
			browser.find_element_by_css_selector("input[type=file]").send_keys(docPath)
			sleep(5)
			whatsapp_caption_feild = browser.find_elements_by_xpath(
			'/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]')[-1]
			message=caption
			if "\n" in message:
				for part in message.split('\n'):
					whatsapp_caption_feild.send_keys(part)
					ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
				whatsapp_caption_feild.send_keys(Keys.ENTER)
			else:
				whatsapp_caption_feild.send_keys(message + Keys.ENTER)
				print("Message sent successfuly")

	elif user =="admin":


		target="Admins"
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
					sleep(1)
					print(" notfound target")
		except Exception as e:
			print(e)
		clipButton = browser.find_elements_by_class_name("PVMjB")[-2]
		clipButton.click()
		sleep(2)
		# To send a Document(PDF, Word file, PPT)
		browser.find_element_by_css_selector("input[type=file]").send_keys(docPath)
		sleep(3)
		whatsapp_caption_feild = browser.find_elements_by_xpath(
		'/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]')[-1]
		message=caption
		if "\n" in message:
			for part in message.split('\n'):
				 whatsapp_caption_feild.send_keys(part)
				 ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
			whatsapp_caption_feild.send_keys(Keys.ENTER)
		else:
			whatsapp_caption_feild.send_keys(message + Keys.ENTER)
			print("Message sent successfuly")

def insta_scraper():
	count=0
	for i in range(10):
		accounts=["criticscut","9gag","aesthetic_kunjamma","ar._beatz","trollmalayalamofficial","book.of.leaders","curiositydotcom","karlniilo"]
		account=random.choice(accounts)
		r = requests.get('https://www.instagram.com/'+account+'/')
		soup = bs(r.text, 'lxml')
		script = soup.find('script', text=lambda t: t.startswith('window._sharedData'))
		page_json = script.string.split(' = ', 1)[1].rstrip(';')
		data = json.loads(page_json)
		non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
		post = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']

		display_url=post[i]["node"]["display_url"]
		type=post[i]["node"]["__typename"]
		if type=="GraphImage":
			image_likes=post[i]["node"]["edge_liked_by"]["count"]
			image_likes=(image_likes/1000)
			format(image_likes, '.2f')
			image_likes=str(image_likes)
			image_id="insi"+random_id()
			if verify("instagram",display_url)==False:
				admin(image_id,"instapic",display_url+" "+str(image_likes))
				#image_downloader_and_sender(display_url,type)
				count+=1
			else:
				continue
		elif type=="GraphVideo":
			video_url=post[i]["node"]["video_url"]
			video_views=post[i]["node"]["video_view_count"]
			video_likes=post[i]["node"]["edge_liked_by"]["count"]
			video_likes=(video_likes/1000)
			format(video_likes, '.2f')
			video_likes=str(video_likes)
			video_id="insv"+random_id()
			if verify("instagram",display_url)==False:
				admin(video_id,"instavideo",(video_url+" "+str(video_likes)))
				# image_downloader_and_sender(video_url,"GraphVideo")
				count+=1
			else:
				continue
		if count==6:
			msg="end"
			admin(msg,msg,msg)
			break

def morning():
	news_topics=["kerala latest","kerala headlines","latest funny news malayalam"]
	news_topic=random.choice(news_topics)
	fn(news_topic)



#schedule.every(2).minutes.do(youtube)
# schedule.every(0.3).minutes.do(insta_scraper)

#schedule.every(5).minutes.do(insta_scraper)
#schedule.every().day.at("07:30").do(news)
schedule.every(3).minutes.do(morning)




while True:
	schedule.run_pending()
	sleep(1)
