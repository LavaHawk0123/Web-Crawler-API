from urllib.request import urlopen
from parser import *
from getLink import *
class Spider:
	
	# Class Variable declerations
	project_name = "" # Name/Project folder
	base_url = ""     # Base URL for crawling
	domain_name = ""  # Domain name for 
	queue_file = ""   # Text file to save the shutdown configuration of the queue var
	crawled_file = "" # Text file to save the shutdown configuration of the crawled var
	crawled = set()
	queue = set()
	home_path = "/home/neo/coursera_courses/scripting-python-sql-IBM/week_3/"
	
	def __init__(self,project_name,base_url,domain_name):
		Spider.project_name = project_name # Name/Project folder
		Spider.base_url = base_url    # Base URL for crawling
		Spider.domain_name = domain_name
		Spider.queue_file = Spider.project_name + "/queue.txt"
		Spider.crawled_file = Spider.project_name + "/crawl.txt"
		
		self.boot_crawler_bot()
		self.crawl_website('first-spider',Spider.base_url)
		
	
	def boot_crawler_bot(self):
	
		# Creates the directory for the project
		getLink.create_webpage_dir(Spider.project_name)
		
		# Creates the Queue and the crawled text files
		getLink.create_data_files(Spider.project_name,Spider.base_url)
		
		# Creates the set for queue using the text file
		Spider.queue = getLink.file_to_set(Spider.queue_file)
		
		# Creates the set for crawled using the text file
		Spider.crawled = getLink.file_to_set(Spider.crawled_file)
		
		
	def crawl_website(self,thread_name,page_url):
		if page_url not in Spider.crawled:
			print(f"{thread_name} crawling {page_url}")
			print("Current queue size : {}".format(str(len(Spider.queue))))
			print("Crawled : {}".format(str(len(Spider.crawled))))
			Spider.add_links_to_queue(Spider.gather_links(page_url))
			Spider.queue.remove(page_url)	
			Spider.crawled.add(page_url)
			Spider.update_files()
	
	def gather_links(page_url):
		# Variable to store the converted server response
		html_string = ""
		try:
			response = url.open(page_url)
			# If the data is of html type
			if response.getheader('Content-Type')=='text/html':
				# Read the data in binary
				html_bytes_data = response.read()
				# Decode the bytes using utf-8 decoding
				html_string = html_bytes_data.decode("utf-8")
			# Create an object of link finder
			finder = parser.getlinksfromWebsite(Spider.base_url,page_url)
			# Calls all the HTML functions
			finder.feed(html_string)
		except:
			print(f"Error : Cannot crawl page {page_url}")
			return set()
			
		# Return the links set
		return finder.get_page_links()				
		
		
	def add_links_to_queue(links):
		for url in links:
			if url in Spider.queue:
				continue
			if url in Spider.crawled:
				continue
			if Spider.domain_name not in url:
				continue
			Spider.queue.add(url)
		
	def update_files():
		getLink.set_to_file(Spider.queue,Spider.queue_file)
		getLink.set_to_file(Spider.crawled,Spider.crawled_file)
				
				
		
			 
				
		
	
