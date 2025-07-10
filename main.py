import requests 
import traceback

def subdomainfinder():
	file = getwords()
	url = input("url(without https): ")
	for i in file:
		request("https://"+str(i) +"."+url)
def directoryfinder():
	file = getwords()
	url = input("url(without https): ")
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
	f = []
	with open(filepath,"r") as f_obj:
		for line in f_obj:
			f.append(line.strip())
	return f
	
if __name__ == "__main__":
	while True:
		print("CustomCrawler\nType --help for help.\n\n")
		userInput = input()
		if userInput == "--help":
			print("-s for subdomain finder\n-d for directory finder\n\n")
		elif userInput == "-s":
				subdomainfinder()
		elif userInput == "-d":
				directoryfinder()
		elif userInput == "exit":
			exit()
