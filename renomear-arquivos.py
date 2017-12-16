import os

def renomear_arquivos():
	#Pega os arquivos que estão no caminho e coloca na lista
	caminho_arquivos = os.listdir(r"D:\udacity\python\imagens-renomear")
	print(caminho_arquivos)
	#Pega o caminho que estou
	caminho_salvo = os.getcwd()
	print("Onde estou agora: "+caminho_salvo)
	os.chdir(r"D:\udacity\python\imagens-renomear")
	for nome_arquivo in caminho_arquivos:
		os.rename(nome_arquivo, nome_arquivo.translate(str.maketrans('','',"0123456789")))
	os.chdir(caminho_salvo)

renomear_arquivos()













