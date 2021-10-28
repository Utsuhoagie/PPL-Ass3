import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test0(self):
        input  ="""
            class A {
                int x;
                float x;
            }
        """

        expect = """Redeclared Attribute: x"""
        self.assertTrue(TestChecker.test(input, expect, 400))


    def test1(self):
        input = """
            class a {

            }

            class a {
                
            }
        """

        expect = """Redeclared Class: a"""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test2(self):
        input = """
            class A extends B {
                
            }
        """

        expect = """Undeclared Class: B"""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3(self):
        input = """
            class A {
                int var1;
                bool var1;
            }
        """

        expect = """Redeclared Attribute: var1"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test4(self):
        input = """
            class A {
                int foo() {

                }
                
                float foo() {

                }
            }
        """

        expect = """Redeclared Method: foo"""
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test10(self):
        input = """
            class Shape {
                float length, width;
                float getArea() {}
            }
            class Rectangle extends Shapeee {
                int length;
            }
        """
        expect = """Undeclared Class: Shapeee"""
        self.assertTrue(TestChecker.test(input, expect, 410)) 


    def test11(self):
        input = """
            class Shape {
                float length;
                float width;
            }
            class Rectangle extends Shape {

            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 411)) 

    def test12(self):
        input = """
            class Shape {
                float length = 5.5;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test13(self):
        input = """
            class Shape {
                float length = 5.5;
                void foo() {

                }
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test14(self):
        input = """
            class Shape {
                int[3] arr = {3, 4.5, 5};
            }
        """
        expect = """Illegal Array Literal: [IntLit(3),FloatLit(4.5),IntLit(5)]"""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test15(self):
        input = """
            class Shape {
                int[3] arr = {3, 4, 5};
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test16(self):
        input = """
            class Shape {
                final int a = 5;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test17(self):
        input = """
            class Shape {
                int num = 5;
                final int a = num;
            }
        """
        expect = """Illegal Constant Expression: Id(num)"""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test18(self):
        input = """
            class Shape {
                final int numf = 5;
                final int a = numf;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test19(self):
        input = """
            class Shape {
                int num = 5 + 3;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test20(self):
        input = """
            class Shape {
                int a = 3;
                final int num = 5 + a;
            }
        """
        expect = """Illegal Constant Expression: BinaryOp(+,IntLit(5),Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test21(self):
        input = """
            class Shape {
                int a = 3;
                final int num = -a;
            }
        """
        expect = """Illegal Constant Expression: UnaryOp(-,Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test22(self):
        input = """
            class Shape {
                int a = 3 + "a";
            }
        """
        expect = """Type Mismatch In Expression: BinaryOp(+,IntLit(3),StringLit(a))"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test23(self):
        input = """
            class Shape {
                int a = 3 \ 3.5;
            }
        """
        expect = """Type Mismatch In Expression: BinaryOp(\,IntLit(3),FloatLit(3.5))"""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test24(self):
        input = """
            class Shape {
                boolean a = true && 1;
            }
        """
        expect = """Type Mismatch In Expression: BinaryOp(&&,BooleanLit(True),IntLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test25(self):
        input = """
            class Shape {
                boolean a = 3 == 6;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test26(self):
        input = """
            class Shape {
                boolean a = 3 == false;
            }
        """
        expect = """Type Mismatch In Expression: BinaryOp(==,IntLit(3),BooleanLit(False))"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test27(self):
        input = """
            class Shape {
                int a;
                int foo(int b) {}
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test28(self):
        input = """
            class Ex {
                int x = 5.5;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 428))



    def test29(self):
        input = """
            class Ex {
                final int x = 10.0;
            }
        """
        expect = """Type Mismatch In Constant Declaration: ConstDecl(Id(x),IntType,FloatLit(10.0))"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test30(self):
        input = """
            class Shape {
                int foo() {}
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test31(self):
        input = """
            class Shape {
                int foo() {}

                float foo() {}
            }
        """
        expect = """Redeclared Method: foo"""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test32(self):
        input = """
            class Shape {
                int foo(int a) {}
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test33(self):
        input = """
            class Shape {
                float a;
                int foo(int a) {}
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test34(self):
        input = """
            class Shape {
                float foo;
                int foo(int a) {}
            }
        """
        expect = """Redeclared Method: foo"""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test35(self):
        input = """
            class Shape {
                int foo(int a) {
                    int b = 0;
                }
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test36(self):
        input = """
            class Shape {
                int foo(int a) {
                    int a = 0;
                }
            }
        """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test37(self):
        input = """
            class Shape {
                void foo() {
                    continue;
                }
            }
        """
        expect = """Continue Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test38(self):
        input = """
            class Shape {
                void foo() {
                    break;
                }
            }
        """
        expect = """Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test39(self):
        input = """
            class Shape {
                int foo() {
                    if true then
                        return 5;
                }
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test40(self):
        input = """
            class Shape {
                int foo() {
                    if true && false || true then
                        return 5;
                }
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test41(self):
        input = """
            class Shape {
                int foo(boolean cond) {
                    if cond then
                        return 5;
                }
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test42(self):
        input = """
            class Shape {
                int foo(int cond) {
                    if cond then
                        return 5;
                }
            }
        """
        expect = """Type Mismatch In Statement: If(Id(cond),Return(IntLit(5)))"""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test43(self):
        input = """
            class Shape {
                Rect r;
            }

            class Rect {
                float w, h;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test44(self):
        input = """
            class Shape {
                void foo() {
                    Shape s;
                }
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test45(self):
        input = """
            class Shape {
                void foo() {
                    Shh s;
                }
            }
        """
        expect = """Undeclared Class: Shh"""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test46(self):
        input = """
            class Shape {
                int i;
                void foo() {
                    for i := 1 to 5 do {}
                }
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test47(self):
        input = """
            class Shape {
                string i;
                void foo() {
                    for i := 1 to 5 do {}
                }
            }
        """
        expect = """Type Mismatch In Statement: For(Id(i),IntLit(1),IntLit(5),True,Block([],[])])"""
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test48(self):
        input = """
            class Shape {
                string a;
                string b;
                string c = a^b;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test49(self):
        input = """
            class Shape {
                string a;
                int b;
                void foo() {
                    string c = a^b;
                } 
            }
        """
        expect = """Type Mismatch In Expression: BinaryOp(^,Id(a),Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test50(self):
        input = """
            class Shape {
                string a;
                string b;
                void foo() {
                    string c;
                    c := a^b;
                } 
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test51(self):
        input = """
            class Shape {
                string a;
                int b;
                void foo() {
                    string c;
                    c := a^b;
                } 
            }
        """
        expect = """Type Mismatch In Expression: BinaryOp(^,Id(a),Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test52(self):
        input = """
            class Shape {
                string a;
                string b;
                void foo() {
                    int c;
                    c := a^b;
                } 
            }
        """
        expect = """Type Mismatch In Statement: AssignStmt(Id(c),BinaryOp(^,Id(a),Id(b)))"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test53(self):
        input = """
            class Shape {
                int a;
                int b;
                void foo() {
                    int c;
                    c := a*b;
                } 
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test54(self):
        input = """
            class Shape {
                int a;
                int b;
                void foo() {
                    int c;
                    c := a*b - a/(a+b);
                } 
            }
        """
        expect = """Type Mismatch In Statement: AssignStmt(Id(c),BinaryOp(-,BinaryOp(*,Id(a),Id(b)),BinaryOp(/,Id(a),BinaryOp(+,Id(a),Id(b)))))"""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test55(self):
        input = """
            class Shape {
                int a;
                int b;
                void foo() {
                    boolean c;
                    c := a == b;
                } 
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test56(self):
        input = """
            class Shape {
                int a;
                float b;
                void foo() {
                    boolean c;
                    c := a == b;
                } 
            }
        """
        expect = """Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test57(self):
        input = """
            class Shape {
                string a = "afasgsd";
                string b = "asdd";
                string c = "fafsasd";
                void foo() {
                    string d;
                    d := a^b^b^c^c^a;
                } 
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test58(self):
        input = """
            class Shape {
                string a;
                Thing b;
                void foo() {
                    string d;
                    d := a^b;
                } 
            }

            class Thing {

            }
        """
        expect = """Type Mismatch In Expression: BinaryOp(^,Id(a),Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test59(self):
        input = """
            class Shape {
                Thing b;
                void foo() {
                    Thing d;
                    d := bf;
                } 
            }

            class Thing {

            }
        """
        expect = """Undeclared Class: bf"""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test60(self):
        input = """
            class Shape {
                float i;
                void foo() {
                    for i := 1 to 5 do {
                        break;
                    }
                } 
            }
        """
        expect = """Type Mismatch In Statement: For(Id(i),IntLit(1),IntLit(5),True,Block([],[Break])])"""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test61(self):
        input = """
            class Shape {
                
                void foo() {
                    float i;
                    for i := 1 to 5 do {
                        continue;
                    }
                } 
            }
        """
        expect = """Type Mismatch In Statement: For(Id(i),IntLit(1),IntLit(5),True,Block([],[Continue])])"""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test62(self):
        input = """
            class Shape {
                
                void foo(int i, j) {
                    for i := 1 to 5 do {
                        for j := i to 10 do {

                        }
                    }
                } 
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test62(self):
        input = """
            class Shape {
                float i;
                
                void foo(int i, j) {
                    for i := 1 to 5 do {
                        for j := i to 10 do {
                            if (j % 2 == 0 && j > 6) then
                                break;
                        }
                    }
                } 
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test63(self):
        input = """
            class Shape {                
                void foo() {
                    for i := 1 to 5 do {

                    }
                } 
            }
        """
        expect = """Undeclared Variable: i"""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test64(self):
        input = """
            class Shape {                
                void foo() {
                    if i < 5 then {} else {}
                } 
            }
        """
        expect = """Undeclared Variable: i"""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test65(self):
        input = """
            class Shape {
                int i, a, b;            
                void foo() {
                    for i := a to b do {}
                } 
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test66(self):
        input = """
            class Shape {
                int i, a, b;            
                void foo() {
                    for i := a+5 to b do {}
                } 
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test67(self):
        input = """
            class Shape {
                void foo() {
                    Shape a = new Shpe();
                } 
            }
        """
        expect = """Undeclared Class: Shpe"""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test68(self):
        input = """
            class Shape {
                int a;
                int b;
                int[3] arr = {1,2,3};
                void foo() {
                    a := b[0];
                } 
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 468))


    # def test64(self):
    #     input = """
    #         class Point {
    #             int x = 0, y = 0;
    #         }

    #         class Shape {
    #             Point a;
    #             int temp;

    #             void foo() {
    #                 temp := a;
    #             } 
    #         }
    #     """
    #     expect = """Type Mismatch In Statement: AssignStmt(Id(temp),Id(a))"""
    #     self.assertTrue(TestChecker.test(input, expect, 464))

    # def test64(self):
    #     input = """
    #         class Point {
    #             int x = 0;
    #         }

    #         class Shape {
    #             Point a;
    #             int temp;

    #             void foo() {
    #                 temp := a.x;
    #             } 
    #         }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 464))






    # def test80(self):
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
    #     self.assertTrue(TestChecker.test(input, expect, 480)) 