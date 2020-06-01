"""
這裡是主程式
"""


import img

print("歡迎來到mykirito的飯製版本，目前還在開發中......")

id=input("登入id:")

player=img.Player(id)
print("成功登入:%s"%player.id)
print("目前經驗:%d"%player.exp)
print("目前等級%d"%player.level)
for i in range(1000):
	player.act()
player.level_up()
print("目前等級%d"%player.level)
print("目前經驗:%d"%player.exp)
quit1=input("")
