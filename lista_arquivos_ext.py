import os

# as extensões dos arquivos precisam estar sem o ponto
# o caminho (path) precisa usar '/' e terminar em '/'


def lista_arq_ext(path, extensoes):
	if extensoes == []: # (vazio)
		return [i for i in os.listdir(path)]
	else:
		 return [i for i in os.listdir(path) if i.split('.')[-1] in extensoes

# Exemplo 1:
# caminho = 'c:/'
# arquivos_csv_txt = lista_arq_ext(caminho, ['csv', 'txt'])

# Exemplo 2:
# caminho = None    # (pasta atual)
# arquivos_csv = lista_arq_ext(caminho, ['csv'])
