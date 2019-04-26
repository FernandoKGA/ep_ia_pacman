# search.py
# coding=utf-8
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

#  ---------------------- LEIA AQUI -----------------------------------
# EP DE IA - ACH2016 - 1SEM 2019
#   ALUNOS:
#   Denise Keiko Ferreira Adati - 10430962
#   Fernando Karchiloff Gouveia de Amorim - 10387644

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
#importa as funcoes de utilidade
import util
#importa a classe de Acoes
from game import Actions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def printa_lista(lista):
    for suc in lista:
      print "Valores na lista: ", suc

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    """------------------------------Inicialização de variáveis e outras estruturas-------------------------------"""
    no_inicial = problem.getStartState()
    stack = util.Stack()  #cria pilha
    stack_actions = util.Stack()  #cria pilha de acoes
    list_nodes_visitados = util.Queue() #cria fila de visitados

    """
    Algoritmo DFS

    Pegue o no inicial.
    Verifique se eh o objetivo e retorne um arranjo vazio.
    Se nao for, visite o no inicial (coloque na lista de visitados).
    Pegue os nos sucessores dele e coloque na pilha  
    Enquanto a pilha nao esta vazia:
      Pegue o sucessor da pilha
      Se ele nao estiver na lista de visitados:
        Coloca na pilha de acoes
        Se eh o objetivo:
          Retorna a pilha de acoes
        Se nao:
          Coloca na lista de visitados
          Pega seus sucessores
          Para cada sucessor:
            Se nao esta na lista de visitados:
              Coloca na pilha
      Se nao:
        Retira da pilha
        Retira da pilha de acoes
        
    """

    if problem.isGoalState(no_inicial): return [] # se o no inicial eh o objetivo
    # ja coloca o inicial como visitado
    list_nodes_visitados.push(no_inicial)
    # pega os sucessores do inicial
    nos_sucessores = problem.getSuccessors(no_inicial)
    # coloca na pilha um dos primeiros sucessores
    for suc in nos_sucessores:
      stack.push(suc)

    #enquanto a pilha tiver elementos
    while(not stack.isEmpty()):
      sucessor_stack = stack.list[len(stack.list)-1]
      
      #ve se nao esta na lista
      if sucessor_stack[0] not in list_nodes_visitados.list:
        #verifica se eh goal
        stack_actions.push(sucessor_stack[1])
        if problem.isGoalState(sucessor_stack[0]):
          return stack_actions.list
        else:
          #pega a coordenada e coloca ja como visitada do removido
          list_nodes_visitados.push(sucessor_stack[0])
          nos_sucessores = problem.getSuccessors(sucessor_stack[0])
          
          for suc in nos_sucessores:
            if suc[0] not in list_nodes_visitados.list:
              stack.push(suc)
      else:
        stack.pop()
        stack_actions.pop()
    if(stack_actions.isEmpty()): return []
    else: return stack_actions.list

def breadthFirstSearch(problem):
    """
    Lógica:
    AUXILIARES:
        fila = borda, nós que serão visitados
        visitados = fila com todos os nós visitados
        caminho = caminho que o pacman irá percorrer

        Se o nó inicial for objetivo, retorna
        coloca o nó inicial na borda
        enquanto a fila não está vazia, faça:
            tira no da borda
            se esse nó for o objetivo, retorna
            coloca nó na fila de visitados
            para cada filho do nó atual, faça:
                se o filho não está na borda ou não está explorado, faça:
                    se filho for o objetivo, retorna
                    insira o filho na borda

    LISTA DE ANTECESSORES:
         usar uma estrutura para guardar o pai de cada nó, com o intuito de fazer o caminho inverso ao achar o objetivo
    THOUGHTS:
        1.guardar os pais de cada nó
    """
    """------------------------------Inicialização de variáveis e outras estruturas-------------------------------"""
    no_inicial = problem.getStartState()                                        # no inicial
    fila = util.Queue()                                                         # fila FIFO
    visitados = []                                                              # estados visitados
    caminho = util.Stack()                                                      # caminho que o pacman terá de percorrer
    pai = []                                                                    # pai(pai,filho)
    ultimo = 0                                                                  # auxilia a fazer backtraking

    """--------------------------------------------verificação dos nós-----------------------------------------------"""
    fila.push((no_inicial, [], []))                                             # coloca primeiro nó na fila
    while not fila.isEmpty():                                                   # enquanto fila nao esta vazia, faça
        no = fila.pop()                                                         # tira nó da borda
        if not no[0] in visitados:
            visitados.append(no[0])                                             # coloca nó na fila de visitados
            """------------------------------------------achou o caminho-------------------------------------------"""
            if problem.isGoalState(no[0]):                                          # se filho for o objetivo
                ultimo = no                                                         # pega o ultimo no do caminho
                while ultimo[0] is not no_inicial:                                  # enquanto nao chega ao inicial
                    for move in pai:                                                # PAI?? se movendo pela lista de pais
                        if ultimo[0] == no_inicial: break;                          # se chegou ao fim do caminho para
                        if move == ultimo:                                          # se achou o filho
                            caminho.push(ultimo[1])                                 # coloca a acao
                            index = pai.index(ultimo) - 1                           # pega o pai do no
                            ultimo = pai[index]                                     # substitui ultimo pelo pai
                resposta = caminho.list                                             # coloca caminho como lista
                resposta.reverse()                                                  # inverte a resposta
                return resposta                                                     # retorna a resposta
            """------------------------------------------não achou o caminho---------------------------------------"""
            sucessores = problem.getSuccessors(no[0])                               # pega sucessores do nó atual
            for filho in sucessores:                                                # para cada filho de nó, faça
                    pai.append(no)                                                  # PAI?? adiciona pai a lista
                    pai.append(filho)                                               # PAI?? adiciona filho a lista
                    fila.push(filho)                                                # se não, colocar filho na borda
    return []
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    Usar problem.getCostOfActions() passando uma sequencia de acoes para ser calculado e colocado no heap, 
    armazenando somente os caminhos que chegaram na meta.
    """
    
    """------------------------------Inicialização de variáveis e outras estruturas-------------------------------"""
    no_inicial = problem.getStartState()
    fila_prioridade = util.PriorityQueue()
    nos_visitados = util.Queue()

    """
    Algoritmo:

    Insert the root into the pqueue
    While the queue is not empty
      Dequeue the maximum priority element from the queue
      (If priorities are same, alphabetically smaller path is chosen)
      If the path is ending in the goal state, print the path and exit
      Else
        Insert all the children of the dequeued element, with the cumulative costs as priority

    Pegue a raiz
    Verifique se eh o objetivo, se nao, pegue os sucessores
    (Faca um loop entre os sucessores, tentando cada um)?
    Insira os sucessores na fila de prioridade de acordo com o custo deles
    Enquanto a fila de prioridade nao eh vazia
      (Remova o elemento com a maior prioridade da fila) Pegue qual o elemento
      Verifique se eh o objetivo, se for
        Pegue o caminho de acoes na pilha atual e coloque na de acoes
        Retorne esse caminho
      Se nao
        Coloque o elemento na lista de nos visitados
        Pegue os seus sucessores
        Para cada sucessor
          Coloque na fila somente os sucessores que não foram visitados, cada um com seu custo e prioridade
        (Se nenhum sucessor foi inserido, remove da fila?!)
    

    A fila de prioridade salva os CAMINHOS INTEIROS, não cada nó visitado por ele, ou seja, assim existe
    o controle de TODOS os caminhos que serão feitos durante a busca pelo objetivo
    """

    if problem.isGoalState(no_inicial): return [] # se o no inicial eh o objetivo
    fila_prioridade.push((no_inicial,[]),0)   # cria uma lista com o no inicial, custo 0 e sem direcao

    while not fila_prioridade.isEmpty():
      lista_atual = fila_prioridade.pop()           # pegamos a lista com o menor custo
      estado_atual = lista_atual[0] # pegamos o ultimo elemento
      acoes = lista_atual[1]

      if estado_atual not in nos_visitados.list:      # verifica se este estado esta presente ou nao nos nos visitados
        nos_visitados.push(estado_atual)       # coloca na lista este estado atual caso esteja
        
        if problem.isGoalState(estado_atual):    # verifica se achou um no objetivo
          return acoes

        nos_sucessores = problem.getSuccessors(estado_atual) # pega os sucessores
        sucessores_nao_visitados = []

        for i in range(len(nos_sucessores)):                      # vasculha os sucessores
          if nos_sucessores[i][0] not in nos_visitados.list:             # pega os sucessores que nao foram visitados
            sucessores_nao_visitados.append(nos_sucessores[i])   # coloca no arranjo de sucessores nao visitados
            fila_prioridade.push(
              (nos_sucessores[i][0], acoes + [ nos_sucessores[i][1] ] ),
              nos_sucessores[i][2] + problem.getCostOfActions(acoes)
              )
        
    return [] # deu erro se chegar aqui

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """
    Pegar heuristica do nó: heuristic(no, problem)
    no[2] é custo do caminho
    """
    """--------------------------------------------Inicialiando váriaveis------------------------------------------"""
    no_inicial = problem.getStartState()                                                # no inicial
    borda = util.PriorityQueue()                                                        # borda, fila de prioridades
    visitados = []                                                                      # lista de visitados
    acoes = []                                                                          # lista de acoes

    """-----------------------------------------------------busca--------------------------------------------------"""
    borda.push((no_inicial, [], 0), 0 + heuristic(no_inicial, problem))                 # coloca o nó inicial
    while not borda.isEmpty():                                                          # se a borda tiver vazia
        no, acoes, custo = borda.pop()                                                  # tira no da borda
        if not no in visitados:                                                         # se nó não foi visitado
            visitados.append(no)                                                        # coloca nó nos visitados
            if problem.isGoalState(no):                                                 # Se achar nó objetivo
                return acoes                                                            # retorna lista de acoes
            sucessores = problem.getSuccessors(no)                                      # pegando filhos de no
            for filho in sucessores:                                                    # para cada filho de no, faca
                h = heuristic(filho[0], problem)                                        # heuristica do nó
                g = custo + filho[2]                                                    # novo custo de caminho
                borda.push((filho[0], acoes + [filho[1]], g), g + h)                    # coloca filho na borda
    return acoes
    # util.raiseNotDefined()

def learningRealTimeAStar(problem, heuristic=nullHeuristic):
    """Execute a number of trials of LRTA* and return the best plan found."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    # MAXTRIALS = ...

#metodos adicionais
def custoElemento(element):
    return element[2]  #pega o custo dele

# Abbreviations 
# *** DO NOT CHANGE THESE ***
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
lrta = learningRealTimeAStar
