From bs4 import BeautifulSoup
Import requests
PAGECOUNT=10

def getPage(url):
	r=requests.get(url)
	data=r.text
	obj=BeautifulSoup(data,”lxml”)
	
	return obj

def main():


	words=[]
	content=getPage(“https://www.heise.de/thema/https”).findAll(“div”,{“class”:”recommendation ”})
	for item in content:
		c=item.find(“header”)
		words+=c.contents[0].encode(“utf-8”)
	print (words)
main()