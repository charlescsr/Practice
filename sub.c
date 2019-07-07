#include<stdio.h>
#include<stdlib.h>
#include<string.h>
   
int main()  
{ 

	char str[1000];
	int n,len,i,k;
	scanf("%[^\n]%*c",str);
	n=strlen(str);

    for (len = 1; len <= n; len++)  
    {     
        
        for (i = 0; i <= n - len; i++)  
        { 
              
            int j = i + len - 1;             
            for (k = i; k <= j; k++)  
                printf("%s",str[k]); 
              
            printf("\n"); 
        } 
    }
	return 0; 
} 
