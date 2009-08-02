__all__ = [
    "ASTNode", "Program", "TopLevelItem", "PredicateDef", "Identifier",
    "InstanceDef", "TypeCondition", "RecordDef", "Field",
    "Variable", "VariableDef", "ProcedureDef", "OverloadableDef",
    "OverloadDef", "Argument", "ValueArgument", "TypeArgument",
    "Statement", "Block", "LocalVariableDef", "Assignment",
    "IfStatement", "BreakStatement", "ContinueStatement",
    "WhileStatement", "ForStatement", "ReturnStatement", "ExprStatement",
    "Expression", "AddressOfExpr", "IndexExpr", "CallExpr",
    "FieldRef", "TupleRef", "PointerRef",
    "ArrayExpr", "TupleExpr", "NameRef", "BoolLiteral", "IntLiteral",
    "CharLiteral", "StringLiteral"]

class ASTNode(object) :
    location = None

def check(x, t) :
    assert isinstance(x,t)

def check2(x, t) :
    assert (x is None) or isinstance(x,t)

def checkList(x, t) :
    check(x, list)
    for item in x :
        check(item, t)

class Program(ASTNode) :
    def __init__(self, topLevelItems) :
        checkList(topLevelItems, TopLevelItem)
        self.topLevelItems = topLevelItems

class TopLevelItem(ASTNode) :
    pass

class PredicateDef(TopLevelItem) :
    def __init__(self, name) :
        check(name, Identifier)
        self.name = name

class Identifier(ASTNode) :
    def __init__(self, s) :
        check(s, str)
        self.s = s

class InstanceDef(TopLevelItem) :
    def __init__(self, name, typeVars, typeArgs, typeConditions) :
        check(name, Identifier)
        checkList(typeVars, Identifier)
        checkList(typeArgs, Expression)
        checkList(typeConditions, TypeCondition)
        self.name = name
        self.typeVars = typeVars
        self.typeArgs = typeArgs
        self.typeConditions = typeConditions

class TypeCondition(ASTNode) :
    def __init__(self, name, typeArgs) :
        check(name, Identifier)
        checkList(typeArgs, Expression)
        self.name = name
        self.typeArgs = typeArgs

class RecordDef(TopLevelItem) :
    def __init__(self, name, typeVars, fields) :
        check(name, Identifier)
        checkList(typeVars, Identifier)
        checkList(fields, Field)
        self.name = name
        self.typeVars = typeVars
        self.fields = fields

class Field(ASTNode) :
    def __init__(self, name, type) :
        check(name, Identifier)
        check(type, Expression)
        self.name = name
        self.type = type

class Variable(ASTNode) :
    def __init__(self, name, type) :
        check(name, Identifier)
        check2(type, Expression)
        self.name = name
        self.type = type

class VariableDef(TopLevelItem) :
    def __init__(self, variables, exprList) :
        checkList(variables, Variable)
        checkList(exprList, Expression)
        self.variables = variables
        self.exprList = exprList

class ProcedureDef(TopLevelItem) :
    def __init__(self, name, typeVars, args, returnType,
                 typeConditions, body) :
        check(name, Identifier)
        checkList(typeVars, Identifier)
        checkList(args, Argument)
        check2(returnType, Expression)
        checkList(typeConditions, TypeCondition)
        check(body, Block)
        self.name = name
        self.typeVars = typeVars
        self.args = args
        self.returnType = returnType
        self.typeConditions = typeConditions
        self.body = body

class OverloadableDef(TopLevelItem) :
    def __init__(self, name) :
        check(name, Identifier)
        self.name = name

class OverloadDef(TopLevelItem) :
    def __init__(self, name, typeVars, args, returnType,
                 typeConditions, body) :
        check(name, Identifier)
        checkList(typeVars, Identifier)
        checkList(args, Argument)
        check2(returnType, Expression)
        checkList(typeConditions, TypeCondition)
        check(body, Block)
        self.name = name
        self.typeVars = typeVars
        self.args = args
        self.returnType = returnType
        self.typeConditions = typeConditions
        self.body = body

class Argument(ASTNode) :
    pass

class ValueArgument(Argument) :
    def __init__(self, variable) :
        check(variable, Variable)
        self.variable = variable

class TypeArgument(Argument) :
    def __init__(self, type) :
        check(type, Expression)
        self.type = type

class Statement(ASTNode) :
    pass

class Block(Statement) :
    def __init__(self, statements) :
        checkList(statements, Statement)
        self.statements = statements

class LocalVariableDef(Statement) :
    def __init__(self, variables, exprList) :
        checkList(variables, Variable)
        checkList(exprList, Expression)
        self.variables = variables
        self.exprList = exprList

class Assignment(Statement) :
    def __init__(self, assignables, exprList) :
        checkList(assignables, Expression)
        checkList(exprList, Expression)
        self.assignables = assignables
        self.exprList = exprList

class IfStatement(Statement) :
    def __init__(self, condition, thenPart, elsePart) :
        check(condition, Expression)
        check(thenPart, Statement)
        check2(elsePart, Statement)
        self.condition = condition
        self.thenPart = thenPart
        self.elsePart = elsePart

class BreakStatement(Statement) :
    pass

class ContinueStatement(Statement) :
    pass

class WhileStatement(Statement) :
    def __init__(self, condition, body) :
        check(condition, Expression)
        check(body, Statement)
        self.condition = condition
        self.body = body

class ForStatement(Statement) :
    def __init__(self, variables, expr, body) :
        checkList(variables, Variable)
        check(expr, Expression)
        check(body, Statement)
        self.variables = variables
        self.expr = expr
        self.body = body

class ReturnStatement(Statement) :
    def __init__(self, exprList) :
        checkList(exprList, Expression)
        self.exprList = exprList

class ExprStatement(Statement) :
    def __init__(self, expr) :
        check(expr, Expression)
        self.expr = expr

class Expression(ASTNode) :
    pass

class AddressOfExpr(Expression) :
    def __init__(self, expr) :
        check(expr, Expression)
        self.expr = expr

class IndexExpr(Expression) :
    def __init__(self, expr, indexes) :
        check2(expr, Expression)
        checkList(indexes, Expression)
        self.expr = expr
        self.indexes = indexes

class CallExpr(Expression) :
    def __init__(self, expr, args) :
        check2(expr, Expression)
        checkList(args, Expression)
        self.expr = expr
        self.args = args

class FieldRef(Expression) :
    def __init__(self, expr, name) :
        check2(expr, Expression)
        check(name, Identifier)
        self.expr = expr
        self.name = name

class TupleRef(Expression) :
    def __init__(self, expr, index) :
        check2(expr, Expression)
        check(index, int)
        self.expr = expr
        self.index = index

class PointerRef(Expression) :
    def __init__(self, expr) :
        check2(expr, Expression)
        self.expr = expr

class ArrayExpr(Expression) :
    def __init__(self, elements) :
        checkList(elements, Expression)
        self.elements = elements

class TupleExpr(Expression) :
    def __init__(self, elements) :
        checkList(elements, Expression)
        self.elements = elements

class NameRef(Expression) :
    def __init__(self, name) :
        check(name, Identifier)
        self.name = name

class BoolLiteral(Expression) :
    def __init__(self, value) :
        check(value, bool)
        self.value = value

class IntLiteral(Expression) :
    def __init__(self, value) :
        assert isinstance(value,int) or isinstance(value,long)
        self.value = value

class CharLiteral(Expression) :
    def __init__(self, value) :
        check(value, unicode)
        self.value = value

class StringLiteral(Expression) :
    def __init__(self, value) :
        check(value, unicode)
        self.value = value



#
# enable xprint support for ast
#

import clay.astprinter
