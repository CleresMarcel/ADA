'''

questão 1
Considere o seguinte trecho de código, parte do preenchimento do perfil de investidor do banco:

i = input('Você sabe o que é uma RENDA FIXA?: ')
Caso o usuário digite na caixa de texto de entrada "True", qual será o tipo de dado da variável i?

Resposta. 

Ao não especificar o tipo da variável, ela será lida como uma string, sendo assim, ela será lida como um TRUE
letra b
i = input('Você sabe o que é uma RENDA FIXA?: ')
print(type(i))

isso confirma
'''


'''
QUESTAO 2:


Você precisa implementar um código em Python que solicite ao usuário o valor principal (capital) inicial, a taxa de juros por período e o tempo em que o dinheiro é emprestado ou investido. Com base nesses valores, o programa deve calcular os juros simples e o montante total ao final do período. Assuma que temos apenas um único mês de investimento/empréstimo. Assinale a alternativa que corretamente implementa este procedimento:

a) juros = principal *= taxa
montante = principal + juros

b) juros = principal * taxa
montante = principal += juros

c) juros = principal *= taxa
montante = principal += juros

d) juros = principal + taxa
montante == principal ** juros

e) juros = principal * taxa
montante = principal + juros

Dica: O montante é calculado somando o principal ao juros e os juros são o produto do principal pela taxa.
'''
'''
principal = int(input('valor do capital inicial:'))
taxa_juros = int(input('valor da taxa de juros'))
tempo_investido = int(input('tempo investido')) #eu preciso verificar se vai ser dias, meses ou anos. isso pede uma verificação.
#calcular os juros simples e o montante final do perido.

#vai depender de como eu recebo esses valores da taxa de juros.

#Dica: O montante é calculado somando o principal ao juros e os juros são o produto do principal pela taxa.
juros_obtidos = taxa_juros*principal
montante = principal + juros

#LETRA E !!!!
'''

'''
QUESTAO 3

Na variável clientes_ano temos uma lista de listas, em que cada elemento é uma lista de dois elementos, o primeiro é o nome do cliente cadastrado na plataforma, e o segundo é o ano em que o cadastro foi realizado. Você deseja criar uma nova lista de listas (chamade de clientes_relacionamento), em que cada elemento é uma lista de dois elementos, sendo o primeiro o nome do cliente (como é na lista original), e o segundo é o número de anos em que o cliente está cadastrado na plataforma (considere que o ano atual é 2023). Qual das alternativas a seguir completa corretamente o trecho de código iniciado abaixo, para construir corretamente a lista desejada?

clientes_ano = [['Cliente A', 2018], ['Cliente B', 2021]] # Este é apenas um exemplo da lista dos anos
clientes_relacionamento = []

for lista in clientes_ano:

    # o código da alternativa correta deve vir aqui
Ao revisar este código, qual das alternativas a seguir produz o mesmo resultado?

a) clientes_relacionamento.append([lista[0], lista[1] - 2023])

b) clientes_relacionamento.append([lista[1], 2023 - lista[0]])

c) clientes_relacionamento.append([lista[1], lista[0] - 2023])

d) clientes_relacionamento.append([lista, 2023 - lista])

e) clientes_relacionamento.append([lista[0], 2023 - lista[1]])

'''

'''
#uma matriz
clientes_ano = [['Cliente A', 2018], ['Cliente B', 2021]]
clientes_relacionamento = []

print(clientes_ano[0]) #assim eu consigo ver
print(clientes_ano[1])



for lista in clientes_ano:

    #eu preciso continar a lista
    #clientes_relacionamento.append([lista[0], lista[1] - 2023])
    #print(clientes_relacionamento)
    clientes_relacionamento.append([lista[0], 2023 - lista[1]])
    print(clientes_relacionamento)

#RESPOSTA LETRA E. já informando a quantos anos a pessoa é cliente da empresa.

'''


#questão 4

'''Queremos criar uma lista para armazenar os preços dos produtos de determinado banco. Em qual das opções abaixo a variável precos_produtos não é uma lista?

a) precos_produtos = []

b) precos_produtos = list("1 2 3 4")

c) precos_produtos = (1, 1.5, 3.8)

d) precos_produtos = [1, 2, 3, 4]

e) precos_produtos = list()

'''
'''
#avaliar tipos. bom, é possível fazer a verificação de várias formas possíveis. mas bem, QUEM CONHECE A ESTRUTURA DE TUPLAS, VAI CONSEGUIR
#RESPONDER DE CARA QUE APENAS A OPÇÃO C ESTA ERRADA. MAS CASO QUEIRA UMA CONFIRMAÇÃO. É POSSÍVEL FAZER UM PRINT TYPE E VERIFICAR NA TELA
#ENTRETANTO ESSAS VERIFICAÇÕES GERALMENTE OCORREM DIRETAMENTE USANDO O TERMINAL DO SOFTWARE DE PROGRAMAÇÃO.

precos_produtos = []
print(type(precos_produtos))
precos_produtos = list("1 2 3 4")
print(type(precos_produtos))
precos_produtos = (1, 1.5, 3.8)
print(type(precos_produtos))
precos_produtos = [1, 2, 3, 4]
print(type(precos_produtos))
precos_produtos = list()
print(type(precos_produtos))

#RESPOSTA LETRA C !!

'''
'''

Em um banco, existe um sistema de alerta na central de suporte que é ativado quando o número de chamados supera 500. Enquanto o volume de chamados permanecer acima desse limite, o sistema exibe uma mensagem indicando quantos chamados ainda precisam ser resolvidos para que o número volte a ficar adequado. Para implementar esta lógica, você começou criando o seguinte código:

num_chamados = 780

while (num_chamados > 500):

    print(f'ALERTA! HÁ UM TOTAL DE {num_chamados}')

    print('Você atendeu um chamado!')

    print(f"Faltam {num_chamados - 500} para o nível estar dentro do aceitável!")

    # código da alternativa correta aqui

print("\nNão estamos mais em estado de alerta!")
Assinale a alternativa que implementa corretamente a lógica desejada, substituindo o comentário no código acima:

a) num_chamados += 1

b) num_chamados = 100 - num_chamados

c) num_chamados -= 1

d) num_chamados = 100 + num_chamados

e) num_chamados += 100
'''

'''


# 500 É UM VALOR LIMITE. #ele vai fazer contagem de quantos faltam
#de forma a tornar a questão mais visual podemos trocar o numero de chamados.
#UMA VEZ QUE É POSSÍVEL VISUALIZAR O QUE PRECISA ACONTECER, FICA BEM CLARO QUE A RESPOSTA C É A RESPOSTA QUE LOGO VEM A CABEÇA..
#feito isso, podemos voltar o num_chamados para seu valor antigo, de forma a preservar a questão.
num_chamados = 503

while (num_chamados > 500):

    print(f'ALERTA! HÁ UM TOTAL DE {num_chamados}')

    print('Você atendeu um chamado!')

    print(f"Faltam {num_chamados - 500} para o nível estar dentro do aceitável!")
    num_chamados = num_chamados -1


    # código da alternativa correta aqui

print("\nNão estamos mais em estado de alerta!")

#RESPOSTA LETRA C !!!

'''



'''
QUESTÃO 6 

Imagine que você está desenvolvendo um aplicativo para planejamento de viagens rodoviárias. 
Uma das funcionalidades desse aplicativo é ajudar os usuários a estimar o tempo que levarão para chegar a seus destinos. 
Para tornar o aplicativo mais interativo e educativo, você decide incluir uma seção onde os usuários podem calcular a distância de uma viagem baseando-se na velocidade média esperada do veículo e no tempo de viagem. Faça um código em Python que calcule a distância em km entre duas cidades, completando o template de código a seguir, no qual o tempo em minutos deve ser informado pelo usuário:



#estimar tempo de chegada.
#calcular distancia usando a velocidade media e o tempo de viagem EM KM
#usuario informa minutos, então não vai ter 3.5 minutos. intuitivamente teremos int.

velocidade = 25 # esta em m/s ESSA PRECISA SER A VELOCIDADE MEDIA.

velocidade_convertida = 25*3.6  # código para colocar a velocidade na unidade adequada

tempo = int(input('Informe o tempo de viagem em minutos:')) # código para receber como input do usuário o tempo em minutos
tempo_convertido = tempo/60 #eu preciso converter esse tmepo para horas, já que eu estou trabalhando com km/hora na distancia.
distancia = velocidade*tempo_convertido # código que implementa a lógica da distância em km

print(f"\nA distância entre os dois locais é {distancia} km!")

'''


#questão 7 # ACABEI NÃO TERMINANDO ESSA QUESTÃO !!!!!


'''
Em um banco, é importante que tenhamos um registro de todos os clientes, sejam correntistas ou não, para que seja possível, por exemplo, realizar a comunicação com eles enviando ofertas de produtos.

Para começar a prototipar esta funcionalidade, você deve criar um programa em Python que leia diversos números inteiros e insira todos em uma lista (esses números são os identificadores dos clientes). A cada solicitação de número, pergunte ao usuário se deseja inserir outro número: tendo como resposta 'S' para inserir mais um; ou 'N' caso queira terminar. É possível que o mesmo número seja digitado mais de uma vez (isso pode representar o mesmo cliente fazendo mais de um pedido). Após construir a lista, mostre:

a) todos os números digitados na ordem em que foram inseridos

b) todos os números digitados em ordem crescente

c) a média destes valores

d) apenas os números pares

e) apenas os números ímpares

f) apenas os números repetidos

Obs.: O usuário obrigatoriamente digitará as letras S e N, contudo não necessariamente de forma padronizada.
'''


'''
#inserir varios inteiros e colocar eles em uma lista.
#a cada inserção. preciso informar se ele quer inserir outro
list=[]
inserir = int(input('Digite um numero a se inserir')).upper()
list.append(inserir)
while inserir != N:
    
    lista = int(input('Numero de itens da lista:'))

#informar na ordem de digitação
print(list)

#informar os numeros na ordem crescente 
 
#media dos valores da lista
media = sum(list)/(len(list))

#informar os pares da lista

#informar os inpares da lista

#informar os numeros repetidos da lista    


'''







'''
Questão 8:
Escreva um código em Python que recebe um número (que possa ter casas decimais) e a escala de temperatura em que este valor se encontra e para qual ele deseja converter (Celsius, Kelvin ou Fahrenheit). Tanto na escala em que se encontra quanto para a que deseja converter, utilize as letras iniciais como entrada: Celsius - 'C', Kelvin - 'K' ou Fahrenheit - 'F'.

Seu código deve solicitar ao usuário as informações necessárias para realizar a conversão de temperatura (temperatura, escala_original, escala_convertida), de acordo com o template abaixo.
Implemente abaixo toda a lógica de conversão de temperaturas, bem como as validações necessárias.

Importante: o programa deve trabalhar apenas com as 3 escalas supracitadas! Então, não deixe de fazer as validações necessárias. Além disso, por definição, não existem temperaturas em Kelvin abaixo de zero (o valor zero pode existir), portanto verifique também esta condição para que sejam feitas conversões válidas!

Dica: as equações de conversão entre as escalas são as seguintes:

Celsius <> Fahrenheit: \color{white}{\frac{C}{5} = \frac{F - 32}{9}}

Celsius <> Kelvin:  \color{white}{C = K - 273}

Kelvin <> Fahrenheit:  \color{white}{\frac{K - 273}{5} = \frac{F - 32}{9}}

'''


#realizar conversao de tabelas..

temperatura = float(input('informe sua temperatura: '))
escala_original = input('informe sua escala original: ').upper()
escala_convertida = input('informe sua escala a se converter: ').upper()

if(escala_original == 'K' and temperatura < 0):
    print('não existe temperatura negativa em kelvin')
elif(escala_original == 'K' and escala_convertida == 'F'):
    temperatura_convertida = (temperatura-273)*9/5 + 32
    print('a temperatura convertida sera:', temperatura_convertida)
elif(escala_original == 'K' and escala_convertida == 'C'):
    temperatura_convertida = temperatura-273
    print('a temperatura convertida sera:', temperatura_convertida)
if(escala_original == 'C' and escala_convertida == 'K'):
    temperatura_convertida = temperatura + 273
    print('a temperatura convertida sera:', temperatura_convertida)
if(escala_original == 'C' and escala_convertida == 'F'):
    temperatura_convertida = (temperatura*9/5) + 32
    print('a temperatura convertida sera:', temperatura_convertida)
if(escala_original == 'F' and escala_convertida == 'C'):
    temperatura_convertida = (temperatura-32)*(5/9)
    print('a temperatura convertida sera:', temperatura_convertida)
if(escala_original == 'F' and escala_convertida == 'K'):
    temperatura_convertida = (5/9)*(temperatura-32)+273
    print('a temperatura convertida sera:', temperatura_convertida)


'''

QUESTAO 9:

Um grande banco deseja saber quais são seus produtos mais vendidos. Em uma lista, são registrados os nomes dos produtos, na ordem em que eles são vendidos (portanto, há elementos repetidos nesta lista). Faça um programa que exibe na tela cada um dos produtos na lista de input, e a quantidade em que eles foram vendidos (separados por um traço), de modo que teremos uma mensagem em cada linha. Os produtos devem ser exibidos em ordem alfabética.

Ex.: para a lista produtos = ["Crediário", "Consórcio", "Consórcio", "Financiamento", "Consórcio", "Crediário"]

Obs: Existem outros produtos além dos da lista acima, seu código deve contemplar outras possibilidades.

Devemos ter as seguintes mensagens exibidas na tela:
Consórcio - 3  
Crediário - 2  
Financiamento - 1


#produtos mais vendidos.
#fazer uma lista na ordem que são vendidos
#existem elementos repetidos na lista
#exibir na tela cada um dos produtos da lista e a quantidade que foram vendidos
#eu preciso separar os produtos que são repetidos. !!!!

lista_produtos = ["Crediário", "Consórcio", "Consórcio", "Financiamento", "Consórcio", "Crediário"]
produtos_repetidos = []
for i in range(len(lista_produtos)):
    produto = lista_produtos[i]

    if produto not in produtos_repetidos:
        contagem = 1

        for j in range(i + 1, len(lista_produtos)):
            if produto == lista_produtos[j]:
                contagem += 1

        # Imprimir o produto e a contagem
        print(f"{produto} - {contagem}")

        # Adicionar o produto à lista de produtos contados
        produtos_repetidos.append(produto)
'''





#questao 10
'''
Um banco está analisando o desempenho de um investimento ao longo de um mês. Eles têm uma lista de valores de fechamento diários deste investimento e querem calcular uma média móvel de 7 dias para entender melhor as tendências no curto prazo. A média móvel de 7 dias é uma forma comum de suavizar flutuações diárias, dando ao banco uma visão mais clara das tendências de desempenho do investimento.

Seu objetivo é desenvolver um código em Python que processe a lista de valores fornecida. O código deve calcular e retornar uma nova lista contendo a média móvel de 7 dias para cada período possível dentro dos dados fornecidos.

Dica: A média móvel em um determinado dia é calculada como a média dos valores de fechamento dos 7 dias anteriores, incluindo o dia atual.


valores_dos_fechamentos = [
    156.89, 155.16, 148.41, 145.18, 150.23, 148.10, 155.68,
    146.07, 149.53, 151.67, 158.16, 150.09, 145.64, 155.12,
    152.37, 145.01, 158.19, 159.66, 156.20, 158.04, 146.20,
    154.60, 157.98, 153.68, 149.44, 142.01, 148.68, 152.22,
    158.26, 159.33
]
'''



#calcular media movel de 7 dias.
#suavizar flutuações.

#processar os valores.
#gerar uma nova lista. com a media movel de 7 dias para cada periodo dentro dos dados.
#Dica: A média móvel em um determinado dia é calculada como a média dos valores de fechamento dos 7 dias anteriores, incluindo o dia atual.

'''

# Imprime os resultados
for dia, media in enumerate(media_movel_7_dias, start=7):
    print(f"Média Móvel de 7 dias no dia {dia}: {media:.2f}")
'''

# como calcular uma media movel de 7 dias?
# média móvel de 7 dias para 30 valores
# selecione um ponto de partida
# para cada ponto a partir desse ponto de partida, some os valores dos próximos 7 dias.
# divida a soma por 7 para obter a média.
# deslocar um dia e repetir o processo.



'''

valores_dos_fechamentos = [
    156.89, 155.16, 148.41, 145.18, 150.23, 148.10, 155.68,
    146.07, 149.53, 151.67, 158.16, 150.09, 145.64, 155.12,
    152.37, 145.01, 158.19, 159.66, 156.20, 158.04, 146.20,
    154.60, 157.98, 153.68, 149.44, 142.01, 148.68, 152.22,
    158.26, 159.33
]

print(len(valores_dos_fechamentos))
media_movel_7_dias = []
dia = 7
while dia <= len(valores_dos_fechamentos):
    media = sum(valores_dos_fechamentos[dia-7:dia]) / 7
    media_movel_7_dias.append(media)
    dia += 1

# Imprime os resultados
dia = 7
for media in media_movel_7_dias:
    print(f"Média Móvel de 7 dias no dia {dia}: {media:.2f}")
    dia += 1
'''
