#!/usr/bin/python
import sys
import re
import datetime
from httplib2 import Http
from json import dumps
from BeautifulSoup import BeautifulSoup 

# url for channel google hangouts
<<<<<<< HEAD
url_primary = "https://chat.googleapis.com/v1/spaces/AAAA-uD-1as/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=tFZsahFaccoXTf360VrZO6GkIDCHMhH3ipZPtzy19_Y%3D"
url_loging = "https://chat.googleapis.com/v1/spaces/AAAAI2sdHWw/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=mJ1V_TRDlhi_EhI2W8l9y0tuWL3MkTkrmSBLY_487h0%3D"
url_test = "https://chat.googleapis.com/v1/spaces/AAAAz9uEl28/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=IiA799lihbxX16DZUzJatIekyQScPisQ2VJN-elzVMQ%3D"
=======
url_primary = "https://chat.googleapis.com/v1/spaces/AAAAjYF3XU0/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=48oMnLqf"
url_loging = "https://chat.googleapis.com/v1/spaces/AAAA1EgMQ9U/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=9LZHV4Tqjff4"
url_test = "https://chat.googleapis.com/16DZUzJatIekyQScPisQ2VJN-elzVMQ%3D"
>>>>>>> 378c8dbc4f2f966b2cc28c734d148603031d34ed

# function send alert for API Hangout, or Slack,...
def sendGG(text, url_input):
	url = url_input
	bot_message = {'text' : text}
	message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}
	
	http_obj = Http()
	
	response = http_obj.request(
		uri=url,
		method='POST',
		headers=message_headers,
		body=dumps(bot_message),
	)


# function open whitelist
def openList(file):
	a = []
	with open(file) as f:
		for line in f:
			a.append(line.strip())
	print a
	return a

# function for delete html tag return plaintext
def clean_html(raw_html):
	cleantext = re.sub('<.*?>', '', raw_html)
	cleantext = re.sub('&#\d+;', '', cleantext)
	cleantext = cleantext.replace("&quot;","")
	return cleantext

# function for search keyword in code and return true or false
# the paramater key is file
def ext_match(key, code):
	key = key.replace("/home/sgithub/scripts/github_search/output/","")
	key = key.replace(".html","")

	if key in code:
		return True
	else:
		return False

# function get project, file name, link and code
def get_info(element):
	s = str(element)
	soup =  BeautifulSoup(s)
	_name = soup.findAll('a')

	# get project name
	_projectName = str(_name[1].contents)
	_projectName = _projectName.replace("[u'","")
	_projectName = _projectName.replace("']","")

	# get file name
	_fileName = str(_name[2].contents)
	_fileName = _fileName.replace("[u'","")
	_fileName = _fileName.replace("']","")

	# get link of file contains sensitive information
	_link = re.findall('https:\/\/.*\"}', str(_name[2]))
	_link = _link[0].replace('"}','')

	# check liw(link in whitelist)
	liw = openList("/home/sgithub/scripts/github_search/whitelist.txt")

<<<<<<< HEAD
	# check repo(repo in whitelist)
	repo = openList("/home/sgithub/scripts/github_search/whitelist_repo.txt")
	
	if (_link in liw) or (_projectName in repo):
=======
	if _link in liw:
>>>>>>> 378c8dbc4f2f966b2cc28c734d148603031d34ed
		return "IN", ""
	else:
		_code = soup.findAll('table')
		str_code = BeautifulSoup(str(_code))
		str_code = str_code.findAll("td", {"class": "blob-code blob-code-inner"})

		_code = ""
		for line in str_code:
			_code = _code + clean_html(str(line)) + "\n"

		_result = ""
		if (ext_match(sys.argv[1],_code) == True):
			_result = "Project: " + _projectName + "\n" + "File: " + _fileName + "\nLink: " + _link +"\n```" + _code + "```"

		return _result, _link

# fuction get day from source code and compare day of system
def get_day(element):
	s = str(element)
	soup = BeautifulSoup(s)
	_time = soup.findAll('relative-time')
	date = re.findall("\d+-\d+-\d+",str(_time[0]))
	date_sys = datetime.datetime.now().date()

	if str(date_sys) == str(date[0]):
		return True
	else:
		return False

# fuction get follow code and alert with slack
def get_data(file):
	f = open(file)
	soup = BeautifulSoup(f) 
	mydivs = soup.findAll("div", {"class": "code-list-item col-12 py-4 code-list-item-public "})
	for div in mydivs:
		flag = get_day(div)
		if flag == True:
			a, _link  = get_info(div)
			#print a
			if a != "IN":
				sendGG(a, url_primary)
					# get code contain sensitive data
				f = open("/home/sgithub/scripts/github_search/whitelist.txt", "a")
				f.write(_link + "\n")
				f.close()


def sendLog(name, cate, status):
        dt = datetime.datetime.now()
        d = str(dt).split(" ")
        message = "```" + d[0] + " | " + d[1] + " | " + name + "\t| " + cate + " | [GIT] Scanning keyword is " + status + "!```"
	sendGG(message, url_loging)

# execute from get_search.sh


try:
	sendLog("get_data.py","INFO","Started")
	get_data(sys.argv[1])
	sendLog("get_data.py","INFO","Completed")
except Exception as e:
	sendLog("get_data.py","ERROR","Fail!")
