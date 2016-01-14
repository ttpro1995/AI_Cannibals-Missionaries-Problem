from problem import SearchProblem
from search import*




mProblemDFS = SearchProblem()
mProblemBFS = SearchProblem()
actionDFS = depthFirstSearch(mProblemDFS)
actionBFS = breadthFirstSearch(mProblemBFS)

print 'actionBFS',actionBFS
print 'BFS expand',mProblemBFS.getNumberOfExpanded()

print 'actionDFS',actionDFS
print 'DFS expand',mProblemDFS.getNumberOfExpanded()

