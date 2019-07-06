#include<stdio.h>

void main()
{
	int a,i;
	scanf("%d",&a);
	
	int notes[10]={2000,500,200,100,50,20,10,5,2,1};
	
	int counter[10]={ 0 };
	
	for(i=0;i<10;i++){
		if(a>=notes[i]){
			counter[i]=a/notes[i];
			a=a-counter[i]*notes[i];
		}
	}
	
	for(i=0;i<10;i++){
		if(counter[i]!=0){
			printf("%d-->%d",notes[i],counter[i]);
			printf("\n");
		}
	}
}
