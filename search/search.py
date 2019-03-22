# search.py
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

    return stack_actions.list

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    Usar problem.getCostOfActions() passando uma sequencia de acoes para ser calculado e colocado no heap, 
    armazenando somente os caminhos que chegaram na meta.
    """
    
    # inicializacao de variaveis
    no_inicial = problem.getStartState()

    # inicializacao de estruturas
    stack = util.Stack()  
    stack_actions = util.Stack()
    list_nodes_visitados = util.Queue()

    """
    Usar as estruturas de Fila de Prioridade e Counter (tabela de hash).
    Como usar o Counter? A Pilha ainda deve ser utilizada?
    """

    util.raiseNotDefined()


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
    

# Abbreviations 
# *** DO NOT CHANGE THESE ***
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
lrta = learningRealTimeAStar
