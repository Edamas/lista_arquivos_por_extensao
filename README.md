# lista_arquivos_por_extensao
#### Lista arquivos de uma pasta com possibilidade de filtrar as extensões (Python)

### Exemplo 1:

arquivos_csv_txt = lista_arq_ext(arquivos, ['csv', 'txt', 'CSV', 'TXT])

> ['caracteristicas.csv', 'destrinchando.txt', 'html_status_codes.csv', 'user_agent_list.csv']

### Exemplo 2:

arquivos_csv = lista_arq_ext(arquivos, ['csv'])

> ['caracteristicas.csv', 'html_status_codes.csv', 'user_agent_list.csv']

### Observações
as extensões dos arquivos precisam estar sem o ponto
o caminho (path) precisa usar '/' e terminar em '/'
