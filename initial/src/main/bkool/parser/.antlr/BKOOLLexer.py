# Generated from e:\Study\Sem7\PPL\Assignment\A2\Second try\initial\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01dd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5\u00a2\n\5\f")
        buf.write("\5\16\5\u00a5\13\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\7\6\u00ae")
        buf.write("\n\6\f\6\16\6\u00b1\13\6\3\6\5\6\u00b4\n\6\3\6\3\6\3\7")
        buf.write("\6\7\u00b9\n\7\r\7\16\7\u00ba\3\b\6\b\u00be\n\b\r\b\16")
        buf.write("\b\u00bf\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\u00c9\n\t\3\n")
        buf.write("\3\n\7\n\u00cd\n\n\f\n\16\n\u00d0\13\n\3\13\3\13\5\13")
        buf.write("\u00d4\n\13\3\13\6\13\u00d7\n\13\r\13\16\13\u00d8\3\f")
        buf.write("\3\f\3\r\3\r\5\r\u00df\n\r\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u00ea\n\20\3\21\3\21\7\21\u00ee")
        buf.write("\n\21\f\21\16\21\u00f1\13\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)")
        buf.write("\3)\3)\3)\3)\3)\3*\3*\5*\u017d\n*\3*\3*\3*\7*\u0182\n")
        buf.write("*\f*\16*\u0185\13*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\39\3")
        buf.write("9\39\3:\3:\3;\3;\3<\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3")
        buf.write("A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3H\3I\3I\7")
        buf.write("I\u01cd\nI\fI\16I\u01d0\13I\3I\3I\3J\3J\7J\u01d6\nJ\f")
        buf.write("J\16J\u01d9\13J\3J\3J\3J\4\u00a3\u00af\2K\3\2\5\2\7\3")
        buf.write("\t\4\13\5\r\6\17\7\21\2\23\2\25\2\27\2\31\b\33\2\35\2")
        buf.write("\37\2!\t#\n%\13\'\f)\r+\16-\17/\20\61\21\63\22\65\23\67")
        buf.write("\249\25;\26=\27?\30A\31C\32E\33G\34I\35K\36M\37O Q!S\"")
        buf.write("U\2W#Y$[%]&_\'a(c)e*g+i,k-m.o/q\60s\61u\62w\63y\64{\65")
        buf.write("}\66\177\67\u00818\u00839\u0085:\u0087;\u0089<\u008b=")
        buf.write("\u008d>\u008f?\u0091@\u0093A\3\2\13\3\2\62;\4\2C\\c|\5")
        buf.write("\2\13\f\16\17\"\"\3\3\f\f\4\2GGgg\4\2--//\5\2\n\13\16")
        buf.write("\17^^\b\2$$^^ddhhttvv\4\2\f\f$$\2\u01e5\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\3\u0095\3\2\2\2\5\u0097\3\2\2\2\7\u0099\3\2\2\2\t\u009d")
        buf.write("\3\2\2\2\13\u00ab\3\2\2\2\r\u00b8\3\2\2\2\17\u00bd\3\2")
        buf.write("\2\2\21\u00c8\3\2\2\2\23\u00ca\3\2\2\2\25\u00d1\3\2\2")
        buf.write("\2\27\u00da\3\2\2\2\31\u00de\3\2\2\2\33\u00e0\3\2\2\2")
        buf.write("\35\u00e2\3\2\2\2\37\u00e9\3\2\2\2!\u00eb\3\2\2\2#\u00f5")
        buf.write("\3\2\2\2%\u00fd\3\2\2\2\'\u0103\3\2\2\2)\u0109\3\2\2\2")
        buf.write("+\u0112\3\2\2\2-\u0115\3\2\2\2/\u011a\3\2\2\2\61\u0122")
        buf.write("\3\2\2\2\63\u0128\3\2\2\2\65\u012b\3\2\2\2\67\u012f\3")
        buf.write("\2\2\29\u0133\3\2\2\2;\u013a\3\2\2\2=\u013f\3\2\2\2?\u0143")
        buf.write("\3\2\2\2A\u014a\3\2\2\2C\u014f\3\2\2\2E\u0155\3\2\2\2")
        buf.write("G\u015a\3\2\2\2I\u015e\3\2\2\2K\u0163\3\2\2\2M\u0169\3")
        buf.write("\2\2\2O\u0170\3\2\2\2Q\u0173\3\2\2\2S\u017c\3\2\2\2U\u0186")
        buf.write("\3\2\2\2W\u0188\3\2\2\2Y\u018a\3\2\2\2[\u018c\3\2\2\2")
        buf.write("]\u018e\3\2\2\2_\u0190\3\2\2\2a\u0192\3\2\2\2c\u0194\3")
        buf.write("\2\2\2e\u0197\3\2\2\2g\u019a\3\2\2\2i\u019c\3\2\2\2k\u019e")
        buf.write("\3\2\2\2m\u01a1\3\2\2\2o\u01a4\3\2\2\2q\u01a7\3\2\2\2")
        buf.write("s\u01aa\3\2\2\2u\u01ac\3\2\2\2w\u01ae\3\2\2\2y\u01b1\3")
        buf.write("\2\2\2{\u01b3\3\2\2\2}\u01b5\3\2\2\2\177\u01b7\3\2\2\2")
        buf.write("\u0081\u01b9\3\2\2\2\u0083\u01bb\3\2\2\2\u0085\u01bd\3")
        buf.write("\2\2\2\u0087\u01bf\3\2\2\2\u0089\u01c1\3\2\2\2\u008b\u01c3")
        buf.write("\3\2\2\2\u008d\u01c5\3\2\2\2\u008f\u01c7\3\2\2\2\u0091")
        buf.write("\u01ca\3\2\2\2\u0093\u01d3\3\2\2\2\u0095\u0096\t\2\2\2")
        buf.write("\u0096\4\3\2\2\2\u0097\u0098\t\3\2\2\u0098\6\3\2\2\2\u0099")
        buf.write("\u009a\t\4\2\2\u009a\u009b\3\2\2\2\u009b\u009c\b\4\2\2")
        buf.write("\u009c\b\3\2\2\2\u009d\u009e\7\61\2\2\u009e\u009f\7,\2")
        buf.write("\2\u009f\u00a3\3\2\2\2\u00a0\u00a2\13\2\2\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a6\u00a7\7,\2\2\u00a7\u00a8\7\61\2\2\u00a8\u00a9\3")
        buf.write("\2\2\2\u00a9\u00aa\b\5\2\2\u00aa\n\3\2\2\2\u00ab\u00af")
        buf.write("\7%\2\2\u00ac\u00ae\13\2\2\2\u00ad\u00ac\3\2\2\2\u00ae")
        buf.write("\u00b1\3\2\2\2\u00af\u00b0\3\2\2\2\u00af\u00ad\3\2\2\2")
        buf.write("\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b4\t")
        buf.write("\5\2\2\u00b3\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6")
        buf.write("\b\6\2\2\u00b6\f\3\2\2\2\u00b7\u00b9\5\3\2\2\u00b8\u00b7")
        buf.write("\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\16\3\2\2\2\u00bc\u00be\5\3\2\2\u00bd")
        buf.write("\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00bf\u00c0\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\5")
        buf.write("\21\t\2\u00c2\20\3\2\2\2\u00c3\u00c4\5\23\n\2\u00c4\u00c5")
        buf.write("\5\25\13\2\u00c5\u00c9\3\2\2\2\u00c6\u00c9\5\23\n\2\u00c7")
        buf.write("\u00c9\5\25\13\2\u00c8\u00c3\3\2\2\2\u00c8\u00c6\3\2\2")
        buf.write("\2\u00c8\u00c7\3\2\2\2\u00c9\22\3\2\2\2\u00ca\u00ce\5")
        buf.write("\u008bF\2\u00cb\u00cd\5\3\2\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write("\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\24\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d3\t\6")
        buf.write("\2\2\u00d2\u00d4\5\27\f\2\u00d3\u00d2\3\2\2\2\u00d3\u00d4")
        buf.write("\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00d7\5\3\2\2\u00d6")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6\3\2\2\2")
        buf.write("\u00d8\u00d9\3\2\2\2\u00d9\26\3\2\2\2\u00da\u00db\t\7")
        buf.write("\2\2\u00db\30\3\2\2\2\u00dc\u00df\5A!\2\u00dd\u00df\5")
        buf.write("C\"\2\u00de\u00dc\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\32")
        buf.write("\3\2\2\2\u00e0\u00e1\t\b\2\2\u00e1\34\3\2\2\2\u00e2\u00e3")
        buf.write("\7^\2\2\u00e3\u00e4\n\t\2\2\u00e4\36\3\2\2\2\u00e5\u00ea")
        buf.write("\n\n\2\2\u00e6\u00ea\5\33\16\2\u00e7\u00e8\7^\2\2\u00e8")
        buf.write("\u00ea\7$\2\2\u00e9\u00e5\3\2\2\2\u00e9\u00e6\3\2\2\2")
        buf.write("\u00e9\u00e7\3\2\2\2\u00ea \3\2\2\2\u00eb\u00ef\7$\2\2")
        buf.write("\u00ec\u00ee\5\37\20\2\u00ed\u00ec\3\2\2\2\u00ee\u00f1")
        buf.write("\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\u00f2\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7$\2\2")
        buf.write("\u00f3\u00f4\b\21\3\2\u00f4\"\3\2\2\2\u00f5\u00f6\7d\2")
        buf.write("\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7")
        buf.write("n\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7p\2\2\u00fc$\3\2\2\2\u00fd\u00fe\7d\2\2\u00fe\u00ff")
        buf.write("\7t\2\2\u00ff\u0100\7g\2\2\u0100\u0101\7c\2\2\u0101\u0102")
        buf.write("\7m\2\2\u0102&\3\2\2\2\u0103\u0104\7e\2\2\u0104\u0105")
        buf.write("\7n\2\2\u0105\u0106\7c\2\2\u0106\u0107\7u\2\2\u0107\u0108")
        buf.write("\7u\2\2\u0108(\3\2\2\2\u0109\u010a\7e\2\2\u010a\u010b")
        buf.write("\7q\2\2\u010b\u010c\7p\2\2\u010c\u010d\7v\2\2\u010d\u010e")
        buf.write("\7k\2\2\u010e\u010f\7p\2\2\u010f\u0110\7w\2\2\u0110\u0111")
        buf.write("\7g\2\2\u0111*\3\2\2\2\u0112\u0113\7f\2\2\u0113\u0114")
        buf.write("\7q\2\2\u0114,\3\2\2\2\u0115\u0116\7g\2\2\u0116\u0117")
        buf.write("\7n\2\2\u0117\u0118\7u\2\2\u0118\u0119\7g\2\2\u0119.\3")
        buf.write("\2\2\2\u011a\u011b\7g\2\2\u011b\u011c\7z\2\2\u011c\u011d")
        buf.write("\7v\2\2\u011d\u011e\7g\2\2\u011e\u011f\7p\2\2\u011f\u0120")
        buf.write("\7f\2\2\u0120\u0121\7u\2\2\u0121\60\3\2\2\2\u0122\u0123")
        buf.write("\7h\2\2\u0123\u0124\7n\2\2\u0124\u0125\7q\2\2\u0125\u0126")
        buf.write("\7c\2\2\u0126\u0127\7v\2\2\u0127\62\3\2\2\2\u0128\u0129")
        buf.write("\7k\2\2\u0129\u012a\7h\2\2\u012a\64\3\2\2\2\u012b\u012c")
        buf.write("\7k\2\2\u012c\u012d\7p\2\2\u012d\u012e\7v\2\2\u012e\66")
        buf.write("\3\2\2\2\u012f\u0130\7p\2\2\u0130\u0131\7g\2\2\u0131\u0132")
        buf.write("\7y\2\2\u01328\3\2\2\2\u0133\u0134\7u\2\2\u0134\u0135")
        buf.write("\7v\2\2\u0135\u0136\7t\2\2\u0136\u0137\7k\2\2\u0137\u0138")
        buf.write("\7p\2\2\u0138\u0139\7i\2\2\u0139:\3\2\2\2\u013a\u013b")
        buf.write("\7v\2\2\u013b\u013c\7j\2\2\u013c\u013d\7g\2\2\u013d\u013e")
        buf.write("\7p\2\2\u013e<\3\2\2\2\u013f\u0140\7h\2\2\u0140\u0141")
        buf.write("\7q\2\2\u0141\u0142\7t\2\2\u0142>\3\2\2\2\u0143\u0144")
        buf.write("\7t\2\2\u0144\u0145\7g\2\2\u0145\u0146\7v\2\2\u0146\u0147")
        buf.write("\7w\2\2\u0147\u0148\7t\2\2\u0148\u0149\7p\2\2\u0149@\3")
        buf.write("\2\2\2\u014a\u014b\7v\2\2\u014b\u014c\7t\2\2\u014c\u014d")
        buf.write("\7w\2\2\u014d\u014e\7g\2\2\u014eB\3\2\2\2\u014f\u0150")
        buf.write("\7h\2\2\u0150\u0151\7c\2\2\u0151\u0152\7n\2\2\u0152\u0153")
        buf.write("\7u\2\2\u0153\u0154\7g\2\2\u0154D\3\2\2\2\u0155\u0156")
        buf.write("\7x\2\2\u0156\u0157\7q\2\2\u0157\u0158\7k\2\2\u0158\u0159")
        buf.write("\7f\2\2\u0159F\3\2\2\2\u015a\u015b\7p\2\2\u015b\u015c")
        buf.write("\7k\2\2\u015c\u015d\7n\2\2\u015dH\3\2\2\2\u015e\u015f")
        buf.write("\7v\2\2\u015f\u0160\7j\2\2\u0160\u0161\7k\2\2\u0161\u0162")
        buf.write("\7u\2\2\u0162J\3\2\2\2\u0163\u0164\7h\2\2\u0164\u0165")
        buf.write("\7k\2\2\u0165\u0166\7p\2\2\u0166\u0167\7c\2\2\u0167\u0168")
        buf.write("\7n\2\2\u0168L\3\2\2\2\u0169\u016a\7u\2\2\u016a\u016b")
        buf.write("\7v\2\2\u016b\u016c\7c\2\2\u016c\u016d\7v\2\2\u016d\u016e")
        buf.write("\7k\2\2\u016e\u016f\7e\2\2\u016fN\3\2\2\2\u0170\u0171")
        buf.write("\7v\2\2\u0171\u0172\7q\2\2\u0172P\3\2\2\2\u0173\u0174")
        buf.write("\7f\2\2\u0174\u0175\7q\2\2\u0175\u0176\7y\2\2\u0176\u0177")
        buf.write("\7p\2\2\u0177\u0178\7v\2\2\u0178\u0179\7q\2\2\u0179R\3")
        buf.write("\2\2\2\u017a\u017d\5\5\3\2\u017b\u017d\5U+\2\u017c\u017a")
        buf.write("\3\2\2\2\u017c\u017b\3\2\2\2\u017d\u0183\3\2\2\2\u017e")
        buf.write("\u0182\5\5\3\2\u017f\u0182\5\3\2\2\u0180\u0182\5U+\2\u0181")
        buf.write("\u017e\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0180\3\2\2\2")
        buf.write("\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3")
        buf.write("\2\2\2\u0184T\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0187")
        buf.write("\7a\2\2\u0187V\3\2\2\2\u0188\u0189\7-\2\2\u0189X\3\2\2")
        buf.write("\2\u018a\u018b\7/\2\2\u018bZ\3\2\2\2\u018c\u018d\7,\2")
        buf.write("\2\u018d\\\3\2\2\2\u018e\u018f\7)\2\2\u018f^\3\2\2\2\u0190")
        buf.write("\u0191\7\61\2\2\u0191`\3\2\2\2\u0192\u0193\7\'\2\2\u0193")
        buf.write("b\3\2\2\2\u0194\u0195\7#\2\2\u0195\u0196\7?\2\2\u0196")
        buf.write("d\3\2\2\2\u0197\u0198\7?\2\2\u0198\u0199\7?\2\2\u0199")
        buf.write("f\3\2\2\2\u019a\u019b\7>\2\2\u019bh\3\2\2\2\u019c\u019d")
        buf.write("\7@\2\2\u019dj\3\2\2\2\u019e\u019f\7>\2\2\u019f\u01a0")
        buf.write("\7?\2\2\u01a0l\3\2\2\2\u01a1\u01a2\7@\2\2\u01a2\u01a3")
        buf.write("\7?\2\2\u01a3n\3\2\2\2\u01a4\u01a5\7~\2\2\u01a5\u01a6")
        buf.write("\7~\2\2\u01a6p\3\2\2\2\u01a7\u01a8\7(\2\2\u01a8\u01a9")
        buf.write("\7(\2\2\u01a9r\3\2\2\2\u01aa\u01ab\7#\2\2\u01abt\3\2\2")
        buf.write("\2\u01ac\u01ad\7`\2\2\u01adv\3\2\2\2\u01ae\u01af\7<\2")
        buf.write("\2\u01af\u01b0\7?\2\2\u01b0x\3\2\2\2\u01b1\u01b2\7?\2")
        buf.write("\2\u01b2z\3\2\2\2\u01b3\u01b4\7}\2\2\u01b4|\3\2\2\2\u01b5")
        buf.write("\u01b6\7\177\2\2\u01b6~\3\2\2\2\u01b7\u01b8\7*\2\2\u01b8")
        buf.write("\u0080\3\2\2\2\u01b9\u01ba\7+\2\2\u01ba\u0082\3\2\2\2")
        buf.write("\u01bb\u01bc\7]\2\2\u01bc\u0084\3\2\2\2\u01bd\u01be\7")
        buf.write("_\2\2\u01be\u0086\3\2\2\2\u01bf\u01c0\7=\2\2\u01c0\u0088")
        buf.write("\3\2\2\2\u01c1\u01c2\7<\2\2\u01c2\u008a\3\2\2\2\u01c3")
        buf.write("\u01c4\7\60\2\2\u01c4\u008c\3\2\2\2\u01c5\u01c6\7.\2\2")
        buf.write("\u01c6\u008e\3\2\2\2\u01c7\u01c8\13\2\2\2\u01c8\u01c9")
        buf.write("\bH\4\2\u01c9\u0090\3\2\2\2\u01ca\u01ce\7$\2\2\u01cb\u01cd")
        buf.write("\5\37\20\2\u01cc\u01cb\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d1\3\2\2\2")
        buf.write("\u01d0\u01ce\3\2\2\2\u01d1\u01d2\bI\5\2\u01d2\u0092\3")
        buf.write("\2\2\2\u01d3\u01d7\7$\2\2\u01d4\u01d6\5\37\20\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9\u01d7\3")
        buf.write("\2\2\2\u01da\u01db\5\35\17\2\u01db\u01dc\bJ\6\2\u01dc")
        buf.write("\u0094\3\2\2\2\24\2\u00a3\u00af\u00b3\u00ba\u00bf\u00c8")
        buf.write("\u00ce\u00d3\u00d8\u00de\u00e9\u00ef\u017c\u0181\u0183")
        buf.write("\u01ce\u01d7\7\b\2\2\3\21\2\3H\3\3I\4\3J\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    BLOCK_CMT = 2
    LINE_CMT = 3
    INTLIT = 4
    FLOATLIT = 5
    BOOLLIT = 6
    STRINGLIT = 7
    BOOLEAN = 8
    BREAK = 9
    CLASS = 10
    CONTINUE = 11
    DO = 12
    ELSE = 13
    EXTENDS = 14
    FLOAT = 15
    IF = 16
    INT = 17
    NEW = 18
    STRING = 19
    THEN = 20
    FOR = 21
    RETURN = 22
    TRUE = 23
    FALSE = 24
    VOID = 25
    NIL = 26
    THIS = 27
    FINAL = 28
    STATIC = 29
    TO = 30
    DOWNTO = 31
    ID = 32
    ADD = 33
    SUB = 34
    MUL = 35
    DIV = 36
    DIVF = 37
    MOD = 38
    NEQ = 39
    EQ = 40
    LESS = 41
    GREATER = 42
    LEQ = 43
    GREQ = 44
    OR = 45
    AND = 46
    NOT = 47
    CONCAT = 48
    ASSIGN = 49
    INIT = 50
    LP = 51
    RP = 52
    LB = 53
    RB = 54
    LQ = 55
    RQ = 56
    SEMI = 57
    COLON = 58
    DOT = 59
    COMMA = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'else'", 
            "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
            "'then'", "'for'", "'return'", "'true'", "'false'", "'void'", 
            "'nil'", "'this'", "'final'", "'static'", "'to'", "'downto'", 
            "'+'", "'-'", "'*'", "'''", "'/'", "'%'", "'!='", "'=='", "'<'", 
            "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "':='", 
            "'='", "'{'", "'}'", "'('", "')'", "'['", "']'", "';'", "':'", 
            "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "WS", "BLOCK_CMT", "LINE_CMT", "INTLIT", "FLOATLIT", "BOOLLIT", 
            "STRINGLIT", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", 
            "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", 
            "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", 
            "STATIC", "TO", "DOWNTO", "ID", "ADD", "SUB", "MUL", "DIV", 
            "DIVF", "MOD", "NEQ", "EQ", "LESS", "GREATER", "LEQ", "GREQ", 
            "OR", "AND", "NOT", "CONCAT", "ASSIGN", "INIT", "LP", "RP", 
            "LB", "RB", "LQ", "RQ", "SEMI", "COLON", "DOT", "COMMA", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "DIGIT", "CHAR", "WS", "BLOCK_CMT", "LINE_CMT", "INTLIT", 
                  "FLOATLIT", "FLOAT_END", "DECPART", "EXPPART", "SIGN", 
                  "BOOLLIT", "ESCAPE", "ILLEGAL_ESC", "CHARS", "STRINGLIT", 
                  "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", 
                  "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", 
                  "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
                  "FINAL", "STATIC", "TO", "DOWNTO", "ID", "UNDERSCORE", 
                  "ADD", "SUB", "MUL", "DIV", "DIVF", "MOD", "NEQ", "EQ", 
                  "LESS", "GREATER", "LEQ", "GREQ", "OR", "AND", "NOT", 
                  "CONCAT", "ASSIGN", "INIT", "LP", "RP", "LB", "RB", "LQ", 
                  "RQ", "SEMI", "COLON", "DOT", "COMMA", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[15] = self.STRINGLIT_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    # self.text = (str(self.text))[1:-1]
                    pass
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[1:])

     


