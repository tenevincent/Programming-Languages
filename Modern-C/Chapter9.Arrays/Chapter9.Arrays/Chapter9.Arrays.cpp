// Chapter9.Arrays.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

int main()
{
    
    std::string s = "Hello World.";
    std::cout << s.c_str();


    bool a = true;
    bool b = true;
    if (a && b)
    {
        std::cout << "The entire condition is true.\n";
    }


    int condition = 4;
    if (condition) {

        std::cout << "condition with integer.\n";
    }

    int* p = new int;
    *p = 123;
    std::cout << "The pointed-to value is: " << *p;
    if (p) { 
        std::cout << "condition with integer.\n";
    }
    
    delete p;



    //int myarr[5] = {  };
    //for (int i = 0; i < 5; i++)
    //{
    //    printf("%d ", myarr[i]);
    //}

    //int arr[6] = { 1, 2, 3,5,5 };
    //size_t arrsize = sizeof(arr);
    //printf("Total array size in bytes: %ld\n", arrsize/sizeof(arr[0]));


    //int x = 123;
    //int* ip = &x; // get an address of an integer object
    //void* vp;
    //vp = ip; // void pointer gets the value of an integer pointer
    //printf("The pointed-to value is: %d\n", *((int*)vp));

    //vp = arr;
    //printf("The pointed-to value is: %d\n", *((int*)vp));

    //const char* ptr[5] = { "This is the first sentence.",
    //    "This is the second sentence.",
    //    "This is the third sentence.",
    //    "This is the last sentence." };

    //for (int i = 0; i < 5; i++)
    //{
    //    printf("%s\n", ptr[i]);
    //}

    //std::cout << "Hello World!\n";
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
