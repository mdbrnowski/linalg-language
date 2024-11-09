// $antlr-format columnLimit 100, useTab false, minEmptyLines 1
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
    : expression relationOperator expression
    ;

assignment
    : (id | elementReference) assignmentOperator expression SEMICOLON
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
    : (ZEROS | ONES | EYE) OPEN_BRACKET_ROUND int CLOSE_BRACKET_ROUND
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
    : id OPEN_BRACKET_SQUARE int (COMMA int)* CLOSE_BRACKET_SQUARE
    ;

assignmentOperator
    : ASSIGN
    | ASSIGN_PLUS
    | ASSIGN_MINUS
    | ASSIGN_MULTIPLY
    | ASSIGN_DIVIDE
    ;

relationOperator
    : LE
    | GE
    | EQ
    | NE
    | LEQ
    | GEQ
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