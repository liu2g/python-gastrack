# Author      : Zuguang Liu
# Date        : 2018-11-27 17:05:16
# Python Ver  : 3.6
# Description : 

import configparser

config = configparser.ConfigParser()

DEFAULT_DICT=dict()
DEFAULT_DICT['gb_url']='https://www.gasbuddy.com/home?search='
DEFAULT_DICT['data_dir']='../database/'


config['DEFAULT']=DEFAULT_DICT
with open('config.ini', 'w') as configfile:
	config.write(configfile)