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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    startNode = (problem.getStartState(), [])
    checked = []
    notChecked = util.Stack()
    notChecked.push(startNode)
    while True:
        
        currentNode, path =notChecked.pop()
        # last in first out = depth first
        if currentNode not in checked: 
        #    dont recheck nodes we already visited

            checked.append(currentNode)
        
        
            if (problem.isGoalState(currentNode)): 
                # print len(path)           
                return path
        
            succs = problem.getSuccessors(currentNode)
           
            for node in succs:
               
                notChecked.push((node[0],path + [node[1]]))


    

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    startNode = (problem.getStartState(), [])
    checked = []
    notChecked = util.Queue()
    notChecked.push(startNode)
    while True and not notChecked.isEmpty():
        
        currentNode, path =notChecked.pop()
        # last in first out = depth first
        
        if currentNode not in checked: 
        #    dont recheck nodes we already visited

            checked.append(currentNode)
        
        
            if (problem.isGoalState(currentNode)): 
                # print len(path)           
                return path
        
            succs = problem.getSuccessors(currentNode)

            for node in succs:
               
                notChecked.push((node[0],path + [node[1]]))
    # print "never converged"
    

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    startNode = (problem.getStartState(), [],0)
    checked = []
    notChecked = util.PriorityQueue()
    notChecked.push(startNode,0)
    while True and not notChecked.isEmpty():
        
        currentNode, path,cost =notChecked.pop()
       
        # just use priority queue here - pops low priorities first so just use cost
        if currentNode not in checked: 
        #    dont recheck nodes we already visited

            checked.append(currentNode)
        
        
            if (problem.isGoalState(currentNode)): 
                # print len(path)           
                return path
        
            succs = problem.getSuccessors(currentNode)
           
            for node in succs:
                #  pushing 2 args as (coordinates, path), cost
                notChecked.push((node[0],path + [node[1]],cost+node[2]),cost+node[2])
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    unExplored = util.PriorityQueue()
    explored = []
    starting = (problem.getStartState(),[],0)

    unExplored.push(starting,0)

    while not unExplored.isEmpty():
        currentState, currentPath, currentCost = unExplored.pop()
        
        explored.append((currentState,currentCost))

        if problem.isGoalState(currentState):
            # print currentPath
            return currentPath
        
        successors = problem.getSuccessors(currentState)
        for successor in successors:
            newState = successor[0]
            newAction = successor[1]
            newPath = currentPath + [newAction]
            newCost = problem.getCostOfActions(newPath)
            # print explored, "explored"
            dontExpand = False
            for item in explored:
                if item[0] == newState and item[1] <=newCost:
                    dontExpand = True
            

            if not dontExpand:
                unExplored.push((newState,newPath,newCost), newCost + heuristic(newState,problem))
                explored.append((newState,newCost))

    return currentPath

    



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
