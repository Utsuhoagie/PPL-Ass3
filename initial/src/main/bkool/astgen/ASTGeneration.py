from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce
from typing import *

def flatten(lst: List[list]) -> list:
    if lst == []:
        return lst
    return list(reduce(lambda x,y: x + y, lst))

# -------------------------------------------------
class ASTGeneration(BKOOLVisitor):

    # def visit(self,ctx:BKOOLParser.Context):
    #     return ([self.visit(x) for x in ctx.classdecl()])

    # def visitClassdecl(self,ctx:BKOOLParser.ClassDeclContext):
    #     return ClassDecl(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.memdecl()])

    # def visitMemdecl(self,ctx):         #:BKOOLParser.MemDeclContext):
    #     return AttributeDecl(Instance(),VarDecl(Id(ctx.ID().getText()),self.visit(ctx.bkooltype())))

    # def visitBkooltype(self,ctx):       #:BKOOLParser.BkooltypeContext):
    #     return IntType() if ctx.INTTYPE() else VoidType()
        
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        # program         : classDeclList EOF;


        print("\n\n\t\t in visitProgram")
        classDeclList = self.visit(ctx.classDeclList())     # this is probably List
        return Program(classDeclList)

    def visitClassDeclList(self, ctx: BKOOLParser.ClassDeclListContext) -> list:
        # classDeclList   : classDecl classDeclList
        #                 | classDecl;


        print("\t\t in visitClassDeclList")
        classDecl = self.visit(ctx.classDecl())
        if ctx.getChildCount() == 2:
            classDeclList = self.visit(ctx.classDeclList())
            return [classDecl] + classDeclList
        return [classDecl]

    def visitClassDecl(self, ctx: BKOOLParser.ClassDeclContext) -> ClassDecl:
        # classDecl       : CLASS ID EXTENDS ID LP (memberList | ) RP
        #                 | CLASS ID LP (memberList | ) RP;
        
        print("\t\t in visitClassDecl")
        id = Id(ctx.getChild(1).getText())   # self.visit(ctx.getChild(1))
        print("\t\t\t" + str(id))
        memberList = []
        idParent = None
        if ctx.memberList():
            print("\t\t\tthere is memberList in classDecl")
            memberList = self.visit(ctx.memberList())
        
        if ctx.EXTENDS():
            idParent = Id(ctx.getChild(3).getText())
        
        return ClassDecl(id, memberList, idParent)

    def visitMemberList(self, ctx: BKOOLParser.MemberListContext):
        # memberList      : member memberList
        #                 | member;

        print("\t\t in visitMemberList")
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
        # should return [Var/ConstDecl]
        # or just 1 method (probably not list?) -----------------

        # member          : attrKeyword attrType attrList SEMI
        #                 | (STATIC | ) returnType method
        #                 | constructor;

        print("\t\t in visitMember")
        if ctx.getChildCount() == 4:
            print("\t\t\t in member, attribute")

            attrKeyword = self.visit(ctx.attrKeyword())
            print("\t\t\t keyword = " + str(attrKeyword))

            attrType = self.visit(ctx.attrType())   # 1 type
            print("\t\t\t attrType = " + str(attrType))

            attrList = self.visit(ctx.attrList())   # multiple tuples of (Id, Expr = None)
            print("\t\t\t attrList = " + str(attrList))
            
            kind = Static() if "static" in attrKeyword else Instance()
            if "final" in attrKeyword:
                if type(attrType) is ClassType:
                    print("-=-=-==-=-=-=-=-===-=-=-=-=-=-=-=-==-=-=-=-=-==-=-=-=-=-===========================")
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
                    print("-=-=-==-=-=-=-=-===-=-=-=-=-=-=-=-==-=-=-=-=-==-=-=-=-=-===========================")
                    AttrDeclListClass = []
                    for idElem in attrList:
                        if idElem[1] == None:
                            AttrDeclListClass.append(AttributeDecl(kind, VarDecl(idElem[0], attrType, NullLiteral())))
                        else:
                            AttrDeclListClass.append(AttributeDecl(kind, VarDecl(idElem[0], attrType, idElem[1])))
                    
                    return AttrDeclListClass
                return [AttributeDecl(kind, VarDecl(idElem[0], attrType, idElem[1])) for idElem in attrList]

            
        if ctx.constructor():
            constructor = self.visit(ctx.constructor())   # (Id, paramList, body)
            return [MethodDecl(Instance(), constructor[0], constructor[1], None, constructor[2])] # --------------------------
        
        if ctx.method():
            returnType = self.visit(ctx.returnType())
            method = self.visit(ctx.method())   # (Id, paramList, body)
            if ctx.STATIC():
                return [MethodDecl(Static(), method[0], method[1], returnType, method[2])] 
            return [MethodDecl(Instance(), method[0], method[1], returnType, method[2])]

    def visitAttrKeyword(self, ctx: BKOOLParser.AttrKeywordContext) -> str:
        # return a string of keywords
        # which dictates Var/Const decl, and Static/Instance kind

        # attrKeyword     : STATIC FINAL | FINAL STATIC | STATIC | FINAL | ;

        print("\t\t in visitAttrKeyword")
        if ctx.getChildCount() > 0:
            print("\t\t\t keyword = " + str(ctx.getChild(0)))

        if ctx.getChildCount() == 2:
            return (ctx.getChild(0).getText() + " " + ctx.getChild(0).getText()).lower()
        elif ctx.getChildCount() == 1:
            return (ctx.getChild(0).getText()).lower()
        
        return ""

    def visitAttrType(self, ctx: BKOOLParser.AttrTypeContext):
        # attrType        : INT | FLOAT | BOOLEAN | STRING | ID | arrayType;  // ID is for class names (e.g Shape s)
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
        # arrayType       : (INT | FLOAT | BOOLEAN | STRING | ID) LQ INTLIT RQ;

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
        # list of [(NAME, INIT = None), (NAME2, INIT2 = None),...] only           e.g: [(a,4), (b)]

        # attrList        : attribute COMMA attrList
        #                 | attribute;

        attr = self.visit(ctx.attribute())
        if ctx.getChildCount() > 1:
            attrList = self.visit(ctx.attrList())
            return [attr] + attrList
        return [attr]

    def visitAttribute(self, ctx: BKOOLParser.AttributeContext) -> Tuple[Id, Expr]:
        # returns a tuple of (Id, Expr = None)
        # to create an actual VarDecl() or ConstDecl() later

        # attribute       : ID INIT exp
        #                 | ID;

        id = Id(ctx.getChild(0).getText())
        if ctx.exp():
            exp = self.visit(ctx.exp())
            return (id, exp)
        return (id, None)

    def visitReturnType(self, ctx: BKOOLParser.ReturnTypeContext):
        # returnType      : INT | FLOAT | BOOLEAN | STRING | VOID;

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

    def visitMethod(self, ctx: BKOOLParser.MethodContext) -> tuple:     # (Id, paramList, blockStmt) -----------------------------
        # method          : ID LB (paramList | ) RB blockStmt;

        id = Id(ctx.ID().getText())
        paramList = [] if not ctx.paramList() else self.visit(ctx.paramList())    # List[VarDecl]
        blockStmt = self.visit(ctx.blockStmt())
        return (id, paramList, blockStmt)

    def visitConstructor(self, ctx: BKOOLParser.ConstructorContext):
        # constructor     : ID LB (paramList | ) RB blockStmt;

        id = Id(ctx.ID().getText())
        paramList = [] if not ctx.paramList() else self.visit(ctx.paramList())    # List[VarDecl]
        blockStmt = self.visit(ctx.blockStmt())
        return (id, paramList, blockStmt) 

    def visitParamList(self, ctx: BKOOLParser.ParamListContext):
        # paramList       : param SEMI paramList
        #                 | param;

        param = self.visit(ctx.param())
        if ctx.paramList():
            paramList = self.visit(ctx.paramList())
            return param + paramList
        return param

    def visitParam(self, ctx: BKOOLParser.ParamContext) -> List[VarDecl]:
        # param           : attrType idList;

        paramType = self.visit(ctx.attrType())
        idList = self.visit(ctx.idList())

        return [VarDecl(id, paramType) for id in idList]

    def visitIdList(self, ctx: BKOOLParser.IdListContext) -> List[Id]:
        # idList          : ID COMMA idList
        #                 | ID;

        id = Id(ctx.ID().getText())
        if ctx.getChildCount() == 3:
            idList = self.visit(ctx.idList())
            return [id] + idList
        return [id]



    def visitExp(self, ctx: BKOOLParser.ExpContext):
        # exp         : LB exp RB | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arrayLit | THIS | ID    // highest priority
        #             | obj_create
        #             | exp DOT ID LB (argList | ) RB // instance_method_invoke
        #             | ID DOT ID LB (argList | )RB   // static_method_invoke
        #             | exp DOT ID                    // instance_attr_access
        #             | ID DOT ID                     // static_attr_access
        #             | exp LQ exp RQ                 // index_op
        #
        #             // arithmetic/bool
        #             | (ADD | SUB) exp
        #             | NOT exp
        #             | exp CONCAT exp
        #             | exp (MUL | DIV | DIVF | MOD) exp
        #             | exp (ADD | SUB) exp
        #             | exp (AND | OR) exp
        #             | exp (EQ | NEQ) exp
        #             | exp (LESS | GREATER | LEQ | GREQ) exp;

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
            # instance/static method invoke
            objName = Id(ctx.getChild(0).getText()) if not ctx.exp() else self.visit(ctx.getChild(0))
            methodName = Id(ctx.getChild(2).getText())
            argList = [] if not ctx.argList() else self.visit(ctx.argList())

            return CallStmt(objName, methodName, argList)

        elif ctx.DOT():
            # instance/static attr access
            objName = Id(ctx.getChild(0).getText()) if not ctx.exp() else self.visit(ctx.getChild(0))
            attrName = Id(ctx.getChild(2).getText())

            return FieldAccess(objName, attrName)

        elif ctx.LQ():
            # array index op
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
        # arrayLit   : LP (INTLIT | FLOATLIT | BOOLLIT | STRINGLIT) litList RP
        #            | LP (INTLIT | FLOATLIT | BOOLLIT | STRINGLIT) RP;

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

    def visitLitList(self, ctx: BKOOLParser.LitListContext) -> list:    # List[Literal]
        # litList     : COMMA (INTLIT | FLOATLIT | BOOLLIT | STRINGLIT) litList
        #             | COMMA (INTLIT | FLOATLIT | BOOLLIT | STRINGLIT);

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
        # argList     : exp COMMA argList
        #             | exp;
        exp = self.visit(ctx.exp())
        if ctx.argList():
            argList = self.visit(ctx.argList())
            return [exp] + argList
        return [exp]

    def visitObj_create(self, ctx: BKOOLParser.Obj_createContext):
        # obj_create  : NEW ID LB (argList | ) RB;

        classId = Id(ctx.ID().getText())
        argList = [] if not ctx.argList() else self.visit(ctx.argList())    # List[Expr]

        return NewExpr(classId, argList)



    def visitStmtList(self, ctx: BKOOLParser.StmtListContext) -> List[Stmt]:
        # stmtList    : stmt stmtList
        #             | stmt;

        stmt = self.visit(ctx.stmt())
        if ctx.stmtList():
            stmtList = self.visit(ctx.stmtList())
            return [stmt] + stmtList
        return [stmt]

    def visitStmt(self, ctx: BKOOLParser.StmtContext) -> Stmt:
        # stmt        : blockStmt                 // each stmt's subrule has its own SEMI or other ending tokens
        #             | assignStmt
        #             | ifStmt
        #             | forStmt
        #             | breakStmt
        #             | continueStmt
        #             | returnStmt
        #             | methodInvokeStmt;

        stmt = self.visit(ctx.getChild(0))
        return stmt

    def visitBlockStmt(self, ctx: BKOOLParser.BlockStmtContext):
        # blockStmt   : LP (blockBody | ) RP;
        if ctx.blockBody():
            blockBody = self.visit(ctx.blockBody())
            print("\t\t\t in blockStmt")
            #print("\t\t\t " + str(blockBody))
            return Block(blockBody[0], blockBody[1])
        return Block([],[])

    def visitBlockBody(self, ctx: BKOOLParser.BlockBodyContext):
        # blockBody   : (declList | ) (stmtList | );

        declList = [] if not ctx.declList() else self.visit(ctx.declList())
        stmtList = [] if not ctx.stmtList() else self.visit(ctx.stmtList())
        return (declList, stmtList)        # 'blockStmt's body'

    def visitDeclList(self, ctx: BKOOLParser.DeclListContext):
        # declList    : decl declList
        #             | decl;

        decl = self.visit(ctx.decl())
        if ctx.getChildCount() == 2:
            declList = self.visit(ctx.declList())
            return decl + declList
        return decl

    def visitDecl(self, ctx: BKOOLParser.DeclContext) -> List[VarDecl]:
        # decl        : (FINAL | ) attrType attrList SEMI;
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
        # assignStmt  : lhs ASSIGN exp SEMI;

        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.exp())
        return Assign(lhs, exp)

    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        # lhs         : ID
        #             | exp DOT ID                // instance_attr_access
        #             | ID DOT ID                 // static_attr_access
        #             | exp LQ exp RQ;

        if ctx.getChildCount() == 1:
            return Id(ctx.getChild(0).getText())   # 'local var'
        elif ctx.getChildCount() == 4:
            exp1 = self.visit(ctx.getChild(0))
            exp2 = self.visit(ctx.getChild(2))
            return ArrayCell(exp1, exp2)    # 'index op'
        elif ctx.exp():
            exp = self.visit(ctx.getChild(0))
            fieldName = Id(ctx.getChild(2).getText())
            return FieldAccess(exp, fieldName)      # 'instance attr access'
        else:
            id = Id(ctx.getChild(0).getText())
            fieldName = Id(ctx.getChild(2).getText())
            return FieldAccess(id, fieldName)       # 'static attr access'



    def visitIfStmt(self, ctx: BKOOLParser.IfStmtContext) -> If:
        # ifStmt      : IF exp THEN stmt ELSE stmt
        #             | IF exp THEN stmt;
        
        exp = self.visit(ctx.exp())
        stmtThen = self.visit(ctx.getChild(3))

        if ctx.getChildCount() > 4:
            stmtElse = self.visit(ctx.getChild(5))
            return If(exp, stmtThen, stmtElse)
        return If(exp, stmtThen)
        
    def visitForStmt(self, ctx: BKOOLParser.ForStmtContext):
        # forStmt     : FOR scalarVar ASSIGN exp (TO | DOWNTO) exp DO stmt;

        scalarVar = self.visit(ctx.scalarVar())
        expFrom = self.visit(ctx.getChild(3))
        expTo = self.visit(ctx.getChild(5))
        dir = True if ctx.TO() else False
        stmt = self.visit(ctx.stmt())
        return For(scalarVar, expFrom, expTo, dir, stmt)

    def visitScalarVar(self, ctx: BKOOLParser.ScalarVarContext):
        # scalarVar   : ID                        // local variable
        #             | exp DOT ID | ID DOT ID    // instance/static attribute access
        #             | exp LQ exp RQ;            // index_op

        if ctx.getChildCount() == 1:
            return Id(ctx.getChild(0).getText())   # 'local var'
        elif ctx.getChildCount() == 4:
            exp1 = self.visit(ctx.getChild(0))
            exp2 = self.visit(ctx.getChild(2))
            return ArrayCell(exp1, exp2)    # 'index op'
        elif ctx.exp():
            exp = self.visit(ctx.getChild(0).getText())
            fieldName = Id(ctx.getChild(2).getText())
            return FieldAccess(exp, fieldName)          # 'instance attr access'
        else:
            className = Id(ctx.getChild(0).getText())
            fieldName = Id(ctx.getChild(2).getText())
            return FieldAccess(className, fieldName)    # 'static attr access'

    def visitBreakStmt(self, ctx: BKOOLParser.BreakStmtContext):
        # breakStmt   : BREAK SEMI;

        return Break()

    def visitContinueStmt(self, ctx: BKOOLParser.ContinueStmtContext):
        # continueStmt: CONTINUE SEMI;

        return Continue()

    def visitReturnStmt(self, ctx: BKOOLParser.ReturnStmtContext):
        # returnStmt  : RETURN exp SEMI
        #             | RETURN SEMI;

        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        return Return()

    def visitMethodInvokeStmt(self, ctx: BKOOLParser.MethodInvokeStmtContext):
        # methodInvokeStmt: exp DOT ID LB (argList | ) RB SEMI    // instance_method_invoke
        #                 | ID DOT ID LB (argList | ) RB SEMI;    // static_method_invoke

        objName = self.visit(ctx.exp()) if ctx.exp() else Id(ctx.getChild(0).getText())
        methodName = Id(ctx.getChild(2).getText())
        argList = [] if not ctx.argList() else self.visit(ctx.argList())

        return CallStmt(objName, methodName, argList)