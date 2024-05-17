import time
import pandas as pd

def consulta():
    caminho_arquivo = "./formulario.xlsm"
    loja = 'DADOS DA LOJA'
    df = pd.read_excel(caminho_arquivo, sheet_name=loja)
    # DADOS DA LOJA:
    print("DADOS DA LOJA: ")
    print(str(df.iat[0,0]) + ": " + str(df.iat[0,1]))
    print(str(df.iat[1,0]) + ": " + str(df.iat[1,1]))
    print(str(df.iat[2,0]) + ": " + str(df.iat[2,1]))
    print(str(df.iat[3,0]) + ": " + str(df.iat[3,1]))
    print(str(df.iat[4,0]) + ": " + str(df.iat[4,1]))
    print(str(df.iat[5,0]) + ": " + str(df.iat[5,1]))
    print(str(df.iat[6,0]) + ": " + str(df.iat[6,1]))
    print(str(df.iat[7,0]) + ": " + str(df.iat[7,1]))
    print(str(df.iat[8,0]) + ": " + str(df.iat[8,1]))
    print(str(df.iat[9,0]) + ": " + str(df.iat[9,1]))
    print(str(df.iat[10,0]) + ": " + str(df.iat[10,1])+"\n")

    # DADOS DO CLIENTE:
    print("DADOS DO CLIENTE: ")
    print(str(df.iat[14,0]) + ": " + str(df.iat[14,1]))
    print(str(df.iat[15,0]) + ": " + str(df.iat[15,1]))
    print(str(df.iat[16,0]) + ": " + str(df.iat[16,1]))
    print(str(df.iat[17,0]) + ": " + str(df.iat[17,1]))
    print(str(df.iat[18,0]) + ": " + str(df.iat[18,1]))
    print(str(df.iat[19,0]) + ": " + str(df.iat[19,1]))
    print(str(df.iat[20,0]) + ": " + str(df.iat[20,1]))
    print(str(df.iat[21,0]) + ": " + str(df.iat[21,1]))
    print(str(df.iat[22,0]) + ": " + str(df.iat[22,1]))
    print(str(df.iat[23,0]) + ": " + str(df.iat[23,1]))
    print(str(df.iat[24,0]) + ": " + str(df.iat[24,1])+"\n")

    # TECNICO:
    print(str(df.iat[27,0]) + ": " + str(df.iat[27,1])+"\n")

    # PRBLEMA:
    print(str(df.iat[30,0]) + ": " + str(df.iat[30,1])+"\n")

    # PLANTA:
    print(str(df.iat[33,0]) + ": " + str(df.iat[33,1])+"\n")
    # MARCA:
    print(str(df.iat[36,0]) + ": " + str(df.iat[36,1])+"\n")
    # SEQUENCIA:
    print(str(df.iat[39,0]) + ": " + str(df.iat[39,1])+"\n")
consulta()

def tabela():
    caminho_arquivo = "./formulario.xlsm"
    loja = 'Produto_Reclamação'
    df = pd.read_excel(caminho_arquivo, sheet_name=loja)
    df_filters = df[(df['Problema'] == "VAZAMENTO") & (df['Planta'] == "SU")]

    #print(df_filters)

    print("DADOS DO PRODUTO:\n")
    
    for index, row in df_filters.iterrows():
        Produto = row["Produto"]
        Codigo = str(int(row["Código"]))
        Quantidade = row["Quantidade"]
        Validade = row["Validade"]
        Tamanho = row["Tamanho"]
        Lote = row["Lote"]
        Marca = row["Marca"]
        Problema = row["Problema"]
        Planta = row["Planta"]

        print("Produto: "+Produto)
        print("Código: "+Codigo)
        print("Quantidade: "+str(Quantidade)+" - "+Tamanho)
        print("Lote: "+Lote)
        print("Problema: "+Problema+"\n")

        # Seu DataFrame
        data = {
            'Produto': [Produto],
            'Código': [Codigo],
            'Quantidade': [Quantidade],
            'Tamanho':[Tamanho],
            'Problema':[Problema]
        }

        df = pd.DataFrame(data)
        # Iterar sobre as linhas do DataFrame e escrever blocos separados
        with open('dados_separados.txt', 'a') as file:
            file.write("DADOS DO PRODUTO: \n")
            for index, row in df.iterrows():
                file.write(f"Nome: {row['Produto']}\n")
                file.write(f"Idade: {row['Código']}\n")
                file.write(f"Cidade: {str(row['Quantidade'])+' - '+row['Tamanho']}\n")
                file.write(f"Problema: {row['Problema']}\n\n")
#tabela()