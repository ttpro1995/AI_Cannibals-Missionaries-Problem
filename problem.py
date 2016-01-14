class SearchProblem:
    def __init__(self):
        self.start = (3, 3, 1) # (3C, 3M, 1) 
        self._expanded = 0 # Number of search nodes expanded

    def validate(self, state):
        leftC = state[0]
        leftM = state[1]
        rightC = 3 - leftC
        rightM = 3 - leftM
        
        if (leftC < 0 or leftM < 0 or rightC < 0 or rightM < 0):
            return False # when the number become negative
        
        if (leftC > leftM and leftM > 0):
            return False # Cannibal outnumber Missionary on left side
        
        if (rightC > rightM and rightM >0):
            return False # Cannibal outnumber Missionary on right side
        return True

    def getStartState(self):
        
        """
        Returns the start state for the search problem.
        """
        return self.start

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        leftC = state[0]
        leftM = state[1]
        if (leftC==0):
            if (leftM == 0):
                return True
        return False

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        successors = []
        cost = 1
        for action in [(1,0),(2,0),(0,1),(0,2),(1,1)]:
            if (state[2] == 1):# boat in left, we row to right
                newState0 = state[0]-action[0]
                newState1 = state[1]-action[1] 
                nextState = (newState0,newState1 , 0)
                if (self.validate(nextState)):
                    successors.append(( nextState, action, cost))
            if (state[2]==0):# boat in right, we row to left
                newState0 = state[0]+action[0]
                newState1 = state[1]+action[1] 
                nextState = (newState0,newState1, 1)
                if (self.validate(nextState)):
                    successors.append(( nextState, action, cost)) 
        self._expanded += 1 # Number of search nodes expanded   
        return successors
        
    def getNumberOfExpanded(self):
        return self._expanded 
        
    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()