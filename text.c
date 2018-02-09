#include <stdio.h>
#include <wchar.h>
#include <locale.h>
#include <stdlib.h>


int main()
{
    wchar_t string[100];
    setlocale(LC_ALL, "");
    printf ("Введите строку: ");
    scanf("%ls",string);
    printf("Введённая строка: %ls: длина строки: %d\n", string, wcslen(string));
    int i = 0;
    while (string[i] != '\0' )
    {
        printf("%lc\n", string[i]);
        i++;
    }
//    system("pause");
    return 0;
}
