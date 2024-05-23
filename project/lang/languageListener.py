# Generated from language.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .languageParser import languageParser
else:
    from languageParser import languageParser


# This class defines a complete listener for a parse tree produced by languageParser.
class languageListener(ParseTreeListener):

    # Enter a parse tree produced by languageParser#prog.
    def enterProg(self, ctx: languageParser.ProgContext):
        pass

    # Exit a parse tree produced by languageParser#prog.
    def exitProg(self, ctx: languageParser.ProgContext):
        pass

    # Enter a parse tree produced by languageParser#stmt.
    def enterStmt(self, ctx: languageParser.StmtContext):
        pass

    # Exit a parse tree produced by languageParser#stmt.
    def exitStmt(self, ctx: languageParser.StmtContext):
        pass

    # Enter a parse tree produced by languageParser#declare.
    def enterDeclare(self, ctx: languageParser.DeclareContext):
        pass

    # Exit a parse tree produced by languageParser#declare.
    def exitDeclare(self, ctx: languageParser.DeclareContext):
        pass

    # Enter a parse tree produced by languageParser#bind.
    def enterBind(self, ctx: languageParser.BindContext):
        pass

    # Exit a parse tree produced by languageParser#bind.
    def exitBind(self, ctx: languageParser.BindContext):
        pass

    # Enter a parse tree produced by languageParser#remove.
    def enterRemove(self, ctx: languageParser.RemoveContext):
        pass

    # Exit a parse tree produced by languageParser#remove.
    def exitRemove(self, ctx: languageParser.RemoveContext):
        pass

    # Enter a parse tree produced by languageParser#add.
    def enterAdd(self, ctx: languageParser.AddContext):
        pass

    # Exit a parse tree produced by languageParser#add.
    def exitAdd(self, ctx: languageParser.AddContext):
        pass

    # Enter a parse tree produced by languageParser#expr.
    def enterExpr(self, ctx: languageParser.ExprContext):
        pass

    # Exit a parse tree produced by languageParser#expr.
    def exitExpr(self, ctx: languageParser.ExprContext):
        pass

    # Enter a parse tree produced by languageParser#set_expr.
    def enterSet_expr(self, ctx: languageParser.Set_exprContext):
        pass

    # Exit a parse tree produced by languageParser#set_expr.
    def exitSet_expr(self, ctx: languageParser.Set_exprContext):
        pass

    # Enter a parse tree produced by languageParser#edge_expr.
    def enterEdge_expr(self, ctx: languageParser.Edge_exprContext):
        pass

    # Exit a parse tree produced by languageParser#edge_expr.
    def exitEdge_expr(self, ctx: languageParser.Edge_exprContext):
        pass

    # Enter a parse tree produced by languageParser#regexp.
    def enterRegexp(self, ctx: languageParser.RegexpContext):
        pass

    # Exit a parse tree produced by languageParser#regexp.
    def exitRegexp(self, ctx: languageParser.RegexpContext):
        pass

    # Enter a parse tree produced by languageParser#range.
    def enterRange(self, ctx: languageParser.RangeContext):
        pass

    # Exit a parse tree produced by languageParser#range.
    def exitRange(self, ctx: languageParser.RangeContext):
        pass

    # Enter a parse tree produced by languageParser#select.
    def enterSelect(self, ctx: languageParser.SelectContext):
        pass

    # Exit a parse tree produced by languageParser#select.
    def exitSelect(self, ctx: languageParser.SelectContext):
        pass

    # Enter a parse tree produced by languageParser#v_filter.
    def enterV_filter(self, ctx: languageParser.V_filterContext):
        pass

    # Exit a parse tree produced by languageParser#v_filter.
    def exitV_filter(self, ctx: languageParser.V_filterContext):
        pass


del languageParser
