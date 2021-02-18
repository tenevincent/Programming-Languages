#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A:
    def __init__(self):
        self.X = 1337
        print("Konstruktor von A")
        
    def m(self):
        print("Methode m von A. Es ist self.X =", self.X)


class B(A):
    def __init__(self):
        super().__init__()
        self.Y = 10000
        print("Konstruktor von B")

    def n(self):
        print("Methode n von B. Es ist self.Y =", self.Y)

    def m(self):
        print("Methode m von B.")
        super().m()


b = B()
b.m()
