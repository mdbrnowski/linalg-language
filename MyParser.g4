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
    : (ID | elementReference) assignmentOperator expression SEMICOLON
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
    | specialMatrixFunction
    | ID
    | INT
    | FLOAT
    | STRING
    | elementReference
    | elementReference
    | vector
    ;

specialMatrixFunction
    : (ZEROS | ONES | EYE) OPEN_BRACKET_ROUND INT CLOSE_BRACKET_ROUND
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
    : ID OPEN_BRACKET_SQUARE INT (COMMA INT)* CLOSE_BRACKET_SQUARE
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