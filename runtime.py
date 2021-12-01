import antlr4
from antlr4.InputStream import InputStream
from example_grammarLexer import example_grammarLexer
from example_grammarParser import example_grammarParser
import sys

def handleMultiply(expr):
    multiplying = True
    value = 1 #initial value is set to 1 to handle the single expression correctly
    for child in expr.getChildren():
        if isinstance(child, antlr4.tree.Tree.TerminalNode):
            multiplying = child.getText() == "*"
        else:
            if multiplying:
                value *= int(child.getText())
            else:
                value /= int(child.getText())

    return value

def handleExpression(expr):
    '''
    We iterate over the children; where we find a multiplying expression,
    we evaluate it. Where we find an operator, we use it to set a flag indicating
    the next operation to perform.
    '''
    adding = True
    value = 0
    for child in expr.getChildren():
        if isinstance(child, antlr4.tree.Tree.TerminalNode):
            adding = child.getText() == "+"
        else:
            multValue = handleMultiply(child) 
            if adding:
                value += multValue
            else:
                value -= multValue
    print("Parsed expression %s has value %s" % (expr.getText(), value))

def main():
    input_stream = None
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())
    lexer = example_grammarLexer(input_stream) 
    stream = antlr4.CommonTokenStream(lexer) 
    parser = example_grammarParser(stream) 
    tree = parser.expression()
    handleExpression(tree) 

if __name__ == '__main__':
    main()

