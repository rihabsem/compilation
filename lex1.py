import ply.lex as lex
# TOKENS
tokens = (
    "NOUNS",
    "VERBS",
    "VERBSWITHAPS",
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
    "RPAREN",
    "LCROCH",
    "RCROCH"
)
t_ignore = r" \t"
t_NOUNS = r"\b(soul|love|heart|children|thanks|lord|place|sinner|mankind|beliefs|song|chance|doom|father|creation|thing|armagiddyon|remarks|question|man|pity|chances|place|plea|battle|kingdoms|house)\b"
t_VERBS = r"\b(beginning|get|feel|hear|crying|saying|give|ask|is|has|hurt|save|comes|singing|let|pass|was|be|fight|have|grows|ain't|hiding|pleading|will|praise|'d|'m|am|like|join|tell|pray|let|would|trust)\b"
t_VERBSWITHAPS = r"\b(let)\b" 
t_ADVERBS = r"\b(really|one|more|alright|just|all|there|together)\b"    
t_ADJECTIVES = r"\b(my|mercy|one|own|holy|thinner|dirty|hopeless)\b"
t_ARTICLES = r"\b(a|the)\b"
t_PREPOSITIONS = r"\b(to|from|in|about|for|of|at|on|among)\b"
t_PRONOUNS = r"\b(you|us|i|them|who|us|it|shall|those|this|what|whose)\b"
t_DETERMINANT = r"\b(his|their|no|yes)\b"
t_CONJUNCTIONS = r"\b(and|or|so|when|as)\b"
t_INTERJECTIONS = r"\b(oh|woah)\b"
t_PUNCTUATION = r"(!|\?|\.|,|;|:|\"|’|-|—)"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LCROCH = r"\["
t_RCROCH = r"\]"
def lexicalAnalysis() :
    verify = True
    print("-----------------------------Lexical analysis-----------------------------")
    lexer = lex.lex()  # Create the lexer
    data = input("Enter the lyric you have in mind: ")
    
    #tokenize the input text
    lexer.input(data.lower()) 

    # Attempt to generate tokens and return True if successful and False if incorrect
    try:
        for tok in lexer:
            print(tok)  
    except Exception as e:
        print(e)
        verify = False
    return verify

# Error handling
def t_error(t):
    raise Exception(f"Illegal character '{t.value[0]}'")

# Newline handling to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#main script
if lexicalAnalysis():
    print("lets pass to the sémantic analysis")
else :
    print("Erreur in the lexical analysor")




# Tokenisation de l'entrée
#for tok in lexer:
#    print(tok)
