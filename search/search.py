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
    
    # inicializacao de variaveis
    no_inicial = problem.getStartState()

    # inicializacao de estruturas
    stack = util.Stack()  #cria objeto
    stack_actions = util.Stack()
    list_nodes_visitados = util.Queue()

    """
    Algoritmo DFS

    Pegue o no inicial.
    Verifique se eh o objetivo e retorne um arranjo vazio.
    Se nao for, visite o no inicial (coloque na lista de visitados).
    Pegue os nos sucessores dele e guarde.
    Para cada sucessor que ele tem
      Coloque um na pilha de caminho.
      Enquanto a pilha nao esta vazia
        Pegue o ultimo elemento a entrar na pilha.
        Verifique se nao eh o objetivo, se for
          Coloque todos os passos feitos na pilha de acoes.
        Se não
          Coloque o ultimo elemento na lista de visitados.
          Pegue os sucessores desse ultimo.
          Para cada sucessor deste ultimo
            Verifique se nao esta na lista de visitados
              Coloque na pilha.
          Se todos estao na lista
            Remove esse elemento da pilha.
      Se a pilha esta vazia, esvazie a lista de acoes e de nos visitados.
      Coloque o no inicial novamente para garantir que ele nao seja visitado.
    """

    if problem.isGoalState(no_inicial): return [] # se o no inicial eh o objetivo
    # ja coloca o inicial como visitado
    list_nodes_visitados.push(no_inicial)
    # pega os sucessores do inicial
    nos_sucessores = problem.getSuccessors(no_inicial)
    # coloca na pilha os primeiros sucessores
    """
    Fara o teste para cada sucessor do inicial que ele tiver,
    se nao encontrar caminho, repete o processo para o proximo sucessor
    """ 
    for sucessor in nos_sucessores:
      stack.push(sucessor)
      #enquanto a pilha tiver elementos
      while(not stack.isEmpty()):
        sucessor_stack = stack.list[len(stack.list)-1]
        #verifica se eh goal
        if problem.isGoalState(sucessor_stack[0]):
          for move in stack.list:
            stack_actions.push(move[1])
          return stack_actions.list
        else:
          #pega a coordenada e coloca ja como visitada do removido
          list_nodes_visitados.push(sucessor_stack[0])
          nos_sucessores = problem.getSuccessors(sucessor_stack[0])
          
          suc_count = 0
          for suc in nos_sucessores:
            if suc[0] not in list_nodes_visitados.list:
              stack.push(suc)
              suc_count += 1
              """
              impede que coloque mais de um no na stack, assim ele permite continuar
              expandindo um no por vez
              """
              break
          #se nao tiver nenhum sucessor daquele no
          if suc_count == 0:
            #tira da pilha
            stack.pop()

      #se nao encontrou caminho entao limpa as listas
      del stack_actions.list[:]
      del list_nodes_visitados.list[:]
      list_nodes_visitados.push(no_inicial[0])

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

    PILHA DE ANTECESSORES:
         usar uma estrutura para guardar o pai de cada nó, com o intuito de fazer o caminho inverso ao achar o objetivo
    THOUGHTS:
        1.guardar os pais de cada nó
        2.guardar todos os caminhos percorridos
    """
    """------------------------------Inicialização de variáveis e outras estruturas-------------------------------"""
    no_inicial = problem.getStartState()                                        # no inicial
    fila = util.Queue()                                                         # fila FIFO
    visitados = util.Queue()                                                    # estados visitados
    caminho = util.Stack()                                                      # caminho que o pacman terá de percorrer
    aux = util.Stack()
    # pai = util.Stack()                                                          # pilha de nós e seus antecessores

    """----------------------------------------verificação só do nó incial----------------------------------------"""
    if problem.isGoalState(no_inicial): return []                               # verifica se o inicio eh o objetivo
    aux.push(no_inicial)
    sucessores_incial = problem.getSuccessors(no_inicial)                       # pega os sucessores no nó inicial
    i = 0                                                                       # indice para pegar os sucessores certos
    for filho in sucessores_incial:                                             # para cada filho de nó, faça
        if filho[i] not in visitados.list and filho[i] not in fila.list:        # se filho não está na borda ou nos visitados
            if problem.isGoalState(filho): return caminho.list                  # se filho for o objetivo, retorna caminho
            aux.push(filho)
            fila.push(aux)                                                      # se não, colocar filho na borda
            aux.pop()
        i = i + 1                                                               # incremento do indice

    """----------------------------------------verificação dos outros nós----------------------------------------"""
    while not fila.isEmpty():                                                   # enquanto fila nao esta vazia, faça
        # no = fila.pop()                                                         # tira nó da borda
        aux = fila.pop()
        no = aux.pop()
        sucessores = problem.getSuccessors(no[0])                               # pega sucessores do nó atual
        print ("ele pegou", no[1])
        # caminho.push(no[1])                                                     # guarda caminho
        print ("Saiu da borda: ", no)
        if problem.isGoalState(no[0]): break;                                   # verifica se nó é o objetivo
        visitados.push(no[0])                                                   # se não, coloca nó na fila de visitados
        i = 0                                                                   # indice p/ pegar os sucessores certos
        for filho in sucessores:                                                # para cada filho de nó, faça
            if filho[i] not in visitados.list and filho[i] not in fila.list:    # se filho não está na borda ou nos visitados
                if problem.isGoalState(filho):                                  # se filho for o objetivo, retorna caminho
                    return caminho.list

                fila.push(filho)                                                # se não, colocar filho na borda
            i = i + 1                                                           # incremento do indice
    """-------------------------------------------montagem do caminho-------------------------------------------"""

    return caminho.list                                                         # retorna caminho


    # if suc[0] not in list_nodes_visitados.list:
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
    
    # inicializacao de variaveis
    no_inicial = problem.getStartState()

    # inicializacao de estruturas
    fila_prioridade = util.PriorityQueue()
    nos_visitados = []

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
    """

    if problem.isGoalState(no_inicial): return [] # se o no inicial eh o objetivo
    # ja coloca o inicial como visitado
    nos_visitados.append(no_inicial[0])
    
    """
    A fila de prioridade salva os CAMINHOS INTEIROS, não cada nó visitado por ele, ou seja, assim existe
    o controle de TODOS os caminhos que serão feitos durante a busca pelo objetivo
    """

    fila_prioridade.push([[no_inicial,None,0]],0)   # cria uma lista com o no inicial, custo 0 e sem direcao

    while not fila_prioridade.isEmpty():
      lista_atual = fila_prioridade.pop()           # pegamos a lista com o menor custo
      estado_atual = lista_atual[len(lista_atual)-1] # pegamos o ultimo elemento

      if estado_atual[0] not in nos_visitados:      # verifica se este estado esta presente ou nao nos nos visitados
        nos_visitados.append(estado_atual[0])       # coloca na lista este estado atual caso esteja

        if problem.isGoalState(estado_atual[0]):    # verifica se achou um no objetivo
          resposta = []                             # cria um vetor de resposta
          for i in range(len(lista_atual)-1):       # passa pelo caminho para pegar os nos de caminho
            estado_inserir = lista_atual[i+1]       # pega o estado atual dado pelo indice
            resposta.append(estado_inserir[1])      # coloca dentro do vetor de resposta
          return resposta

        nos_sucessores = problem.getSuccessors(estado_atual[0]) # pega os sucessores
        sucessores_nao_visitados = []

        for i in range(len(nos_sucessores)):                      # vasculha os sucessores
          if nos_sucessores[i][0] not in nos_visitados:             # pega os sucessores que nao foram visitados
            sucessores_nao_visitados.append(nos_sucessores[i])   # coloca no arranjo de sucessores nao visitados
        """
        Aqui eh feito o calculo para calcular o CUSTO DO NOVO CAMINHO para colocar na fila de prioridade do novo
        CAMINHO que eh uma lista
        """
        custo_caminho = 0

        for i in range(len(lista_atual)):            # calcula o custo total para este caminho
          custo_caminho = custo_caminho + i

        for estado_vizinho in sucessores_nao_visitados: # para cada vizinho nao visitado cria uma nova lista
          lista_temporaria = [] + lista_atual        # cria uma lista temporaria para adicionar novo sucessor
          lista_temporaria.append(estado_vizinho)    # adiciona esse novo sucessor
          custo_lista_temporaria = custo_caminho + estado_vizinho[2] # coloca o novo custo desse caminho
          fila_prioridade.push(lista_temporaria,custo_lista_temporaria) # coloca na fila de prioridade do caminho

    return [] # deu erro se chegar aqui

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


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
