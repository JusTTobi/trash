#include <stdio.h>
#include <stdlib.h>
#define MAX_NAME 20
struct cart {
int id;
char name[MAX_NAME];
char fam[MAX_NAME];
int age;
char sex;
};

void getcart(struct cart * p, int n);
void printcart(struct cart * p, int n);
void savecart(struct cart * p, int n, char fname[]);

int main()
{

int n = 0;
struct cart * cart_n = NULL;
do{
cart_n = realloc(cart_n, (n+1)*sizeof(*cart_n));
if (cart_n == NULL){
    printf("Не хватает памяти!\n");
    return -1;
}
getcart(cart_n, n);
printf("Ещё карточка? (y): ");
char ansv = 'n';
scanf("%*c%c%", &ansv);
if (ansv != 'y')
    break;
n++;
} while (1);
printcart(cart_n, n);
savecart(cart_n, n, "file.txt");
return 0;
}

void getcart(struct cart * p, int n)
{
(p+n)->id = n+1;
printf("Введите Имя: ");
scanf("%s", (p+n)->name);
printf("Введите Фамилию: ");
scanf("%s", (p+n)->fam);
printf("Введите пол (m/f): ");
scanf("%*c%c", &((p+n)->sex));
printf("Введите возраст: ");
scanf("%d", &((p+n)->age));
}

void printcart(struct cart * p, int n)
{
for (int i = 0; i <= n; i++)
{
printf("------------------------------------\n");
printf("ID: %d\n", (p+i)->id);
printf("Имя: %s\n", (p+i)->name);
printf("Фамилия:  %s\n", (p+i)->fam);
printf("Пол: %c\n", (p+i)->sex);
printf("Возраст возраст: %d\n", (p+i)->age);
printf("------------------------------------\n");
}
}

void savecart(struct cart * p, int n, char fname[])
{
    FILE *fp;
    fp = fopen(fname, "w");
    if (fp == NULL)
    {
        printf("Не удалось сохранить файл!\n");
        return;
    }
    fwrite(p, n+1, sizeof(*p) , fp );
    fclose(fp);
}
