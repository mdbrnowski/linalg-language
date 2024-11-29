# Generated from MyParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,234,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,1,1,1,5,1,57,8,1,10,1,12,1,60,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,71,8,1,1,2,1,2,1,2,3,2,76,8,2,1,3,1,3,1,3,1,3,1,3,1,
        4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,
        8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,3,10,110,8,10,1,10,1,
        10,1,10,1,10,1,10,1,10,3,10,118,8,10,1,10,1,10,1,10,1,10,3,10,124,
        8,10,1,11,1,11,1,11,1,11,5,11,130,8,11,10,11,12,11,133,9,11,1,11,
        1,11,1,12,1,12,3,12,139,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,157,8,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        5,13,173,8,13,10,13,12,13,176,9,13,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,5,14,188,8,14,10,14,12,14,191,9,14,1,14,1,14,
        3,14,195,8,14,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,
        5,17,207,8,17,10,17,12,17,210,9,17,1,17,1,17,1,18,1,18,1,18,1,18,
        1,18,5,18,219,8,18,10,18,12,18,222,9,18,1,18,1,18,1,19,1,19,1,20,
        1,20,1,21,1,21,1,22,1,22,1,22,0,1,26,23,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,0,7,1,0,17,22,1,0,13,16,1,
        0,5,6,1,0,9,10,1,0,3,4,1,0,7,8,1,0,40,41,243,0,49,1,0,0,0,2,70,1,
        0,0,0,4,72,1,0,0,0,6,77,1,0,0,0,8,82,1,0,0,0,10,84,1,0,0,0,12,87,
        1,0,0,0,14,93,1,0,0,0,16,97,1,0,0,0,18,103,1,0,0,0,20,123,1,0,0,
        0,22,125,1,0,0,0,24,136,1,0,0,0,26,156,1,0,0,0,28,194,1,0,0,0,30,
        196,1,0,0,0,32,199,1,0,0,0,34,202,1,0,0,0,36,213,1,0,0,0,38,225,
        1,0,0,0,40,227,1,0,0,0,42,229,1,0,0,0,44,231,1,0,0,0,46,48,3,2,1,
        0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,
        1,0,0,0,51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,58,5,27,0,0,
        55,57,3,2,1,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,
        0,0,0,59,61,1,0,0,0,60,58,1,0,0,0,61,71,5,28,0,0,62,71,3,4,2,0,63,
        71,3,12,6,0,64,71,3,16,8,0,65,71,3,20,10,0,66,71,3,22,11,0,67,71,
        3,24,12,0,68,71,3,30,15,0,69,71,3,32,16,0,70,54,1,0,0,0,70,62,1,
        0,0,0,70,63,1,0,0,0,70,64,1,0,0,0,70,65,1,0,0,0,70,66,1,0,0,0,70,
        67,1,0,0,0,70,68,1,0,0,0,70,69,1,0,0,0,71,3,1,0,0,0,72,73,3,6,3,
        0,73,75,3,8,4,0,74,76,3,10,5,0,75,74,1,0,0,0,75,76,1,0,0,0,76,5,
        1,0,0,0,77,78,5,32,0,0,78,79,5,23,0,0,79,80,3,18,9,0,80,81,5,24,
        0,0,81,7,1,0,0,0,82,83,3,2,1,0,83,9,1,0,0,0,84,85,5,33,0,0,85,86,
        3,2,1,0,86,11,1,0,0,0,87,88,5,34,0,0,88,89,3,38,19,0,89,90,5,12,
        0,0,90,91,3,14,7,0,91,92,3,2,1,0,92,13,1,0,0,0,93,94,3,26,13,0,94,
        95,5,29,0,0,95,96,3,26,13,0,96,15,1,0,0,0,97,98,5,35,0,0,98,99,5,
        23,0,0,99,100,3,18,9,0,100,101,5,24,0,0,101,102,3,2,1,0,102,17,1,
        0,0,0,103,104,3,26,13,0,104,105,7,0,0,0,105,106,3,26,13,0,106,19,
        1,0,0,0,107,110,3,38,19,0,108,110,3,36,18,0,109,107,1,0,0,0,109,
        108,1,0,0,0,110,111,1,0,0,0,111,112,5,12,0,0,112,113,3,26,13,0,113,
        114,5,31,0,0,114,124,1,0,0,0,115,118,3,38,19,0,116,118,3,36,18,0,
        117,115,1,0,0,0,117,116,1,0,0,0,118,119,1,0,0,0,119,120,7,1,0,0,
        120,121,3,26,13,0,121,122,5,31,0,0,122,124,1,0,0,0,123,109,1,0,0,
        0,123,117,1,0,0,0,124,21,1,0,0,0,125,126,5,42,0,0,126,131,3,26,13,
        0,127,128,5,30,0,0,128,130,3,26,13,0,129,127,1,0,0,0,130,133,1,0,
        0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,
        0,0,134,135,5,31,0,0,135,23,1,0,0,0,136,138,5,38,0,0,137,139,3,26,
        13,0,138,137,1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,0,140,141,5,31,
        0,0,141,25,1,0,0,0,142,143,6,13,-1,0,143,144,5,23,0,0,144,145,3,
        26,13,0,145,146,5,24,0,0,146,157,1,0,0,0,147,148,5,4,0,0,148,157,
        3,26,13,13,149,157,3,28,14,0,150,157,3,38,19,0,151,157,3,40,20,0,
        152,157,3,42,21,0,153,157,3,44,22,0,154,157,3,36,18,0,155,157,3,
        34,17,0,156,142,1,0,0,0,156,147,1,0,0,0,156,149,1,0,0,0,156,150,
        1,0,0,0,156,151,1,0,0,0,156,152,1,0,0,0,156,153,1,0,0,0,156,154,
        1,0,0,0,156,155,1,0,0,0,157,174,1,0,0,0,158,159,10,11,0,0,159,160,
        7,2,0,0,160,173,3,26,13,12,161,162,10,10,0,0,162,163,7,3,0,0,163,
        173,3,26,13,11,164,165,10,9,0,0,165,166,7,4,0,0,166,173,3,26,13,
        10,167,168,10,8,0,0,168,169,7,5,0,0,169,173,3,26,13,9,170,171,10,
        12,0,0,171,173,5,11,0,0,172,158,1,0,0,0,172,161,1,0,0,0,172,164,
        1,0,0,0,172,167,1,0,0,0,172,170,1,0,0,0,173,176,1,0,0,0,174,172,
        1,0,0,0,174,175,1,0,0,0,175,27,1,0,0,0,176,174,1,0,0,0,177,178,5,
        39,0,0,178,179,5,23,0,0,179,180,3,26,13,0,180,181,5,24,0,0,181,195,
        1,0,0,0,182,183,7,6,0,0,183,184,5,23,0,0,184,189,3,26,13,0,185,186,
        5,30,0,0,186,188,3,26,13,0,187,185,1,0,0,0,188,191,1,0,0,0,189,187,
        1,0,0,0,189,190,1,0,0,0,190,192,1,0,0,0,191,189,1,0,0,0,192,193,
        5,24,0,0,193,195,1,0,0,0,194,177,1,0,0,0,194,182,1,0,0,0,195,29,
        1,0,0,0,196,197,5,36,0,0,197,198,5,31,0,0,198,31,1,0,0,0,199,200,
        5,37,0,0,200,201,5,31,0,0,201,33,1,0,0,0,202,203,5,25,0,0,203,208,
        3,26,13,0,204,205,5,30,0,0,205,207,3,26,13,0,206,204,1,0,0,0,207,
        210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,211,1,0,0,0,210,
        208,1,0,0,0,211,212,5,26,0,0,212,35,1,0,0,0,213,214,3,38,19,0,214,
        215,5,25,0,0,215,220,3,26,13,0,216,217,5,30,0,0,217,219,3,26,13,
        0,218,216,1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,
        0,221,223,1,0,0,0,222,220,1,0,0,0,223,224,5,26,0,0,224,37,1,0,0,
        0,225,226,5,43,0,0,226,39,1,0,0,0,227,228,5,44,0,0,228,41,1,0,0,
        0,229,230,5,45,0,0,230,43,1,0,0,0,231,232,5,46,0,0,232,45,1,0,0,
        0,16,49,58,70,75,109,117,123,131,138,156,172,174,189,194,208,220
    ]

class MyParser ( Parser ):

    grammarFileName = "MyParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'.+'", "'.-'", "'.*'", "'./'", "'''", 
                     "'='", "'+='", "'-='", "'*='", "'/='", "'<'", "'>'", 
                     "'=='", "'!='", "'<='", "'>='", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "':'", "','", "';'", "'if'", "'else'", 
                     "'for'", "'while'", "'break'", "'continue'", "'return'", 
                     "'eye'", "'zeros'", "'ones'", "'print'" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "COMMENT", "PLUS", "MINUS", 
                      "MULTIPLY", "DIVIDE", "MAT_PLUS", "MAT_MINUS", "MAT_MULTIPLY", 
                      "MAT_DIVIDE", "MAT_TRANSPOSE_OP", "ASSIGN", "ASSIGN_PLUS", 
                      "ASSIGN_MINUS", "ASSIGN_MULTIPLY", "ASSIGN_DIVIDE", 
                      "LE", "GE", "EQ", "NE", "LEQ", "GEQ", "OPEN_BRACKET_ROUND", 
                      "CLOSE_BRACKET_ROUND", "OPEN_BRACKET_SQUARE", "CLOSE_BRACKET_SQUARE", 
                      "OPEN_BRACKET_CURLY", "CLOSE_BRACKET_CURLY", "RANGE_OP", 
                      "COMMA", "SEMICOLON", "IF", "ELSE", "FOR", "WHILE", 
                      "BREAK", "CONTINUE", "RETURN", "EYE", "ZEROS", "ONES", 
                      "PRINT", "ID", "INT", "FLOAT", "STRING" ]

    RULE_program = 0
    RULE_codeBlock = 1
    RULE_ifThenElse = 2
    RULE_if = 3
    RULE_then = 4
    RULE_else = 5
    RULE_forLoop = 6
    RULE_range = 7
    RULE_whileLoop = 8
    RULE_comparison = 9
    RULE_assignment = 10
    RULE_print = 11
    RULE_return = 12
    RULE_expression = 13
    RULE_specialMatrixFunction = 14
    RULE_break = 15
    RULE_continue = 16
    RULE_vector = 17
    RULE_elementReference = 18
    RULE_id = 19
    RULE_int = 20
    RULE_float = 21
    RULE_string = 22

    ruleNames =  [ "program", "codeBlock", "ifThenElse", "if", "then", "else", 
                   "forLoop", "range", "whileLoop", "comparison", "assignment", 
                   "print", "return", "expression", "specialMatrixFunction", 
                   "break", "continue", "vector", "elementReference", "id", 
                   "int", "float", "string" ]

    EOF = Token.EOF
    WHITESPACE=1
    COMMENT=2
    PLUS=3
    MINUS=4
    MULTIPLY=5
    DIVIDE=6
    MAT_PLUS=7
    MAT_MINUS=8
    MAT_MULTIPLY=9
    MAT_DIVIDE=10
    MAT_TRANSPOSE_OP=11
    ASSIGN=12
    ASSIGN_PLUS=13
    ASSIGN_MINUS=14
    ASSIGN_MULTIPLY=15
    ASSIGN_DIVIDE=16
    LE=17
    GE=18
    EQ=19
    NE=20
    LEQ=21
    GEQ=22
    OPEN_BRACKET_ROUND=23
    CLOSE_BRACKET_ROUND=24
    OPEN_BRACKET_SQUARE=25
    CLOSE_BRACKET_SQUARE=26
    OPEN_BRACKET_CURLY=27
    CLOSE_BRACKET_CURLY=28
    RANGE_OP=29
    COMMA=30
    SEMICOLON=31
    IF=32
    ELSE=33
    FOR=34
    WHILE=35
    BREAK=36
    CONTINUE=37
    RETURN=38
    EYE=39
    ZEROS=40
    ONES=41
    PRINT=42
    ID=43
    INT=44
    FLOAT=45
    STRING=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MyParser.EOF, 0)

        def codeBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.CodeBlockContext)
            else:
                return self.getTypedRuleContext(MyParser.CodeBlockContext,i)


        def getRuleIndex(self):
            return MyParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13731144663040) != 0):
                self.state = 46
                self.codeBlock()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(MyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET_CURLY(self):
            return self.getToken(MyParser.OPEN_BRACKET_CURLY, 0)

        def CLOSE_BRACKET_CURLY(self):
            return self.getToken(MyParser.CLOSE_BRACKET_CURLY, 0)

        def codeBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.CodeBlockContext)
            else:
                return self.getTypedRuleContext(MyParser.CodeBlockContext,i)


        def ifThenElse(self):
            return self.getTypedRuleContext(MyParser.IfThenElseContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(MyParser.ForLoopContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(MyParser.WhileLoopContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MyParser.AssignmentContext,0)


        def print_(self):
            return self.getTypedRuleContext(MyParser.PrintContext,0)


        def return_(self):
            return self.getTypedRuleContext(MyParser.ReturnContext,0)


        def break_(self):
            return self.getTypedRuleContext(MyParser.BreakContext,0)


        def continue_(self):
            return self.getTypedRuleContext(MyParser.ContinueContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_codeBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeBlock" ):
                listener.enterCodeBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeBlock" ):
                listener.exitCodeBlock(self)




    def codeBlock(self):

        localctx = MyParser.CodeBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_codeBlock)
        self._la = 0 # Token type
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(MyParser.OPEN_BRACKET_CURLY)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13731144663040) != 0):
                    self.state = 55
                    self.codeBlock()
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 61
                self.match(MyParser.CLOSE_BRACKET_CURLY)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.ifThenElse()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.forLoop()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.whileLoop()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                self.assignment()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.print_()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 7)
                self.state = 67
                self.return_()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 8)
                self.state = 68
                self.break_()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 9)
                self.state = 69
                self.continue_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfThenElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(MyParser.IfContext,0)


        def then(self):
            return self.getTypedRuleContext(MyParser.ThenContext,0)


        def else_(self):
            return self.getTypedRuleContext(MyParser.ElseContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_ifThenElse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfThenElse" ):
                listener.enterIfThenElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfThenElse" ):
                listener.exitIfThenElse(self)




    def ifThenElse(self):

        localctx = MyParser.IfThenElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifThenElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.if_()
            self.state = 73
            self.then()
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 74
                self.else_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MyParser.IF, 0)

        def OPEN_BRACKET_ROUND(self):
            return self.getToken(MyParser.OPEN_BRACKET_ROUND, 0)

        def comparison(self):
            return self.getTypedRuleContext(MyParser.ComparisonContext,0)


        def CLOSE_BRACKET_ROUND(self):
            return self.getToken(MyParser.CLOSE_BRACKET_ROUND, 0)

        def getRuleIndex(self):
            return MyParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)




    def if_(self):

        localctx = MyParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(MyParser.IF)
            self.state = 78
            self.match(MyParser.OPEN_BRACKET_ROUND)
            self.state = 79
            self.comparison()
            self.state = 80
            self.match(MyParser.CLOSE_BRACKET_ROUND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def codeBlock(self):
            return self.getTypedRuleContext(MyParser.CodeBlockContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_then

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThen" ):
                listener.enterThen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThen" ):
                listener.exitThen(self)




    def then(self):

        localctx = MyParser.ThenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_then)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.codeBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MyParser.ELSE, 0)

        def codeBlock(self):
            return self.getTypedRuleContext(MyParser.CodeBlockContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)




    def else_(self):

        localctx = MyParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(MyParser.ELSE)
            self.state = 85
            self.codeBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MyParser.FOR, 0)

        def id_(self):
            return self.getTypedRuleContext(MyParser.IdContext,0)


        def ASSIGN(self):
            return self.getToken(MyParser.ASSIGN, 0)

        def range_(self):
            return self.getTypedRuleContext(MyParser.RangeContext,0)


        def codeBlock(self):
            return self.getTypedRuleContext(MyParser.CodeBlockContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)




    def forLoop(self):

        localctx = MyParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(MyParser.FOR)
            self.state = 88
            self.id_()
            self.state = 89
            self.match(MyParser.ASSIGN)
            self.state = 90
            self.range_()
            self.state = 91
            self.codeBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)


        def RANGE_OP(self):
            return self.getToken(MyParser.RANGE_OP, 0)

        def getRuleIndex(self):
            return MyParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)




    def range_(self):

        localctx = MyParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.expression(0)
            self.state = 94
            self.match(MyParser.RANGE_OP)
            self.state = 95
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MyParser.WHILE, 0)

        def OPEN_BRACKET_ROUND(self):
            return self.getToken(MyParser.OPEN_BRACKET_ROUND, 0)

        def comparison(self):
            return self.getTypedRuleContext(MyParser.ComparisonContext,0)


        def CLOSE_BRACKET_ROUND(self):
            return self.getToken(MyParser.CLOSE_BRACKET_ROUND, 0)

        def codeBlock(self):
            return self.getTypedRuleContext(MyParser.CodeBlockContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)




    def whileLoop(self):

        localctx = MyParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(MyParser.WHILE)
            self.state = 98
            self.match(MyParser.OPEN_BRACKET_ROUND)
            self.state = 99
            self.comparison()
            self.state = 100
            self.match(MyParser.CLOSE_BRACKET_ROUND)
            self.state = 101
            self.codeBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)


        def LE(self):
            return self.getToken(MyParser.LE, 0)

        def GE(self):
            return self.getToken(MyParser.GE, 0)

        def EQ(self):
            return self.getToken(MyParser.EQ, 0)

        def NE(self):
            return self.getToken(MyParser.NE, 0)

        def LEQ(self):
            return self.getToken(MyParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(MyParser.GEQ, 0)

        def getRuleIndex(self):
            return MyParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = MyParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.expression(0)
            self.state = 104
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 105
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyParser.RULE_assignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CompoundAssignmentContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)

        def SEMICOLON(self):
            return self.getToken(MyParser.SEMICOLON, 0)
        def ASSIGN_PLUS(self):
            return self.getToken(MyParser.ASSIGN_PLUS, 0)
        def ASSIGN_MINUS(self):
            return self.getToken(MyParser.ASSIGN_MINUS, 0)
        def ASSIGN_MULTIPLY(self):
            return self.getToken(MyParser.ASSIGN_MULTIPLY, 0)
        def ASSIGN_DIVIDE(self):
            return self.getToken(MyParser.ASSIGN_DIVIDE, 0)
        def id_(self):
            return self.getTypedRuleContext(MyParser.IdContext,0)

        def elementReference(self):
            return self.getTypedRuleContext(MyParser.ElementReferenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundAssignment" ):
                listener.enterCompoundAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundAssignment" ):
                listener.exitCompoundAssignment(self)


    class SimpleAssignmentContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ASSIGN(self):
            return self.getToken(MyParser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)

        def SEMICOLON(self):
            return self.getToken(MyParser.SEMICOLON, 0)
        def id_(self):
            return self.getTypedRuleContext(MyParser.IdContext,0)

        def elementReference(self):
            return self.getTypedRuleContext(MyParser.ElementReferenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleAssignment" ):
                listener.enterSimpleAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleAssignment" ):
                listener.exitSimpleAssignment(self)



    def assignment(self):

        localctx = MyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = MyParser.SimpleAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 107
                    self.id_()
                    pass

                elif la_ == 2:
                    self.state = 108
                    self.elementReference()
                    pass


                self.state = 111
                self.match(MyParser.ASSIGN)
                self.state = 112
                self.expression(0)
                self.state = 113
                self.match(MyParser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = MyParser.CompoundAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 115
                    self.id_()
                    pass

                elif la_ == 2:
                    self.state = 116
                    self.elementReference()
                    pass


                self.state = 119
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 120
                self.expression(0)
                self.state = 121
                self.match(MyParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MyParser.PRINT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)


        def SEMICOLON(self):
            return self.getToken(MyParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.COMMA)
            else:
                return self.getToken(MyParser.COMMA, i)

        def getRuleIndex(self):
            return MyParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print_(self):

        localctx = MyParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(MyParser.PRINT)
            self.state = 126
            self.expression(0)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 127
                self.match(MyParser.COMMA)
                self.state = 128
                self.expression(0)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(MyParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MyParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(MyParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)




    def return_(self):

        localctx = MyParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MyParser.RETURN)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135789727973392) != 0):
                self.state = 137
                self.expression(0)


            self.state = 140
            self.match(MyParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BinaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)

        def MULTIPLY(self):
            return self.getToken(MyParser.MULTIPLY, 0)
        def DIVIDE(self):
            return self.getToken(MyParser.DIVIDE, 0)
        def MAT_MULTIPLY(self):
            return self.getToken(MyParser.MAT_MULTIPLY, 0)
        def MAT_DIVIDE(self):
            return self.getToken(MyParser.MAT_DIVIDE, 0)
        def PLUS(self):
            return self.getToken(MyParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(MyParser.MINUS, 0)
        def MAT_PLUS(self):
            return self.getToken(MyParser.MAT_PLUS, 0)
        def MAT_MINUS(self):
            return self.getToken(MyParser.MAT_MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryExpression" ):
                listener.enterBinaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryExpression" ):
                listener.exitBinaryExpression(self)


    class ParenthesesExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPEN_BRACKET_ROUND(self):
            return self.getToken(MyParser.OPEN_BRACKET_ROUND, 0)
        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)

        def CLOSE_BRACKET_ROUND(self):
            return self.getToken(MyParser.CLOSE_BRACKET_ROUND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesesExpression" ):
                listener.enterParenthesesExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesesExpression" ):
                listener.exitParenthesesExpression(self)


    class TransposeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)

        def MAT_TRANSPOSE_OP(self):
            return self.getToken(MyParser.MAT_TRANSPOSE_OP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransposeExpression" ):
                listener.enterTransposeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransposeExpression" ):
                listener.exitTransposeExpression(self)


    class MinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(MyParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinusExpression" ):
                listener.enterMinusExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinusExpression" ):
                listener.exitMinusExpression(self)


    class SingleExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def specialMatrixFunction(self):
            return self.getTypedRuleContext(MyParser.SpecialMatrixFunctionContext,0)

        def id_(self):
            return self.getTypedRuleContext(MyParser.IdContext,0)

        def int_(self):
            return self.getTypedRuleContext(MyParser.IntContext,0)

        def float_(self):
            return self.getTypedRuleContext(MyParser.FloatContext,0)

        def string(self):
            return self.getTypedRuleContext(MyParser.StringContext,0)

        def elementReference(self):
            return self.getTypedRuleContext(MyParser.ElementReferenceContext,0)

        def vector(self):
            return self.getTypedRuleContext(MyParser.VectorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleExpression" ):
                listener.enterSingleExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleExpression" ):
                listener.exitSingleExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = MyParser.ParenthesesExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 143
                self.match(MyParser.OPEN_BRACKET_ROUND)
                self.state = 144
                self.expression(0)
                self.state = 145
                self.match(MyParser.CLOSE_BRACKET_ROUND)
                pass

            elif la_ == 2:
                localctx = MyParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                self.match(MyParser.MINUS)
                self.state = 148
                self.expression(13)
                pass

            elif la_ == 3:
                localctx = MyParser.SingleExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.specialMatrixFunction()
                pass

            elif la_ == 4:
                localctx = MyParser.SingleExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.id_()
                pass

            elif la_ == 5:
                localctx = MyParser.SingleExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.int_()
                pass

            elif la_ == 6:
                localctx = MyParser.SingleExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 152
                self.float_()
                pass

            elif la_ == 7:
                localctx = MyParser.SingleExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.string()
                pass

            elif la_ == 8:
                localctx = MyParser.SingleExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 154
                self.elementReference()
                pass

            elif la_ == 9:
                localctx = MyParser.SingleExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                self.vector()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 172
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = MyParser.BinaryExpressionContext(self, MyParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 158
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 159
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 160
                        self.expression(12)
                        pass

                    elif la_ == 2:
                        localctx = MyParser.BinaryExpressionContext(self, MyParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 161
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 162
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 163
                        self.expression(11)
                        pass

                    elif la_ == 3:
                        localctx = MyParser.BinaryExpressionContext(self, MyParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 164
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 165
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 166
                        self.expression(10)
                        pass

                    elif la_ == 4:
                        localctx = MyParser.BinaryExpressionContext(self, MyParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 167
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 168
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 169
                        self.expression(9)
                        pass

                    elif la_ == 5:
                        localctx = MyParser.TransposeExpressionContext(self, MyParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 170
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 171
                        self.match(MyParser.MAT_TRANSPOSE_OP)
                        pass

             
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SpecialMatrixFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EYE(self):
            return self.getToken(MyParser.EYE, 0)

        def OPEN_BRACKET_ROUND(self):
            return self.getToken(MyParser.OPEN_BRACKET_ROUND, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)


        def CLOSE_BRACKET_ROUND(self):
            return self.getToken(MyParser.CLOSE_BRACKET_ROUND, 0)

        def ZEROS(self):
            return self.getToken(MyParser.ZEROS, 0)

        def ONES(self):
            return self.getToken(MyParser.ONES, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.COMMA)
            else:
                return self.getToken(MyParser.COMMA, i)

        def getRuleIndex(self):
            return MyParser.RULE_specialMatrixFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecialMatrixFunction" ):
                listener.enterSpecialMatrixFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecialMatrixFunction" ):
                listener.exitSpecialMatrixFunction(self)




    def specialMatrixFunction(self):

        localctx = MyParser.SpecialMatrixFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_specialMatrixFunction)
        self._la = 0 # Token type
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(MyParser.EYE)
                self.state = 178
                self.match(MyParser.OPEN_BRACKET_ROUND)
                self.state = 179
                self.expression(0)
                self.state = 180
                self.match(MyParser.CLOSE_BRACKET_ROUND)
                pass
            elif token in [40, 41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                _la = self._input.LA(1)
                if not(_la==40 or _la==41):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 183
                self.match(MyParser.OPEN_BRACKET_ROUND)
                self.state = 184
                self.expression(0)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 185
                    self.match(MyParser.COMMA)
                    self.state = 186
                    self.expression(0)
                    self.state = 191
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 192
                self.match(MyParser.CLOSE_BRACKET_ROUND)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MyParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MyParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MyParser.RULE_break

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)




    def break_(self):

        localctx = MyParser.BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(MyParser.BREAK)
            self.state = 197
            self.match(MyParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MyParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MyParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MyParser.RULE_continue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue" ):
                listener.enterContinue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue" ):
                listener.exitContinue(self)




    def continue_(self):

        localctx = MyParser.ContinueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(MyParser.CONTINUE)
            self.state = 200
            self.match(MyParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET_SQUARE(self):
            return self.getToken(MyParser.OPEN_BRACKET_SQUARE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)


        def CLOSE_BRACKET_SQUARE(self):
            return self.getToken(MyParser.CLOSE_BRACKET_SQUARE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.COMMA)
            else:
                return self.getToken(MyParser.COMMA, i)

        def getRuleIndex(self):
            return MyParser.RULE_vector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVector" ):
                listener.enterVector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVector" ):
                listener.exitVector(self)




    def vector(self):

        localctx = MyParser.VectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_vector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(MyParser.OPEN_BRACKET_SQUARE)
            self.state = 203
            self.expression(0)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 204
                self.match(MyParser.COMMA)
                self.state = 205
                self.expression(0)
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 211
            self.match(MyParser.CLOSE_BRACKET_SQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(MyParser.IdContext,0)


        def OPEN_BRACKET_SQUARE(self):
            return self.getToken(MyParser.OPEN_BRACKET_SQUARE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)


        def CLOSE_BRACKET_SQUARE(self):
            return self.getToken(MyParser.CLOSE_BRACKET_SQUARE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.COMMA)
            else:
                return self.getToken(MyParser.COMMA, i)

        def getRuleIndex(self):
            return MyParser.RULE_elementReference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementReference" ):
                listener.enterElementReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementReference" ):
                listener.exitElementReference(self)




    def elementReference(self):

        localctx = MyParser.ElementReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_elementReference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.id_()
            self.state = 214
            self.match(MyParser.OPEN_BRACKET_SQUARE)
            self.state = 215
            self.expression(0)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 216
                self.match(MyParser.COMMA)
                self.state = 217
                self.expression(0)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
            self.match(MyParser.CLOSE_BRACKET_SQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyParser.ID, 0)

        def getRuleIndex(self):
            return MyParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)




    def id_(self):

        localctx = MyParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MyParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MyParser.INT, 0)

        def getRuleIndex(self):
            return MyParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)




    def int_(self):

        localctx = MyParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(MyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(MyParser.FLOAT, 0)

        def getRuleIndex(self):
            return MyParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)




    def float_(self):

        localctx = MyParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MyParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MyParser.STRING, 0)

        def getRuleIndex(self):
            return MyParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = MyParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(MyParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 12)
         




