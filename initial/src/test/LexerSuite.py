import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_varDecl(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("int a;","int,a,;,<EOF>",101))

    def test_separators(self):
        self.assertTrue(TestLexer.test("""{(]
            }""","{,(,],},<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.test("ab~svn","ab,Error Token ~",103))

    def test_string(self):
        self.assertTrue(TestLexer.test("""string a := "t\thing";""", """string,a,:=,"t\thing",;,<EOF>""", 104))

    def test_dubQuotesString(self):
        # \" -> \\"
        # because in a string, \ can only show as \\
        self.assertTrue(TestLexer.test(""" "some\\"thing" """,""""some\\"thing",<EOF>""",105))

    def test_class(self):
        self.assertTrue(TestLexer.test("""class abc {}""","class,abc,{,},<EOF>", 106))

    def test_extClass(self):
        self.assertTrue(TestLexer.test("""class Bird extends Animal {}""","class,Bird,extends,Animal,{,},<EOF>",107))

    def test_wrongClass(self):
        self.assertTrue(TestLexer.test("classs abc {}","classs,abc,{,},<EOF>",108))

    def test_lineComment(self):
        self.assertTrue(TestLexer.test("#line comment!!","<EOF>",109))

    def test_blockComment(self):
        self.assertTrue(TestLexer.test("/*block comment on 1 line!!*/int a","int,a,<EOF>",110))

    def test_blockCommentMul(self):
        self.assertTrue(TestLexer.test("""/* multiline block\ncomment!!*/""","<EOF>", 111))

    def test_unclosedString(self):
        self.assertTrue(TestLexer.test(""" "abc""","""Unclosed String: abc""", 112))

    # def test_illegalEscapedString(self):
    #     self.assertTrue(TestLexer.test(""" "sss\z" ""","""Illegal Escape In String: sss""",113))
    #     # WRONG!!!!!!!!!

    # def test_ArrayLit(self):
    #     self.assertTrue(TestLexer.test("{1,5}","{1,5},<EOF>",113))

    def test_class2(self):
        self.assertTrue(TestLexer.test("class A {}", "class,A,{,},<EOF>",114))
    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.test("Var x;","Var,x,;,<EOF>",104))

    # def test_illegal_escape(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.test(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    # def test_unterminated_string(self):
    #     """test unclosed string"""
    #     self.assertTrue(TestLexer.test(""" "abc def  ""","""Unclosed String: abc def  """,106))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.test(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

