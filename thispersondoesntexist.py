import requests , os

url = "https://thispersondoesnotexist.com"
Val = int(input("Введите количество: "))
x=1
path = os.getcwd()
while x != Val+1:
	s=requests.Session()
	r = s.post('https://thispersondoesnotexist.com/image')
	d = requests.get(r.url)
	save = open(path+f"//thispersondoesnotexist({x}).png", "wb")
	save.write(d.content)
	save.close()
	print(f"{x} файл сохранен по пути {path} с названием thispersondoesnotexist({x}).png")
	x+=1
input("Нажмите любую клавишу чтобы выйти..")
