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
#numero de matricula

n_matricula = str(input("Ola, Bem vindo a prova, informe o numero de matricula para continuar:  "))

#numero de matricula

#alternativas da prova

perguntas = ["1 - Em linguagem de programação, uma variável é: ","2 - O que é um algoritmo?","3 - O que é um fluxograma em lógica de programação? ","4 - O que é a Lógica de programação: "]
respostas = [""] * 8
correcao = ["D","B","A","D","","","",""]
alternativas =["(A) o resultado de uma expressão aritmética.","(B) o nome dado às informações salvas no disco.","(C) um número, uma letra ou um ponto-flutuante.","(D) uma posição de memória identificada."],["(A) Contas matemáticas realizadas por computador","(B) É uma lista de instruções, finita, capaz de especificar precisamente, os passos para a resolução de uma determinada tarefa.","(C) É um conjunto de comandos ambíguos passados passados na forma de código morse.","(D) Uma lista de tarefas que o hardware precisa executar, que muitas vezes não são claras."],["(A) Uma foma de representação que utiliza ilustrações gráficas para representar as instruções.","(B) Uso de código fonte para representar algoritmos","(C) É um tipo de linguagem de programação que compila o código fonte.","(D) Uma forma de criar programas a baixo custo computacional."],["(A) É especificar uma sequência de passos ambíguos,(B) É especificar uma sequência de passos sem um ordem predefinida,(C) É especificar uma sequência de passos, para usar apenas os recursos de hardware.,(D) É especificar uma sequência de passos, utilizando uma ordem lógica de execução.,"]

for x in range(0,4):
    print(perguntas[x])
    for y in range(0,4):
        print(alternativas[x][y])
    respostas[x] = (str(input("Qual alternativa é a correta?: ")))        
    
#alternativas da prova

