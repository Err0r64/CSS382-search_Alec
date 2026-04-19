# Alec Situ - Search

The following details a brief explanation of the work done for each question.

## Q1: Finding a Fixed Food Dot using DFS

Depth first search was compelted with a stack, where for each explored state, legal and reachable states are added to the stack. This means we will keep adding states to be explored to the stack until we reach a leaf.

As we're traversing we are appending actions to each state to represent the actions that are required to reach it from the start start.

Once we have reached a leaf, that is where the implementation will start backtracking if a solution had not been found. If the goal state is reached then we return the path that is used to reach it from the start state.

## Q2: BFS

Utilizes the same implementation as DFS but we use a Queue for Breath First Search behavior. Meaning instead of searching the deepest node first it will search the successors adjacent to it. If a goal state is reached then the return behavior is the same.

## Q3: Varying the Cost Function

Utilizes the same implementation as the previous two implementation but uses a Priority Queue instead. Meaning we built the path to the goal state will the lowest costs steps each time.

Therefore in the end we return the path to the goal state from the start state containing
the cheapest cost actions.

## Q4: A* Search

Utilizes the same implementation as Q3 but adds a heuristic to the priority. Meaning the priority for each state is the cost of the path so far plus the heuristic estimate of the remaining cost to the goal.
Therefore in the end we return the cheapest path to the goal state, but expand fewer nodes than UCS since the heuristic guides the search toward the goal.

## Q5: Finding All the Corners

The state is stored as a tuple of (position, visitedCornersTuple), where visitedCornersTuple holds the corner coordinates we've already touched. In getSuccessors, whenever a successor lands on a corner we haven't visited yet, that corner gets appended to the visited tuple in the new state.
Therefore the goal state is reached when the length of the visited corners tuple is 4.

## Q6 Corners Problem: Heuristic

Uses a greedy nearest-neighbor tour over the unvisited corners, using Manhattan distance. Starting from the current position, we repeatedly hop to the closest remaining unvisited corner and sum those distances.
Therefore the heuristic stays admissible since Manhattan distance never exceeds true maze distance, and the tour is a lower bound on any path that must still reach every remaining corner.

## Q7: Eating All The Dots

Returns the maximum maze distance from Pacman's current position to any remaining food dot. Meaning Pacman has to reach the farthest dot eventually, so that distance is a valid lower bound on the remaining cost. Maze distances are cached in problem.heuristicInfo keyed by (position, food) so we don't rerun BFS on the same pair.
Therefore the heuristic is admissible and consistent, and A* expands fewer nodes than UCS on trickySearch.

## Q8: Suboptimal Search

Fills in AnyFoodSearchProblem.isGoalState to return True whenever Pacman is standing on a square that still contains food. findPathToClosestDot then just runs BFS on this problem.
Therefore we return the shortest path to the nearest food dot, since BFS expands states in order of shallowest depth first.
