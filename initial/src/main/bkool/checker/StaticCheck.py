
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

# ====== GetRefEnv visitor ==================

class GetRefEnv(BaseVisitor):
    def visitProgram(self, ctx, refEnv) -> dict:

        # create new refEnv
        refEnv = {}
        [self.visit(classDecl, refEnv) for classDecl in ctx.decl]

        # FINALLY:
        # add parents' members & methods to this refEnv
        # but this class will override previous declares
        # and if parents aren't declared, raise Undeclared(Class(),...)
        for classDecl in ctx.decl:
            if classDecl.parentname:
                parentName = self.visit(classDecl.parentname, refEnv)

                # check if parent is declared
                if parentName not in refEnv:
                    raise Undeclared(Class(), parentName)

                tempParentEnv = refEnv[parentName].copy()
                tempParentEnv.update(refEnv[parentName])
                refEnv[parentName] = tempParentEnv

        return refEnv

    def visitClassDecl(self, ctx, refEnv):
        
        # new refEnv
        # key = this class' name AS A STRING, NOT AS Id()
        # val = all available IDs in this class
        className = self.visit(ctx.classname, refEnv)
        if className in refEnv:
            raise Redeclared(Class(), className)
        refEnv[className] = {}
        [self.visit(memDecl, refEnv[className]) for memDecl in ctx.memlist]

    def visitAttributeDecl(self, ctx, refEnv):
        kindInsStat = self.visit(ctx.kind, refEnv)
        storeDecl = self.visit(ctx.decl, refEnv)

        if type(storeDecl) is tuple:
            raise Redeclared(Attribute(), storeDecl[1])

    def visitVarDecl(self, ctx, refEnv):
        varName = self.visit(ctx.variable, refEnv)
        
        if varName in refEnv:
            # can't raise, because this must be Attribute() instead
            # just return a flag
            # raise Redeclared(Variable(), varName)
            return ("redeclared", varName)

        refEnv[varName] = ctx.varType

    def visitConstDecl(self, ctx, refEnv):
        constName = self.visit(ctx.constant, refEnv)

        if constName in refEnv:
            # can't raise, because this must be Attribute() instead
            # just return a flag
            # raise Redeclared(Constant(), constName)
            return ("redeclared", constName)

        refEnv[constName] = ctx.constType

    # def visitFuncDecl(self, ctx, refEnv):
    #     if ctx.name in refEnv:
    #         raise Redeclared(ctx.name)
            
    #     refEnv[ctx.name] = {}


    def visitId(self, ctx, refEnv) -> str:
        return ctx.name


    def visitIntType(self, ctx, refEnv) -> IntType:
        return ctx
    
    def visitFloatType(self, ctx, refEnv) -> FloatType:
        return ctx
    
    def visitBoolType(self, ctx, refEnv) -> BoolType:
        return ctx
    
    def visitStringType(self, ctx, refEnv) -> StringType:
        return ctx
    
    def visitVoidType(self, ctx, refEnv) -> VoidType:
        return ctx
    
    def visitArrayType(self, ctx, refEnv) -> ArrayType:
        size = ctx.size
        eleType = self.visit(ctx.eleType, refEnv)
        return ArrayType(size, eleType)
    
    def visitClassType(self, ctx, refEnv) -> ClassType:
        className = self.visit(ctx.classname, refEnv)
        return ClassType(className)


# ===============================================

class StaticChecker(BaseVisitor):

    global_envi = [
        Symbol("getInt",MType([],IntType())),
        Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self, ctx):
        self.ctx = ctx
    
    def check(self):
        return self.visit(self.ctx,StaticChecker.global_envi)

    # =============================================================

    def visitProgram(self, ctx, refEnv): 
        
        # Get all class names and their own refEnv
        # with attributes and methods inside
        refEnv = GetRefEnv().visit(ctx, None)

        print("refEnv = %s\n" % refEnv)

        # return [self.visit(classDecl,refEnv) for classDecl in ctx.decl]


    # ---- Classes ------

    def visitClassDecl(self, ctx, refEnv): 
        # if ctx.parentname:
        #     if ctx.parentname.name not in map(lambda x: x.name, refEnv):
        #         raise Undeclared(Class(), ctx.parentname.name)
        # return list(map(lambda x: self.visit(x, refEnv),ctx.memlist)) 
        if ctx.parentname:
            for className in refEnv:
                if ctx.parentname.name != className:
                    raise Undeclared(Class(), ctx.parentname.name)

    def visitMethodDecl(self, ctx, refEnv):
        return None
    
    def visitAttributeDecl(self, ctx, refEnv):
        return None

    def visitVarDecl(self, ctx, refEnv):
        return None
    
    def visitConstDecl(self, ctx, refEnv):
        return None
    
    def visitStatic(self, ctx, refEnv):
        return None
    
    def visitInstance(self, ctx, refEnv):
        return None
    

    # ---- Type -----
    
    def visitIntType(self, ctx, refEnv):
        return None
    
    def visitFloatType(self, ctx, refEnv):
        return None
    
    def visitBoolType(self, ctx, refEnv):
        return None
    
    def visitStringType(self, ctx, refEnv):
        return None
    
    def visitVoidType(self, ctx, refEnv):
        return None
    
    def visitArrayType(self, ctx, refEnv):
        return None
    
    def visitClassType(self, ctx, refEnv):
        return None
    

    # ---- Expression -----

    def visitBinaryOp(self, ctx, refEnv):
        return None
    
    def visitUnaryOp(self, ctx, refEnv):
        return None
    
    def visitCallExpr(self, ctx, refEnv):
        return None
    
    def visitNewExpr(self, ctx, refEnv):
        return None
    
    def visitId(self, ctx, refEnv):
        return None
    
    def visitArrayCell(self, ctx, refEnv):
        return None
    
    def visitFieldAccess(self, ctx, refEnv):
        return None

    
    # ---- Stmt -----

    def visitBlock(self, ctx, refEnv):
        return None
    
    def visitIf(self, ctx, refEnv):
        return None
    
    def visitFor(self, ctx, refEnv):
        return None
    
    def visitContinue(self, ctx, refEnv):
        return None
    
    def visitBreak(self, ctx, refEnv):
        return None
    
    def visitReturn(self, ctx, refEnv):
        return None
    
    def visitAssign(self, ctx, refEnv):
        return None
    
    def visitCallStmt(self, ctx, refEnv):
        return None
    

    # --- Literal -----

    def visitIntLiteral(self, ctx, refEnv):
        return None
    
    def visitFloatLiteral(self, ctx, refEnv):
        return None
    
    def visitBooleanLiteral(self, ctx, refEnv):
        return None
    
    def visitStringLiteral(self, ctx, refEnv):
        return None
    
    def visitNullLiteral(self, ctx, refEnv):
        return None
    
    def visitSelfLiteral(self, ctx, refEnv):
        return None 

    def visitArrayLiteral(self, ctx, refEnv):
        return None 
    