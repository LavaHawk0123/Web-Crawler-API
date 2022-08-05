import os

home_path = "/home/neo/coursera_courses/scripting-python-sql-IBM/week_3/"


# Create a directory for each website
# @params -> directory : The specified path to create a folder for a new project
# output : void

def create_webpage_dir(directory):
	if not os.path.exists(directory):
		print(f"creating project folder : {directory}")
		os.makedirs(directory)
	
# Function to create a new file
# @params -> path : The specified path to create a file
# 		  -> data : The data to write to the newly created file
# output : void

def create_file(path,data):
	f = open(path,'w')
	f.write(data)
	f.close()
	
	
# Function to create the data files for a project
# @params -> project_name : The specified folder/project to use
# 		  -> base_url     : The base url for the bot to crawl
# output : void
	
def create_data_files(project_name,base_url):
	queue = project_name+"/queue.txt"
	crawled = project_name+"/crawl.txt"
	if not os.path.isfile(queue):
		create_file(queue,base_url) # We need to add a base URL otherwise no place to start
	if not os.path.isfile(crawled):
		create_file(crawled,"") # We need to initialise it to empty

# Function to append to a file
# @params -> path : The specified path to append to a file
# 		  -> data : The data to write to the file
# output : void

def append_to_file(path,data):
	with open(path,'a') as file:
		file.write(data+"\n")
		file.close()	

# Function to delete a file
# @params -> path : The specified path to a file to delete
# output : void

def delete_file(path):
	with open(path,'w') as file:
		pass

# Function to read lines of a file and load a set
# @params -> path : The specified path to a file to read and convert 
# output : set of links in project url	
def file_to_set(path):
	links = set()
	with open(path,'rt') as file:
		for line in file:
			links.add(line.replace("\n",""))
	return links

# Function to append links in a set and save it in a file
# @params -> path : The specified path to a file to save contents of the set
# output : void			
def set_to_file(link_set,path):
	delete_file(path)
	for l in sorted(link_set):
		append_to_file(path,l)

# Function to test functionality of package
# @params	: void
# output	: void
def testbench():		
	create_webpage_dir("test")
	create_data_files("test","www.google.com")
