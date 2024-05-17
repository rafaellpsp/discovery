from selenium import webdriver
import time
import config
import json

# VERIFICANDO SESSÃO:

# MANTER O NAVEGADOR ABERTO:
options = webdriver.ChromeOptions() 
options.add_experimental_option("detach",True) 
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://discovery.sherwin.com/Discovery/")
driver.implicitly_wait(20)

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

# HOME:
driver.implicitly_wait(20)
driver.find_element("xpath",config.home["btnNovo"]).click()
driver.find_element("xpath",config.home["btnProdutoAcabado"]).click()
driver.find_element("xpath",config.home["btnComplaint"]).click()
driver.find_element("xpath",config.home["btnProximo"]).click()
driver.implicitly_wait(20)
driver.find_element("xpath",config.loja["btnRegiao"]).click()
driver.find_element("xpath",config.loja["optLatam"]).click()

## TESTE VOLTA
while True:
    # Código que você deseja repetir

    # Perguntar ao usuário se ele deseja continuar
    resposta = input("Deseja dar mais uma volta? (s/n): ")

    # Verificar a resposta do usuário
    if resposta.lower() != 's':
        break  # Sair do loop se a resposta não for 's'

# Código a ser executado após o loop
print("Fim do programa")

# LOJA:
time.sleep(1)
with open("chamados.json","r", encoding="utf-8") as json_file:
    # Carregar os dados do arquivo JSON
    dados = json.load(json_file)
    driver.find_element("xpath",config.home["menu"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.loja["vendedor"]).send_keys(dados["DADOS DA LOJA"]["Vendedor"])
    driver.find_element("xpath",config.loja["telefone"]).send_keys(dados["DADOS DA LOJA"]["Telefone 1"])
    driver.find_element("xpath",config.loja["email"]).send_keys(dados["DADOS DA LOJA"]["Email"])
    driver.find_element("xpath",config.loja["loja"]).send_keys(dados["DADOS DA LOJA"]["Loja"])
    driver.find_element("xpath",config.loja["brlacg"]).send_keys(dados["DADOS DA LOJA"]["Brlacg"])
    driver.find_element("xpath",config.loja["rua"]).send_keys(dados["DADOS DA LOJA"]["Endereco completo"])
    driver.find_element("xpath",config.loja["bairro"]).send_keys(dados["DADOS DA LOJA"]["Bairro"])
    driver.find_element("xpath",config.loja["cidade"]).send_keys(dados["DADOS DA LOJA"]["Cidade"])
    driver.find_element("xpath",config.loja["estado"]).send_keys(dados["DADOS DA LOJA"]["Estado"])
    driver.find_element("xpath",config.loja["cep"]).send_keys(dados["DADOS DA LOJA"]["Cep"])
    driver.find_element("xpath",config.loja["pais"]).send_keys(dados["DADOS DA LOJA"]["Pais"])
    driver.find_element("xpath",config.loja["btnNext"]).click()

driver.implicitly_wait(20)
time.sleep(1)
for k, v in dados["DADOS DO PRODUTO"].items():
    driver.find_element("xpath", config.produto["btnAdicionar"]).click()
    codigo = v["Codigo"]
    lote = v["LOTE"]
    produto = v["Nproduto"]
    marca = v["Nproduto"]
    tamanho = v["Tamanho"]
    quantidade = v["Quantidade"]
    
    driver.implicitly_wait(20)
    driver.find_element("xpath",config.produto["lote"]).send_keys(lote)
    driver.find_element("xpath",config.produto["topo"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.produto["codigo"]).send_keys(codigo)
    driver.find_element("xpath",config.produto["topo"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.produto["produto"]).send_keys(produto)
    driver.find_element("xpath",config.produto["marca"]).send_keys(marca)
    driver.find_element("xpath",config.produto["tamanho"]).send_keys(tamanho)
    driver.find_element("xpath",config.produto["quantidade"]).send_keys(quantidade)
    driver.find_element("xpath",config.produto["topo"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.produto["grupo_de_negocio"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.produto["architectural"]).click()
    driver.find_element("xpath",config.produto["topo"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.produto["unidade"]).click()
    driver.find_element("xpath",config.produto["un"]).click()
    driver.find_element("xpath",config.produto["topo"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.produto["justificativa"]).click()
    driver.find_element("xpath",config.produto["certeza"]).click()
    driver.find_element("xpath",config.produto["topo"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.produto["btnEnviar"]).click()
    time.sleep(2)

driver.find_element("xpath", config.produto["btnNext"]).click()

# CONSUMIDOR:
driver.implicitly_wait(20)
driver.find_element("xpath",config.consumidor["responsavel"]).send_keys(dados["DADOS_DA_OBRA_CONSUMIDOR_FINAL"]["Nome"])
driver.find_element("xpath",config.consumidor["empresa"]).send_keys(dados["DADOS_DA_OBRA_CONSUMIDOR_FINAL"]["Razao Social"])
driver.find_element("xpath",config.consumidor["telefone"]).send_keys(dados["DADOS_DA_OBRA_CONSUMIDOR_FINAL"]["Telefone 1"])
driver.find_element("xpath",config.consumidor["email"]).send_keys(dados["DADOS_DA_OBRA_CONSUMIDOR_FINAL"]["Email"])
driver.find_element("xpath",config.consumidor["rua"]).send_keys(dados["DADOS_DA_OBRA_CONSUMIDOR_FINAL"]["Endereco completo"])
driver.find_element("xpath",config.consumidor["bairro"]).send_keys(dados["DADOS_DA_OBRA_CONSUMIDOR_FINAL"]["Bairro"])
driver.find_element("xpath",config.consumidor["cidade"]).send_keys(dados["DADOS_DA_OBRA_CONSUMIDOR_FINAL"]["Cidade"])
driver.find_element("xpath",config.consumidor["estado"]).send_keys(dados["DADOS_DA_OBRA_CONSUMIDOR_FINAL"]["Estado"])
driver.find_element("xpath",config.consumidor["cep"]).send_keys(dados["DADOS_DA_OBRA_CONSUMIDOR_FINAL"]["CEP"])
driver.find_element("xpath",config.consumidor["pais"]).send_keys(dados["DADOS_DA_OBRA_CONSUMIDOR_FINAL"]["Pais"])
driver.find_element("xpath",config.consumidor["btnSubmit"]).click()
time.sleep(5)

# TECNICO:
driver.find_element("xpath",config.tecnico["btnFacilitador"]).click()

if dados["TECNICO"] == 'Anoel':
    driver.find_element("xpath",config.tecnico["Anoel Junior"]).click()
elif dados["TECNICO"] == 'Antonio':
    driver.find_element("xpath",config.tecnico["Antonio Marcos Santos"]).click()
elif dados["TECNICO"] == 'Anderson':
    driver.find_element("xpath",config.tecnico["Anderson Barbosa Oliveira"]).click()
elif dados["TECNICO"] == 'Claudenir':
    driver.find_element("xpath",config.tecnico["Definir"]).click() #Definir
elif dados["TECNICO"] == 'Ewerton':
    driver.find_element("xpath",config.tecnico["Anoel Junior"]).send_keys(config.nomeTecnico["ewerton"])
    time.sleep(2)
    driver.find_element("xpath",config.tecnico["Ewerton L da Silva"]).click()
elif dados["TECNICO"] == 'Fabio':
    driver.find_element("xpath",config.tecnico["Fabio C Santanna"]).click() #Confirmar nome no discovery
elif dados["TECNICO"] == 'Jefferson':
    driver.find_element("xpath",config.tecnico["Jefferson Xavier"]).click()
elif dados["TECNICO"] == 'Ronaldo':
    driver.find_element("xpath",config.tecnico["Ronaldo N Moreira"]).click()
elif dados["TECNICO"] == 'Sidney':
    driver.find_element("xpath",config.tecnico["Sidney A Junior"]).click()
elif dados["TECNICO"] == 'Tiago':
    driver.find_element("xpath",config.tecnico["Tiago Antonio T Da Silveira"]).click()
else:
    driver.quit()
    print('Não encontrou o técnico')

if dados["PROBLEMA"] == 'Abertura na emenda':
    driver.find_element("xpath",config.niveis["nivel 1"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.problema["nivel 1"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.niveis["nivel 2"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.problema["nivel 2"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.niveis["nivel 3"]).click()
    time.sleep(2)
    driver.find_element("xpath",config.problema["nivel 3"]).click()
    time.sleep(2)


driver.find_element("xpath",config.relato["relato"]).send_keys(dados["RELATO DO PROBLEMA"])