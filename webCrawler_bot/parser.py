from html.parser import HTMLParser
from urllib import parse
import getLink

class getlinksfromWebsite(HTMLParser):

	def __init__(self,base_url,page_url):
		super().__init__()
		self.tagFound = False
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()
		
	def error(self,msg):
		pass
	
	def handle_starttag(self,tag,att):
		if tag=="a":
			for (attr,val) in att:
				if(attr =="href"):
					print(f"Found link {val}")
					# If it is a www.% i.e a full url then left unmodified, if relative it adds a base url
					url = parse.urljoin(self.base_url,val)
					self.links.add(url)
		else:
			pass
	
	def get_page_links(self):
		return self.links()
