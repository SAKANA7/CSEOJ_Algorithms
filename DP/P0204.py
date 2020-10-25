#include <stdio.h>
int main()
{
    int a[10001];
    a[1] = 2;
  	int i;
    for(i = 2 ;i < 10001;i++)
    {
        a[i] = a[i-1] + 4*i - 3;
    }
    int n,T;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        printf("%d\n",a[n]);
    }
    return 0;
}