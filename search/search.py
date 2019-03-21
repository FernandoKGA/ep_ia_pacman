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
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    #inicializacao de variaveis
    no_inicial = problem.getStartState()

    #inicializacao de estruturas
    stack = util.Stack()  #cria objeto
    fila_prioridade = util.PriorityQueue()
    stack_actions = util.Stack()
    list_nodes = util.Queue()

    #inicializacao de classe utilitaria
    acoes = Actions()

    if problem.isGoalState(no_inicial): #se o no inicial eh o objetivo
      return []
    else:
      #ja coloca o inicial como visitado
      list_nodes.push(no_inicial)
      #pega os sucessores do inicial
      nos_sucessores = problem.getSuccessors(no_inicial)
      counter_suc = 0
      #coloca na pilha os primeiros sucessores
      for sucessor in nos_sucessores:
        #stack.push(sucessor)
        fila_prioridade.push(sucessor,counter_suc)
        print sucessor
        counter_suc += 1
    
    #enquanto a pilha tiver elementos
    #while(not stack.isEmpty()):
    while(not fila_prioridade.isEmpty()):
      #sucessor_stack = stack.pop()
      sucessor_stack = fila_prioridade.pop()
      print "Removido da fila priori ", sucessor_stack
      #verifica se eh goal
      if problem.isGoalState(sucessor_stack[0]):
        #verificar se o retorno eh correto, se precisa alterar para Queue
        stack_actions.push(sucessor_stack[1])
        for action in stack_actions.list:
          print action
        return stack_actions.list
      else:
        #pega a parte de acao do removido
        stack_actions.push(sucessor_stack[1])
        #pega a coordenada e coloca ja como visitada do removido
        list_nodes.push(sucessor_stack[0])
        print sucessor_stack
        nos_sucessores = problem.getSuccessors(sucessor_stack[0])
        suc_count = 0
        for suc in nos_sucessores:
          if suc[0] not in list_nodes.list:
            print "Sucessor de ",sucessor_stack[0],": ", suc
            #stack.push(suc)
            fila_prioridade.push(suc,suc_count)
            print "Colocando novo sucessor na pilha: ", suc[1]
            suc_count += 1
        #se nao tiver nenhum sucessor daquele no
        if suc_count == 0:
          #retira da pilha de acoes
          removido = stack_actions.pop()
          print "Removido da pilha pois nao tem: ", removido
          #coloca a posicao reversa
          stack_actions.push(acoes.reverseDirection(removido[1]))
    """
    enquanto houverem sucessores que possa expandir e entrar, coloque na pilha
    se nao houver sucessor para ir, volte
    """
    
    #verificar se o retorno eh correto, se precisa alterar para Queue
    return stack_actions.list
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
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
