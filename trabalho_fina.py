import os
'''
Correção de prova: Faça um programa para corrigir provas de múltipla escolha. Cada prova tem oito
questões e cada questão vale um ponto. O primeiro conjunto de dados a ser lido é o gabarito da prova. Os
outros dados são os números de matrícula dos alunos e as respostas que deram às questões. Existem 10
alunos matriculados.
O algoritmo deve permitir mostrar:
    a- O número e a nota de cada aluno;
    b- A percentagem de aprovação, sabendo-se que a nota mínima é 6;
    c- Pesquisar a nota de um determinado aluno.
'''

# declaracao de variaveis

nulo = [""]*8
n_matricula = [0] * 10
perguntas = []
alternativas =[]
respostas = [nulo]*10
correcao = ["D","B","A","D","A","B","C","D"]
nota = [0]*10
pesquisar_matricula = (0)

# declaracao de variaveis

#função de limpar

def clear():
    if os.name == 'posix':
        os.system('clear')

    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')  

#função de limpar

#função de matricula

def pesquisar_nota ():
    pesquisar_matricula = int(input("informe a matricula do aluno"))
    for x in range(0,len(n_matricula)):
        if pesquisar_matricula == n_matricula[x]  :
            print("a nota do aluno matricula {} é {}".format(n_matricula[x],nota[x]))

#função de matricula

#parte feia


perguntas.append("1 - Em linguagem de programação, uma variável é: \n")
perguntas.append("2 - O que é um algoritmo? \n")
perguntas.append("3 - O que é um fluxograma em lógica de programação? \n")
perguntas.append("4 - O que é a Lógica de programação: \n")
perguntas.append("5 - Os passos de um algoritmos devem ser \n")
perguntas.append("6 - Dentre as diversas formas de representação de algoritmos tem-se a Descrição Narrativa, que é uma especificação verbal dos passos em linguagem natural. Quais são as duas desvantagens da descrição narrativa: \n")
perguntas.append("7 - A proposição funcional Para todo e qualquer valor de n, tem-se 6n < n² + 8 será verdadeira, se n for um número real \n")
perguntas.append("8 - Uma duplicata no valor de R$ 6 900,00 foi resgatada 3 meses antes de seu vencimento. Considerando que a taxa anual de desconto comercial simples foi de 48%, então, se o valor atual dessa duplicata era X reais, é correto afirmar que \n")

alternativas.append(["(A) o resultado de uma expressão aritmética.1","(B) o nome dado às informações salvas no disco.","(C) um número, uma letra ou um ponto-flutuante.","(D) uma posição de memória identificada. \n"])
alternativas.append(["(A) Contas matemáticas realizadas por computador","(B) É uma lista de instruções, finita, capaz de especificar precisamente, os passos para a resolução de uma determinada tarefa.","(C) É um conjunto de comandos ambíguos passados passados na forma de código morse.","(D) Uma lista de tarefas que o hardware precisa executar, que muitas vezes não são claras. \n"])
alternativas.append(["(A) Uma foma de representação que utiliza ilustrações gráficas para representar as instruções.","(B) Uso de código fonte para representar algoritmos","(C) É um tipo de linguagem de programação que compila o código fonte.","(D) Uma forma de criar programas a baixo custo computacional. \n"])
alternativas.append(["(A) É especificar uma sequência de passos ambíguos","(B) É especificar uma sequência de passos sem um ordem predefinida","(C) É especificar uma sequência de passos, para usar apenas os recursos de hardware.","(D) É especificar uma sequência de passos, utilizando uma ordem lógica de execução. \n"])
alternativas.append(["(A) Claros precisos e sem ambiguidade.","(B) Claros imprecisos e sem ambiguidade.","(C) Claros eficaz e pode ter ambiguidade","(D) Claros preciso e eficaz \n"])
alternativas.append(["(A) Possibilita comentar algoritmos e é imprecisa.","(B) Proporciona maior trabalho de codificação e pode gerar amnésia computacional.","(C) É imprecisa e proporciona maior trabalho na codificação.","(D) Utiliza muito processamento e consumo de memória. \n"])
alternativas.append(["(A) menor que 8","(B) menor que 4","(C) menor que 2","(D) maior que 2 \n"])
alternativas.append(["(A) X 5 700","(B) 5 700 < X 5 800","(C) 5 800 < X 5 900","(D) X > 6 000 \n"])
#parte feia


#alternativas da prova
for z in range(0,10):
    clear()
    n_matricula[z] = int(input("Ola, Bem vindo a prova, informe o numero de matricula para continuar: "))
    clear()
    for x in range(0,8):
        print(perguntas[x])
        for y in range(0,4):
            print(alternativas[x][y])
        respostas[z][x] = (str(input("Sua Resposta: "))) 
        clear()        

#alternativas da prova

#correcao das provas

for b in range(0,10):
    for a in range(0,8):
        if respostas[b][a] == correcao[a]:
           nota[b] += 1.25
           

#correcao das provas
for j in range(0,10):
    if nota[j] >= 6:
        print ("Matricula: {}, nota: {},APROVADO com {}% De Aprovação \n".format(n_matricula[j],nota[j],(nota[j]*10)))
    else:
        print ("Matricula: {}, nota: {},REPROVADO com {}% De Reprovção \n".format(n_matricula[j],nota[j],(nota[j]*10)))  
    
if str(input("Deseja saber o resultado de algum alundo? S/N")) == "S" :
    clear()
    pesquisar_nota()

        
    
    