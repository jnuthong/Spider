# author : jianbin.hong.cn@gmail.com
# date	 : 2015/09/10

import sys
from bs4 import BeautifulSoup

def main():
	"""
	"""
	path = sys.argv[2].split(";")
	name = sys.argv[3]
	with open(sys.argv[1], 'r') as file_obj:
		soup = BeautifulSoup(file_obj)
		entity = None
		if len(path) == 0:
			print "[Error] Expected path length more then zero"
			exit()

		for i in range(len(path)):
			ele = path[i].split(":")
			assert len(ele) >= 1
			if i == 0:
				entity = soup.find(ele[0], {"class": ele[1]})
			else:
				entity = entity.find(ele[0], attrs={"class": ele[1]})

		print entity[name]

if __name__ == "__main__":
	reload(sys)
	sys.setdefaultencoding("utf-8")

	main()