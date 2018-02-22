#include <stdio.h>
#include <math.h>
#define ITEM 10

void printmatrix(int matrix[][ITEM]);
void printmatrix2(int *matrix);
void create_matrix(int matrix[][ITEM]);

int main()
{
    int matrix [ITEM] [ITEM] = {0};
    create_matrix(matrix);
    printmatrix(matrix);
    printf("\n");
    printmatrix2((int *) matrix);
    return 0;
}

void printmatrix(int matrix[][ITEM])
    {

    for(int i = 0; i < ITEM; i++)
    {
        for(int j = 0; j < ITEM; j++)
            {
            printf("%d\t", matrix[i][j]);
            }
            putchar('\n');
    }
    }

void printmatrix2(int *matrix)
    {

    for(int i = 0; i < ITEM; i++)
    {
        for(int j = 0; j < ITEM; j++)
            {
            printf("%d\t", *(matrix + ITEM*i + j));
            }
            putchar('\n');
    }
    }
void create_matrix(int matrix[][ITEM])
    {
        for(int i = 0; i < ITEM; i++)
            for(int j = 0; j < ITEM; j++)
            {
                if (i <= j)
                    matrix [i] [j] = 1;
                else
                    matrix [i] [j] = 0;
            }

    }

