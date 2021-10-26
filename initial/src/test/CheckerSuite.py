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
                void foo() {

                }
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 412))



    # def test20(self):
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
    #     self.assertTrue(TestChecker.test(input, expect, 420)) 