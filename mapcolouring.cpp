#include<bits/stdc++.h>
using namespace std;

#define n 6//change as per no. of countries/states
string cmap="";
map<int,int> mapq;
vector<int> smap[n];


bool is_constraint_satisfied(string code)//check if no neighbour has same color
{
    int index=code.size()-1;
    int c=code[index];
    for(auto it=smap[index].begin();it!=smap[index].end();it++)
    {
        if(code[*it]==c)
        {
            return false;
        }
    }
    return true;
}

bool mapcolor(string code,int l,int r)//function for finding colors
{
    if(l==r)//if all countries coloured then return code
    {
        cout<<"Colour Code: "<<code<<endl;
        return true;
    }

    for(auto c:cmap)//try all possible colour codes
    {
        if(is_constraint_satisfied(code+c))//if satisfies then find the next colour code
        {
            mapcolor(code+c,l+1,r);
        }
        
    }
    return false;
}

bool fun(vector<int> vect[n],int color)
{
    vector<char> colorcode {'a','b','c','d','e','f','g','h','i','j'};//depending upon no. of colours assign that many codes
    
    for(int i=0;i<color;i++)
    {
        cmap=cmap+colorcode[i];
    }
    string str="";
    return mapcolor(str,0,n);

}

//driver code
int main()
{
	//code
    int state,neighbor,ch;
    //cout<<"Enter the number of states:";
    //cin>>n;
    int i=0;
    while(i!=n)//until all countries/state finish 
    {
        cout<<"Enter the state number:"<<endl;
        cin>>state;
        ch=1;
        while(ch)//enter all possible country/state numbers
        {
            cout<<"Enter neighbor: ";
            cin>>neighbor;
            smap[state].push_back(neighbor);
            cout<<"Any more neighbors?: ";
            cin>>ch;
        }
        i++;
    }
    int color;
    cout<<"Enter the number of colors available:";
    cin>>color;
    fun(smap,color);
    
}