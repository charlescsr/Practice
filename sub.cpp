#include<bits/stdc++.h> 
using namespace std; 
   
int main()  
{ 
	char str[1000],n;
	scanf("%[^\n]%*c",str);
	n=strlen(str);

    for (int len = 1; len <= n; len++)  
    {     
        
        for (int i = 0; i <= n - len; i++)  
        { 
              
            int j = i + len - 1;             
            for (int k = i; k <= j; k++)  
                cout << str[k]; 
              
            cout << endl; 
        } 
    }
	return 0; 
} 
