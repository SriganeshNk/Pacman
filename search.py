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
from util import Stack
from util import Queue
from util import PriorityQueue

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

def genericsearch(state, problem, fringe, history, method, heuristic=nullHeuristic):
  visited = list()
  way = list()

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
  return genericsearch(problem.getStartState(), problem, Stack(), Stack(), "dfs");

def breadthFirstSearch(problem):
  return genericsearch(problem.getStartState(), problem, Queue(), Queue(), "bfs");
      
def uniformCostSearch(problem):
  return genericsearch(problem.getStartState(), problem, PriorityQueue(), list(), "other");

def aStarSearch(problem, heuristic=nullHeuristic):
  return genericsearch(problem.getStartState(), problem, PriorityQueue(), list(), "other", heuristic);
    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
