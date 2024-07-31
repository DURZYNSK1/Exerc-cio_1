#FAÇA UMA LITA DE COMPRAS COM LSTAS 
#O USUARIO DEVE TER A POSSIBILIDADE DE ISERIR, APAGAR E LISTAR VALORES DE SUA LISTA

# INICIALIZANDO A LISTA

lista_compras = []

def inserir_item(item):
    lista_compras.append(item)
    
def apagar_item(item):
    if item in lista_compras:
        lista_compras.remove(item)
    else:
        print("Item não encontrado na lista")

def listar_itens():
    print("Itens na lista:")
    for item in lista_compras:
        print(item)

# LOOP INFINITO QUE PERMITE CONTINUAR A COMPRAR

while True:
    print("\nMenu:")
    print("1 - Inserir item")
    print("2 - Apagar item")
    print("3 - Listar itens")
    
    escolha = input('Escolha uma opção:')
   
    if escolha == '1':
        item = input("Digite o item:")
        inserir_item(item)
        
    elif escolha == '2':
        item = input("Digite o item para apagar:")
        apagar_item(item)
        
    elif escolha  == "3":
        listar_itens()
        break
    else:
        print("Opção inválida!")
        continue
