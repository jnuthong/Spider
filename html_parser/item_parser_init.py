# -*- encoding: utf-8 -*- 
# author : jianbin.hong.cn@gmail.com
# date	 : 2015/09/12

import os, sys
sys.path.append(os.getcwd())
from item_parser import *

if __name__ == "__main__":
	if os.path.isfile(img_data_toadd):
		os.remove(img_data_toadd)
	if os.path.isfile(mat_data_toadd):
		os.remove(mat_data_toadd)
	if os.path.isfile(basic_data):
		os.remove(basic_data)