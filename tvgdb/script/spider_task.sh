# author : jianbin.hong.cn@gmail.com
# date	 : 2015/09/10

HTML_SCRIPT_DIR=$(dirname $(dirname $(pwd)))/html_parser
SCRIPT_DIR=$(pwd)
DATA_DIR=$(dirname $(pwd))/data
DATE=$(date +"%Y%m%d")
DATA_DIR_GAME_TYPE=$DATA_DIR/game_type
DATA_DIR_GAME=$DATA_DIR/game_page
PYTHON=/opt/local/bin/python

_DOMAIN="http://tvgdb.duowan.com/"
# step 1, get all type of game main page;
if [ ! -d "$DATA_DIR_GAME_TYPE/$DATE" ]; then
	mkdir $DATA_DIR_GAME_TYPE/$DATE
fi

if [ ! -d "$DATA_DIR_GAME/$DATE" ]; then
	mkdir $DATA_DIR_GAME/$DATE;
fi

while IFS="" read -r line
do
	# get total number of page number
	curl $_DOMAIN$line > $DATA_DIR_GAME_TYPE/$DATE/$line
	res=$($PYTHON $HTML_SCRIPT_DIR/path_parser.py $DATA_DIR_GAME_TYPE/$DATE/$line "div:mod-page-bd;a:last" href)
	page=$(echo $res | grep -o 'page=[0-9]\+' | grep -o '[0-9]\+')
	for i in $(seq 1 $page);
	do
		curl $_DOMAIN$line"?page=$i" > $DATA_DIR_GAME/$DATE/$line"_$i";
		exit
	done
	# echo "$_DOMAIN$line"
done < $DATA_DIR/SETTING_GAME_TYPE