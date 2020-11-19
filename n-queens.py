
import random

DEFINE_MAX=10000000000

def getscore(arr):#function to check score of current state
    score=0
    for k in range(N):#check left up diagonal
        i=k
        j=arr[k]
        while i-1>=0 and j-1>=0:
            i=i-1
            j=j-1
            
            if arr[i]==j:
                score=score+1
    k=0
    for k in range(N):#check left down diagonal
        i=k
        j=arr[k]
        while i+1<N and j+1<N:
            i=i+1
            j=j+1
            
            if arr[i]==j:
                score=score+1
    k=0
    for k in range(N):
        i=k
        j=arr[k]
        while i-1>=0 and j<N:#check right up diagonal
            i=i-1
            j=j+1
            if arr[i]==j:
                score=score+1
        i=k
        j=arr[k]
        while i+1<N and j-1>=0:#check right down diagonal
            i=i+1
            j=j-1
            if arr[i]==j:
                score=score+1
    return score
    
def emptygrid():
    matrix=[]
    for i in range(N):
        col=[]
        for j in range(N):
            col.append(0)
        matrix.append(col)
    return matrix
    
def generateRandom():#generate random configuration
    matrix=[]
    for i in range(N):
        col=[]
        for j in range(N):
            col.append(0)
        matrix.append(col)
    pond=[]
    i=0
    while i<N:
        x=random.randint(0,N-1)
        if x not in pond:
            pond.append(x)
            matrix[i][x]=1
            i=i+1
    
    val=getscore(pond)
    return val,matrix


def getpond(matrix):#1d representation od matrix
    pond=[]
    for i in range(N):
        for j in range(N):
            if matrix[i][j]==1:
                pond.append(j)
                break
    return pond

def isvalid(pond):#check if valid state of queens in vertical direction
    if len(set(pond))==len(pond):
        return True
    else:
        return False
    
def generatechild(matrix):
    minscore=DEFINE_MAX
    for i in range(N):
        zoop=[]#duplicate for input matrix i.e.board
        for k in range(N):
            col=[]
            for l in range(N):
                col.append(matrix[k][l])
            zoop.append(col)
        for j in range(N):
            if matrix[i][j]==1:#condition for sliding queen to left and evaluate score
                if j!=0:
                    dummy=zoop
                    dummy[i][j]=0
                    dummy[i][j-1]=1
                    pond=getpond(dummy)
                    val=getscore(pond)
                    if val<minscore:#if score is min then update
                        minscore=val
                        minpond=pond
                        mindummy=dummy
    for i in range(N):
        zoop=[]
        for k in range(N):
            col=[]
            for l in range(N):
                col.append(matrix[k][l])
            zoop.append(col)
        for j in range(N):
            if matrix[i][j]==1:#condition for sliding queen to right and evaluate score
                if j!=N-1:
                    
                    dummy=zoop
                    dummy[i][j]=0
                    dummy[i][j+1]=1
    
                    pond=getpond(dummy)
                    val=getscore(pond)
                    if val<minscore:#if score is min then update
                        minscore=val
                        minpond=pond
                        mindummy=dummy
                
    
    return mindummy,minscore#return board and score
            

#hill climb algorithm for n queens
def hillclimb_n_queen():
    board=[]
    mingoal,board=generateRandom()#generate random board configurations
    if mingoal==0:#if first state itself is goal
        return board
    while True:
        board,x=generatechild(board)#generates and returns child with the least score and board configuration
        pond=getpond(board)#array represenation of board configuration
        
        if x==0 and isvalid(pond):#if state configuration is proper and score=0
            print "Configuration found...."
            print ""
            return board
        elif x< mingoal:#if new state is better then update score and continue till score=0
            mingoal=x
            continue
        else:#else start again from random config
            
            mingoal,board=generateRandom()
            continue


#main program
def main():
    global N
    N=input("Enter The number of Queens:")
    board=hillclimb_n_queen()
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                print 'Q',
            else:
                print '-',
        print('\n')


#driver program
if __name__ == "__main__":
    main()
