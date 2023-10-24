#include <stdio.h>

int main()
{
    int num[5], i;
    for (i = 0; i < 5; i++)
    {
        printf("Enter the number %d:  ", i + 1);
        scanf("%d", &num[i]);
    }
    printf("The numbers in reverse order are:\n");
    for (i = 0; i < 5; i++)
    {
        printf("%d\n", num[4 - i]);
    }
    return 0;
}