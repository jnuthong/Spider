# !/bin/sh
# author : jianbin.hong.cn@gmail.com
# date	 : 2015/09/10

HTML_SCRIPT_DIR=$(dirname $(dirname $(pwd)))/html_parser
SCRIPT_DIR=$(pwd)
DATA_DIR=$(dirname $(pwd))/data
DATE=$(date +"%Y%m%d")
DATA_DIR_GAME_TYPE=$DATA_DIR/game_type
DATA_DIR_GAME=$DATA_DIR/game_page
PYTHON=/opt/local/bin/python

FILE_LIST=$(ls $DATA_DIR_GAME/"20150910")
IFS=$'\n' array=($FILE_LIST);
#　set up the initial env
$PYTHON $HTML_SCRIPT_DIR/item_parser_init.py

for ele in "${array[@]}";
do
	$PYTHON $HTML_SCRIPT_DIR/item_parser.py $DATA_DIR_GAME/"20150910/$ele"
done;