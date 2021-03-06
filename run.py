# -*- coding: utf-8 -*-

import os
import get_json_v3 
import json_parse
import download_process
from multiprocessing import freeze_support

if __name__ == '__main__':
	# 解决使用 pyinstaller 打包程序后，多进程错误
	freeze_support()

	get_json_v3.main()
	json_parse.main()
	download_process.main() # 多进程

	os.system("pause")