#include<stdio.h>
#include<math.h>

void Selectsort(int *arr,int n)
{  int i=0,j,key,t,k;
  for(;i<n-1;i++)
    { key=i;
        for(j=i+1;j<n;j++)
        { if(arr[j]<arr[key])
            key=j;
            }
      t=arr[i];
      arr[i]=arr[key];
      arr[key]=t;
      printf("\n");
       for(k=0;k<5;k++)
            printf("%d",arr[k]);
}
   
 }

int main()
{ int A[5]={5,8,2,3,4};
  Selectsort(A,5);
}
          
