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
    | ifElse
    | forLoop
    | whileLoop
    | assignment
    | print
    | return
    | break
    | continue
    ;

ifElse
    : IF OPEN_BRACKET_ROUND comparison CLOSE_BRACKET_ROUND codeBlock (
        ELSE codeBlock
    )?
    ;

forLoop
    : FOR ID ASSIGN range codeBlock
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
    : (ID | vectorElementReference | matrixElementReference) assignmentOperator expression SEMICOLON
    ;

print
    : PRINT expression (COMMA expression)* SEMICOLON
    ;

return
    : RETURN expression? SEMICOLON
    ;

expression
    : OPEN_BRACKET_ROUND expression CLOSE_BRACKET_ROUND
    | MINUS expression
    | expression MAT_TRANSPOSE_OP
    | expression op = (MULTIPLY | DIVIDE) expression
    | expression op = (MAT_MULTIPLY | MAT_DIVIDE) expression
    | expression op = (PLUS | MINUS) expression
    | expression op = (MAT_PLUS | MAT_MINUS) expression
    | ZEROS OPEN_BRACKET_ROUND INT CLOSE_BRACKET_ROUND
    | ONES OPEN_BRACKET_ROUND INT CLOSE_BRACKET_ROUND
    | EYE OPEN_BRACKET_ROUND INT CLOSE_BRACKET_ROUND
    | ID
    | INT
    | FLOAT
    | STRING
    | vectorElementReference
    | matrixElementReference
    | vector
    | matrix
    ;

break
    : BREAK SEMICOLON
    ;

continue
    : CONTINUE SEMICOLON
    ;

matrix
    : OPEN_BRACKET_SQUARE vector (COMMA vector)* CLOSE_BRACKET_SQUARE
    ;

vector
    : OPEN_BRACKET_SQUARE expression (COMMA expression)* CLOSE_BRACKET_SQUARE
    ;

matrixElementReference
    : ID OPEN_BRACKET_SQUARE INT COMMA INT CLOSE_BRACKET_SQUARE
    ;

vectorElementReference
    : ID OPEN_BRACKET_SQUARE INT CLOSE_BRACKET_SQUARE
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