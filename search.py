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

import util

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


def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def genericsearch(state, problem, fringe, method, heuristic=nullHeuristic):
  from util import Stack
  from util import Queue
  from util import PriorityQueue
  visited = list()
  way = list()
  history = list()

  if method=="bfs":
    history = Queue()
  if method=="dfs":
    history = Stack()

  if method=="other":
  	fringe.push((state,way),problem.getCostOfActions(way))
  else:
    fringe.push(state)

  while not fringe.isEmpty():
    if method =="other":
      nextstate,directions = fringe.pop()
      if problem.isGoalState(nextstate):
         return directions
    else:
      nextstate = fringe.pop()
      if not history.isEmpty():
        way=history.pop()
      if problem.isGoalState(nextstate):
        return way
    
    if nextstate not in visited:
      visited.append(nextstate)
      successor = problem.getSuccessors(nextstate)
      print "currentstate:", nextstate
      for each in successor:
        print each
        if method == "other":
          fringe.push((each[0],directions+[each[1]]), problem.getCostOfActions(directions+[each[1]])+heuristic(each[0],problem))
        else:
          fringe.push(each[0])
          history.push(way+[each[1]])

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  from util import Stack
  start = problem.getStartState();
  fringe = Stack()
  method="dfs"
  way = genericsearch(start, problem, fringe, method);
  return way
  #util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  from util import Queue
  start = problem.getStartState();
  fringe = Queue()
  method="bfs"
  way = genericsearch(start, problem, fringe, method);
  return way
  #util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  from util import PriorityQueue
  start = problem.getStartState();
  fringe= PriorityQueue()
  method= "other"
  way = genericsearch(start, problem, fringe, method);
  return way
  #util.raiseNotDefined()


def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  from util import PriorityQueue
  start = problem.getStartState();
  fringe= PriorityQueue()
  method= "other"
  way = genericsearch(start, problem, fringe, method, heuristic);
  return way
  """util.raiseNotDefined()"""
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
