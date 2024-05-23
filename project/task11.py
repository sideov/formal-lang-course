from project.lang.languageLexer import languageLexer
from project.lang.languageParser import languageParser
from project.lang.languageVisitor import languageVisitor
from project.lang.languageListener import languageListener

from antlr4 import *
from antlr4.InputStream import InputStream


class CountNodesVisitor(languageVisitor):

    count = 0

    def __init__(self):
        super(languageVisitor, self).__init__()

    def enterEveryRule(self, rule):
        self.count += 1


class ParseTreeToProgVisitor(languageVisitor):

    progText = ""

    def __init__(self):
        super(languageVisitor, self).__init__()

    def enterEveryRule(self, rule):
        self.progText += rule.getText()


def get_parser(program: str) -> languageParser:
    return languageParser(CommonTokenStream(languageLexer(InputStream(program))))


def prog_to_tree(program: str) -> tuple[ParserRuleContext, bool]:
    parser = get_parser(program)
    ctx = parser.prog()
    return ctx, parser.getNumberOfSyntaxErrors() == 0


def nodes_count(tree: ParserRuleContext) -> int:
    visitor = CountNodesVisitor()
    tree.accept(visitor)
    return visitor.count


def tree_to_prog(tree: ParserRuleContext) -> str:
    visitor = ParseTreeToProgVisitor()
    tree.accept(visitor)
    return visitor.progText
