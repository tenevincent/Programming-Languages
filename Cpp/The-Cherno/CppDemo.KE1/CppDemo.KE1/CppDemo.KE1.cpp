// CppDemo.KE1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <stdio.h>
#include "CppDemo.KE1.h"

void DemoDeclareVariables();



int main()
{

    DemoDeclareVariables();


    char c = 'a';
    switch (c)
    {
    case 'a':
        printf("The value of c is 'a'.\n");
        break;
    case 'b':
        printf("The value of c is 'b'.\n");
        break;
    case 'c':
        printf("The value of x is 'c'.\n");
        break;
    }




    std::cout << "Hello World!\n";
    std::cin.get();
}



void DemoDeclareVariables()
{
    int x = 1;
    int y = 0;
    int myand = x && y;
    int myor = x || y;
    int mynegation = !x;
    printf("The value of an AND expression is: %d\n", myand);
    printf("The value of an OR expression is: %d\n", myor);
    printf("The value of a NEGATION expression is: %d\n", mynegation);

    if (std::cout) {
        printf("The value of an OR expression is: %d\n", myor);
    }
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
