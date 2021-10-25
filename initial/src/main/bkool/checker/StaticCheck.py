
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
#from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor):

    global_envi = [
        Symbol("getInt",MType([],IntType())),
        Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self, ast):
        self.ast = ast
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)



    def visitProgram(self, ast, refEnv): 
        return [self.visit(x,refEnv) for x in ast.decl]

    def visitClassDecl(self, ast, refEnv): 
        if ast.parentname:
            if ast.parentname.name not in map(lambda x: x.name, refEnv):
                raise Undeclared(Class(), ast.parentname.name)
        return list(map(lambda x: self.visit(x, refEnv),ast.memlist)) 
    

    def visitVarDecl(self, ast, refEnv):
        return None
    
    def visitConstDecl(self, ast, refEnv):
        return None
    
    def visitStatic(self, ast, refEnv):
        return None
    
    def visitInstance(self, ast, refEnv):
        return None
    
    def visitMethodDecl(self, ast, refEnv):
        return None
    
    def visitAttributeDecl(self, ast, refEnv):
        return None
    
    def visitIntType(self, ast, refEnv):
        return None
    
    def visitFloatType(self, ast, refEnv):
        return None
    
    def visitBoolType(self, ast, refEnv):
        return None
    
    def visitStringType(self, ast, refEnv):
        return None
    
    def visitVoidType(self, ast, refEnv):
        return None
    
    def visitArrayType(self, ast, refEnv):
        return None
    
    def visitClassType(self, ast, refEnv):
        return None
    
    def visitBinaryOp(self, ast, refEnv):
        return None
    
    def visitUnaryOp(self, ast, refEnv):
        return None
    
    def visitCallExpr(self, ast, refEnv):
        return None
    
    def visitNewExpr(self, ast, refEnv):
        return None
    
    def visitId(self, ast, refEnv):
        return None
    
    def visitArrayCell(self, ast, refEnv):
        return None
    
    def visitFieldAccess(self, ast, refEnv):
        return None
    
    def visitBlock(self, ast, refEnv):
        return None
    
    def visitIf(self, ast, refEnv):
        return None
    
    def visitFor(self, ast, refEnv):
        return None
    
    def visitContinue(self, ast, refEnv):
        return None
    
    def visitBreak(self, ast, refEnv):
        return None
    
    def visitReturn(self, ast, refEnv):
        return None
    
    def visitAssign(self, ast, refEnv):
        return None
    
    def visitCallStmt(self, ast, refEnv):
        return None
    
    def visitIntLiteral(self, ast, refEnv):
        return None
    
    def visitFloatLiteral(self, ast, refEnv):
        return None
    
    def visitBooleanLiteral(self, ast, refEnv):
        return None
    
    def visitStringLiteral(self, ast, refEnv):
        return None
    
    def visitNullLiteral(self, ast, refEnv):
        return None
    
    def visitSelfLiteral(self, ast, refEnv):
        return None 

    def visitArrayLiteral(self, ast, refEnv):
        return None 
    