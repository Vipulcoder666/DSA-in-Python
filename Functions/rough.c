#include<stdio.h>
int main()
{
    int i,n,arr[n],sum = 0;
    printf("Enter n : ");
    scanf("%d",&n);

    for(i=1;i<=n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=1;i<=n;i++)
    {
        sum = sum + arr[i];
    }
    printf("%d",sum);
    return 0;
}