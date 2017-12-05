import os

def renomear_arquivos():
	arquivo = os.listdir(r"D:\udacity\python\imagens-renomear")
	print(arquivo)

	#Mostra lugar atual
	lugar_atual = os.getcwd()
	print("Caminho atual: " +lugar_atual)

	#Faz o os trabalhar com o caminho das imagens
	os.chdir(r"D:\udacity\python\imagens-renomear")

	for nome_arquivo in arquivo:
		os.rename(nome_arquivo, nome_arquivo.translate(str.maketrans('','','1234567890')))
	
	os.chdir(lugar_atual)

renomear_arquivos()
















