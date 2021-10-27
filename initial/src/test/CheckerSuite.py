import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    # def test0(self):
    #     input  ="""
    #         class A {
    #             int x;
    #             float x;
    #         }
    #     """

    #     expect = """Redeclared Attribute: x"""
    #     self.assertTrue(TestChecker.test(input, expect, 400))


    # def test1(self):
    #     input = """
    #         class a {

    #         }

    #         class a {
                
    #         }
    #     """

    #     expect = """Redeclared Class: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test2(self):
    #     input = """
    #         class A extends B {
                
    #         }
    #     """

    #     expect = """Undeclared Class: B"""
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test3(self):
    #     input = """
    #         class A {
    #             int var1;
    #             bool var1;
    #         }
    #     """

    #     expect = """Redeclared Attribute: var1"""
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test4(self):
    #     input = """
    #         class A {
    #             int foo() {

    #             }
                
    #             float foo() {

    #             }
    #         }
    #     """

    #     expect = """Redeclared Method: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 404))

    # def test10(self):
    #     input = """
    #         class Shape {
    #             float length, width;
    #             float getArea() {}
    #         }
    #         class Rectangle extends Shapeee {
    #             int length;
    #         }
    #     """
    #     expect = """Undeclared Class: Shapeee"""
    #     self.assertTrue(TestChecker.test(input, expect, 410)) 


    # def test11(self):
    #     input = """
    #         class Shape {
    #             float length;
    #             float width;
    #         }
    #         class Rectangle extends Shape {

    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 411)) 

    # def test12(self):
    #     input = """
    #         class Shape {
    #             float length = 5.5;
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 412))

    # def test13(self):
    #     input = """
    #         class Shape {
    #             float length = 5.5;
    #             void foo() {

    #             }
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 413))

    # def test14(self):
    #     input = """
    #         class Shape {
    #             int[3] arr = {3, 4.5, 5};
    #         }
    #     """
    #     expect = """Illegal Array Literal: [IntLit(3),FloatLit(4.5),IntLit(5)]"""
    #     self.assertTrue(TestChecker.test(input, expect, 414))

    # def test15(self):
    #     input = """
    #         class Shape {
    #             int[3] arr = {3, 4, 5};
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 415))

    # def test16(self):
    #     input = """
    #         class Shape {
    #             final int a = 5;
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 416))

    # def test17(self):
    #     input = """
    #         class Shape {
    #             int num = 5;
    #             final int a = num;
    #         }
    #     """
    #     expect = """Illegal Constant Expression: Id(num)"""
    #     self.assertTrue(TestChecker.test(input, expect, 417))

    # def test18(self):
    #     input = """
    #         class Shape {
    #             final int numf = 5;
    #             final int a = numf;
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 418))

    # def test19(self):
    #     input = """
    #         class Shape {
    #             int num = 5 + 3;
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 419))

    # def test20(self):
    #     input = """
    #         class Shape {
    #             int a = 3;
    #             final int num = 5 + a;
    #         }
    #     """
    #     expect = """Illegal Constant Expression: BinaryOp(+,IntLit(5),Id(a))"""
    #     self.assertTrue(TestChecker.test(input, expect, 420))

    # def test21(self):
    #     input = """
    #         class Shape {
    #             int a = 3;
    #             final int num = -a;
    #         }
    #     """
    #     expect = """Illegal Constant Expression: UnaryOp(-,Id(a))"""
    #     self.assertTrue(TestChecker.test(input, expect, 421))

    # def test22(self):
    #     input = """
    #         class Shape {
    #             int a = 3 + "a";
    #         }
    #     """
    #     expect = """Type Mismatch In Expression: BinaryOp(+,IntLit(3),StringLit(a))"""
    #     self.assertTrue(TestChecker.test(input, expect, 422))

    # def test23(self):
    #     input = """
    #         class Shape {
    #             int a = 3 \ 3.5;
    #         }
    #     """
    #     expect = """Type Mismatch In Expression: BinaryOp(\,IntLit(3),FloatLit(3.5))"""
    #     self.assertTrue(TestChecker.test(input, expect, 423))

    # def test24(self):
    #     input = """
    #         class Shape {
    #             bool a = true && 1;
    #         }
    #     """
    #     expect = """Type Mismatch In Expression: BinaryOp(&&,BooleanLit(True),IntLit(1))"""
    #     self.assertTrue(TestChecker.test(input, expect, 424))

    # def test25(self):
    #     input = """
    #         class Shape {
    #             bool a = 3 == 6;
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 425))

    # def test26(self):
    #     input = """
    #         class Shape {
    #             bool a = 3 == false;
    #         }
    #     """
    #     expect = """Type Mismatch In Expression: BinaryOp(==,IntLit(3),BooleanLit(False))"""
    #     self.assertTrue(TestChecker.test(input, expect, 426))

    # def test27(self):
    #     input = """
    #         class Shape {
    #             int a;
    #             int foo(int b) {}
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 427))

    # def test28(self):
    #     input = """
    #         class Ex {
    #             int x = 5.5;
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 428))



    # def test29(self):
    #     input = """
    #         class Ex {
    #             final int x = 10.0;
    #         }
    #     """
    #     expect = """Type Mismatch In Constant Declaration: ConstDecl(Id(x),IntType,FloatLit(10.0))"""
    #     self.assertTrue(TestChecker.test(input, expect, 429))

    # def test30(self):
    #     input = """
    #         class Shape {
    #             int foo() {}
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 430))

    # def test31(self):
    #     input = """
    #         class Shape {
    #             int foo() {}

    #             float foo() {}
    #         }
    #     """
    #     expect = """Redeclared Method: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 431))

    # def test32(self):
    #     input = """
    #         class Shape {
    #             int foo(int a) {}
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 432))

    # def test33(self):
    #     input = """
    #         class Shape {
    #             float a;
    #             int foo(int a) {}
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 433))

    # def test34(self):
    #     input = """
    #         class Shape {
    #             float foo;
    #             int foo(int a) {}
    #         }
    #     """
    #     expect = """Redeclared Method: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 434))

    # def test35(self):
    #     input = """
    #         class Shape {
    #             int foo(int a) {
    #                 int b = 0;
    #             }
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 435))

    # def test36(self):
    #     input = """
    #         class Shape {
    #             int foo(int a) {
    #                 int a = 0;
    #             }
    #         }
    #     """
    #     expect = """Redeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 436))

    # def test37(self):
    #     input = """
    #         class Shape {
    #             void foo() {
    #                 continue;
    #             }
    #         }
    #     """
    #     expect = """Continue Not In Loop"""
    #     self.assertTrue(TestChecker.test(input, expect, 437))

    # def test38(self):
    #     input = """
    #         class Shape {
    #             void foo() {
    #                 break;
    #             }
    #         }
    #     """
    #     expect = """Break Not In Loop"""
    #     self.assertTrue(TestChecker.test(input, expect, 438))

    # def test39(self):
    #     input = """
    #         class Shape {
    #             int foo() {
    #                 if true then
    #                     return 5;
    #             }
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 439))

    # def test40(self):
    #     input = """
    #         class Shape {
    #             int foo() {
    #                 if true && false || true then
    #                     return 5;
    #             }
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 440))

    # def test41(self):
    #     input = """
    #         class Shape {
    #             int foo(boolean cond) {
    #                 if cond then
    #                     return 5;
    #             }
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 441))

    # def test42(self):
    #     input = """
    #         class Shape {
    #             int foo(int cond) {
    #                 if cond then
    #                     return 5;
    #             }
    #         }
    #     """
    #     expect = """Type Mismatch In Statement: If(Id(cond),Return(IntLit(5)))"""
    #     self.assertTrue(TestChecker.test(input, expect, 442))

    # def test43(self):
    #     input = """
    #         class Shape {
    #             Rect r;
    #         }

    #         class Rect {
    #             float w, h;
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 443))

    # def test44(self):
    #     input = """
    #         class Shape {
    #             void foo() {
    #                 Shape s;
    #             }
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 444))

    # def test45(self):
    #     input = """
    #         class Shape {
    #             void foo() {
    #                 Shh s;
    #             }
    #         }
    #     """
    #     expect = """Undeclared Class: Shh"""
    #     self.assertTrue(TestChecker.test(input, expect, 445))

    def test46(self):
        input = """
            class Shape {
                void foo() {
                    Shh s;
                }
            }

            class Shh {

            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 446))



    # def test50(self):
    #     input = """
    #         class Shape {
    #             float length;
    #             float width = 0.0;
    #             float getArea() {}
    #             Shape(float length,width) {
    #                 this.length := length;
    #                 this.width := width;
    #             }
    #         }
    #         class Rectangle extends Shape {
    #             float getArea() {
    #                 return this.length * this.width;
    #             }
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 450)) 