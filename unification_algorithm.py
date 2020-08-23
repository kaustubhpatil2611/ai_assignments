def functor(x):
    fun=""
    i=0
    while(i<len(x)):
        if(x[i]=='('):
            return fun
        fun=fun+x[i]
        i=i+1
    fun=''
    return fun 

def classify(s1):
    stack1=[]
    i=0
    while(i<len(s1) and s1[i]!='('):
        i=i+1
    i=i+1
    if(i==len(s1)+1):
        i=0
    str1=""
    while(i<len(s1)):
        if s1[i]=='(':
            count=1
            str1=str1+s1[i] 
            while(count>0):
                i=i+1
                if s1[i]=='(':
                    count=count+1
                if s1[i]==')':
                    count=count-1
                str1=str1+s1[i]
        elif s1[i]==',' or s1[i]==')':
            stack1.append(str1)
            str1=""
        else:
            str1=str1+s1[i]
            if i==len(s1)-1:
                stack1.append(str1)
        i=i+1
    return stack1
    
def check(s):
    if (s[0].isupper()):
        return "variable"
    else:
        i=0
        while(i<len(s)):
            if(s[i]=='('):
                return "function"
            i=i+1
        return "constant"

def substitute(s1,s2,stack1,stack2):
    for j in range(len(stack1)):
        for i in range(len(stack1[j])):
            if stack1[j][i] == s1:
                stack1[j]=stack1[j][0:i]+s2+stack1[j][i+1:]
    for j in range(len(stack2)):
        for i in range(len(stack2[j])):
            if stack2[j][i] == s1:
                stack2[j]=stack2[j][0:i]+s2+stack2[j][i+1:]
    return stack1,stack2

def substitute1(subs,stack1,stack2):
    for item,value in subs.items():     
        for j in range(len(stack1)):
            for i in range(len(stack1[j])):
                if stack1[j][i] == item:
                    stack1[j]=stack1[j][0:i]+value+stack1[j][i+1:]
        for j in range(len(stack2)):
            for i in range(len(stack2[j])):
                if stack2[j][i] == item:
                    stack2[j]=stack2[j][0:i]+value+stack2[j][i+1:]
    return stack1,stack2

def unify(s1,s2,subs):
    stack1=classify(s1)
    stack2=classify(s2)
    if(len(stack1)!=len(stack2)):
        stack1=[]
        stack2=[]
        subs.clear()
        return subs,stack1,stack2
    for i in range(len(stack1)):
        q1=stack1[i]
        q2=stack2[i]
        t1=check(stack1[i])
        t2=check(stack2[i])
        if(q1==q2):
            continue
        elif(t1=="variable"):
            subs[q1]=q2
            stack1,stack2=substitute(q1,q2,stack1,stack2)
        elif(t2=="variable"):
            subs[q2]=q1
            stack1,stack2=substitute(q2,q1,stack2,stack1)
        elif(t1=="function" or t2=="function"):
            subs,tack1,tack2=unify(q1,q2,subs)
            if(bool(subs)==False and bool(tack1)==False and bool(tack2)==False):
                return subs,tack1,tack2
            stack1,stack2=substitute1(subs,stack1,stack2)
        else:
            stack1=[]
            stack2=[]
            subs.clear()
            return subs,stack1,stack2
    return subs,stack1,stack2
            
    
s1="p(b,X,f(g(Z)))" #"X,*,1,=,3"raw_input("Enter the string: ")
s2="p(Z,f(Y),f(Y))" #"Z,*,1,=,Z"raw_input("Enter the string: ")
func=functor(s1)
subs={}
subs,stack1,stack2=unify(s1,s2,subs)

if(bool(subs)==False and bool(stack1)==False and bool(stack2)==False):
    print("Not unify.")
else:
    flag=0
    if func!='':
        func=func+"("+stack1[0]
        flag=1
    else:
        func=func+stack1[0]
    for i in range(1,len(stack1)):     
        func=func+","+stack1[i]
    if flag==1:
        func=func+")"
    print "Unified string: ",func
    print "Substitutions: ",subs
 
