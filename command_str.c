#include <stdio.h>
int main(int argv, char ** argc)
{
    for (int i = 1; i < argv; i++)
    {
    printf("%d аргумент равен: %s\n", i, *(argc+i));
    }
    return 0;
}
