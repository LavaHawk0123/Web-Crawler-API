from urllib.parse import urlparse

# Get the domain name for the crawler 
# Input : (name.email.example.com)
# Output : example.com

def getDomainName(url):
	try:
		sub_domain = getSubDomainName(url).split('.')
		return sub_domain[-2]+'.'+sub_domain[-1]
	except:
		return ''
		

# Function to get sub domain names (name.email.example.com)
def getSubDomainName(url):
	try:
		return urlparse(url).netloc
	except:
		return ''
