access = {
    "user":"rafael.pires@sherwin.com.br",
    "senha":"84860189@Shs"
}

# XPATH:

login = {
    "email":'//*[@id="i0116"]',
    "btnAvancar":'//*[@id="idSIButton9"]',
    "senha":'//*[@id="i0118"]',
    "btnEntrar":'//*[@id="idSIButton9"]',
    "btnLigar":'//*[@id="idDiv_SAOTCS_Proofs"]/div[2]/div/div/div[2]/div'
}

home = {
    "menu":'//*[@id="anchorIcon"]', 
    "btnNovo":'//*[@id="navbar-sidebar"]/li[3]/a', 
    "btnProdutoAcabado":'//*[@id="j_idt105"]/span',
    "btnComplaint":'//*[@id="selectCategoryTypeRadio"]/tbody/tr[1]/td/div/div[2]/span',
    "btnProximo":'//*[@id="submitCatergorySelectionButton"]/span[2]'
}

loja = {
    "btnRegiao":'//*[@id="j_idt85_label"]',
    "optLatam":'//*[@id="j_idt85_3"]',
    "vendedor":'//*[@id="contactName"]',
    "telefone":'//*[@id="phoneNumber"]',
    "email":'//*[@id="email"]',
    "razao":'//*[@id="CompanyName"]',
    "brlacg":'//*[@id="CustomerNumber"]',
    "rua":'//*[@id="street1"]',
    "bairro":'//*[@id="street2"]',
    "cidade":'//*[@id="city"]',
    "estado":'//*[@id="state"]',
    "cep":'//*[@id="postalcode"]',
    "pais":'//*[@id="country"]',
    "btnNext":'//*[@id="j_idt120_content"]/div[2]/a' 
}

produto = {
    "topo":'//*[@id="j_idt305"]/div[1]',
    "btnAdicionar":'//*[@id="ComplaintLotsTable:j_idt205"]/span[2]',
    "lote":'//*[@id="newLotNumber"]', 
    "codigo":'//*[@id="newFillRx"]',
    "produto":'//*[@id="newProductDescription"]',
    "marca":'//*[@id="newBrand"]',
    "tamanho":'//*[@id="newPackageSize"]',
    "quantidade":'//*[@id="j_idt315"]',
    "grupo_de_negocio":'//*[@id="newBusinessGroup_label"]',
    "architectural":'//*[@id="newBusinessGroup_1"]',
    "unidade":'//*[@id="newUnitOfMeasure_label"]',
    "unsw":'//*[@id="newUnitOfMeasure_12"]',
    "uncg":'//*[@id="newUnitOfMeasure_6"]',
    "justificativa":'//*[@id="batchDateExplanation_label"]',
    "certeza":'//*[@id="batchDateExplanation_1"]',
    "Ilegivel":'//*[@id="batchDateExplanation_3"]',
    "btnEnviar":'//*[@id="j_idt327"]/span[2]',
    "btnNext":'//*[@id="productInfoPanel_content"]/div[3]/a[1]'
}

consumidor = {
    "responsavel":'//*[@id="contactnameenduser"]',
    "razao":'//*[@id="companyNameEndUser"]',
    "telefone":'//*[@id="phoneNumEndUser"]',
    "email":'//*[@id="emailEndUser"]',
    "rua":'//*[@id="endUserStreet1"]',
    "bairro":'//*[@id="endUserStreet2"]',
    "cidade":'//*[@id="endUserCity"]',
    "estado":'//*[@id="endUserState"]',
    "cep":'//*[@id="enduserpostalCode"]',
    "pais":'//*[@id="endusercountry"]',
    "btnSubmit":'//*[@id="SubmitNewComplaintButton"]/span[2]'
}

optTecnico = {
    "btnFacilitador":'//*[@id="lead_input"]',
    "Anoel":'//*[@id="lead_panel"]/table/tbody/tr/td',
    "Antonio":'//*[@id="lead_panel"]/table/tbody/tr/td',
    "Anderson":'//*[@id="lead_panel"]/table/tbody/tr/td',
    "Claudenir":'//*[@id="lead_panel"]/table/tbody/tr/td',
    "Ewerton":'//*[@id="lead_panel"]/table/tbody/tr/td',
    "Fabio":'//*[@id="lead_panel"]/table/tbody/tr/td',
    "Jefferson":'//*[@id="lead_panel"]/table/tbody/tr/td',
    "Ronaldo":'//*[@id="lead_panel"]/table/tbody/tr/td',
    "Sidney":'//*[@id="lead_panel"]/table/tbody/tr/td',
    "Tiago":'//*[@id="lead_panel"]/table/tbody/tr[1]/td',
}

nomeTecnico = {
    "anoel":"Anoel Junior",
    "Marcos":"Antonio Marcos Santos",
    "Anderson":"Anderson Barbosa Oliveira",
    "Claudenir":"Claudenir C De Sousa",
    "Ewerton":"Ewerton L da Silva",
    "Fabio":"Fabio Santanna",
    "Jefferson":"Jefferson Xavier",
    "Ronaldo":"Ronaldo N Moreira",
    "Sidney":"Sidney A Junior",
    "Tiago":"Tiago Antonio T Da Silveira"
}

allLevel = {
    "Nível de Problema I ":{

    },
    "Nível de Problema II":{

    },
    "Nível de Problema III":{

    }
}

niveis = {
    "nivel 1":'//*[@id="ComplaintTabs:problemL1_label"]',
    "nivel 2":'//*[@id="ComplaintTabs:problemL2_label"]',
    "nivel 3":'//*[@id="ComplaintTabs:problemL3_label"]',
    "fora":'//*[@id="ComplaintTabs:defineTab"]'
}

problema = {
    "abertura na emenda":{
        "nivel 1":'//*[@id="ComplaintTabs:problemL1_8"]',
        "nivel 2":'//*[@id="ComplaintTabs:problemL2_2"]',
        "nivel 3":'//*[@id="ComplaintTabs:problemL3_3"]'
    },
    "descacamento":{
        "nivel 1":'//*[@id="ComplaintTabs:problemL1_7"]',
        "nivel 2":'//*[@id="ComplaintTabs:problemL2_6"]',
        "nivel 3":'//*[@id="ComplaintTabs:problemL3_3"]'
    },
    "diferenaca_de_tonalidade":{
        "nivel 1":'//*[@id="ComplaintTabs:problemL1_7"]',
        "nivel 2":'//*[@id="ComplaintTabs:problemL2_1"]',
        "nivel 3":'//*[@id="ComplaintTabs:problemL3_3"]'
    },
    "defeito_valvula":{
        "nivel 1":'//*[@id="ComplaintTabs:problemL1_6"]',
        "nivel 2":'//*[@id="ComplaintTabs:problemL2_3"]',
        "nivel 3":'//*[@id="ComplaintTabs:problemL3_6"]'
    }
}

relato = {
    "relato":'//*[@id="ComplaintTabs:ProblemStatement"]'
}

chamado = {
    "numero":'//*[@id="ncIdLongForm"]'
}

btn = {
    "abrirChamado":'//*[@id="j_idt1083"]/span[2]'
}