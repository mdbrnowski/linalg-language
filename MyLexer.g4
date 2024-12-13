// $antlr-format columnLimit 120, useTab false, minEmptyLines 0
// $antlr-format alignSemicolons none, alignColons trailing
// $antlr-format alignLexerCommands true, alignLabels true, alignTrailers true

lexer grammar MyLexer;

WHITESPACE: [ \t\r\n]+ -> skip;

COMMENT: '#' ~[\r\n]* -> skip;

PLUS     : '+';
MINUS    : '-';
MULTIPLY : '*';
DIVIDE   : '/';

MAT_PLUS     : '.+';
MAT_MINUS    : '.-';
MAT_MULTIPLY : '.*';
MAT_DIVIDE   : './';

MAT_TRANSPOSE_OP: '\'';

ASSIGN          : '=';
ASSIGN_PLUS     : '+=';
ASSIGN_MINUS    : '-=';
ASSIGN_MULTIPLY : '*=';
ASSIGN_DIVIDE   : '/=';

LT  : '<';
GT  : '>';
EQ  : '==';
NEQ  : '!=';
LEQ : '<=';
GEQ : '>=';

OPEN_BRACKET_ROUND   : '(';
CLOSE_BRACKET_ROUND  : ')';
OPEN_BRACKET_SQUARE  : '[';
CLOSE_BRACKET_SQUARE : ']';
OPEN_BRACKET_CURLY   : '{';
CLOSE_BRACKET_CURLY  : '}';

RANGE_OP: ':';

COMMA     : ',';
SEMICOLON : ';';

IF    : 'if';
ELSE  : 'else';
FOR   : 'for';
WHILE : 'while';

BREAK    : 'break';
CONTINUE : 'continue';
RETURN   : 'return';

EYE   : 'eye';
ZEROS : 'zeros';
ONES  : 'ones';

PRINT: 'print';

ID: [a-zA-Z_][a-zA-Z_0-9]*;

INT: [0-9]+;

FLOAT:
    [0-9]+ '.'
    | [0-9]* '.' [0-9]+
    | [0-9]* '.' [0-9]+ [eE] [+-]? [0-9]+
    | [0-9]+ [eE] [+-]? [0-9]+;

STRING: '"' ~["]* '"';