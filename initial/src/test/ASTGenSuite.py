import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_program2(self):
        """Simple program: class main {} """
        input = """
            class main {

            }
            class foo {
                
            }"""
        expect = str(Program([ClassDecl(Id("main"),[]), ClassDecl(Id("foo"),[])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_simple_program3(self):
        """Simple program: class main {} """
        input = """class main extends foo {}"""
        expect = str(Program([ClassDecl(Id("main"),[],Id("foo"))]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_class_with_one_decl_program(self):
        
        input = """class main {
            int a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,303))
    
    def test_class_with_two_decl_program(self):
        
        input = """class main {
            int a;
            int b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,304))
   
    def test_class_with_sameline_decl_program(self):
        
        input = """class main {
            int a,b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_class_with_samelinediff_decl_program(self):
        
        input = """class main {
            static int a,b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Static(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Static(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def testBlock(self):
        
        input = """class main {
            void foo() {

            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,307))

    def testBlock2(self):
        
        input = """class main {
            void foo(int a) {

            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],VoidType(),Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,308))

    def testBlock3(self):
        
        input = """class main {
            void foo(int a,b,c; float d) {

            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType()),VarDecl(Id("d"),FloatType())],
            VoidType(),Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,309))

    def testBlock4(self):
        
        input = """class main {
            static int foo;
            void foo(int a,b,c; float d) {

            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Static(),VarDecl(Id("foo"),IntType())),
            MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType()),VarDecl(Id("d"),FloatType())],
            VoidType(),Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,310))

    def testBlock5(self):
        
        input = """class main {
            foo(string bar) {
                
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("bar"),StringType())],
            None,Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,311))

    def testBlock6(self):
        
        input = """class main {
            void foo() {
                a := 5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],
            VoidType(),Block([],[Assign(Id("a"),IntLiteral(5))]))])]))
        self.assertTrue(TestAST.test(input,expect,312))

    def testBlock7(self):
        
        input = """class main {
            void foo(int a) {
                a := 5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"), IntType())],
            VoidType(),Block([],[Assign(Id("a"),IntLiteral(5))]))])]))
        self.assertTrue(TestAST.test(input,expect,313))

    def testIf(self):
        
        input = """class main {
            void foo(int a) {
                if true then
                    a := 5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],
            VoidType(),Block([],[If(BooleanLiteral(True), Assign(Id("a"),IntLiteral(5)))]))])]))
        self.assertTrue(TestAST.test(input,expect,314))

    def testIfElse(self):
        
        input = """class main {
            float foo(int a) {
                if true then
                    a := 5;
                else
                    return 5.5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())], FloatType(),
            Block([],[
                If(BooleanLiteral(True), Assign(Id("a"),IntLiteral(5)), Return(FloatLiteral(5.5)))
            ]))])]))
        self.assertTrue(TestAST.test(input,expect,315))

    def testFor(self):
        
        input = """class main {
            void foo(int a) {
                for b := 0 to 10 do
                    a := 5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())], VoidType(),
            Block([],[
                For(Id("b"), IntLiteral(0), IntLiteral(10),True,
                    Assign(Id("a"), IntLiteral(5)))
                ]))])]))
        self.assertTrue(TestAST.test(input,expect,316))

    def testForBreak(self):
        
        input = """class main {
            void foo(int a) {
                for b := 0 to 10 do
                    break;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())], VoidType(),
            Block([],[
                For(Id("b"), IntLiteral(0), IntLiteral(10),True,
                    Break())
                ]))])]))
        self.assertTrue(TestAST.test(input,expect,317))

    def testFieldAccess(self):
        
        input = """class main {
            void foo() {
                shape.width := 5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block([],[
                    Assign(FieldAccess(Id("shape"),Id("width")),IntLiteral(5))
                ]))])]))
        self.assertTrue(TestAST.test(input,expect,318))

    def testFullFieldAccess(self):
        
        input = """class main {
            void foo() {
                Shape s;


                Shape.width := 5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("s"), ClassType(Id("Shape")), NullLiteral())
                    ]
                    ,
                    [
                    Assign(FieldAccess(Id("Shape"),Id("width")),IntLiteral(5))
                ]))])]))
        self.assertTrue(TestAST.test(input,expect,319))

    def testCall(self):
        
        input = """class main {
            void foo() {
                shape.getWidth();
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block([],
                    [
                        CallStmt(Id("shape"), Id("getWidth"), [])
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,320))

    def testArray(self):
        
        input = """class main {
            int[5] a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(5,IntType())))]
            )]))
        self.assertTrue(TestAST.test(input,expect,321))

    def testArrayLit(self):
        
        input = """class main {
            int[1] a = {5};
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(1,IntType()),
            ArrayLiteral([IntLiteral(5)])
            ))]
            )]))
        self.assertTrue(TestAST.test(input,expect,322))

    def testNew(self):
        
        input = """class main {
            void foo() {
                Shape s;
                
                s := new Shape();
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("s"), ClassType(Id("Shape")), NullLiteral())
                    ]
                    ,
                    [
                    Assign(Id("s"),NewExpr(Id("Shape"),[]))
                ]))])]))
        self.assertTrue(TestAST.test(input,expect,323))

    def testThis(self):
        
        input = """class main {
            void foo() {
                Shape s;
                
                s := this;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("s"), ClassType(Id("Shape")), NullLiteral())
                    ]
                    ,
                    [
                    Assign(Id("s"),SelfLiteral())
                ]))])]))
        self.assertTrue(TestAST.test(input,expect,324))

    def testCallExp(self):
        
        input = """class main {
            void foo() {
                int s;
                
                s := fumo.getPrice();
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("s"), IntType())
                    ]
                    ,
                    [
                        Assign(Id("s"), CallStmt(Id("fumo"), Id("getPrice"), []))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,325))

    def testArrayLitExp(self):
        
        input = """class main {
            void foo() {
                int[2] s;
                
                s := {4,5};
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("s"), ArrayType(2,IntType()))
                    ]
                    ,
                    [
                        Assign(Id("s"), ArrayLiteral([IntLiteral(4),IntLiteral(5)]))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,326))

    def testAttrAccessExp(self):
        
        input = """class main {
            void foo() {
                int n;
                Shape s;

                n := s.width;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), IntType()),
                        VarDecl(Id("s"), ClassType(Id("Shape")), NullLiteral())
                    ]
                    ,
                    [
                        Assign(Id("n"), FieldAccess(Id("s"), Id("width")))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,327))

    def testArrayExp(self):
        
        input = """class main {
            void foo() {
                int n;
                int[3] arr = {2,3,4};
                
                n := arr[1];
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), IntType()),
                        VarDecl(Id("arr"), ArrayType(3, IntType()), ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)]))
                    ]
                    ,
                    [
                        Assign(Id("n"), ArrayCell(Id("arr"), IntLiteral(1)))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,328))

    def testUnExp(self):
        
        input = """class main {
            void foo() {
                int n;
                
                n := -5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), IntType())
                    ]
                    ,
                    [
                        Assign(Id("n"), UnaryOp("-",IntLiteral(5)))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,329))

    def testUnExpNot(self):
        
        input = """class main {
            void foo() {
                boolean n;
                
                n := !false;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), BoolType())
                    ]
                    ,
                    [
                        Assign(Id("n"), UnaryOp("!",BooleanLiteral(False)))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,330))

    def testStringLitExp(self):
        
        input = """class main {
            void foo() {
                string n;
                
                n := "abc";
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), StringType())
                    ]
                    ,
                    [
                        Assign(Id("n"), StringLiteral("abc"))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,331))

    def testConcat(self):
        
        input = """class main {
            void foo() {
                string n;
                
                n := "abc" ^ "def";
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), StringType())
                    ]
                    ,
                    [
                        Assign(Id("n"), BinaryOp("^",StringLiteral("abc"),StringLiteral("def")))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,332))

    def testMul(self):
        
        input = """class main {
            void foo() {
                int n;
                
                n := 5*3;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), IntType())
                    ]
                    ,
                    [
                        Assign(Id("n"), BinaryOp("*",IntLiteral(5),IntLiteral(3)))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,333))

    def testAdd(self):
        
        input = """class main {
            void foo() {
                int n;
                
                n := 5+7;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), IntType())
                    ]
                    ,
                    [
                        Assign(Id("n"), BinaryOp("+",IntLiteral(5),IntLiteral(7)))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,334))

    def testAddAssoc(self):
        
        input = """class main {
            void foo() {
                int n;
                
                n := 5+7+9;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), IntType())
                    ]
                    ,
                    [
                        Assign(Id("n"), BinaryOp("+",BinaryOp("+",IntLiteral(5),IntLiteral(7)),IntLiteral(9)))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,335))

    def testFlags(self):
        
        input = """class main {
            void foo() {
                boolean n, flag1 = true, flag2 = false;
                
                
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), BoolType()),
                        VarDecl(Id("flag1"), BoolType(), BooleanLiteral(True)),
                        VarDecl(Id("flag2"), BoolType(), BooleanLiteral(False))
                    ]
                    ,
                    [
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,336))

    def testAnd(self):
        
        input = """class main {
            void foo() {
                boolean n, flag1 = true, flag2 = false;
                
                n := flag1 && flag2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), BoolType()),
                        VarDecl(Id("flag1"), BoolType(), BooleanLiteral(True)),
                        VarDecl(Id("flag2"), BoolType(), BooleanLiteral(False))
                    ]
                    ,
                    [
                        Assign(Id("n"), BinaryOp("&&",Id("flag1"),Id("flag2")))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,337))

    def testNeq(self):
        
        input = """class main {
            void foo() {
                boolean n, flag1 = true, flag2 = false;
                
                n := flag1 != flag2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), BoolType()),
                        VarDecl(Id("flag1"), BoolType(), BooleanLiteral(True)),
                        VarDecl(Id("flag2"), BoolType(), BooleanLiteral(False))
                    ]
                    ,
                    [
                        Assign(Id("n"), BinaryOp("!=",Id("flag1"),Id("flag2")))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,338))

    def testLess(self):
        
        input = """class main {
            void foo() {
                boolean n;
                int n1 = 5, n2 = 8;
                
                n := n1 > n2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), BoolType()),
                        VarDecl(Id("n1"), IntType(), IntLiteral(5)),
                        VarDecl(Id("n2"), IntType(), IntLiteral(8))
                    ]
                    ,
                    [
                        Assign(Id("n"), BinaryOp(">",Id("n1"),Id("n2")))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,339))

    def testInvokeStmt(self):
        
        input = """class main {
            void foo() {
                boolean n;
                Shape s;
                
                s.print();
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), BoolType()),
                        VarDecl(Id("s"), ClassType(Id("Shape")), NullLiteral())
                    ]
                    ,
                    [
                        CallStmt(Id("s"),Id("print"),[])
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,340))

    def testAttrNull(self):
        
        input = """class main {
            Shape s;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(
                    Instance(),VarDecl(Id("s"), ClassType(Id("Shape")), NullLiteral())
                )
            ]
            )]))
        self.assertTrue(TestAST.test(input,expect,341))

    def testCallWithExpr(self):
        
        input = """class main {
            void foo() {
                int[3] s = {2,4,6};
                int index = 2, n = 1;
                
                n := s[index - n];
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("s"), ArrayType(3,IntType()), ArrayLiteral([IntLiteral(2),IntLiteral(4),IntLiteral(6)])),
                        VarDecl(Id("index"), IntType(), IntLiteral(2)),
                        VarDecl(Id("n"), IntType(), IntLiteral(1))
                    ]
                    ,
                    [
                        Assign(Id("n"), ArrayCell(Id("s"),BinaryOp("-",Id("index"),Id("n"))))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,342))

    def testCallWithExpr2(self):
        
        input = """class main {
            void foo() {
                int[3] arr = {2,4,6};
                Shape s = new Shape();
                int n = 1;
                
                n := arr[s.getWidth() - n];
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("arr"), ArrayType(3,IntType()), ArrayLiteral([IntLiteral(2),IntLiteral(4),IntLiteral(6)])),
                        VarDecl(Id("s"), ClassType(Id("Shape")), NewExpr(Id("Shape"),[])),
                        VarDecl(Id("n"), IntType(), IntLiteral(1))
                    ]
                    ,
                    [
                        Assign(Id("n"), ArrayCell(Id("arr"),BinaryOp("-",CallStmt(Id("s"),Id("getWidth"),[]),Id("n"))))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,343))

    def testOrder(self):
        
        input = """class main {
            void foo() {
                int n;
                
                n := 2 - 3*5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), IntType())
                    ]
                    ,
                    [
                        Assign(Id("n"), BinaryOp("-",IntLiteral(2),BinaryOp("*",IntLiteral(3),IntLiteral(5))))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,344))

    def testOrder2(self):
        
        input = """class main {
            void foo() {
                int n;
                
                n := (2 - 3)*5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [MethodDecl(Instance(),Id("foo"),[],VoidType(),
                Block(
                    [
                        VarDecl(Id("n"), IntType())
                    ]
                    ,
                    [
                        Assign(Id("n"), BinaryOp("*",BinaryOp("-",IntLiteral(2),IntLiteral(3)),IntLiteral(5)))
                    ]
                ))])]))
        self.assertTrue(TestAST.test(input,expect,345))

    def testFull(self):
        
        input = """class main extends thing{
            static int count = 5*2;

            int foo(int count) {
                int n;
                
                n := count * 2;
                return n;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                AttributeDecl(Static(),VarDecl(Id("count"), IntType(), BinaryOp("*", IntLiteral(5),IntLiteral(2)))),
                MethodDecl(Instance(),Id("foo"),[VarDecl(Id("count"),IntType())],IntType(),
                    Block(
                        [
                            VarDecl(Id("n"), IntType())
                        ]
                        ,
                        [
                            Assign(Id("n"), BinaryOp("*",Id("count"),IntLiteral(2))),
                            Return(Id("n"))
                        ]
                ))],Id("thing"))]))
        self.assertTrue(TestAST.test(input,expect,346))

    def testFull2(self):
        
        input = """class Circle extends Shape {
            float radius;
            static int count = 0;

            Circle(float r) {
                this.radius := r;
            }

            float getRadius() {
                return this.radius;
            }

            static int getCount() {
                return Circle.count;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Circle"),
            [
                AttributeDecl(Instance(),VarDecl(Id("radius"), FloatType())),
                AttributeDecl(Static(),VarDecl(Id("count"), IntType(), IntLiteral(0))),
                MethodDecl(Instance(), Id("Circle"), [VarDecl(Id("r"),FloatType())], None, 
                    Block([],[
                        Assign(FieldAccess(SelfLiteral(),Id("radius")), Id("r"))
                    ])),
                MethodDecl(Instance(),Id("getRadius"),[],FloatType(),
                    Block(
                        [
                        ]
                        ,
                        [
                            Return(FieldAccess(SelfLiteral(), Id("radius")))
                        ]
                )),
                MethodDecl(Static(),Id("getCount"),[],IntType(),
                    Block(
                        [
                        ]
                        ,
                        [
                            Return(FieldAccess(Id("Circle"), Id("count")))
                        ]
                    ))
            ],Id("Shape"))]))
        self.assertTrue(TestAST.test(input,expect,347))