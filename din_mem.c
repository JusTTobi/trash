#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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
void sortcart(cart * p, int n);
void printcart(const cart * p, int n);
void savecart(const cart * p, int n, char fname[]);
cart * opencart(int * n, char fname[]);
int findcart(const cart * p, int n);
int compid(const void * val1, const void * val2);
int compname(const void * x1, const void * x2);
int compfam(const void * x1, const void * x2);
int compsex(const void * x1, const void * x2);
int compage(const void * x1, const void * x2);
int delcart(cart * p, int n);
int findid(const cart * p, int n, int m);
cart * addcart(cart * p, int * n);
int findidmax(const cart * p, int n);


int main()
{
    int n = 0;
    char fname[100];
    cart * cart_n = NULL;
    while (1)
    {
        printf("Меню:\n1 - Открыть картотеку\n2 - Создать картотеку\n3 - Сохранить картотеку \
               \n4 - Печатать картотеку\n5 - Найти карточку\n6 - Сортировать картотеку \
               \n7 - Добавить карточку\n8 - Удалить карточку\n9 - Выход\nВаш выбор: ");
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
            else
                printf("Считано из файла %s карточек: %d\n", fname, n);
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
                    printf("Найдено карточек: %d\n", findn);
                else if (n == 0)
                    printf("Карточек не найдено!\n");
                else
                    printf("Ошибка!\n");
            }
            break;
        case 6:
            if (cart_n != NULL)
            {
                sortcart(cart_n, n);
            }
            break;
        case 7:
            cart_n = addcart(cart_n, &n);
            break;

        case 8:
            if (cart_n != NULL)
            {
                n = delcart(cart_n, n);
            }
            break;
        case 9:
            return 0;
            break;
        default:
            printf("Неверный вариант!\n");
            return 0;
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
            return p;
        }
        (p+(*n))->id = (*n)+1;
        printf("Введите Имя: ");
        scanf("%s", (p+(*n))->name);
        printf("Введите Фамилию: ");
        scanf("%s", (p+(*n))->fam);
        printf("Введите пол (m/f): ");
        char ansv;
        do {
            ansv = getchar();
        } while (ansv == '\n' || ansv == ' ' || ansv == '\r' );
        (p+(*n))->sex = ansv;
        printf("Введите возраст: ");
        scanf("%d", &((p+(*n))->age));
        (*n)++;
        printf("Ещё карточка? (y): ");
        do {
            ansv = getchar();
        } while (ansv == '\n' || ansv == ' ' || ansv == '\r' );
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
        if (ptr->id == temp.id || strcmp(ptr->name, temp.name) == 0 || strcmp(ptr->fam, temp.fam) == 0 || ptr->sex == temp.sex || ptr->age == temp.age)
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

void sortcart(cart * p, int n)
{
    printf("Критерий сортировки? (1-5) (1-ID, 2-Имя, 3-Фамилия, 4-Пол, 5-Возраст): ");
    int ansv = 0;
    scanf("%d", &ansv);
    switch (ansv)
    {
    case 1:
    {
        qsort(p, n, sizeof(cart), compid);
    }
    break;
    case 2:
    {
        qsort(p, n, sizeof(cart), compname);
    }
    break;
    case 3:
    {
        qsort(p, n, sizeof(cart), compfam);
    }
    break;
    case 4:
    {
        qsort(p, n, sizeof(cart), compsex);
    }
    break;
    case 5:
    {
        qsort(p, n, sizeof(cart), compage);
    }
    break;
    default:
        printf("Неверный критерий");
    }
}

int compid(const void * x1, const void * x2)
{
    return (((cart*)x1)->id - ((cart*)x2)->id);
}

int compname(const void * x1, const void * x2)
{
    return strcmp(((cart*)x1)->name, ((cart*)x2)->name);
}

int compfam(const void * x1, const void * x2)
{
    return strcmp(((cart*)x1)->fam, ((cart*)x2)->fam);
}

int compsex(const void * x1, const void * x2)
{
    return (int) (((cart*)x1)->sex - ((cart*)x2)->sex);
}

int compage(const void * x1, const void * x2)
{
    return (((cart*)x1)->age - ((cart*)x2)->age);
}

int delcart(cart * p, int n)
{
    int m = -1;
    int x = -1;
    printf("Введите ID удаляемой записи: ");
    scanf("%d", &m);
    if (m > -1)
    {
        x = findid(p, n, m);
        if (x < 0)
        {
            printf("ID %d не найден!\n", m);
            return n;
        }
    }
    else return n;
    if (x == n-1)
    {
        p = realloc(p, (n-1)*sizeof(cart));
        return n-1;
    }
    cart * dst = p + x;
    cart * src = p + x + 1;
    printf("%d", x);
    memmove(dst, src, (n-x-1)*sizeof(cart));
    p = realloc(p, (n-1)*sizeof(cart));
    return n-1;
}

int findid(const cart * p, int n, int m)
{
    for (int i = 0; i < n; i++)
    {
        if ((p+i)->id == m)
            return i;
    }
    return -1;
}

cart * addcart(cart * p, int * n)
{
    int id = 1;
    if (p != NULL)
        id = findidmax(p, (*n))+1;
    p = (cart *) realloc(p, ((*n)+1)*sizeof(cart));
    if (p == NULL)
    {
        printf("Не хватает памяти!\n");
        return NULL;
    }
    (p+(*n))->id = id;
    printf("Введите Имя: ");
    scanf("%s", (p+(*n))->name);
    printf("Введите Фамилию: ");
    scanf("%s", (p+(*n))->fam);
    printf("Введите пол (m/f): ");
    char ansv;
    do {
        ansv = getchar();
    } while (ansv == '\n' || ansv == ' ' || ansv == '\r' );
    (p+(*n))->sex = ansv;
    printf("Введите возраст: ");
    scanf("%d", &((p+(*n))->age));
    (*n)++;
    return p;
}

int findidmax(const cart * p, int n)
{
    int max = 1;
    for (int i = 0; i < n; i++)
        if ((p->id) > max)
            max = (p->id);
    return max;
}
