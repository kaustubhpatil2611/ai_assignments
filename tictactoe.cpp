#include<bits/stdc++.h>
using namespace std;

#define n 3
char board[n][n];

struct Move 
{ 
    int row, col; 
}; 

int calculatescore(char board[n][n])
{
    int i,j;
    int flag=false;
    for(i=1;i<n;i++)//top-down diagonal check
    {
        if(board[i][i]==board[i-1][i-1])
        {
            flag=true;
        }
        else
        {
            flag=false;
            break;
        }
    }
    if(flag==true)
    {
        if(board[i-1][i-1]=='X')
        {
            return 10;
        }
        else
        {
            return -10;
        }
    }
    for(i=1;i<n;i++)//down-top diagonal check
    {
        if(board[i][n-i-1]==board[i-1][n-i-2])
        {
            flag=true;
        }
        else
        {
            flag=false;
            break;
        }
    }
    if(flag==true)
    {
        if(board[i-1][n-i-2]=='X')
        {
            return 10;
        }
        else
        {
            return -10;
        }
    }
    for(i=0;i<n;i++)//horizontal X
    {
        for(j=0;j<n;j++)
        {
            if(board[i][j]=='X')
            {
                flag=true;
            }
            else
            {
                flag=false;
                break;
            }
        }
        if(flag==true)
        {
            return 10;
        }
    }
    for(i=0;i<n;i++)//vertical X
    {
        for(j=0;j<n;j++)
        {
            if(board[j][i]=='X')
            {
                flag=true;
            }
            else
            {
                flag=false;
                break;
            }
        }
        if(flag==true)
        {
            return 10;
        }
    }
    for(i=0;i<n;i++)//horizontal O
    {
        for(j=0;j<n;j++)
        {
            if(board[i][j]=='O')
            {
                flag=true;
            }
            else
            {
                flag=false;
                break;
            }
        }
        if(flag==true)
        {
            return -10;
        }
    }
    for(i=0;i<n;i++)//vertical X
    {
        for(j=0;j<n;j++)
        {
            if(board[j][i]=='O')
            {
                flag=true;
            }
            else
            {
                flag=false;
                break;
            }
        }
        if(flag==true)
        {
            return -10;
        }
    }
    return 0;

}

int minimax(char board[n][n],int depth,bool player)
{
    int score = calculatescore(board); 
  
    if (score == 10) 
        return score; 
  
    if (score == -10) 
        return score; 

    if(player)//maximizer turn selects the highest value
    {
        int best=INT_MIN;
        for(int i=0;i<n;i++)
        {
            for (int j = 0; j < n; j++)
            {
                /* code */
                if(board[i][j]=='_')
                {
                    board[i][j]='X';          
                    best = max( best,minimax(board, depth+1, !player) ); 

                    board[i][j] = '_'; 
                }

            }
            
        }
    }
    else//minimizer turn selects the least value
    {
        int best=INT_MAX;
        for(int i=0;i<n;i++)
        {
            for (int j = 0; j < n; j++)
            {
                /* code */
                if(board[i][j]=='_')
                {
                    board[i][j] = 'O'; 
  
                    best = min(best,minimax(board, depth+1, !player)); 
  
                    board[i][j] = '_';   
                                      
                }

            }
            
        }
    }

}

bool findBestMove(char board[n][n]) 
{ 
    int bestVal = -1000; 
    Move bestMove; 
    bestMove.row = -1; 
    bestMove.col = -1; 

    for (int i = 0; i<n; i++) 
    { 
        for (int j = 0; j<n; j++) 
        {  
            if (board[i][j]=='_') 
            { 
                board[i][j] = 'X'; //check move
                int moveVal = minimax(board, 0, false);  
                board[i][j] = '_'; //undo move
  
                if (moveVal > bestVal) //check if best
                { 
                    bestMove.row = i; 
                    bestMove.col = j; 
                    bestVal = moveVal; 
                } 
            } 
        } 
    } 

    //input the best move
    board[bestMove.row][bestMove.col]='X';

    int val=calculatescore(board);
    if(val==10)//if computer won 
    {
        cout<<"Computer Won!"<<endl;
        return true;
    }
    if(val==-10)//if human won
    {
        cout<<"You won!"<<endl;
        return true;
    }

    
    for(int i=0;i<n;i++)
    {
        for (int j = 0; j < n; j++)
        {
            if(board[i][j]=='_')//if no one won and moves remaining
            {
                return false;
            }

        }
    }

    if(val==0)//else draw
    {
        cout<<"The game has ended in draw"<<endl;
        return true;
    }

  
} 

int main()
{
    int x,y;
    board= 
    { 
        { 'X', '_', '_' }, 
        { '_', '_', '_' }, 
        { '_', '_', '_' } 
    }; 
    while(1)//while game continues
    {
        cout<<"Enter your Move: ";
        cin>>x>>y;
        if(board[x-1][y-1]=='_')//if proper move
        {
            board[x-1][y-1]='O';
            bool x=findBestMove(board);
            for(int i=0;i<n;i++)
            {
                for (int j = 0; j < n; j++)
                {
                    /* code */
                    cout<<board[i][j]<<" ";
                }
                cout<<endl;
                cout<<endl;
            }
            if(x)//if game finished
            {
                break;
            }
        }
        else//else enter proper move
        {
            cout<<"Please enter proper coordinates"<<endl;
        }
    }
}