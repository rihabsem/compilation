import ply.lex as lex
import ply.yacc as yacc
import logging
import json
import os 
null_logger = logging.getLogger("ply")
null_logger.setLevel(logging.CRITICAL)

#creating a json file :

def writeJson(data, filename=r'C:\Users\DELL\Desktop\S7\compilation\projet\code\compilation\errorLog.json'):
    # Check if the file exists in our file system using the library "os"
    if os.path.exists(filename): 
        # Read existing data
        with open(filename, 'r') as f:
            try:
                existing_data = json.load(f) #storing the existing data in the json file in a list called existing_data
            except json.JSONDecodeError:
                existing_data = {"lexical_error": [], "syntactic_error": []}
    else:
        existing_data = {"lexical_error": [], "syntactic_error": []}
    
    # Merge new data with existing data
    for key in data:
        existing_data[key].extend(data[key]) #appending the new error in the existing_data list
    
    # Write the merged data back to the file
    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=4) #updating the json file


#dictionary
dataDic = {
    "lexical_error": [],
    "syntactic_error": []
}
dataTemplate = {
        "Type": "",
        "Description": "",
        "Position": "",
        "Line":""
   
}

#function for storing the errors in the dictionaries defined before
def errorLog(error_type, description, line=None, position=None):
    errorEntry = dataTemplate.copy()
    errorEntry["Type"] = error_type
    errorEntry["Description"] = description
    errorEntry["Line"] = line
    errorEntry["Position"] = position

    if error_type == "lexical":
        dataDic["lexical_error"].append(errorEntry)
    elif error_type == "syntactic":
        dataDic["syntactic_error"].append(errorEntry)




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
    error_message = f"Illegal character '{t.value[0]}'"
    errorLog("lexical", error_message, t.lineno, t.lexpos)
    writeJson(dataDic)
    raise Exception(f"ERROR: '{error_message}'")
    t.lexer.skip(1)
    

# Newline handling to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
#S grammatical rule
def p_S(p):
    '''
    S : VERBS
    '''
    filtered_p = [item for item in p[1:] if item is not None]
    print(f"Rule matched: S → {filtered_p}")



def p_error(p):
    if p:
        error_message = f"Syntax error at token '{p.type}' with value '{p.value}'"
        errorLog("syntactic", error_message, p.lineno, p.lexpos)
        print(error_message)
    else:
        error_message = "Syntax error at EOF (end of file)"
        errorLog("syntactic", error_message)
        print(error_message)
    writeJson(dataDic)

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


