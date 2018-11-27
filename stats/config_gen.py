# Author      : Zuguang Liu
# Date        : 2018-11-27 17:00:27
# Python Ver  : 3.6
# Description : 

import configparser

config = configparser.ConfigParser()

DEFAULT_DICT=dict()
DEFAULT_DICT['data_dir']='../database/'
DEFAULT_DICT['ptofile']=True

config['DEFAULT']=DEFAULT_DICT
with open('config.ini', 'w') as configfile:
	config.write(configfile)