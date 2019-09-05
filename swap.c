#include <stdio.h>
#include <stdlib.h>

int main() {
    int n,a_i,i,j,n_swaps=0; 
    scanf("%d", &n);
    int *a = malloc(sizeof(int) * n);
    for(a_i = 0; a_i < n; a_i++){
    	scanf("%d",&a[a_i]);
    }
    for(i=0;i<n;i++){
        for(j=0;j<n-1;j++){
            if(a[j]>a[j+1]){
                int t=a[j];
                a[j]=a[j+1];
                a[j+1]=t;
                n_swaps++;
            }
        }
        if(n_swaps==0){
            break;
        }
    }
    printf("Array is sorted in %d swaps.\n",n_swaps);
    printf("First Element: %d\n",a[0]);
    printf("Last Element: %d",a[n-1]);
    return 0;
}

