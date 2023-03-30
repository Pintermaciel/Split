import pandas as pd
import chardet

def detect_encoding(file_path):
    """Identifica a codificação de um arquivo"""
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

def format_mascara_plano(mascara):
    """Adiciona os pontos na mascara de plano"""
    return f"{mascara[:1]}.{mascara[1:2]}.{mascara[2:3]}.{mascara[3:5]}.{mascara[5:]}" 

file_path = 'C:\\Users\\Matheus\\OneDrive\\Área de Trabalho\\plano.txt'
encoding = detect_encoding(file_path)

with open(file_path, 'r', encoding=encoding) as f:
    lines = f.readlines()

cod = [line[:7].strip() for line in lines]
mascara_plano = [line[7:18].strip() for line in lines]
descricao = [line[27:67].strip() for line in lines]
tipo = [line[67:68].strip() for line in lines]

df = pd.DataFrame({'cod': cod, 'mascara_plano': mascara_plano, 'descricao': descricao, 'tipo': tipo})
df['mascara_plano'] = df['mascara_plano'].apply(format_mascara_plano)

print(df)
df.to_excel('C:\\Users\\Matheus\\OneDrive\\Área de Trabalho\\plano.xlsx')
