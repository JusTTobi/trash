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
    for (int i = 0; string[i] != '\0'; i++ )
    {
        printf("%lc\n", string[i]);
    }
//    system("pause");
    for (int i = 0, l = wcslen(string); i < l / 2; i++)
    {
        wchar_t c = string[i];
        string[i] = string[l - i - 1];
        string[l - i - 1] = c;
    }
    printf("%ls\n", string);
    for (int i = 0; string[i] != '\0'; i++ )
    {
        printf("%lc\n", string[i]);
    }
    return 0;

}
