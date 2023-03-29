import pandas as pd
import chardet

# Função que identifica a codificação de um arquivo
def encoding(x):
    with open(x, 'rb') as f:
        # Abre o arquivo em modo binário
        result = chardet.detect(f.read())
        encoding = result['encoding']
    # Retorna a codificação encontrada    
    return encoding

# Ler o arquivo txt
with open('C:\\Users\\Matheus\\OneDrive\\Área de Trabalho\\plano.txt', 'r', encoding=encoding('C:\\Users\\Matheus\\OneDrive\\Área de Trabalho\\plano.txt')) as f:
    linhas = f.readlines()

# Criar as listas para cada coluna
cod = []
mascara_plano = []
descricao = []
tipo = []

# Realizar o split em cada linha do arquivo e armazenar nas listas correspondentes
for linha in linhas:
    cod.append(linha[:7].strip())
    mascara_plano.append(linha[7:18].strip())
    descricao.append(linha[27:67].strip())
    tipo.append(linha[67:68].strip())

# Criar o dataframe com as colunas criadas
df = pd.DataFrame({'cod': cod, 'mascara_plano': mascara_plano, 'descricao': descricao, 'tipo': tipo})

# Exibir o dataframe
print(df)