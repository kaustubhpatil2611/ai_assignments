
'''
Scenario: There are four room A B C D arranged in 2*2 box in clockwise direction respectively. Here the rule is that each room gets dirty after every
5 hours the room is cleaned. Each room requires 1 hour to be cleaned.

While execution of program 1 hour corresponds to 4 seconds

Assumptions: 1) Time used for relocating the vaccum is ignored(here taken 2 seconds)
             2) If there is a tie between rooms(in terms of time to be cleaned) then randomly any one of the rooms is selected. 
'''

###########################################################################################################################
import random
import time

class Environment(object):#environment agent
    def __init__(self):
        #key represent th room and its value represents the time left for cleaning the room
        self.locationCondition={'A':0,'B':0,'C':0,'D':0}
        #initialize the hours left to clean the room randomly between 0 to 5 hours
        for items in self.locationCondition:
            self.locationCondition[items]= random.randint(0,5)        
        print "Initial condition ",self.locationCondition
        print("\n\n")
        time.sleep(3)

class stateAgent(Environment):#state agent
    def __init__(self,Environment):
        #possible perecepts and their actions
        self.percept={'AB':'Moving Right...',
              'AC':'Moving Right... Moving Left...',
              'AD':'Moving Down... ',
              'BA':'Moving Left...',
              'BC':'Moving Down...',
              'BD':'Moving Down... Moving Left...',
              'CA':'Moving Up... Moving Left...',
              'CB':'Moving Up...',
              'CD':'Moving Left...',
              'DA':'Moving Up...',
              'DB':'Moving Right... Moving Up...',
              'DC':'Moving Right...'}
    
        #check the room that needs to be cleaned first i.e. with least time left to be cleaned by finding min of the keys
        room_to_be_cleaned=min(Environment.locationCondition,key=Environment.locationCondition.get)
        
    
        while(1):
            #current status of all rooms
            print "Current room:time left in hrs to clean =",Environment.locationCondition
            time_left_to_clean=Environment.locationCondition[room_to_be_cleaned]#check the time left for the room to be cleaned
            
            if(time_left_to_clean > 0):#if time is left shut down the vacuum cleaner till the time comes
                print"Sleeping down for ",time_left_to_clean," hours as all rooms are clean."
                time.sleep(time_left_to_clean*4)
                for room in Environment.locationCondition:
                    #also update other rooms condition by subtracting the time for whichagent slept
                    Environment.locationCondition[room]=Environment.locationCondition[room]-time_left_to_clean
                #time to clean
                print"Time to clean room ",room_to_be_cleaned,"!!!..."
                print("\n")
                
            
            print"Location ",room_to_be_cleaned," is dirty"
            #clean the room
            print"Cleaning the room ",room_to_be_cleaned,"..."
            time.sleep(4)
            print"Cleaned the room ",room_to_be_cleaned," :)"#cleaning finished
            
            for room in Environment.locationCondition:
                if(room_to_be_cleaned!=room):#except the room that is cleaned
                    #Update the time left for other rooms to clean by reducing 1 hr as cleaning takes 1 hr
                    Environment.locationCondition[room]=Environment.locationCondition[room]-1
            Environment.locationCondition[room_to_be_cleaned]=5#update time as no cleaning required for next 5 hrs
            #checking next location
            next_room_to_be_cleaned=min(Environment.locationCondition,key=Environment.locationCondition.get)
            loc=room_to_be_cleaned+next_room_to_be_cleaned
            print "\n"
            print(self.percept[loc])#finding actions
            time.sleep(2)
            print "\n"
            room_to_be_cleaned=next_room_to_be_cleaned
            print "Moved to Room ",room_to_be_cleaned #taking action
            print "\n"
            time.sleep(2)#additional time sleep so that previous steps can be seen
            
    
        
#Program starts here            
print " ---------"
print "|    |    |"
print "| A  | B  |"
print "==========="
print "|    |    |"
print "| D  | C  |"
print " ---------"

print "There are in total 4 room two above A and B and below two C and D as shown in figure."
print "Once cleaned the room remains clean for next 5 hours that is it need not be cleaned till next 5 hours."
power=0
while(power!=1):
    power= input("Type 1 to start the vacuum cleaner : ")
print("Starting the Vacuum Cleaner........")
time.sleep(3)
theEnvironment = Environment()
agent=stateAgent(theEnvironment)

