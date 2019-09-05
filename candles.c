#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
void birthdayCakeCandles(int a[70])
{
    int n,i,c=0;
    scanf("%d",&n);
    int max=a[0];
    for(i=0;i<n;i++)
    {
        scanf("%d ",&a[i]);
        if(a[i]>max)
        {
            max=a[i];
        }
        if(a[i]==max)
        {
            c++;
        }
    }
    printf("%d",c);
}
int main()
{
    int a[100];
    birthdayCakeCandles(a);
    return 0;
}
