from collections import OrderedDict

#defining states
class State():
    def __init__(self,cl,ml,cr,mr,pos):
        self.canniballeft=cl
        self.missionaryleft=ml
        self.cannibalright=cr
        self.missionaryright=mr
        self.boat=pos
        self.parent=None

    def is_valid(self):
        
        if ((self.missionaryleft>=0 and self.missionaryright>=0) and (self.canniballeft>=0 and self.cannibalright>=0)and (self.missionaryleft>=0 and self.missionaryright>=0) and ((self.cannibalright + self.canniballeft)==3)and((self.missionaryright + self.missionaryleft)==3) and (self.missionaryleft==0 or self.missionaryleft >=self.canniballeft) and (self.missionaryright==0 or self.missionaryright >=self.cannibalright)):
            return True
        else:
            return False
    def __eq__(self,other):
        if(self.canniballeft==other.canniballeft) and (self.cannibalright==other.cannibalright) and (self.missionaryleft==other.missionaryleft) and (self.missionaryleft==other.missionaryleft) and (self.boat==other.boat):
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.canniballeft,self.missionaryleft,self.cannibalright,self.missionaryright,self.boat))
    
def is_eq(self,other):#check if 2 states are equal

    if(self.canniballeft==other.canniballeft) and (self.cannibalright==other.cannibalright) and (self.missionaryleft==other.missionaryleft) and (self.missionaryleft==other.missionaryleft) and (self.boat==other.boat):

        return True
    else:
        return False


def is_goal(explored_start,explored_goal):#function to check when the two states cross each other
    for child1 in explored_start:
        for child2 in explored_goal:
            if(child1.parent and child2.parent):
                if is_eq(child1.parent,child2.parent):
                    return child1,child2
    return False   

def successor_start(cur_state):#calculate successors
    children=[]
    if(cur_state.boat=='left'):
        new_state=State(cur_state.canniballeft-2,cur_state.missionaryleft,cur_state.cannibalright+2,cur_state.missionaryright,'right')
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.canniballeft,cur_state.missionaryleft-2,cur_state.cannibalright,cur_state.missionaryright+2,'right')
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.canniballeft-1,cur_state.missionaryleft-1,cur_state.cannibalright+1,cur_state.missionaryright+1,'right')
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.canniballeft-1,cur_state.missionaryleft,cur_state.cannibalright+1,cur_state.missionaryright,'right')
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.canniballeft,cur_state.missionaryleft-1,cur_state.cannibalright,cur_state.missionaryright+1,'right')
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
    else:
        new_state=State(cur_state.canniballeft+2,cur_state.missionaryleft,cur_state.cannibalright-2,cur_state.missionaryright,'left')
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.canniballeft,cur_state.missionaryleft+2,cur_state.cannibalright,cur_state.missionaryright-2,'left')
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.canniballeft+1,cur_state.missionaryleft+1,cur_state.cannibalright-1,cur_state.missionaryright-1,'left')
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.canniballeft+1,cur_state.missionaryleft,cur_state.cannibalright-1,cur_state.missionaryright,'left')
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.canniballeft,cur_state.missionaryleft+1,cur_state.cannibalright,cur_state.missionaryright-1,'left')
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
    return children


def print_result(a,b):#order the states and print
    c=[]
    while(len(a)!=0):
        c.append(a.pop())
    while(len(b)!=0):
        c.append(b.pop(0))
    result=list(OrderedDict.fromkeys(c))#remove duplicate states
    while(len(result)!=0):
        child=result.pop(0)
        print(child.canniballeft,child.missionaryleft,child.boat,child.cannibalright,child.missionaryright)
    
def bidirectional_search():
    start_state=State(3,3,0,0,'left')
    goal_state=State(0,0,3,3,'right')
    frontier_start=list()#frontier for state beginning from start
    explored_start=set()#explored set for state beginning from start
    frontier_goal=list()#frontier for state beginning from end
    explored_goal=set()#explored set for state beginning from end
    #append state
    frontier_start.append(start_state)
    frontier_goal.append(goal_state)
    i=0
    while(frontier_start or frontier_goal):#while both frontiers not empty
        i=i+1
        if frontier_start:#if not empty then pop
            start_state=frontier_start.pop(0)
            explored_start.add(start_state)
        if frontier_goal:#if not empty then pop
            goal_state=frontier_goal.pop(0)
            explored_goal.add(goal_state)

        #check if two states cross at any point and if cross then form the state chain with the common states as pivot    
        if(is_goal(explored_start,explored_goal)):
            
            child1,child2= is_goal(explored_start,explored_goal)
            stack1=[]
            stack2=[]
            while(child1):
                stack1.append(child1)
                child1=child1.parent
            while(child2):
                stack2.append(child2)
                child2=child2.parent
            print_result(stack1,stack2)
            print "Total iterations: ",i
            return
        
        children_start=successor_start(start_state)
        children_goal=successor_start(goal_state)
        #push all the child states of current states
        for child in children_start:
            if (child not in explored_start) or (child not in frontier_start):
                frontier_start.append(child)
                
        for child1 in children_goal:
            if (child1 not in explored_goal) or (child1 not in frontier_goal):
                frontier_goal.append(child1)



#main program starts here
print 'Missionary-Cannibals problem solution states:'
a=bidirectional_search()
