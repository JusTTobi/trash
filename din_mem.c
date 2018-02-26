#include <stdio.h>
#include <stdlib.h>
#define MAX_NAME 20
struct cart
{
    int id;
    char name[MAX_NAME];
    char fam[MAX_NAME];
    int age;
    char sex;
};

typedef struct cart cart;
cart * getcart(int * n);
void printcart(const cart * p, int n);
void savecart(const cart * p, int n, char fname[]);
cart * opencart(int * n, char fname[]);
int findcart(const cart * p, int n);

int main()
{
    int n = 0;
    char fname[100];
    cart * cart_n = NULL;
    while (1)
    {
        printf("Меню:\n1 - Открыть картотеку\n2 - Создать картотеку\n3 - Сохранить картотеку\n4 - Печатать картотеку\n5 - Найти карточку\n6 - Выход\nВаш выбор: ");
        int m = 0;
        scanf("%d", &m);
        switch (m)
        {
        case 1:
        {
            if (cart_n != NULL)
            {
                printf("Данные в ОП будут стёрты!\n");
                free(cart_n);
                cart_n = NULL;
            }
            n = 0;
            printf("Введите имя файла: ");
            scanf("%s", fname);
            cart_n = opencart(&n, fname);
            if (cart_n == NULL)
            {
                printf("Не удаётся прочитать файл!\n");
            }
        }
        break;
        case 2:
        {
            if (cart_n != NULL)
            {
                printf("Данные в ОП будут стёрты!\n");
                free(cart_n);
                cart_n = NULL;
            }
            n = 0;
            cart_n = getcart(& n);
        }
        break;
        case 4:
            if (cart_n != NULL)
            {
                printcart(cart_n, n);
            }
            break;
        case 3:
            if (cart_n != NULL)
            {
                printf("Введите имя файла: ");
                scanf("%s", fname);
                savecart(cart_n, n, fname);
            }
            break;
        case 5:
            if (cart_n != NULL)
            {
                int findn = 0;
                findn = findcart(cart_n, n);
                if (n > 0)
                    printf("Найдено %d карточек\n", findn);
                else if (n == 0)
                    printf("Карточек не найдено!\n");
                else
                    printf("Ошибка!\n");
            }
            break;
        case 6:
            return 0;
            break;
        default:
            printf("Неверный вариант!\n");
        }
    }
}

cart * getcart(int * n)
{
    cart * p = NULL;
    while (1)
    {
        p = (cart *) realloc(p, ((*n)+1)*sizeof(cart));
        if (p == NULL)
        {
            printf("Не хватает памяти!\n");
        }
        (p+(*n))->id = (*n)+1;
        printf("Введите Имя: ");
        scanf("%s", (p+(*n))->name);
        printf("Введите Фамилию: ");
        scanf("%s", (p+(*n))->fam);
        printf("Введите пол (m/f): ");
        scanf("%*c%c", &((p+(*n))->sex));
        printf("Введите возраст: ");
        scanf("%d", &((p+(*n))->age));
        (*n)++;
        printf("Ещё карточка? (y): ");
        char ansv = 'n';
        scanf("%*c%c%", &ansv);

        if (ansv != 'y')
            break;
    }
    return p;
}


void printcart(const cart * p, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("------------------------------------\n");
        printf("ID: %d\n", (p+i)->id);
        printf("Имя: %s\n", (p+i)->name);
        printf("Фамилия:  %s\n", (p+i)->fam);
        printf("Пол: %c\n", (p+i)->sex);
        printf("Возраст: %d\n", (p+i)->age);
        printf("------------------------------------\n");
    }
}

cart * opencart(int * n, char fname[])
{
    FILE *fp;
    fp = fopen(fname, "r");
    if (fp == NULL)
    {
        printf("Не удалось найти файл!\n");
        return NULL;
    }
    cart * p = (cart *) malloc(sizeof(cart));
    for (cart * ptr = p; ; ptr++)
    {
        if (fread(ptr, sizeof(cart), 1, fp))
        {
            (*n)++;
            p = (cart *) realloc(p, ((*n)+1)*sizeof(cart));
        }
        else
            break;
    }
    fclose(fp);
    return p;
}

int findcart(const cart * p, int n)
{
    printf("Введите критерий поиска (1-5) (1-ID, 2-Имя, 3-Фамилия, 4-Пол, 5-Возраст): ");
    int ansv = 0;
    cart temp = {.id = 0,
                 .age = 0,
                 .sex = '\0',
                 .name = '\0',
                 .fam = '\0'
                };
    scanf("%d", &ansv);
    switch (ansv)
    {
    case 1:
    {
        printf("Введите ID: ");
        scanf("%d", &temp.id);
    }
    break;
    case 2:
    {
        printf("Введите Имя: ");
        scanf("%s", temp.name);
        printcart(&temp, 1);
    }
    break;
    case 3:
    {
        printf("Введите Фамилию: ");
        scanf("%s", temp.fam);
    }
    break;
    case 4:
    {
        printf("Введите Пол: ");
        scanf("%*c%c", &temp.sex);
    }
    break;
    case 5:
    {
        printf("Введите Возраст: ");
        scanf("%d", &temp.age);
    }
    break;
    default:
        return -1;
    }
    int m = 0;
    int f = 0;
    for (const cart * ptr = p; m < n; m++, ptr++)
        if (ptr->id == temp.id || ptr->name == temp.name || ptr->fam == temp.fam || ptr->sex == temp.sex || ptr->age == temp.age)
        {
            printcart(ptr, 1);
            f++;
        }
    return f;
}

void savecart(const cart * p, int n, char fname[])
{
    FILE *fp;
    fp = fopen(fname, "w");
    if (fp == NULL)
    {
        printf("Не удалось сохранить файл!\n");
        return;
    }
    fwrite(p, n, sizeof(cart), fp);
    fclose(fp);
}
