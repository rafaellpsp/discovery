from selenium import webdriver
import pandas as pd
import time
import config
import sys

# MANTER O NAVEGADOR ABERTO:
options = webdriver.ChromeOptions() 
options.add_experimental_option("detach",True) 
driver = webdriver.Chrome(options=options)
script = "document.body.style.zoom=0.8"
driver.maximize_window()
driver.get("https://discovery.sherwin.com/Discovery/")
driver.implicitly_wait(20)

#sys.exit()

# LOGIN:
driver.find_element("xpath",config.login["email"]).send_keys(config.access["user"])
driver.find_element("xpath",config.login["btnAvancar"]).click()
driver.find_element("xpath",config.login["senha"]).send_keys(config.access["senha"])
time.sleep(2)
driver.find_element("xpath",config.login["btnEntrar"]).click()
driver.implicitly_wait(20)
driver.find_element("xpath",config.login["btnLigar"]).click()
time.sleep(15)

# ESPERANDO:
verificando = 'Entrar em sua conta'
handle = 'Entrar em sua conta'

while handle == verificando:
    handle = driver.title
    time.sleep(1)
    print('Await...')
    if handle != verificando:
        print('mudou para: '+handle)
        break

resp = 'yes'

while resp == 'yes':
    resp = input('Continuar? yes or exit: ')
    caminho_arquivo = input("Caminho do arquivo: ")
    #BREAK
    if resp == 'exit':
        print("Sistema encerrado..")
        driver.quit()
        break
    else:
        time.sleep(1)
        driver.implicitly_wait(20)
        print("########################## INICIO DO CHAMADO #################")
        # HOME:
        driver.find_element("xpath",config.home["btnNovo"]).click()
        driver.find_element("xpath",config.home["btnProdutoAcabado"]).click()
        driver.find_element("xpath",config.home["btnComplaint"]).click()
        driver.find_element("xpath",config.home["btnProximo"]).click()
        driver.implicitly_wait(20)
        driver.find_element("xpath",config.loja["btnRegiao"]).click()
        driver.find_element("xpath",config.loja["optLatam"]).click()
        driver.implicitly_wait(20)
        time.sleep(5)

        
        loja = 'DADOS DA LOJA'
        df = pd.read_excel(caminho_arquivo, sheet_name=loja)
        
        problemaFilter = str(df.iat[30,1])
        plantaFilter = str(df.iat[33,1])
        marcaFilter = str(df.iat[36,1])
        sequenciaFilter = str(df.iat[39,1])
                
        print("########################## DADOS DA LOJA #####################")
        driver.find_element("xpath",config.home["menu"]).click()
        time.sleep(2)
        driver.find_element("xpath",config.loja["vendedor"]).send_keys(str(df.iat[0,1]))
        driver.find_element("xpath",config.loja["telefone"]).send_keys(str(df.iat[1,1]))
        driver.find_element("xpath",config.loja["email"]).send_keys(str(df.iat[2,1]))
        driver.find_element("xpath",config.loja["razao"]).send_keys(str(df.iat[3,1]))
        driver.find_element("xpath",config.loja["brlacg"]).send_keys(str(df.iat[11,1]))
        driver.find_element("xpath",config.loja["rua"]).send_keys(str(df.iat[5,1]))
        driver.find_element("xpath",config.loja["bairro"]).send_keys(str(df.iat[6,1]))
        driver.find_element("xpath",config.loja["cidade"]).send_keys(str(df.iat[7,1]))
        driver.find_element("xpath",config.loja["estado"]).send_keys(str(df.iat[8,1]))
        driver.find_element("xpath",config.loja["cep"]).send_keys(str(df.iat[9,1]))
        driver.find_element("xpath",config.loja["pais"]).send_keys(str(df.iat[10,1]))
        time.sleep(2)
        driver.find_element("xpath",config.loja["btnNext"]).click()                                

        print("########################## DADOS DO PRODUTO #####################")
                
        # Carregar a planilha Excel
        sheet = 'Produto_Reclamação'
        df_complaint = pd.read_excel(caminho_arquivo,sheet_name=sheet)

        # Filtrar as linhas onde o problema é "AMASSADO"
        df_filters = df_complaint[(df_complaint['Problema'] == problemaFilter) & (df_complaint['Planta'] == plantaFilter)]

        for index, row in df_filters.iterrows():
            form = driver.window_handles[0]
            driver.switch_to.window(form)
            time.sleep(2)
            
            Produto = row["Produto"]
            Codigo = str(int(row["Código"]))
            Quantidade = row["Quantidade"]
            Validade = row["Validade"]
            Tamanho = row["Tamanho"]
            Lote = row["Lote"]
            Marca = row["Marca"]
            Problema = row["Problema"]
            Planta = row["Planta"]

            driver.find_element("xpath",config.produto["btnAdicionar"]).click()
            driver.implicitly_wait(20)
            driver.find_element("xpath",config.produto["lote"]).send_keys(Lote)
            driver.find_element("xpath",config.produto["topo"]).click()
            time.sleep(1)
            driver.find_element("xpath",config.produto["codigo"]).send_keys(Codigo)
            driver.find_element("xpath",config.produto["topo"]).click()
            time.sleep(1)
            driver.find_element("xpath",config.produto["produto"]).send_keys(Produto)
            driver.find_element("xpath",config.produto["marca"]).send_keys(Produto)
            driver.find_element("xpath",config.produto["tamanho"]).send_keys(Tamanho)
            driver.find_element("xpath",config.produto["quantidade"]).send_keys(Quantidade)
            driver.find_element("xpath",config.produto["topo"]).click()
            time.sleep(1)
            driver.find_element("xpath",config.produto["grupo_de_negocio"]).click()
            driver.find_element("xpath",config.produto["architectural"]).click()
            driver.find_element("xpath",config.produto["topo"]).click()
            time.sleep(1)
            driver.find_element("xpath",config.produto["unidade"]).click()
            time.sleep(0.5)
            if plantaFilter == "TA":
                driver.find_element("xpath",config.produto["unsw"]).click()
                driver.find_element("xpath",config.produto["topo"]).click()
                time.sleep(0.5)
            elif plantaFilter == "SU":
                driver.find_element("xpath",config.produto["uncg"]).click()
                driver.find_element("xpath",config.produto["topo"]).click()
                time.sleep(0.5)
            driver.find_element("xpath",config.produto["justificativa"]).click()
            driver.find_element("xpath",config.produto["certeza"]).click()
            driver.find_element("xpath",config.produto["topo"]).click()
            time.sleep(1)
            driver.find_element("xpath",config.produto["btnEnviar"]).click()
            time.sleep(1)

            # Seu DataFrame
            data = {
                'Produto': [Produto],
                'Código': [Codigo],
                'Quantidade': [Quantidade],
                'Tamanho':[Tamanho],
                'Problema':[Problema]
            }

            df_writer = pd.DataFrame(data)
            # Iterar sobre as linhas do DataFrame e escrever blocos separados
            with open('dados_separados.txt', 'a') as file:
                file.write("DADOS DO PRODUTO: \n")
                file.write(f"Nome: {row['Produto']}\n")
                file.write(f"Idade: {row['Código']}\n")
                file.write(f"Cidade: {str(row['Quantidade'])+' - '+row['Tamanho']}\n")
                file.write(f"Problema: {row['Problema']}\n\n")
        
        driver.find_element("xpath",config.produto["btnNext"]).click()

        print("########################## DADOS DO CLIENTE ################")

        driver.implicitly_wait(20)
        driver.find_element("xpath",config.consumidor["responsavel"]).send_keys(str(df.iat[14,1]))
        driver.find_element("xpath",config.consumidor["razao"]).send_keys(str(df.iat[16,1]))
        driver.find_element("xpath",config.consumidor["telefone"]).send_keys(str(df.iat[17,1]))
        driver.find_element("xpath",config.consumidor["email"]).send_keys(str(df.iat[18,1]))
        driver.find_element("xpath",config.consumidor["rua"]).send_keys(str(df.iat[19,1]))
        driver.find_element("xpath",config.consumidor["bairro"]).send_keys(str(df.iat[20,1]))
        driver.find_element("xpath",config.consumidor["cidade"]).send_keys(str(df.iat[21,1]))
        driver.find_element("xpath",config.consumidor["estado"]).send_keys(str(df.iat[22,1]))
        driver.find_element("xpath",config.consumidor["cep"]).send_keys(str(df.iat[23,1]))
        driver.find_element("xpath",config.consumidor["pais"]).send_keys(str(df.iat[24,1]))
        time.sleep(2)
        driver.find_element("xpath",config.consumidor["btnSubmit"]).click()
        
        print("########################## RELATO DO PROBLEMA #####################")
