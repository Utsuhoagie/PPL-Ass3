
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

def getObjName(obj) -> str:
    if obj is None:
        return "None"
    return str(obj)
    #return type(obj).__name__ + "(" + str(obj) + ")"

def printDict(refEnv: dict, spaces: int, isStatic: bool = False):

    quotes = "'" if isStatic else ""
    for key in refEnv:
        if type(refEnv[key]) is not dict:
            line = " "*spaces + quotes + ("%s%s: %s" % (key, quotes, getObjName(refEnv[key])))
            #print(line)
        else:
            line = " "*spaces + quotes + ("%s%s: {" % (key, quotes))
            #print(line)
            printDict(refEnv[key], spaces + 4, isStatic)
            #print(" "*spaces + "}")

def isConstExpr(exp: Expr, baseExp: Expr, refEnv) -> bool:
    if type(exp) is Id:
        if refEnv[exp.name]['mutable'] == 'var':
            raise IllegalConstantExpression(baseExp)
        elif refEnv[exp.name]['mutable'] == 'const':
            return True
    elif isinstance(exp, Literal): # or isinstance(exp, Const)
        return True
    else:
        if type(exp) is BinaryOp:
            return isConstExpr(exp.left, baseExp, refEnv) and isConstExpr(exp.right, baseExp, refEnv)
    return False

def getCheckExprType(exp: Expr, baseExp: Expr, refEnv) -> Type:
    if isinstance(exp, Literal):
        if type(exp) is IntLiteral:
            return IntType()
        elif type(exp) is FloatLiteral:
            return FloatType()
        elif type(exp) is BooleanLiteral:
            return BoolType()
        elif type(exp) is StringLiteral:
            return StringType()
        

    elif isinstance(exp, Id):
        #print("-"*4 + "type of %s" % exp.name + " = " + str(refEnv[exp.name]['type']))
        return refEnv[exp.name]['type']
    
    
    else:
        if type(exp) is BinaryOp:
            t1 = getCheckExprType(exp.left, baseExp, refEnv)
            t2 = getCheckExprType(exp.right, baseExp, refEnv)
            op = exp.op

            ##print("here!!!! t1 = " + str(t1) + " and t1 equals IntType? %s" % (type(t1) == IntType) + " | t2 = " + str(t2))

            if op in ['+','-','*']:
                if type(t1) not in [IntType, FloatType] or type(t2) not in [IntType, FloatType]:
                    raise TypeMismatchInExpression(exp)
                elif type(t1) is FloatType or type(t2) is FloatType:
                    return FloatType()
                else:
                    return IntType()
            elif op in ['\\','%']:
                if type(t1) is not IntType or type(t2) is not IntType:
                    raise TypeMismatchInExpression(exp)
                else:
                    return IntType()
            elif op in ['/']:
                if type(t1) not in [IntType, FloatType] or type(t2) not in [IntType, FloatType]:
                    raise TypeMismatchInExpression(exp)
                else:
                    return FloatType()

            elif op in ['&&','||']:
                if type(t1) is not BoolType or type(t2) is not BoolType:
                    raise TypeMismatchInExpression(exp)
                else:
                    return BoolType()
            
            elif op in ['==','!=']:
                if type(t1) not in [IntType, BoolType] or type(t2) not in [IntType, BoolType] or type(t1) != type(t2):
                    raise TypeMismatchInExpression(exp)
                else:
                    return BoolType()
            elif op in ['<','<=','>','>=']:
                if type(t1) not in [IntType, FloatType] or type(t2) not in [IntType, FloatType]:
                    raise TypeMismatchInExpression(exp)
                else:
                    return BoolType()
            

def getCheckInitType(constDecl: ConstDecl, expL: Expr, baseExpL: Expr, expR: Expr, baseExpR: Expr, refEnv) -> Type:

    rhsType = getCheckExprType(expR, baseExpR, refEnv)

    # expL can only be among [Id(), ArrayCell(), FieldAccess()] which are all LHS
    # but Id() can point to anything except VoidType
    if not isinstance(expL, Id):
        raise TypeMismatchInConstant(baseExpL)
    else:
        # check what the Id() is pointing to
        lhsType = getCheckExprType(expL, baseExpL, refEnv)
        #print("-"*4 + "lhsType = " + str(lhsType) + " | rhsType = " + str(rhsType))

        if not typesCompat(lhsType, rhsType) or type(lhsType) is VoidType:
            #print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            raise TypeMismatchInConstant(constDecl)

    # DON'T NEED TO DO, SPECS DON'T HAVE IT!!!!!
    #pass

def typesCompat(t1: Type, t2: Type) -> bool:
    if type(t1) is type(t2):
        return True
    
    if type(t1) is FloatType and type(t2) is IntType:
        return True

    # TODO
    # parent vs child types

    return False

    

# ====== GetRefEnv visitor ==================


# Get environment of class + attr + method declarations
# and also catch some Redeclared/Undeclared
class GetRefEnv(BaseVisitor):

    def visitProgram(self, ctx, refEnv) -> dict:

        #print("=================================================")

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

            for memDecl in classDecl.memlist:
                if type(memDecl) is AttributeDecl:
                    storeDecl = memDecl.decl
                    storeDeclName = None
                    storeDeclType = None
                    if type(storeDecl) is VarDecl:
                        storeDeclType = storeDecl.varType
                    else:
                        storeDeclType = storeDecl.constType
                    
                    if type(storeDeclType) is ClassType:
                        storeDeclName = storeDeclType.classname.name    # string
                        if storeDeclName not in refEnv:
                            raise Undeclared(Class(), storeDeclName)
                    
        #print("\n\nin GetRefEnv, refEnv = ")
        printDict(refEnv, 4)

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
            # storeDecl is tuple of (name, type, init, isConst)
            attrName = storeDecl[0]
            attrType = storeDecl[1]
            attrInit = storeDecl[2]
            attrIsConst = storeDecl[3]
            mutable = "const" if attrIsConst else "var"

            if attrIsConst and attrInit is None:
                raise IllegalConstantExpression(None)
            elif attrIsConst and not isConstExpr(attrInit, attrInit, refEnv):
                raise IllegalConstantExpression(attrInit)
            

            refEnv[attrName] = {
                'type': attrType,
                'kind': kind,
                'mutable': mutable,
                'init': attrInit
            }

            # check type of init expr

            # check type of assigning that init expr to the const itself
            if attrIsConst:
                getCheckInitType(ctx.decl, Id(attrName), Id(attrName), attrInit, attrInit, refEnv)
            else:
                getCheckExprType(attrInit, attrInit, refEnv)

            #refEnv[storeDecl[0]]['init'] = storeDecl[2]


    def visitVarDecl(self, ctx, refEnv):
        varName = ctx.variable.name
        varType = ctx.varType
        varInit = ctx.varInit
        
        if varName in refEnv:
            # can't raise, because this must be Attribute() instead
            # just return a flag
            # raise Redeclared(Variable(), varName)
            return varName

        return (varName, varType, varInit, False)

        

    def visitConstDecl(self, ctx, refEnv):
        constName = ctx.constant.name
        constType = ctx.constType
        constInit = ctx.value

        if constName in refEnv:
            # can't raise, because this must be Attribute() instead
            # just return a flag
            # raise Redeclared(Constant(), constName)
            return constName
        #getCheckExprType(constInit, constInit, refEnv)
        #refEnv['global'][refEnv['current'].name][constName]['init'] = constInit

        return (constName, constType, constInit, True)

        

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

        # #print("\nrefEnv = ")
        # printDict(refEnv, 4)

        #print("\n=====================================\nin StaticChecker")

        [self.visit(classDecl, refEnv) for classDecl in ctx.decl]

        #print("\n" + "after visit, refEnv = ")
        printDict(refEnv, 4)



    # ---- Classes ------

    def visitClassDecl(self, ctx, refEnv): 
    
        clsRefEnv = {
            'current': ctx.classname,
            'global': refEnv
        }

        #print(" "*4 + "clsRefEnv: ")
        printDict(clsRefEnv, 8)

        [self.visit(memDecl, clsRefEnv) for memDecl in ctx.memlist]



    def visitMethodDecl(self, ctx, refEnv):

        mthdRefEnv = {
            'current': refEnv['current'],
            'global': refEnv['global'],
            'local': {}
        }

        mthdRefEnv['local']['isParam'] = True
        # visit param: List[VarDecl]
        [self.visit(param, mthdRefEnv) for param in ctx.param]
        mthdRefEnv['local']['isParam'] = False
        self.visit(ctx.body, mthdRefEnv)

        #print(" "*8 + "mthdRefEnv: ")
        printDict(mthdRefEnv, 12)

        #[GetRefEnv().visit(ctx.)]


    def visitAttributeDecl(self, ctx, refEnv):
        #print(" "*12 + "visiting attrDecl!")
        self.visit(ctx.decl, refEnv)

    def visitVarDecl(self, ctx, refEnv):
        # refEnv is only 'local' or 'blockLocal'!!!!!
        
        # SCRATCH THAT !!!!!!!!!!!!!!!
        # refEnv is full refEnv !!!!!
        
        varName = ctx.variable.name     # string
        varType = ctx.varType           # Type
        varInit = self.visit(ctx.varInit, refEnv) if ctx.varInit else None  # visit and evaluate the Expr


        if varType.classname.name not in refEnv['global']:
            raise Undeclared(Class(), varType.classname.name)

        if varName in refEnv['local']:
            if refEnv['isParam']:
                raise Redeclared(Parameter(), varName)
            else:
                raise Redeclared(Variable(), varName)

        refEnv['local'][varName] = {
            'type': varType,
            'init': varInit
        }


    def visitConstDecl(self, ctx, refEnv):
        constName = ctx.constant.name     # string
        constType = ctx.constType           # Type
        constInit = self.visit(ctx.value, refEnv)  # visit and evaluate the Expr

        if constName in refEnv:
            raise Redeclared(Constant(), constName)

        refEnv[constName] = {
            'type': constType,
            'init': constInit
        }
        

    def visitStatic(self, ctx, refEnv):
        return None
    
    def visitInstance(self, ctx, refEnv):
        return None
    

    # ---- Type -----
    
    # def visitIntType(self, ctx, refEnv):
    #     return None
    
    # def visitFloatType(self, ctx, refEnv):
    #     return None
    
    # def visitBoolType(self, ctx, refEnv):
    #     return None
    
    # def visitStringType(self, ctx, refEnv):
    #     return None
    
    # def visitVoidType(self, ctx, refEnv):
    #     return None
    
    # def visitArrayType(self, ctx, refEnv):
    #     return None
    
    # def visitClassType(self, ctx, refEnv):
    #     return None
    

    # ---- Expression -----

    def visitBinaryOp(self, ctx, refEnv):
        return ctx
    
    def visitUnaryOp(self, ctx, refEnv):
        return ctx
    
    def visitFieldAccess(self, ctx, refEnv):

        return None

    def visitCallExpr(self, ctx, refEnv):
        return None
    
    def visitNewExpr(self, ctx, refEnv):
        return None
    
    def visitId(self, ctx, refEnv):
        return ctx
    
    def visitArrayCell(self, ctx, refEnv):
        return None


    # --- Literal -----

    def visitIntLiteral(self, ctx, refEnv):
        return ctx
    
    def visitFloatLiteral(self, ctx, refEnv):
        return ctx
    
    def visitBooleanLiteral(self, ctx, refEnv):
        return ctx
    
    def visitStringLiteral(self, ctx, refEnv):
        return ctx
    
    def visitNullLiteral(self, ctx, refEnv):
        return ctx
    
    def visitSelfLiteral(self, ctx, refEnv):
        return ctx 

    def visitArrayLiteral(self, ctx, refEnv):
        arrType = type(ctx.value[0])

        for elem in ctx.value:
            if type(elem) is not arrType:
                raise IllegalArrayLiteral(ctx)

        return ctx
    
    
    # ---- Stmt -----

    def visitBlock(self, ctx, refEnv):
        # decl: List[StoreDecl]
        [self.visit(decl, refEnv) for decl in ctx.decl]

        #print(" "*16 + "in block, refEnv = ")
        printDict(refEnv, 20)

        [self.visit(stmt, refEnv) for stmt in ctx.stmt]

        return 
    
    def visitIf(self, ctx, refEnv):
        cond = self.visit(ctx.expr, refEnv)
        if type(getCheckExprType(cond, cond, refEnv)) is not BoolType:
            raise TypeMismatchInStatement(ctx)

        return None
    
    def visitFor(self, ctx, refEnv):
        refEnv['isInLoop'] = True

        return None
    
    def visitContinue(self, ctx, refEnv):
        if 'isInLoop' not in refEnv:
            raise MustInLoop(ctx)
        return
    
    def visitBreak(self, ctx, refEnv):
        if 'isInLoop' not in refEnv:
            raise MustInLoop(ctx)
        return

    def visitReturn(self, ctx, refEnv):
        return ctx
    
    def visitAssign(self, ctx, refEnv):
        return None
    
    def visitCallStmt(self, ctx, refEnv):
        return None
    

