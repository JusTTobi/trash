#include <stdio.h>   //Для printf
#include <unistd.h>  //Для sleep

int main(void)
{
    const int max_n = 10;
   //Вывод сообщения о приостановке работы
    printf("Взрыв через %d секунд!\n", max_n);
   //Цикл на пять тактов
   for (int MyTik=0; MyTik < max_n; MyTik++)
   {
      //Вывод оставшегося времени до возобновления работы
      printf ("Осталось %d сек.\n", max_n-MyTik);
      //Приостановка работы на 1 секунду
      sleep (1);
   }
   //Вывод сообщения о возобновлении работы
   printf("БУММ!!\n");
   return 0;
}
