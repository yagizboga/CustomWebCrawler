import requests 
import traceback
import os

def subdomainfinder():
	file = getwords()
	if file is None:
		return
	
	url = input("url(without https): ")
	if not url:
		print("Invalid URL Input.")
		return
	
	for i in file:
		request("https://"+str(i) +"."+url)

def directoryfinder():
	file = getwords()
	if file is None:
		return
	
	url = input("url(without https): ").strip()
	if not url:
		print("Invalid URL Input.")
		return
	
	for i in file:
		request("https://"+url+"/"+str(i))


def request(url):
	session = requests.Session()
	try:
		r = session.get(url)
		if r:
			print("----------> "+url + " is found!")
	except Exception as e:
		print(url + " " +type(e).__name__)


def getwords():
	filepath = input("wordlist file path: ")
	if not os.path.isfile(filepath):
		print("File not found or path is invalid.")
		return None
	f = []
	with open(filepath,"r") as f_obj:
		for line in f_obj:
			f.append(line.strip())
	return f
	

if __name__ == "__main__":
	while True:
		print("\nCustomCrawler\nType --help for help.\n")
		userInput = input()
		if userInput == "--help":
			print("-s for subdomain finder\n-d for directory finder\n")
		elif userInput == "-s":
				subdomainfinder()
		elif userInput == "-d":
				directoryfinder()
		elif userInput == "exit":
			print("Exiting..")
			exit()