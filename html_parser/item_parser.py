# -*- encoding: utf-8 -*- 
# author : jianbin.hong.cn@gmail.com
# date	 : 2015/09/10

import sys, os, re, json
from bs4 import BeautifulSoup
from datetime import datetime

current_date 	= datetime.now().strftime("%Y%m%d")
current_dir 	= os.path.dirname(os.path.realpath(__file__))
img_dir			= os.path.abspath(os.path.join(current_dir, "../img_data/"))
mat_dir			= os.path.abspath(os.path.join(current_dir, "../game_material/"))
img_data_dir 	= img_dir + "/" + current_date
mat_data_dir 	= mat_dir + "/" + current_date

img_data_toadd 	= img_data_dir + "/img_to_retrieve" # still save the pure url link
mat_data_toadd	= mat_data_dir + "/mat_to_retrieve"
basic_data		= os.path.abspath(os.path.join(current_dir, "../")) + "game_data"

if os.path.isdir(img_data_dir) is False:
	os.mkdir(img_data_dir)

if os.path.isdir(mat_data_dir) is False:
	os.mkdir(mat_data_dir)

IMG_FILE = open(img_data_toadd, 'aw+')
MAT_FILE = open(mat_data_toadd, "aw+")
GAM_FILE = open(basic_data, "aw+")

def main():
	"""
	"""
	game_type = sys.argv[1].split("/")[-1]
	game_type = game_type.split("_")[0]
	with open(sys.argv[1], 'r') as file_obj:
		soup = BeautifulSoup(file_obj)
		items = soup.find_all("div", {"class": "item"})
		for item in items:
			# process each game item
			dl 		= item.find("dl", {"class": "clearfix"})
			img 	= dl.find("img")["src"]
			dd 		= item.find("dd")
			title 	= dd.find("h4").find("a").text
			ul 		= dd.find("ul")
			lis 	= ul.find_all("li")
			info 	= dict()
			for li in lis:
				# res = re.findall(r'.*<b>.*?</b>', li.text)
				# handle the outlink part, both for the game img and game article
				if "游戏图片" in li.text:
					res = [ele.strip("\n\r\t") for ele in li.text.strip("\n\r").split(" ") if len(ele.strip("\n\r\t")) > 1]
					for ele in res: 
						ele = ele.split("：")
						info[ele[0]] = ele[1]

					hrefs = li.find_all("a")
					for href in hrefs:
						if "article" in href["href"]:
							MAT_FILE.write(title + "\t" + href["href"] + "\n")
						elif "pic" in href["href"]:
							IMG_FILE.write(title + "\t" + href["href"] + "\n")
				else:
					res = li.text.split("：")
					info[res[0]] = res[1]
			info["img"] = img
			GAM_FILE.write(title + "\t" + game_type + "\t" + json.dumps(info) + "\n")

if __name__ == "__main__":
	reload(sys)
	sys.setdefaultencoding("utf-8")

	main()
	IMG_FILE.close()
	MAT_FILE.close()
	GAM_FILE.close()