import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],IntType(),Block([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    
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

    def test26(self):
        input = """
            class Shape {
                bool a = 3 == false;
            }
        """
        expect = """Type Mismatch In Expression: BinaryOp(==,IntLit(3),BooleanLit(False))"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    # def test30(self):
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
    #     self.assertTrue(TestChecker.test(input, expect, 40)) 