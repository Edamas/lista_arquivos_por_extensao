import os

# as extensões dos arquivos precisam estar sem o ponto
# o caminho (path) precisa usar '/' e terminar em '/'


def lista_arquivos(path, extensoes):
	if extensoes == []: # (vazio)
		return [i for i in os.listdir(path)]
	else:
		 return [i for i in os.listdir(path) if i.split('.')[-1] in extensoes

# Exemplo 1:
# arquivos_csv_txt = lista(arquivos, ['csv', 'txt']

# Exemplo 2:
# arquivos_csv = lista(arquivos, ['csv']
