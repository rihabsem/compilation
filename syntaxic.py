import ply.yacc as yacc
from lex1 import tokens, lexicalAnalysis
import lex1
#S grammatical rule
def p_S(p):
    '''
    S : 
    | VP
    | ADVP
    | ADJP
    | CONJUNCTIONS
    | LPAREN
    | RPAREN
    | INTERJECTIONS
    | NG
    | PP
    | ADVERBS
    | PRONOUNS
    '''
    print(f"Rule matched: NP → {p[1:]}")

# NG grammatical rule
def p_NG(p):
    '''
    NG : DETERMINANT ADJECTIVES NOUNS
    | ADJECTIVES NOUNS
    '''
    print(f"Rule matched: NP → {p[1:]}")
#NP grammatical rule
def p_NP(p):
    '''
    NP : NOUNS 
    | NOUNS PREPOSITIONS ADJECTIVES
    | ADVERBS NOUNS
    | DETERMINANT NOUNS
    '''
    print(f"Rule matched: NP → {p[1:]}")

#VP grammatical rules
def p_VP(p):
    '''
    VP : VERBS
    | VERBS ADVERBS
    | PRONOUNS VERBS PRONOUNS
    | VERBS ADVERBS LPAREN PREPOSITIONS PRONOUNS NOUNS
    | PRONOUNS VERBS RPAREN
    | PRONOUNS VERBS ADVERBS
    | VERBS PRONOUNS ADVERBS VERBS
    | PREPOSITIONS VERBS 
    | VERBS ADVERBS ARTICLES NOUNS 
    | VERBS ADJECTIVES NOUNS 
    | VERBS ADVERBS VERBS PREPOSITIONS ARTICLES NOUNS 
    | VERBS ADVERBS PREPOSITIONS VERBS PRONOUNS 
    | ARTICLES NOUNS VERBS 
    | VERBS NOUNS 
    | PRONOUNS NOUNS VERBS ADJECTIVES 
    | PRONOUNS VERBS
    | DETERMINANT VERBS NOUNS 
    | VERBS PRONOUNS NOUNS ARTICLES PUNCTUATION VERBS 
    | VERBS ADVERBS CONJUNCTIONS VERBS ADVERBS 
    | VERBS PREPOSITIONS ARTICLES NOUNS
    '''
    print(f"Rule matched: NP → {p[1:]}")

#PP grammatical rules
def p_PP(p):
    '''
    PP : PREPOSITIONS ARTICLES ADJECTIVES NOUNS
    | PREPOSITIONS VERBS DETERMINANT ADJECTIVES NOUNS
    | PREPOSITIONS PRONOUNS
    | PREPOSITIONS ARTICLES NOUNS
    | PREPOSITIONS NOUNS
    | PREPOSITIONS VERBS DETERMINANT ADJECTIVES
    | PREPOSITIONS PRONOUNS NOUNS
    '''
    print(f"Rule matched: NP → {p[1:]}")

#ADVP grammatical rule
def p_ADVP(p):
    '''
    ADVP : ADVERBS NP
    | ADVERBS VP
    | ADVERBS NP PUNCTUATION ADVERBS NP
    '''
    print(f"Rule matched: NP → {p[1:]}")

#ADVP grammatical rule
def p_ADJP(p):
    '''
    ADJP : ADJECTIVES NP
    | ADJECTIVES VP
    '''
    print(f"Rule matched: NP → {p[1:]}")

def p_error(p):
    print("oups")

def main():
    tokens_list = lexicalAnalysis()  # Perform lexical analysis
    if tokens_list:
        print("Proceeding to syntactic analysis...")
        parser = yacc.yacc()  # Build the parser
        raw_input = " ".join(tok.value for tok in tokens_list)  # Convert tokens back to string
        print("successful!!")
    else:
        print("Error in lexical analysis. Syntactic analysis will not be performed.")

if __name__ == "__main__":
    main()