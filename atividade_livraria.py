# Modificações a serem realizadas
# 1 - Complementar as ações 4, 5 e 6
# 2 - Implementar o método recInfo em Livro, de modo similiar a Autor
# 3 - Garantir que apenas cpf únicos sejam cadastrados
# 4 - Garantir que apenas isbns únicos sejam cadastrados
# 5 - Garantir que na remoção de um autor todos os livros
#    do autor sejam removidos não houver mais nenhum autor associado ao livro
# 6 - Analisar o código em busca de trechos duplicados e movê-los para funções
#    visando o reúso de código


class Livro(object):
    isbn = None
    nome = None #titulo
    lingua = None
    ano = None
    autores = []

    def __init__(self, isbn, nome = None, lingua = None, ano = None, autores = []):
        self.isbn = isbn
        self.nome = nome
        self.lingua = lingua
        self.ano = ano
        self.autores = autores
    def exibir(self):
        print("ISBN: ",self.isbn)
        print("Nome: ",self.nome)
        print("Lingua: ",self.lingua)
        print("Ano de lançamento", self.ano)
        if len(self.autores) == 1:
            print("CPF do Autor: ",self.autores[0])
        else:
            for x in range(len(self.autores)):
                  print("CPF do autor %i :"%self.autores[x])
        
class Autor(object):
    nome = None
    cpf = None
    data_nascimento = None
    pais_nascimento = None
    nota_biografica = None
    livros = []

    def __init__(self, cpf, nome = None, data_nascimento = None, pais_nascimento = None, nota_biografica = None, livros = []):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.pais_nascimento = pais_nascimento
        self.nota_biografica = nota_biografica
        self.livros = livros

    #Se o parâmetro passado for True passa as infromações completas do usuário,
    #caso contrário apenas cpf e nome
    def recInfo(self, infocompletas = True):
        if(not(infocompletas)):
            return "("+str(self.cpf)+") - " + str(self.nome)
        else:
            retorno = "Nome: " + str(self.nome)
            retorno += "\nCPF: " + str(self.cpf)
            retorno += "\nData de nascimento: " + str(self.data_nascimento)
            retorno += "\nPaís de nascimento: " + str(self.pais_nascimento)
            retorno += "\nNota biográfica: " + str(self.nota_biografica)
            retorno += "\nLivros publicados: \n"
            

autores = []
livros = []
def apresentação():
    print("======Nova biblioteca====")
    print("1 - Cadastrar autor")
    print("2 - Exibir autor")
    print("3 - Remover autor")
    print("4 - Cadastrar livro")
    print("5 - Exibir livro")
    print("6 - Remover livro")
    print("7 - Sair")
while True:
    apresentação()
    opcao = int(input("Digite sua opção: "))
    

    if(opcao == 1):
        print("++Cadastro Autor++")
        cpf = input("CPF: ")
        for a in autores:
            if(a.cpf == cpf):
                print("Autor já cadastrado")
                break        
        else:
            nome = input("Nome: ")
            data_nascimento = input("Data nascimento: ")
            pais_nascimento = input("País de nascimento: ")
            nota_biografica = input("Nota biográfica: ")
            autor = Autor(cpf, nome, data_nascimento, pais_nascimento, nota_biografica)
            autores.append(autor)
    elif(opcao == 2):
        print("++Exibir Autor++")
        cpf = input("CPF: ")
        for autor in autores:
            if(autor.cpf == cpf):
                informacoes = autor.recInfo()
                print(informacoes)
                break
        else:
            print("Autor não encontrado!")
    elif(opcao == 3):
        print("++Remover Autor++")
        cpf = input("CPF: ")
        for autor in autores:
            if(autor.cpf == cpf):
                for livro in livros:
                    if autor.cpf in livro.autores and len(livro.autores) == 1:
                        livros.remove(livro)
                        print("fui executado")
                autores.remove(autor)
                print("Autor removido com sucesso!")
                break
        else:
            print("Autor não encontrado!")
        
    elif(opcao == 4):
        print("++Cadastrar livro++")
        isbn = input("ISBN: ")
        for l in livros:
            if(l.isbn == isbn):
                print("Livro já cadastrado")
                break
        else:
            nome = input("Título: ")
            lingua = input("Idioma: ")
            ano = input("Ano de publicação: ")
            num_autores = int(input("Informe o número de autores >> "))
            autores_livro = []
            for num in range(num_autores):
                cpf = input("Informe o cpf do autor #" + str(num))
                nao_possui = True
                for a in autores:
                    if(a.cpf == cpf):
                        autores_livro.append(a.cpf)
                        
                        nao_possui = False
                        break
                if nao_possui == True:
                    print("O autor indicado não está cadastrado! ")
                    sim_ou_não = input("deseja cadastralo? ")
                    sim_ou_não.lower()
                    if sim_ou_não == "sim":
                        print("++Cadastro Autor++")
                        cpf = input("CPF: ")      
                        
                        nome = input("Nome: ")
                        data_nascimento = input("Data nascimento: ")
                        pais_nascimento = input("País de nascimento: ")
                        nota_biografica = input("Nota biográfica: ")
                        autor = Autor(cpf, nome, data_nascimento, pais_nascimento, nota_biografica)
                        autores.append(autor)
            else:
                livro = Livro(isbn, nome, lingua, ano, autores_livro)
                livros.append(livro)
            
            
        #Complementar, solicitando que o usuário informe o CPF do usuário
    elif(opcao == 5):
        print("++exibir livro")
        isbn = input("ISBN: ")
        for x in livros:
            if(x.isbn == isbn):
                x.exibir()

    elif(opcao == 6):
        print("")
    elif(opcao == 7):
        print("Muito obrigado por ter utilizado o sistema!")
        break
    else:
        print("Opção inválida!! Tente novamente!")
    
    print("\n\n\n\n\n")    
