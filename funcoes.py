import time
import os
import globais

# Funções
def exibir_menu():

  animar("Aguarde")

  print("=== Loja Python ===\n")

  print("1 - Registar produto.")
  print("2 - Editar produto.")
  print("3 - Apagar produto.")
  print("4 - Lista produtos.\n")

  print("5 - Vender.")
  print("6 - Lista de vendas.")

  print("\n0 - Sair.\n")
  return int(input("- Opção: "))

def registar():

  print("--- Registar Produto ---\n")
  
  nome = input("- Digite o nome do novo produto: ")
  
  if nome == "" or any(c.isdigit() for c in nome):
    print("\n--- OPERAÇÃO INVÁLIDA! (O nome não pode estar em BRANCO ou conter NÚMEROS!)")
    return

  try:

    preco = float(input("- Digite o preço deste produto: "))
    
    if preco <= 0 :
      print("\n--- OPERAÇÃO INVÁLIDA! (O preço do produto tem que ser maior de 0!) ---")
      return
    
    quantidade = int(input("- Digite a quantidade deste produto: "))

    if quantidade < 0:
      print("\n--- OPERAÇÃO INVÁLIDA! (Tem que inserir uma quantidade positiva!) ---")
      return

    novo_produto = [nome, preco, quantidade]
    globais.produtos.append(novo_produto)
    print("\n--- SUCESSO! ---")
  
  except ValueError:
        print("\n--- OPERAÇÃO INVÁLIDA! (Preço ou quantidade com valor INVÁLIDO!) ---")

def editar(): 

  print("--- Editar Produto ---\n")

  lista(False)

  id = int(input("\n - Digite o ID do produto que quer editar: ")) - 1

  if(id >= 0 and id < len(globais.produtos)):
    c = globais.produtos[id]
    print(f"\n#{id+1} - (Nome: {c[0]}) (Preço: {c[1]} €)  (Quantidade: {c[2]})")

    print("\n--- Menu de Edição ----\n")
    print("1 - Nome.")
    print("2 - Preço.")
    print("3 - Quantidade.")

    print("\n0 - Cancelar\n")

    opcao = int(input("- Opção: "))
  

    print()

    if(opcao == 0): 

      print("\n--- OPERAÇÃO CANCELADA! ---")

      return

    elif(opcao == 1): 
      
      novo_nome = input(f"- Digite o nome para substituir ({c[0]}): ")

      if novo_nome == "" or any(c.isdigit() for c in novo_nome):
        print("\n--- OPERAÇÃO INVÁLIDA! (O nome não pode estar em BRANCO ou conter NÚMEROS!)")
        return
      
      else:
        globais.produtos[id][0] = novo_nome
        print("\n--- SUCESSO ---")

    
    elif(opcao == 2): 

      novo_preco = input(f"- Digite o preço para substituir ({c[1]} €): ")

      if novo_preco.replace('.','', 2).isdigit():

        preco = float(novo_preco)

        if preco > 0:
          globais.produtos[id][1] = preco
          print("\n--- SUCESSO ---")

      else: 
        print("\n--- OPERAÇÃO INVÁLIDA! (O preço do produto NÃO pode conter letras ou números negativos) ---")

    elif(opcao == 3): 

      nova_quantidade = input(f"- Digite a quantidade substituir ({c[2]}): ")

      if nova_quantidade.replace('.','', 2).isdigit():

        quantidade = int(nova_quantidade)

        if quantidade >= 0:
          globais.produtos[id][2] = quantidade
          print("\n--- SUCESSO ---")

      else:
        print("\n--- OPERAÇÃO INVÁLIDA! (O preço do produto NÃO pode conter letras ou números negativos) ---")

  else: 
    print("\n--- ID INVÁLIDO ---")

def apagar():

  print("--- Apagar produto ---\n")

  lista(False)

  id_produto = input("\n- Digite o ID do produto que quer apagar: ")

  if id_produto.isdigit():
    id = int(id_produto) - 1

    if(id >= 0 and id < len(globais.produtos)):

        c = globais.produtos[id]
      
        resposta = input(f"\n- Tem certeza de que deseja apagar este produto ({c[0]}) (sim/nao)? ")

        if(resposta.lower() == "sim"):
          print(f"\n--- ({c[0]}) APAGADO COM SUCESSO ---")
          globais.produtos.pop(id)

        else: 
          print("\n --- OPERAÇÃO CANCELADA COM SUCESSO ---")
    else: 
      print("\n --- OPERACAÇÃO INVÁLIDA! ---")
  else:
    print("\n--- OPERAÇÃO INVÁLIDA! (Tem que inserir apenas NÚMEROS e POSITIVOS!)")

def lista(com_titulo):

  if (com_titulo): 
    print("--- Lista de produtos ---\n")

  for i in range(len(globais.produtos)):

    c = globais.produtos[i]

    print(f"#{i+1} - (Nome: {c[0]}) (Preço: {c[1]} €) (Quantidade: {c[2]}).")
    
def vender():
  
  print("--- Vender Produto ---\n")

  lista(False)

  id_produto1 = input("\n- Digite o ID do produto que quer vender: ")

  if id_produto1.isdigit():
    id = int(id_produto1) - 1
  
    if(id >= 0 and id < len(globais.produtos)):

      c = globais.produtos[id]

      quantidade = int(input(f"\n- Digite a quantidade de ({c[0]}) que será vendida: "))

      if (quantidade > 0 and quantidade <= c[2]):
        
        c[2] -= quantidade

        total = c[1] * quantidade

        id_venda = len(globais.vendas)

        print(f"\nVenda #{id_venda+1} - ({c[0]}) ({c[1]} €) x ({quantidade} uni.) = ({round(total, 2)} €)")

        print(f"\n--- SUCESSO! ---")

        globais.vendas.append([c[0], c[1], quantidade])

        if c[2] == 0:
          globais.produtos.pop(id)
      
      else:
        print("\n--- OPERAÇÃO INVÁLIDA! ---")

    else: 
      print("\n --- OPERCAÇÃO INVÁLIDA! ---")

  else:
    print("\n--- OPERAÇÃO INVÁLIDA! (Tem que inserir apenas NÚMEROS e POSITIVOS!)")

def lista_de_vendas():

  total_vendas = 0

  print("--- Lista de Vendas ---\n")

  for i in range(len(globais.vendas)):
    
    v = globais.vendas[i]

    valor_tvendas = v[1] * v[2]

    total_vendas += valor_tvendas

    print(f"Vendas #{i+1} - (Nome: {v[0]}) ({v[1]} €) x ({v[2]} uni.) = ({round(valor_tvendas, 2)} €)")

  print(f"\nTotal de Vendas: ({round(total_vendas, 2)} €)")



# Funções Especiais
def limpa():
  if(os.name == "nt"): os.system("cls")
  else: os.system("clear")

def aguarde(segundos): time.sleep(segundos)

def prima_enter(): input("\nPrima <ENTER> para continuar...")

def animar(frase):
  tempo = 0.2
  limpa()
  print(frase, end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  limpa()