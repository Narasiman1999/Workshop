
#include<stdio.h>

void value(int *c,int *d)
{

    int temp;

    temp=*c;
    *c=*d;
    *d=temp;
   // printf("AFTER SWAPPING %d %d",a,b);


}





void main()
{
    int a=20,b=10;
    printf("BEFORE SWAPPING %d %d\n",a,b);
    value(&a,&b);
    printf("AFTER SWAPPING %d %d\n",a,b);


}
