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

# adicionar os pontos nas posições especificadas
df['mascara_plano'] = [
    ''.join([
        s[:1], '.' if len(s) > 1 else '', s[1:2], '.' if len(s) > 2 else '', s[2:3],
        '.' if len(s) > 3 else '', s[3:5], '.' if len(s) > 5 else '', s[5:]
    ]) for s in df['mascara_plano']
]

# exibir o DataFrame resultante
print(df)

# salvar o arquivo Excel formatado
df.to_excel('C:\\Users\\Matheus\\OneDrive\\Área de Trabalho\\plano.xlsx')
