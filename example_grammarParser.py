# Generated from example_grammar.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("!\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\f\n\2\f\2\16")
        buf.write("\2\17\13\2\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\4")
        buf.write("\5\4\32\n\4\3\4\6\4\35\n\4\r\4\16\4\36\3\4\2\2\5\2\4\6")
        buf.write("\2\4\3\2\3\4\3\2\5\6\2!\2\b\3\2\2\2\4\20\3\2\2\2\6\31")
        buf.write("\3\2\2\2\b\r\5\4\3\2\t\n\t\2\2\2\n\f\5\4\3\2\13\t\3\2")
        buf.write("\2\2\f\17\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2")
        buf.write("\2\17\r\3\2\2\2\20\25\5\6\4\2\21\22\t\3\2\2\22\24\5\6")
        buf.write("\4\2\23\21\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3")
        buf.write("\2\2\2\26\5\3\2\2\2\27\25\3\2\2\2\30\32\7\4\2\2\31\30")
        buf.write("\3\2\2\2\31\32\3\2\2\2\32\34\3\2\2\2\33\35\7\7\2\2\34")
        buf.write("\33\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2")
        buf.write("\37\7\3\2\2\2\6\r\25\31\36")
        return buf.getvalue()


class example_grammarParser ( Parser ):

    grammarFileName = "example_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "TIMES", "DIV", "DIGIT", 
                      "WS" ]

    RULE_expression = 0
    RULE_multiplyingExpression = 1
    RULE_number = 2

    ruleNames =  [ "expression", "multiplyingExpression", "number" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    TIMES=3
    DIV=4
    DIGIT=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplyingExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(example_grammarParser.MultiplyingExpressionContext)
            else:
                return self.getTypedRuleContext(example_grammarParser.MultiplyingExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(example_grammarParser.PLUS)
            else:
                return self.getToken(example_grammarParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(example_grammarParser.MINUS)
            else:
                return self.getToken(example_grammarParser.MINUS, i)

        def getRuleIndex(self):
            return example_grammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = example_grammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.multiplyingExpression()
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==example_grammarParser.PLUS or _la==example_grammarParser.MINUS:
                self.state = 7
                _la = self._input.LA(1)
                if not(_la==example_grammarParser.PLUS or _la==example_grammarParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 8
                self.multiplyingExpression()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyingExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(example_grammarParser.NumberContext)
            else:
                return self.getTypedRuleContext(example_grammarParser.NumberContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(example_grammarParser.TIMES)
            else:
                return self.getToken(example_grammarParser.TIMES, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(example_grammarParser.DIV)
            else:
                return self.getToken(example_grammarParser.DIV, i)

        def getRuleIndex(self):
            return example_grammarParser.RULE_multiplyingExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplyingExpression" ):
                listener.enterMultiplyingExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplyingExpression" ):
                listener.exitMultiplyingExpression(self)




    def multiplyingExpression(self):

        localctx = example_grammarParser.MultiplyingExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_multiplyingExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.number()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==example_grammarParser.TIMES or _la==example_grammarParser.DIV:
                self.state = 15
                _la = self._input.LA(1)
                if not(_la==example_grammarParser.TIMES or _la==example_grammarParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 16
                self.number()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(example_grammarParser.MINUS, 0)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(example_grammarParser.DIGIT)
            else:
                return self.getToken(example_grammarParser.DIGIT, i)

        def getRuleIndex(self):
            return example_grammarParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = example_grammarParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==example_grammarParser.MINUS:
                self.state = 22
                self.match(example_grammarParser.MINUS)


            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self.match(example_grammarParser.DIGIT)
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==example_grammarParser.DIGIT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





