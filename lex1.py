import ply.lex as lex
import ply.yacc as yacc
import logging
null_logger = logging.getLogger("ply")
null_logger.setLevel(logging.CRITICAL)
# TOKENS
tokens = (
    "NOUNS",
    "VERBS",
    "ADVERBS",
    "ADJECTIVES",
    "ARTICLES",
    "PREPOSITIONS",
    "PRONOUNS",
    "DETERMINANT",
    "CONJUNCTIONS",
    "INTERJECTIONS",
    "PUNCTUATION",
    "LPAREN",
    "RPAREN"
)
t_ignore = " \t"
t_NOUNS = r"\b(soul|love|heart|children|thanks|lord|place|sinner|mankind|beliefs|song|chance|doom|father|creation|thing|remarks|question|man|pity|chances|place|plea|battle|kingdoms|house)\b"
t_VERBS = r"\b(beginning|get|feel|hear|crying|saying|give|ask|is|has|hurt|save|comes|singing|pass|was|be|fight|have|grows|ain't|hiding|pleading|will|let's|let|praise|i'd|'m|am|like|join|tell|pray|would|trust)\b"
t_ADVERBS = r"\b(together|really|one|more|alright|just|all|there)\b"    
t_ADJECTIVES = r"\b(my|mercy|own|holy|thinner|dirty|hopeless)\b"
t_ARTICLES = r"\b(a|the)\b"
t_PREPOSITIONS = r"\b(to|from|in|about|for|of|at|on|among)\b"
t_PRONOUNS = r"\b(you|us|i|them|who|us|it|shall|those|this|what|whose)\b"
t_DETERMINANT = r"\b(his|their|no|yes)\b"
t_CONJUNCTIONS = r"\b(and|or|so|when|as)\b"
t_INTERJECTIONS = r"\b(oh|woah)\b"
t_PUNCTUATION = r"(!|\?|\.|,|;|:|\"|-|—)"
t_LPAREN = r"\("
t_RPAREN = r"\)"
#t_LCROCH = r"\["
#t_RCROCH = r"\]"
tokens_list = []
def lexicalAnalysis() :

        print("-----------------------------Lexical analysis-----------------------------")
        lexer = lex.lex()  # Create the lexer
        data = input("Enter the lyric you have in mind: ").lower()
        lexer.input(data)

        tokens_list = []
        try:
            for tok in lexer:
                tokens_list.append(tok)
                print(f"Token: {tok.type}, Value: {tok.value}")  # Print tokens as they are generated
            return tokens_list  # Return the list of tokens
        except Exception as e:
            print(f"Lexical analysis error: {e}")
            return None

# Error handling
def t_error(t):
    raise Exception(f"Illegal character '{t.value[0]}'")

# Newline handling to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
#S grammatical rule
def p_S(p):
    '''
    S : 
      | ADVERBS VP ADVP VERBS ADVERBS VERBS PREPOSITIONS VERBS S
      | CON S
      | PRONOUNS S
      | ADVP S
      | NP S
      | VP S
      | ADJP S
      | INTERJECTIONS S
      | LPAREN S RPAREN
      | NG S
      | PP S
      | PUN S
      | DETERMINANT S
      | ARTICLES S
      | PREPOSITIONS S
      | PP
    '''
    print(f"Rule matched: S → {p[1:]}")

#ADVP grammatical rule
def p_ADVP(p):
    '''
    ADVP : ADVERBS
    | ADVERBS NOUNS
    | ADVERBS VP
    | ADVP PUNCTUATION ADVERBS NOUNS
    | ADVERBS VP PP
    | ADVERBS S
    '''
    print(f"Rule matched: ADVP → {p[1:]}")

#ADJP grammatical rule
def p_ADJP(p):
    '''
    ADJP : ADJECTIVES 
    | ADJECTIVES NP
    | ADJECTIVES VP
    '''
    print(f"Rule matched: ADJP → {p[1:]}")

#NP grammatical rule
def p_NP(p):
    '''
    NP : NOUNS 
    | NP PREPOSITIONS ADJECTIVES
    | DETERMINANT S NP
    | ARTICLES NOUNS
    '''
    print(f"Rule matched: NP → {p[1:]}")

#VP grammatical rules
def p_VP(p):
    '''
    VP : VERBS
       | VP ADVP
       | VP ARTICLES
       | PRONOUNS VP
       | VP NOUNS
       | VERBS PREPOSITIONS NOUNS
       | VERBS ADJECTIVES NOUNS
       | ARTICLES NOUNS VERBS
       | DETERMINANT VERBS NOUNS
       | PRONOUNS NOUNS VERBS ADJECTIVES
       | VP LPAREN S RPAREN
    '''
    print(f"Rule matched: VP → {p[1:]}")
# NG grammatical rule
def p_NG(p):
    '''
    NG : ADVERBS DETERMINANT ADJECTIVES NOUNS
    '''
    print(f"Rule matched: NG → {p[1:]}")

#PP grammatical rules
def p_PP(p):
    '''
    PP : PREPOSITIONS
       | PREPOSITIONS ARTICLES NOUNS
       | PP NOUNS
       | PP PRONOUNS
       | PREPOSITIONS VERBS
       | PP ARTICLES NOUNS
    '''
    print(f"Rule matched: PP → {p[1:]}")

#CON grammatical rules
def p_CON(p):
    '''CON : CONJUNCTIONS'''
    print(f"Rule matched: CON → {p[1:]}")

#PUN grammatical rules
def p_PUN(p):
    '''
    PUN : PUNCTUATION
    '''
    print(f"Rule matched: PUN → {p[1:]}")

def p_error(p):
    if p:
        print(f"Syntax error at token '{p.type}' with value '{p.value}'")
    else:
        print("Syntax error at EOF (end of file)")

def main():
    tokens_list = lexicalAnalysis()  # Perform lexical analysis
    if tokens_list:
        print("Proceeding to syntactic analysis...")
        parser = yacc.yacc(errorlog=null_logger)  # Build the parser
        raw_input = " ".join(tok.value for tok in tokens_list)  # Convert tokens back to string
        try:
            parser.parse(raw_input)  # Parse the string according to the grammar
            print("Grammar is correct!")  # If no syntax errors, print success
        except Exception as e:
            print(f"Syntax error: {e}")
    else:
        print("Error in lexical analysis. Syntactic analysis will not be performed.")

if __name__ == "__main__":
    main()
#| VERBS VERBS ADVERBS LPAREN VERBS ADVERBS VERBS PREPOSITIONS ARTICLES NOUNS RPAREN
#| VERBS VERBS ADVERBS LPAREN VERBS VERBS PREPOSITIONS ARTICLES NOUNS RPAREN


