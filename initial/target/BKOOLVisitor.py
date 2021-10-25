# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classDeclList.
    def visitClassDeclList(self, ctx:BKOOLParser.ClassDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classDecl.
    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#memberList.
    def visitMemberList(self, ctx:BKOOLParser.MemberListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member.
    def visitMember(self, ctx:BKOOLParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrKeyword.
    def visitAttrKeyword(self, ctx:BKOOLParser.AttrKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrType.
    def visitAttrType(self, ctx:BKOOLParser.AttrTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayType.
    def visitArrayType(self, ctx:BKOOLParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrList.
    def visitAttrList(self, ctx:BKOOLParser.AttrListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute.
    def visitAttribute(self, ctx:BKOOLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnType.
    def visitReturnType(self, ctx:BKOOLParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method.
    def visitMethod(self, ctx:BKOOLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor.
    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramList.
    def visitParamList(self, ctx:BKOOLParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idList.
    def visitIdList(self, ctx:BKOOLParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayLit.
    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#litList.
    def visitLitList(self, ctx:BKOOLParser.LitListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#argList.
    def visitArgList(self, ctx:BKOOLParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#obj_create.
    def visitObj_create(self, ctx:BKOOLParser.Obj_createContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtList.
    def visitStmtList(self, ctx:BKOOLParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockStmt.
    def visitBlockStmt(self, ctx:BKOOLParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockBody.
    def visitBlockBody(self, ctx:BKOOLParser.BlockBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#declList.
    def visitDeclList(self, ctx:BKOOLParser.DeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl.
    def visitDecl(self, ctx:BKOOLParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignStmt.
    def visitAssignStmt(self, ctx:BKOOLParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifStmt.
    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forStmt.
    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scalarVar.
    def visitScalarVar(self, ctx:BKOOLParser.ScalarVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#breakStmt.
    def visitBreakStmt(self, ctx:BKOOLParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continueStmt.
    def visitContinueStmt(self, ctx:BKOOLParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnStmt.
    def visitReturnStmt(self, ctx:BKOOLParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodInvokeStmt.
    def visitMethodInvokeStmt(self, ctx:BKOOLParser.MethodInvokeStmtContext):
        return self.visitChildren(ctx)



del BKOOLParser