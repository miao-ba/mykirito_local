"""
這是mykirito飯製的本地端試手版
這裡是類別庫
作者:喵八
目前功能:
創建新角色
行動
升級
"""

#匯入函式庫區
import time
import random
import os

#類別庫
class Player():
	def get_level_list(self):
		f=open("level.txt","r",encoding="utf-8")
		level_list=f.read()
		f.close()
		level_list=level_list.split("\n")
		for i in range(len(level_list)):
			level_list[i]=level_list[i].split(",")
			level_list[i]=int(level_list[i][0]),int(level_list[i][1])
		return level_list
	def get_info(self,name):
		if os.path.isfile(name+".txt"):
			file=open(name+".txt","r")
			L=file.read()
			box=L.split(",")
			for i in range(len(box)):
				box[i]=int(box[i])
			return [name,box]
		else:
			file=open(name+".txt","w")
			file.write("0,1")
			file.close()
			return [name,[0,1]]
	def __init__(self,name):
		info=self.get_info(name)
		self.level_list=self.get_level_list()
		self.id=info[0]
		self.exp=info[1][0]
		self.level=info[1][1]
	def act(self):
		self.exp=self.exp+random.randrange(15,21)
	def level_up(self):
		for i in self.level_list:
			if self.exp > i[1]:
				self.level=i[0]
				break