// $antlr-format alignTrailingComments true, columnLimit 140, maxEmptyLinesToKeep 1, reflowComments false
// $antlr-format useTab false, allowShortRulesOnASingleLine true, allowShortBlocksOnASingleLine true, minEmptyLines 0
// $antlr-format alignSemicolons ownLine, alignColons trailing, singleLineOverrulesHangingColon true
// $antlr-format alignLexerCommands true, alignLabels true, alignTrailers true

lexer grammar MyLexer;

WHITESPACE: [ \t\r\n]+ -> skip;

COMMENT: '#' ~[\r\n]* -> skip;

PLUS      : '+';
MINUS     : '-';
MULTIPLY  : '*';
DIVIDE    : '/';
BINARY_OP : PLUS | MINUS | MULTIPLY | DIVIDE;

MAT_PLUS      : '.+';
MAT_MINUS     : '.-';
MAT_MULTIPLY  : '.*';
MAT_DIVIDE    : './';
BINARY_MAT_OP : MAT_PLUS | MAT_MINUS | MAT_MULTIPLY | MAT_DIVIDE;

MAT_TRANSPOSE_OP: '\'';

ASSIGN          : '=';
ASSIGN_PLUS     : '+=';
ASSIGN_MINUS    : '-=';
ASSIGN_MULTIPLY : '*=';
ASSIGN_DIVIDE   : '/=';
ASSIGN_OP       : ASSIGN | ASSIGN_PLUS | ASSIGN_MINUS | ASSIGN_MULTIPLY | ASSIGN_DIVIDE;

LE          : '<';
GE          : '>';
EQ          : '==';
NE          : '!=';
LEQ         : '<=';
GEQ         : '>=';
RELATION_OP : LE | GE | EQ | NE | LEQ | GEQ;

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

ID: [a-zA-Z_][a-z_0-9]*;

INT: [0-9]+;

FLOAT: [0-9]* [.][0-9]+ | [0-9]+ [.][0-9]*;

STRING: '"' ~["]* '"';