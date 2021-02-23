from konlpy.tag import Mecab

m = Mecab()

with open("B25J.txt", "r", encoding='CP949') as f:
	text = f.read()
	a = m.morphs(text)

file = open('B25J_Mecab.txt','w', encoding='CP949')
for i in range(len(a)):
	file.write(a[i] + " ")

file.close()
