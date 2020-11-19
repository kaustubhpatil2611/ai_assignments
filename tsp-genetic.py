import random

DEFINE_MAX=10000000000


class individual():#class for individuals representing the complete path
    def __init__(self):
        self.path=""#path
        self.fitness=DEFINE_MAX#fitness score

def mutate_path(path):#mutate path by altering any random 2 cities
    while True:
        v=random.randint(1,N-1)
        v1=random.randint(1,N-1)
        if(v1!=v):
            strlst=list(path)
            temp=strlst[v]
            strlst[v]=strlst[v1]
            strlst[v1]=temp
            path="".join(strlst)
            break
    return path

def create_path():#create path
    path="0"
    while True:
        if(len(path)==N):#close path by initial city
            path=path+"0"
            break
        v=random.randint(1,N-1)
        
        if(str(v) not in path):
            path=path+str(v)
    return path
            
def fitness_score(path,distance):#calculate fitness score
    score=0
    for i in range(len(path)-1):
        score=score+distance[int(path[i])][int(path[i+1])]
    return score

def get_me_key(obj):
    return obj.fitness

def tsp(distance):#function to execute best path for travelling salesmen problem
    population=[]
    
    for i in range(10):#create population of 10 paths
        temp=individual()
        temp.path=create_path()
        temp.fitness=fitness_score(temp.path,distance)
        population.append(temp)
    population.sort(key=get_me_key)#sort by fitness score
    print "Path::Cost"
    for i in range(10):
        print population[i].path,population[i].fitness
    
    while True:
        for i in range(6):
            population.pop()#consider only top 4 paths
        
        for i in range(2):#mutate 2 new paths from top paths of population
            temp=individual()
            new_path=mutate_path(population[0].path)
            temp.path=new_path
            temp.fitness=fitness_score(temp.path,distance)
            population.append(temp)
        for i in range(1,5):#mutate 4 new paths from next top 4 paths of population
            temp=individual()
            new_path=mutate_path(population[i].path)
            temp.path=new_path
            temp.fitness=fitness_score(temp.path,distance)
            population.append(temp)
            
        print('\n')
        population.sort(key=get_me_key)
        print "Path::Cost"
        for i in range(10):
            print population[i].path,population[i].fitness
        
        check=population[0].fitness
        counter=0
        for i in range(10):#if the top path is in majority in population return path
            if check==population[i].fitness:
                counter=counter+1
                if counter==4:
                    print "Final Solution: "
                    print "Path::Cost"
                    print population[i].path,population[i].fitness
                    return
                    
    
        
#main program
def main():
    global N
    N=input("Enter the number of cities: ")

    distance = []
    for i in range(0,N):#input distance graph
        col=[]
        for j in range(0,N):
            print "Enter the distance from city ",i," to city ",j," :",
            x=input("")
            col.append(x)
        distance.append(col)
    print "Distance graph"
    for i in range(0,N):
        for j in range(0,N):
            print distance[i][j],
        print "\n"
    tsp(distance)
    

#driver program
if __name__ == "__main__":
    main()
