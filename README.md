# PythonAIBerkeley

My solutions to some of the Berkeley Pacman Projects. At the time of writing this I am taking a course at Washington University in St. Louis that is partially following along with this course work.
Project 1: Files of interest are search.py and searchAgents.py. Certain sections of these files were filled in by me (Wherever it says "your code here". Particularly interesting sections are my implementations of BFS, DFS, UCS, and hueristic A-Star search.
NOTE: this is written in python 2, you may need to change the "python" command to "python2" if you get errors.

run DFS:
python pacman.py -l bigMaze -z .5 -p SearchAgent
run BFS:
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
run UCS:
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
run A-Star seach:
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
run A-Star with goal of visiting all corners:
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
run A-Star with goal of eating all dots:
python pacman.py -l trickySearch -p AStarFoodSearchAgent

