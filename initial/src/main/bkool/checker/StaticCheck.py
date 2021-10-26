
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

# ====== Helper functions ===================

def getObjValue(obj) -> str:
    #if type(obj) in [IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral, ArrayLiteral]:
    if isinstance(obj, Expr):
        return str(obj)

def getObjName(obj) -> str:
    if obj is None:
        return "None"
    return str(obj)
    #return type(obj).__name__ + "(" + str(obj) + ")"

def printDict(refEnv: dict, spaces: int, isStatic: bool):

    quotes = "'" if isStatic else ""
    for key in refEnv:
        if type(refEnv[key]) is not dict:
            line = " "*spaces + quotes + ("%s%s: %s" % (key, quotes, getObjName(refEnv[key])))
            print(line)
        else:
            line = " "*spaces + quotes + ("%s%s: {" % (key, quotes))
            print(line)
            printDict(refEnv[key], spaces + 4, isStatic)
            print(" "*spaces + "}")


# ====== GetRefEnv visitor ==================


# Get environment of class + attr + method declarations
# and also catch some Redeclared/Undeclared
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
                className = classDecl.classname.name
                parentName = classDecl.parentname.name

                # check if parent is declared
                if parentName not in refEnv:
                    raise Undeclared(Class(), parentName)

                tempParentEnv = refEnv[parentName].copy()
                tempParentEnv.update(refEnv[className])
                refEnv[className] = tempParentEnv

        print("\n\nin GetRefEnv, refEnv = ")
        printDict(refEnv, 4, False)

        return refEnv

    def visitClassDecl(self, ctx, refEnv):
        
        # new refEnv
        # key = this class' name AS A STRING, NOT AS Id()
        # val = all available IDs in this class
        className = ctx.classname.name
        if className in refEnv:
            raise Redeclared(Class(), className)
        refEnv[className] = {}
        [self.visit(memDecl, refEnv[className]) for memDecl in ctx.memlist]

    def visitAttributeDecl(self, ctx, refEnv):
        kind = ctx.kind
        storeDecl = self.visit(ctx.decl, refEnv)

        if type(storeDecl) is str:
            raise Redeclared(Attribute(), storeDecl)
        else:
            # storeDecl is tuple of (name, type)

            if type(storeDecl) is ConstDecl and storeDecl[2] is None:
                raise IllegalConstantExpression(None)

            refEnv[storeDecl[0]] = {
                'type': storeDecl[1],
                'kind': kind
                #'init': storeDecl[2]
            }

    def visitVarDecl(self, ctx, refEnv):
        varName = ctx.variable.name
        varType = ctx.varType
        varInit = ctx.varInit
        
        if varName in refEnv:
            # can't raise, because this must be Attribute() instead
            # just return a flag
            # raise Redeclared(Variable(), varName)
            return varName

        return (varName, varType, varInit)

        

    def visitConstDecl(self, ctx, refEnv):
        constName = ctx.constant.name
        constType = ctx.constType
        constInit = ctx.value

        if constName in refEnv:
            # can't raise, because this must be Attribute() instead
            # just return a flag
            # raise Redeclared(Constant(), constName)
            return constName

        return (constName, constType, constInit)

        

    def visitMethodDecl(self, ctx, refEnv):
        methodName = ctx.name.name
        methodKind = ctx.kind
        methodReturnType = ctx.returnType

        if methodName in refEnv:
            raise Redeclared(Method(), methodName)
        
        refEnv[methodName] = {
            'returnType': methodReturnType,
            'kind': methodKind
        }



# ===============================================

class StaticChecker(BaseVisitor):

    global_envi = [
        Symbol("getInt",MType([],IntType())),
        Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self, ctx):
        self.ctx = ctx
    
    def check(self):
        return self.visit(self.ctx, StaticChecker.global_envi)

    # =============================================================

    def visitProgram(self, ctx, refEnv): 
        
        # Get all class names and their own refEnv
        # with attributes and methods inside
        refEnv = GetRefEnv().visit(ctx, None)

        # print("\nrefEnv = ")
        # printDict(refEnv, 4)

        print("\nin StaticChecker")

        [self.visit(classDecl, refEnv) for classDecl in ctx.decl]

        


    # ---- Classes ------

    def visitClassDecl(self, ctx, refEnv): 
        # if ctx.parentname:
        #     if ctx.parentname.name not in map(lambda x: x.name, refEnv):
        #         raise Undeclared(Class(), ctx.parentname.name)
        # return list(map(lambda x: self.visit(x, refEnv),ctx.memlist)) 

        # if ctx.parentname:
        #     for className in refEnv:
        #         if ctx.parentname.name != className:
        #             raise Undeclared(Class(), ctx.parentname.name)

        
        # No need to do all that!
        clsRefEnv = {
            'current': ctx.classname,
            'global': refEnv
        }

        print(" "*4 + "clsRefEnv: ")
        printDict(clsRefEnv, 8, True)

        [self.visit(memDecl, clsRefEnv) for memDecl in ctx.memlist]


    def visitMethodDecl(self, ctx, refEnv):

        mthdRefEnv = {
            'current': refEnv['current'],
            'global': refEnv['global'],
            'local': {}
        }

        # visit param: List[VarDecl]
        for param in ctx.param:
            self.visit(param, mthdRefEnv['local'])

        print(" "*8 + "mthdRefEnv: ")
        printDict(mthdRefEnv, 12, True)

        #[GetRefEnv().visit(ctx.)]
        return None
    
    def visitAttributeDecl(self, ctx, refEnv):
        self.visit(ctx.decl, refEnv)
        return None

    def visitVarDecl(self, ctx, refEnv):
        varName = ctx.variable.name     # string
        varType = ctx.varType           # Type
        varInit = self.visit(ctx.varInit, refEnv) if ctx.varInit else None

        if varName in refEnv:
            raise Redeclared(Variable(), varName)
        else:
            refEnv[varName] = {
                'type': varType,
                'init': varInit
            }
    
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
    

