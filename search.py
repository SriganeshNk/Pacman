# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import math
import util
from util import Stack
from util import Queue


class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):

  "*** YOUR CODE HERE ***"
  dfsStack = Stack() # Main DFS stack
  histStack = Stack() # Stack which keeps track of path
  vis = [] # visited array
  way = [] # Ways returned to the pacman agent

  # starting state
  state = [(problem.getStartState(), 'Begin')]

  dfsStack.push(state)

  # DFS Algo
  while not dfsStack.isEmpty():
    inter_state = dfsStack.pop()

    if not histStack.isEmpty():
      way = histStack.pop()

    # check if the node is visited or not
    if problem.isGoalState(inter_state[0][0]):
      break

    if(vis.count(inter_state[0][0]) == 0):
      vis.append(inter_state[0][0])
      succ_nodes = problem.getSuccessors(inter_state[0][0])

      # Find the successor nodes
      for item in succ_nodes:
        # Get the co-ordinates and the direction to reach
        co_ord,_dir = (item[0],item[1])
        dfsStack.push([(co_ord,_dir)])
        histStack.push(way + [_dir])

  return way




def breadthFirstSearch(problem):
  "*** YOUR CODE HERE ***"
  bfsQueue = Queue() # Main DFS stack
  histQueue = Queue() # Stack which keeps track of path
  vis = [] # visited array
  way = [] # Ways returned to the pacman agent

  # starting state
  state = [(problem.getStartState(), 'Begin')]

  bfsQueue.push(state)

  # BFS Algo
  while not bfsQueue.isEmpty():
    inter_state = bfsQueue.pop()

    if not histQueue.isEmpty():
      way = histQueue.pop()

    # check if the node is visited or not
    if problem.isGoalState(inter_state[0][0]):
      break

    if(vis.count(inter_state[0][0]) == 0):
      vis.append(inter_state[0][0])
      succ_nodes = problem.getSuccessors(inter_state[0][0])

      # Find the successor nodes
      for item in succ_nodes:
        # Get the co-ordinates and the direction to reach
        co_ord,_dir = (item[0],item[1])
        bfsQueue.push([(co_ord,_dir)])
        histQueue.push(way + [_dir])

  return way


      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
