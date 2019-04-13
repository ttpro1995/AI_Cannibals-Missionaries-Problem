import util
def meow():
    print ('keep calm and meow on')

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
   
    m_counter = 0
    visited = []
    v = problem.getStartState()      
    S = util.Stack()
    v = (v,'start',0)
    v = [v] # make it an array
    S.push(v)
    while (S.isEmpty()==False):
        v = S.pop()
        #print v 
        m_counter = m_counter +1
        #print m_counter
        cur_state = v[-1]
        cur_position = cur_state[0]
        #print cur_position
        if (problem.isGoalState(cur_position)):
            break 
        if (cur_position in visited):
            continue # skip node already expanded
        v_succ= problem.getSuccessors(cur_position) #expanded a node
        visited.append(cur_position)
        for edge in v_succ:
            if edge in v:
                continue # avoid loop  
            if edge in visited:
                continue # not expand state already visit
            tmp_arr = list(v)  # a tmp array clone from v
            tmp_arr.append(edge) # push edge into array
            edge = tmp_arr # new plan (the path + new edge)
            S.push(edge)    
        

            
    result = []
    del v[0] # start dummy
    for state in v:
        directon = state[1]
        result.append(directon)
    return result                     
    
    #util.raiseNotDefined()

def breadthFirstSearch(problem):#done
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    m_counter = 0
    visited = []
    v = problem.getStartState()      
    S = util.Queue()
    v = (v,'start',0)
    v = [v] # make it an array
    S.push(v)
    while (S.isEmpty()==False):
        v = S.pop()
        #print v 
        m_counter = m_counter +1
        #print m_counter
        cur_state = v[-1]
        cur_position = cur_state[0]
        #print cur_position
        if (problem.isGoalState(cur_position)):
            break         
        if cur_position in visited:
            continue # skip if node already expanded
        v_succ= problem.getSuccessors(cur_position)  # expand a node
        visited.append(cur_position) # mark already visited (expanded) node        
        for edge in v_succ: 
            tmp_arr = list(v)  # a tmp array clone from v
            tmp_arr.append(edge) # push edge into array
            edge = tmp_arr # new plan (the path + new edge)
            S.push(edge)    
            
    

    
    del v[0] # start dummy
    result = []
    for state in v:
        directon = state[1]
        result.append(directon)
    return result         

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    m_counter = 0
    visited = []
    v = problem.getStartState()      
    S = util.PriorityQueue()
    v = (v,'start',0)
    v = [v] # make it an array
    S.push(v,0)
    while (S.isEmpty()==False):
        v = S.pop()
        #print v 
        m_counter = m_counter +1
        #print m_counter
        cur_state = v[-1]
        cur_position = cur_state[0]
        #print cur_position
        if (problem.isGoalState(cur_position)):
            break         
        if cur_position in visited:
            continue # skip if node already expanded
        v_succ= problem.getSuccessors(cur_position)  # expand a node
        visited.append(cur_position) # mark already visited (expanded) node        
        for edge in v_succ: 
            new_cost = edge[2] # the cost to new node
            cur_cost = (v[-1])[2] # old cost so far, write at index 2 in last tuple of array
            sum_cost = cur_cost + new_cost
            # create new state from edge with sum cost
            new_edge = (edge[0],edge[1],sum_cost)
            tmp_arr = list(v)  # a tmp array clone from v
            tmp_arr.append(new_edge) # push edge into array
            new_edge = tmp_arr # new plan (the path + new edge)
            S.push(new_edge,sum_cost)    
            
    

    
    del v[0] # start dummy
    result = []
    for state in v:
        directon = state[1]
        result.append(directon)
    return result    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    m_counter = 0
    visited = []
    v = problem.getStartState()      
    S = util.PriorityQueue()
    v = (v,'start',0)
    v = [v] # make it an array
    S.push(v,0)
    while (S.isEmpty()==False):
        v = S.pop()
        #print v 
        m_counter = m_counter +1
        #print m_counter
        cur_state = v[-1]
        cur_position = cur_state[0]
        #print cur_position
        if (problem.isGoalState(cur_position)):
            break         
        if cur_position in visited:
            continue # skip if node already expanded
        v_succ= problem.getSuccessors(cur_position)  # expand a node
        visited.append(cur_position) # mark already visited (expanded) node        
        for edge in v_succ: 
            new_cost = edge[2] # the cost to new node
            cur_cost = (v[-1])[2] # old cost so far, write at index 2 in last tuple of array
            sum_cost = cur_cost + new_cost
            # create new state from edge with sum cost
            new_edge = (edge[0],edge[1],sum_cost)
            tmp_arr = list(v)  # a tmp array clone from v
            tmp_arr.append(new_edge) # push edge into array
            new_edge = tmp_arr # new plan (the path + new edge)
            total_cost = sum_cost + heuristic(edge[0],problem)
            S.push(new_edge,total_cost)    
            
    

    
    del v[0] # start dummy
    result = []
    for state in v:
        directon = state[1]
        result.append(directon)
    return result    