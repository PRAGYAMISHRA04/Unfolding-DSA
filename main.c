#include<stdio.h>
#include<math.h>

void find(int ele,int low,int high,int B[])
{ int mid;
  mid=floor((low+high)/2);
  if(ele==B[mid])
      printf("Found at %d",mid);
  else if(ele<B[mid])
      find(ele,low,mid-1,B);
  else if(ele>B[mid])
      find(ele,mid+1,high,B);
  else if(high<=low)
      printf("Not found");
}
int main()
{ int A[]={3,4,5,6,7,8},e;
  printf("\n Enter element to be searched ");scanf("%d",&e);
  int len;
  find(e,0,5,A);
}