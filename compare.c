#include <stdio.h>
void compareTriplets(int a[3],int b[3]) 
{
    int i,o[2]={0,0};
    for(i=0;i<3;i++)
    {
        if(a[i]>b[i]) 
        {
            o[0]++;
        }
        else if(a[i]<b[i])
        {
            o[1]++;
        }   
    }
    printf("%d %d",o[0],o[1]);
}
int main()
{
    int a[3],b[3],i;
    for(i=0;i<3;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<3;i++)
    {
        scanf("%d",&b[i]);
    }
    compareTriplets(a,b);
    return 0;
}
