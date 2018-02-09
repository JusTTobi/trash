#include <stdio.h>

int main()
{
    int n;
    long long factor = 1;
    printf("Введите число: ");
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        factor *= i;
    }
    printf("Факториал равен: %d", factor);
    return 0;
}
