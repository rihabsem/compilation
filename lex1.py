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

# Ignoring spaces and tabs
t_ignore = " \t"

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Newline handling to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Build the lexer
lexer = lex.lex()

# Exemple d'utilisation
data = """
I tell you, let them all pass all their dirty remarks (one love)
There is one question I'd really like to ask (one soul)
Is there a place for the hopeless sinner
Who has hurt all mankind just to save his own?
One love (oh Lord of mercy)
One heart (I tell you)
Let us join together (at this house I pray)
And a-feel alright (and I will feel alright)
One love (hear my plea)
One heart (hear my plea)
Let us join together and a-feel alright (and I will feel alright)
Let us join together (let us pray to the Lord)
And a-feel alright (and I will feel alright)
"""
lexer.input(data.lower())

# Tokenisation de l'entrée
for tok in lexer:
    print(tok)
