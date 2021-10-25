from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce
from typing import *

def flatten(lst: List[list]) -> list:
    if lst == []:
        return lst
    return list(reduce(lambda x,y: x + y, lst))


class ASTGeneration(BKOOLVisitor):

    
    

    
    

    
    

    
    
        
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        


       
        classDeclList = self.visit(ctx.classDeclList())     
        return Program(classDeclList)

    def visitClassDeclList(self, ctx: BKOOLParser.ClassDeclListContext) -> list:
        
        


       
        classDecl = self.visit(ctx.classDecl())
        if ctx.getChildCount() == 2:
            classDeclList = self.visit(ctx.classDeclList())
            return [classDecl] + classDeclList
        return [classDecl]

    def visitClassDecl(self, ctx: BKOOLParser.ClassDeclContext) -> ClassDecl:
        
        
        
       
        id = Id(ctx.getChild(1).getText())   
       
        memberList = []
        idParent = None
        if ctx.memberList():
           
            memberList = self.visit(ctx.memberList())
        
        if ctx.EXTENDS():
            idParent = Id(ctx.getChild(3).getText())
        
        return ClassDecl(id, memberList, idParent)

    def visitMemberList(self, ctx: BKOOLParser.MemberListContext):
        
        

       
        member = self.visit(ctx.member())
        if ctx.getChildCount() == 2:
            memberList = self.visit(ctx.memberList())
            if type(member) is not list:
                return [member] + memberList
            else:
                return member + memberList

        if type(member) is not list:
            return [member]
        else:
            return member

    def visitMember(self, ctx: BKOOLParser.MemberContext):
        
        

        
        
        

       
        if ctx.getChildCount() == 4:
           

            attrKeyword = self.visit(ctx.attrKeyword())
           

            attrType = self.visit(ctx.attrType())   
           

            attrList = self.visit(ctx.attrList())   
           
            
            kind = Static() if "static" in attrKeyword else Instance()
            if "final" in attrKeyword:
                if type(attrType) is ClassType:
                   
                    AttrDeclListClass = []
                    for idElem in attrList:
                        if idElem[1] == None:
                            AttrDeclListClass.append(AttributeDecl(kind, ConstDecl(idElem[0], attrType, NullLiteral())))
                        else:
                            AttrDeclListClass.append(AttributeDecl(kind, ConstDecl(idElem[0], attrType, idElem[1])))
                    
                    return AttrDeclListClass
                return [AttributeDecl(kind, ConstDecl(idElem[0], attrType, idElem[1])) for idElem in attrList]
            else:
                if type(attrType) is ClassType:
                   
                    AttrDeclListClass = []
                    for idElem in attrList:
                        if idElem[1] == None:
                            AttrDeclListClass.append(AttributeDecl(kind, VarDecl(idElem[0], attrType, NullLiteral())))
                        else:
                            AttrDeclListClass.append(AttributeDecl(kind, VarDecl(idElem[0], attrType, idElem[1])))
                    
                    return AttrDeclListClass
                return [AttributeDecl(kind, VarDecl(idElem[0], attrType, idElem[1])) for idElem in attrList]

            
        if ctx.constructor():
            constructor = self.visit(ctx.constructor())   
            return [MethodDecl(Instance(), constructor[0], constructor[1], None, constructor[2])] 
        
        if ctx.method():
            returnType = self.visit(ctx.returnType())
            method = self.visit(ctx.method())   
            if ctx.STATIC():
                return [MethodDecl(Static(), method[0], method[1], returnType, method[2])] 
            return [MethodDecl(Instance(), method[0], method[1], returnType, method[2])]

    def visitAttrKeyword(self, ctx: BKOOLParser.AttrKeywordContext) -> str:
        
        

        

       
           

        if ctx.getChildCount() == 2:
            return (ctx.getChild(0).getText() + " " + ctx.getChild(0).getText()).lower()
        elif ctx.getChildCount() == 1:
            return (ctx.getChild(0).getText()).lower()
        
        return ""

    def visitAttrType(self, ctx: BKOOLParser.AttrTypeContext):
        
        if ctx.arrayType():
            arrayType = self.visit(ctx.arrayType())
            return arrayType
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.STRING():
            return StringType()
        if ctx.ID():
            return ClassType(Id(ctx.getChild(0).getText()))

    def visitArrayType(self, ctx: BKOOLParser.ArrayTypeContext):
        

        arrType = None
        if ctx.INT():
            arrType = IntType()
        if ctx.FLOAT():
            arrType = FloatType()
        if ctx.BOOLEAN():
            arrType = BoolType()
        if ctx.STRING():
            arrType = StringType()
        if ctx.ID():
            arrType = ClassType(Id(ctx.getChild(0).getText()))
        
        size = int(ctx.INTLIT().getText())

        return ArrayType(size, arrType)

    def visitAttrList(self, ctx: BKOOLParser.AttrListContext):
        

        
        

        attr = self.visit(ctx.attribute())
        if ctx.getChildCount() > 1:
            attrList = self.visit(ctx.attrList())
            return [attr] + attrList
        return [attr]

    def visitAttribute(self, ctx: BKOOLParser.AttributeContext) -> Tuple[Id, Expr]:
        
        

        
        

        id = Id(ctx.getChild(0).getText())
        if ctx.exp():
            exp = self.visit(ctx.exp())
            return (id, exp)
        return (id, None)

    def visitReturnType(self, ctx: BKOOLParser.ReturnTypeContext):
        

        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.STRING():
            return StringType()
        if ctx.VOID():
            return VoidType()

    def visitMethod(self, ctx: BKOOLParser.MethodContext) -> tuple:     
        

        id = Id(ctx.ID().getText())
        paramList = [] if not ctx.paramList() else self.visit(ctx.paramList())    
        blockStmt = self.visit(ctx.blockStmt())
        return (id, paramList, blockStmt)

    def visitConstructor(self, ctx: BKOOLParser.ConstructorContext):
        

        id = Id(ctx.ID().getText())
        paramList = [] if not ctx.paramList() else self.visit(ctx.paramList())    
        blockStmt = self.visit(ctx.blockStmt())
        return (id, paramList, blockStmt) 

    def visitParamList(self, ctx: BKOOLParser.ParamListContext):
        
        

        param = self.visit(ctx.param())
        if ctx.paramList():
            paramList = self.visit(ctx.paramList())
            return param + paramList
        return param

    def visitParam(self, ctx: BKOOLParser.ParamContext) -> List[VarDecl]:
        

        paramType = self.visit(ctx.attrType())
        idList = self.visit(ctx.idList())

        return [VarDecl(id, paramType) for id in idList]

    def visitIdList(self, ctx: BKOOLParser.IdListContext) -> List[Id]:
        
        

        id = Id(ctx.ID().getText())
        if ctx.getChildCount() == 3:
            idList = self.visit(ctx.idList())
            return [id] + idList
        return [id]



    def visitExp(self, ctx: BKOOLParser.ExpContext):
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        if ctx.LB() and ctx.exp() and ctx.getChildCount() == 3:
            exp = self.visit(ctx.getChild(1))
            return exp

        elif ctx.getChildCount() == 1 and not ctx.obj_create():
            if ctx.INTLIT():
                return IntLiteral(int(ctx.INTLIT().getText()))
            if ctx.FLOATLIT():
                return FloatLiteral(float(ctx.FLOATLIT().getText()))
            if ctx.BOOLLIT():
                val = ctx.BOOLLIT().getText()
                return BooleanLiteral(True) if val == "true" else BooleanLiteral(False)
            if ctx.STRINGLIT():
                return StringLiteral(ctx.STRINGLIT().getText()[1:-1])
            if ctx.arrayLit():
                arrayLit = self.visit(ctx.arrayLit())
                return arrayLit
            if ctx.THIS():
                return SelfLiteral()
            if ctx.ID():
                return Id(ctx.getChild(0).getText())

        elif ctx.obj_create():
            objCreate = self.visit(ctx.obj_create())
            return objCreate

        elif ctx.getChildCount() >= 5:
            
            objName = Id(ctx.getChild(0).getText()) if not ctx.exp() else self.visit(ctx.getChild(0))
            methodName = Id(ctx.getChild(2).getText())
            argList = [] if not ctx.argList() else self.visit(ctx.argList())

            return CallStmt(objName, methodName, argList)

        elif ctx.DOT():
            
            objName = Id(ctx.getChild(0).getText()) if not ctx.exp() else self.visit(ctx.getChild(0))
            attrName = Id(ctx.getChild(2).getText())

            return FieldAccess(objName, attrName)

        elif ctx.LQ():
            
            arrObj = self.visit(ctx.getChild(0))
            index = self.visit(ctx.getChild(2))

            return ArrayCell(arrObj, index)
        
        elif (ctx.ADD() or ctx.SUB()) and ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            exp = self.visit(ctx.getChild(1))

            return UnaryOp(op, exp)
        
        elif ctx.NOT():
            op = ctx.getChild(0).getText()
            exp = self.visit(ctx.getChild(1))

            return UnaryOp(op, exp)

        elif ctx.CONCAT():
            op = ctx.getChild(1).getText()
            str1 = self.visit(ctx.getChild(0))
            str2 = self.visit(ctx.getChild(2))

            return BinaryOp(op, str1, str2)

        elif ctx.MUL() or ctx.DIV() or ctx.DIVF() or ctx.MOD():
            op = ctx.getChild(1).getText()
            exp1 = self.visit(ctx.getChild(0))
            exp2 = self.visit(ctx.getChild(2))

            return BinaryOp(op, exp1, exp2)

        elif ctx.ADD() or ctx.SUB():
            op = ctx.getChild(1).getText()
            exp1 = self.visit(ctx.getChild(0))
            exp2 = self.visit(ctx.getChild(2))

            return BinaryOp(op, exp1, exp2)

        elif ctx.AND() or ctx.OR():
            op = ctx.getChild(1).getText()
            exp1 = self.visit(ctx.getChild(0))
            exp2 = self.visit(ctx.getChild(2))

            return BinaryOp(op, exp1, exp2)

        elif ctx.EQ() or ctx.NEQ():
            op = ctx.getChild(1).getText()
            exp1 = self.visit(ctx.getChild(0))
            exp2 = self.visit(ctx.getChild(2))

            return BinaryOp(op, exp1, exp2)

        elif ctx.LESS() or ctx.GREATER() or ctx.LEQ() or ctx.GREQ():
            op = ctx.getChild(1).getText()
            exp1 = self.visit(ctx.getChild(0))
            exp2 = self.visit(ctx.getChild(2))

            return BinaryOp(op, exp1, exp2)


    def visitArrayLit(self, ctx: BKOOLParser.ArrayLitContext):
        
        

        literal = ctx.getChild(1).getText()

        if ctx.INTLIT():
            literal = IntLiteral(int(literal))
        if ctx.FLOATLIT():
            literal = FloatLiteral(float(literal))
        if ctx.BOOLLIT():
            literal = BooleanLiteral(True) if literal == "true" else BooleanLiteral(False)
        if ctx.STRINGLIT():
            literal = StringLiteral(literal)

        if ctx.litList():
            litList = self.visit(ctx.litList())
            return ArrayLiteral([literal] + litList)

        return ArrayLiteral([literal])

    def visitLitList(self, ctx: BKOOLParser.LitListContext) -> list:    
        
        

        literal = ctx.getChild(1).getText()

        if ctx.INTLIT():
            literal = IntLiteral(int(literal))
        if ctx.FLOATLIT():
            literal = FloatLiteral(float(literal))
        if ctx.BOOLLIT():
            literal = BooleanLiteral(True) if literal == "true" else BooleanLiteral(False)
        if ctx.STRINGLIT():
            literal = StringLiteral(literal)

        if ctx.litList():
            litList = self.visit(ctx.litList())
            return [literal] + litList

        return [literal]

    def visitArgList(self, ctx: BKOOLParser.ArgListContext) -> List[Expr]:
        
        
        exp = self.visit(ctx.exp())
        if ctx.argList():
            argList = self.visit(ctx.argList())
            return [exp] + argList
        return [exp]

    def visitObj_create(self, ctx: BKOOLParser.Obj_createContext):
        

        classId = Id(ctx.ID().getText())
        argList = [] if not ctx.argList() else self.visit(ctx.argList())    

        return NewExpr(classId, argList)



    def visitStmtList(self, ctx: BKOOLParser.StmtListContext) -> List[Stmt]:
        
        

        stmt = self.visit(ctx.stmt())
        if ctx.stmtList():
            stmtList = self.visit(ctx.stmtList())
            return [stmt] + stmtList
        return [stmt]

    def visitStmt(self, ctx: BKOOLParser.StmtContext) -> Stmt:
        
        
        
        
        
        
        
        

        stmt = self.visit(ctx.getChild(0))
        return stmt

    def visitBlockStmt(self, ctx: BKOOLParser.BlockStmtContext):
        
        if ctx.blockBody():
            blockBody = self.visit(ctx.blockBody())
           
            
            return Block(blockBody[0], blockBody[1])
        return Block([],[])

    def visitBlockBody(self, ctx: BKOOLParser.BlockBodyContext):
        

        declList = [] if not ctx.declList() else self.visit(ctx.declList())
        stmtList = [] if not ctx.stmtList() else self.visit(ctx.stmtList())
        return (declList, stmtList)        

    def visitDeclList(self, ctx: BKOOLParser.DeclListContext):
        
        

        decl = self.visit(ctx.decl())
        if ctx.getChildCount() == 2:
            declList = self.visit(ctx.declList())
            return decl + declList
        return decl

    def visitDecl(self, ctx: BKOOLParser.DeclContext) -> List[VarDecl]:
        
        attrType = self.visit(ctx.attrType())
        attrList = self.visit(ctx.attrList())

        if ctx.FINAL():
            if type(attrType) is ClassType:
                declList = []
                for idElem in attrList:
                    if idElem[1] == None:
                        declList.append(ConstDecl(idElem[0], attrType, NullLiteral()))
                    else:
                        declList.append(ConstDecl(idElem[0], attrType, idElem[1]))
                return declList

            return [ConstDecl(idElem[0], attrType, idElem[1]) for idElem in attrList]
        
        if type(attrType) is ClassType:
                declList = []
                for idElem in attrList:
                    if idElem[1] == None:
                        declList.append(VarDecl(idElem[0], attrType, NullLiteral()))
                    else:
                        declList.append(VarDecl(idElem[0], attrType, idElem[1]))
                return declList
                    
        return [VarDecl(idElem[0], attrType, idElem[1]) for idElem in attrList]

    def visitAssignStmt(self, ctx: BKOOLParser.AssignStmtContext):
        

        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.exp())
        return Assign(lhs, exp)

    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        
        
        
        

        if ctx.getChildCount() == 1:
            return Id(ctx.getChild(0).getText())   
        elif ctx.getChildCount() == 4:
            exp1 = self.visit(ctx.getChild(0))
            exp2 = self.visit(ctx.getChild(2))
            return ArrayCell(exp1, exp2)    
        elif ctx.exp():
            exp = self.visit(ctx.getChild(0))
            fieldName = Id(ctx.getChild(2).getText())
            return FieldAccess(exp, fieldName)      
        else:
            id = Id(ctx.getChild(0).getText())
            fieldName = Id(ctx.getChild(2).getText())
            return FieldAccess(id, fieldName)       



    def visitIfStmt(self, ctx: BKOOLParser.IfStmtContext) -> If:
        
        
        
        exp = self.visit(ctx.exp())
        stmtThen = self.visit(ctx.getChild(3))

        if ctx.getChildCount() > 4:
            stmtElse = self.visit(ctx.getChild(5))
            return If(exp, stmtThen, stmtElse)
        return If(exp, stmtThen)
        
    def visitForStmt(self, ctx: BKOOLParser.ForStmtContext):
        

        scalarVar = self.visit(ctx.scalarVar())
        expFrom = self.visit(ctx.getChild(3))
        expTo = self.visit(ctx.getChild(5))
        dir = True if ctx.TO() else False
        stmt = self.visit(ctx.stmt())
        return For(scalarVar, expFrom, expTo, dir, stmt)

    def visitScalarVar(self, ctx: BKOOLParser.ScalarVarContext):
        
        
        

        if ctx.getChildCount() == 1:
            return Id(ctx.getChild(0).getText())   
        elif ctx.getChildCount() == 4:
            exp1 = self.visit(ctx.getChild(0))
            exp2 = self.visit(ctx.getChild(2))
            return ArrayCell(exp1, exp2)    
        elif ctx.exp():
            exp = self.visit(ctx.getChild(0).getText())
            fieldName = Id(ctx.getChild(2).getText())
            return FieldAccess(exp, fieldName)          
        else:
            className = Id(ctx.getChild(0).getText())
            fieldName = Id(ctx.getChild(2).getText())
            return FieldAccess(className, fieldName)    

    def visitBreakStmt(self, ctx: BKOOLParser.BreakStmtContext):
        

        return Break()

    def visitContinueStmt(self, ctx: BKOOLParser.ContinueStmtContext):
        

        return Continue()

    def visitReturnStmt(self, ctx: BKOOLParser.ReturnStmtContext):
        
        

        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        return Return()

    def visitMethodInvokeStmt(self, ctx: BKOOLParser.MethodInvokeStmtContext):
        
        

        objName = self.visit(ctx.exp()) if ctx.exp() else Id(ctx.getChild(0).getText())
        methodName = Id(ctx.getChild(2).getText())
        argList = [] if not ctx.argList() else self.visit(ctx.argList())

        return CallStmt(objName, methodName, argList)