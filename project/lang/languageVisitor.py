# Generated from language.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .languageParser import languageParser
else:
    from languageParser import languageParser

# This class defines a complete generic visitor for a parse tree produced by languageParser.


class languageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by languageParser#prog.
    def visitProg(self, ctx: languageParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by languageParser#stmt.
    def visitStmt(self, ctx: languageParser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by languageParser#declare.
    def visitDeclare(self, ctx: languageParser.DeclareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by languageParser#bind.
    def visitBind(self, ctx: languageParser.BindContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by languageParser#remove.
    def visitRemove(self, ctx: languageParser.RemoveContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by languageParser#add.
    def visitAdd(self, ctx: languageParser.AddContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by languageParser#expr.
    def visitExpr(self, ctx: languageParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by languageParser#set_expr.
    def visitSet_expr(self, ctx: languageParser.Set_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by languageParser#edge_expr.
    def visitEdge_expr(self, ctx: languageParser.Edge_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by languageParser#regexp.
    def visitRegexp(self, ctx: languageParser.RegexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by languageParser#range.
    def visitRange(self, ctx: languageParser.RangeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by languageParser#select.
    def visitSelect(self, ctx: languageParser.SelectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by languageParser#v_filter.
    def visitV_filter(self, ctx: languageParser.V_filterContext):
        return self.visitChildren(ctx)


del languageParser
