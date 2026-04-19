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

import util


####### STUDENT NO TOUCHIE #########
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


########### WE CODE BELOW THIS LINE IN search.py ##########


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    getStartState() returns the start pair (x, y) starting position for the search problem.
    isGoalState(state) returns True if and only if the state is a valid goal state.
    getSuccessors(state) returns a list of triples, (successor, action, stepCost),
        where 'successor' is a successor to the current state, 'action' is the action required to
        get there, and 'stepCost' is the incremental cost of expanding to that successor.
    """

    start_state = problem.getStartState()
    if start_state is None or problem.isGoalState(start_state):
        return []

    unexplored = util.Stack()
    # Each stack entry stores (state, path_to_state).
    # push start state and empty path to frontier
    #     Each time an unexplored state is pushed, the path to that state is appended to the actions
    #     list. which will be returned when the goal is found.
    unexplored.push((start_state, []))
    explored = set()

    # While there is an unexplored state.
    while not unexplored.isEmpty():
        # Pop an unexplored state from the stack and the path to that state. from current state.
        state, path = unexplored.pop()

        # skip if state has already been explored
        if state in explored:
            continue

        # mark state explored
        explored.add(state)

        # If the state is a goal, return the path to that state.
        if problem.isGoalState(state):
            return path

        # For each state adjacent to current, add to stack if unexplored,
        #     and add the action to get there to the path from current state.
        # (Successor, action, stepCost)
        for successor, action, _ in problem.getSuccessors(state):
            if successor not in explored:
                unexplored.push((successor, path + [action]))

    return []  # if no solution is found, return empty list of actions


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    start_state = problem.getStartState()
    if start_state is None or problem.isGoalState(start_state):
        return []

    # BFD uses queue
    unexplored = util.Queue()
    unexplored.push((start_state, []))  # same reasoning as DFS for state stroage
    explored = set()  # same reasoning as DFS for explored set

    while not unexplored.isEmpty():
        state, path = unexplored.pop()

        if state in explored:
            continue

        explored.add(state)

        if problem.isGoalState(state):
            return path
        # (Successor, action, stepCost)
        for successor, action, _ in problem.getSuccessors(state):
            if successor not in explored:
                unexplored.push((successor, path + [action]))

    return []


# uses a priority queue to explore the lowest cost node first
def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    start_state = problem.getStartState()
    if start_state is None or problem.isGoalState(start_state):
        return []
    unexplored = util.PriorityQueue()
    unexplored.push((start_state, []), 0)  # same reasoning as others
    explored = set()  # same reasoning as others

    while not unexplored.isEmpty():
        state, path = unexplored.pop()

        if state in explored:
            continue

        explored.add(state)

        if problem.isGoalState(state):
            return path
        # (Successor, action, stepCost)
        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in explored:
                unexplored.push(
                    (successor, path + [action]),
                    problem.getCostOfActions(path + [action]),
                )

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # lowest cost means we also sum the cost to get to the current state as well as the steps
    #     to get to the goal from the current state (heuristic)
    start_state = problem.getStartState()
    if start_state is None or problem.isGoalState(start_state):
        return []

    unexplored = util.PriorityQueue()
    unexplored.push((start_state, []), 0)  # same reasoning as others
    explored = set()  # same reasoning as others

    while not unexplored.isEmpty():
        state, path = unexplored.pop()

        if state in explored:
            continue

        explored.add(state)

        if problem.isGoalState(state):
            return path
        # (Successor, action, stepCost), minQ uses stepCost
        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in explored:
                cost = problem.getCostOfActions(path + [action]) + heuristic(
                    successor, problem
                )
                unexplored.push((successor, path + [action]), cost)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
