#include <stdio.h>
#include <windows.h>

typedef BOOL (WINAPI *SETCONSOLEFONT)(HANDLE, DWORD);
SETCONSOLEFONT SetConsoleFont;

int main(){
  HMODULE hmod = GetModuleHandleA("KERNEL32.DLL");
  SetConsoleFont =(SETCONSOLEFONT) GetProcAddress(hmod, "SetConsoleFont");
  SetConsoleFont(GetStdHandle(STD_OUTPUT_HANDLE), 8);
  SetConsoleCP(1251);
  SetConsoleOutputCP(1251);
  printf("Привет Мир!\nВот такая фигня нужна, чтобы вывести текст на русском языке в консоле Wndows :-)\n");
  getchar();
  return 0;
}
