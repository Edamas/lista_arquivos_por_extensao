# lista_arquivos_por_extensao
#### Lista arquivos de uma pasta com possibilidade de filtrar as extensões (Python)


### Observações
1 as extensões dos arquivos precisam estar sem o ponto

2 o caminho (path) precisa usar '/' e terminar em '/'

3 o caminho pode ser None, para a pasta atual

4 as extensões podem ser [] para todos os arquivos


#### Exemplo 1:
path = '/./'  # pasta atual
arquivos_csv_txt = lista_arq_ext(path, ['csv', 'txt', 'CSV', 'TXT])

> ['caracteristicas.csv', 'destrinchando.txt', 'html_status_codes.csv', 'user_agent_list.csv']


#### Exemplo 2:
path = 'c:/windows/'
arquivos_csv = lista_arq_ext(arquivos, ['csv'])

> ['caracteristicas.csv', 'html_status_codes.csv', 'user_agent_list.csv']

