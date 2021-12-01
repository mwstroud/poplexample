# Generated from example_grammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .example_grammarParser import example_grammarParser
else:
    from example_grammarParser import example_grammarParser

# This class defines a complete listener for a parse tree produced by example_grammarParser.
class example_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by example_grammarParser#expression.
    def enterExpression(self, ctx:example_grammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by example_grammarParser#expression.
    def exitExpression(self, ctx:example_grammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by example_grammarParser#multiplyingExpression.
    def enterMultiplyingExpression(self, ctx:example_grammarParser.MultiplyingExpressionContext):
        pass

    # Exit a parse tree produced by example_grammarParser#multiplyingExpression.
    def exitMultiplyingExpression(self, ctx:example_grammarParser.MultiplyingExpressionContext):
        pass


    # Enter a parse tree produced by example_grammarParser#number.
    def enterNumber(self, ctx:example_grammarParser.NumberContext):
        pass

    # Exit a parse tree produced by example_grammarParser#number.
    def exitNumber(self, ctx:example_grammarParser.NumberContext):
        pass



del example_grammarParser