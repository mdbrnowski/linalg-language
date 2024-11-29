// $antlr-format columnLimit 120, useTab false, minEmptyLines 1
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true
// $antlr-format alignSemicolons hanging, alignColons hanging

parser grammar MyParser;

options {
    tokenVocab = MyLexer;
}

program
    : (codeBlock)* EOF
    ;

codeBlock
    : OPEN_BRACKET_CURLY (codeBlock)* CLOSE_BRACKET_CURLY
    | ifThenElse
    | forLoop
    | whileLoop
    | assignment
    | print
    | return
    | break
    | continue
    ;

ifThenElse
    : if then else?
    ;

if
    : IF OPEN_BRACKET_ROUND comparison CLOSE_BRACKET_ROUND
    ;

then
    : codeBlock
    ;

else
    : ELSE codeBlock
    ;

forLoop
    : FOR id ASSIGN range codeBlock
    ;

range
    : expression RANGE_OP expression
    ;

whileLoop
    : WHILE OPEN_BRACKET_ROUND comparison CLOSE_BRACKET_ROUND codeBlock
    ;

comparison
    : expression (LE | GE | EQ | NE | LEQ | GEQ) expression
    ;

assignment
    : (id | elementReference) ASSIGN expression SEMICOLON # simpleAssignment
    | (id | elementReference) (
        ASSIGN_PLUS
        | ASSIGN_MINUS
        | ASSIGN_MULTIPLY
        | ASSIGN_DIVIDE
    ) expression SEMICOLON # compoundAssignment
    ;

print
    : PRINT expression (COMMA expression)* SEMICOLON
    ;

return
    : RETURN expression? SEMICOLON
    ;

expression
    : OPEN_BRACKET_ROUND expression CLOSE_BRACKET_ROUND      # parenthesesExpression
    | MINUS expression                                       # minusExpression
    | expression MAT_TRANSPOSE_OP                            # transposeExpression
    | expression op = (MULTIPLY | DIVIDE) expression         # binaryExpression
    | expression op = (MAT_MULTIPLY | MAT_DIVIDE) expression # binaryExpression
    | expression op = (PLUS | MINUS) expression              # binaryExpression
    | expression op = (MAT_PLUS | MAT_MINUS) expression      # binaryExpression
    | specialMatrixFunction                                  # singleExpression
    | id                                                     # singleExpression
    | int                                                    # singleExpression
    | float                                                  # singleExpression
    | string                                                 # singleExpression
    | elementReference                                       # singleExpression
    | vector                                                 # singleExpression
    ;

specialMatrixFunction
    : EYE OPEN_BRACKET_ROUND expression CLOSE_BRACKET_ROUND
    | (ZEROS | ONES) OPEN_BRACKET_ROUND expression (COMMA expression)* CLOSE_BRACKET_ROUND
    ;

break
    : BREAK SEMICOLON
    ;

continue
    : CONTINUE SEMICOLON
    ;

vector
    : OPEN_BRACKET_SQUARE expression (COMMA expression)* CLOSE_BRACKET_SQUARE
    ;

elementReference
    : id OPEN_BRACKET_SQUARE expression (COMMA expression)* CLOSE_BRACKET_SQUARE
    ;

id
    : ID
    ;

int
    : INT
    ;

float
    : FLOAT
    ;

string
    : STRING
    ;