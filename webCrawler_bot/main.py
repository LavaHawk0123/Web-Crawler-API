import threading
from queue import Queue
from crawler import Spider
from domain import *
from getLink import *

home_path = "/home/neo/coursera_courses/scripting-python-sql-IBM/week_3/"

PROJECT_NAME = "ROS"
HOMEPAGE = "http://wiki.ros.org"
DOMAIN_NAME = getDomainName(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME+"/queue.txt"
CRAWLED_FILE = PROJECT_NAME+"/crawl.txt"
NUMBER_OF_THREADS = 8
thread_queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)
