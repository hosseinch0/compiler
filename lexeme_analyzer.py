lexeme_list = []
keywords_tokens = []
symbol_table = dict()


def error_execution(file="./errors.txt"):
    with open(file, "w") as errors:
        errors.write("FIRST EXECUTION")


def read_file(file_to_open="./test.txt"):
    with open(file_to_open, 'r') as file:

        for line in file:
            for word in line.split():
                lexeme_list.append(word)


def write_errors(file_to_read="./test.txt", file_to_write="./errors.txt"):
    with open(file_to_read, 'r') as file:
        i = 0
        error_counter = 0
        data = file.read()
        try:
            for i in range(0, len(lexeme_list) - 1):
                if (keywords_tokens[i] == "ERROR_TK"):
                    error_counter += 1
                    data = data.replace(
                        lexeme_list[i] + " ", "\033$(" + lexeme_list[i] + ")$" + " ")
                    i += 1
                else:
                    i += 1
        except:
            pass
    with open(file_to_write, "w") as write_file:
        write_file.write(data)
        if (error_counter > 0):
            print("ERRORS ARE NOW VISIBLE WITH  ESC$(INPUT)$   FORMAT")
        else:
            print("NO LEXICAL ERROR FOUND")
    print(f"ERROR COUNTS: {error_counter}")


def isdigit_19(character):
    if (character >= "1" and character <= "9"):
        return True
    else:
        return False


def isdigit_09(character):
    if (character >= "0" and character <= "9"):
        return True
    else:
        return False


# THIS FUNCTION HELPS TOKENIZER TO ADAPT THE RIGHT TOKEN AND STORE IT
def lexeme_validation(character):
    token = None
    state = 1
    while (True):
        match (state):
            case 1:
                token = if_validation(character)
                if (token != None):
                    return token
                elif (token == None):
                    state = 2
            case 2:
                token = elif_validation(character)
                if (token != None):
                    return token
                elif (token == None):
                    state = 3
            case 3:
                if (character == "("):
                    return "("
                else:
                    state = 4
            case 4:
                if (character == ")"):
                    return ")"
                else:
                    state = 5
            case 5:
                token = while_validation(character)
                if (token != None):
                    return token
                elif (token == None):
                    state = 6
            case 6:
                token = from_validation(character)
                if (token != None):
                    return token
                elif (token == None):
                    state = 7
            case 7:
                token = else_validation(character)
                if (token != None):
                    return token
                elif (token == None):
                    state = 8
            case 8:
                token = function_validation(character)
                if (token != None):
                    return token
                elif (token == None):
                    state = 9
            case 9:
                if (character == "{"):
                    return "{"
                else:
                    state = 10
            case 10:
                if (character == "}"):
                    return "}"
                else:
                    state = 11
            case 11:
                if (character == "-"):
                    return "-"
                else:
                    state = 12
            case 12:
                if (character == "+"):
                    return "+"
                else:
                    state = 13
            case 13:
                if (character == "/"):
                    return "/"
                else:
                    state = 14
            case 14:
                if (character == "*"):
                    return '*'
                else:
                    state = 15
            case 15:
                if (character == "="):
                    return "="
                else:
                    state = 16
            case 16:
                if (character == "==="):
                    return "==="
                else:
                    state = 17
            case 17:
                token = to_validation(character)
                if (token != None):
                    return token
                else:
                    state = 18
            case 18:
                if (character == "<"):
                    return "<"
                else:
                    state = 19
            case 19:
                if (character == ">"):
                    return ">"
                else:
                    state = 20
            case 20:
                token = id_validation(character)
                if (token != None):
                    return token
                else:
                    state = 21
            case 21:
                token = positive_integer_validation(character)
                if (token != None):
                    return token
                else:
                    state = 22

            case 22:
                token = negative_integer_validation(character)
                if (token != None):
                    return token
                else:
                    state = 23

            case 23:
                token = positive_float_validation(character)
                if (token != None):
                    return token
                else:
                    state = 24
            case 24:
                token = negative_float_validation(character)
                if (token != None):
                    return token
                else:
                    state = 25
            case 25:
                token = string_validation(character)
                if (token != None):
                    return token
                else:
                    state = 26
            case 26:
                return "ERROR"


# FUNCTIONS BELOW ARE MY LANGUAGE KEYWORDS (DFA) THAT ARE BEING USED INSIDE lexeme_validation() FUNCTION

def if_validation(character):
    state = 1
    while (True):
        match (state):
            case 1:
                if (character[0] == "i"):
                    state = 2
                else:
                    return None
            case 2:
                if (character[1] == "f"):
                    state = 3
                else:
                    return None
            case 3:
                try:
                    if (character[2] != " "):
                        return None
                except:
                    return "if"


def while_validation(character):
    state = 1
    while (True):
        match (state):
            case 1:
                if (character[0] == 'w'):
                    state = 2
                else:
                    return None
            case 2:
                if (character[1] == "h"):
                    state = 3
                else:
                    return None
            case 3:
                if (character[2] == 'i'):
                    state = 4
                else:
                    return None
            case 4:
                if (character[3] == 'l'):
                    state = 5
                else:
                    return None
            case 5:
                if (character[4] == 'e'):
                    state = 6
                else:
                    return None
            case 6:
                try:
                    if (character[5] != " "):
                        return None
                except:
                    return "while"


def elif_validation(character):
    state = 1
    while (True):
        match (state):
            case 1:
                if (character[0] == 'e'):
                    state = 2
                else:
                    return None
            case 2:
                if (character[1] == "l"):
                    state = 3
                else:
                    return None
            case 3:
                if (character[2] == 'i'):
                    state = 4
                else:
                    return None
            case 4:
                if (character[3] == 'f'):
                    state = 5
                else:
                    return None
            case 5:
                try:
                    if (character[4] != " "):
                        return None
                except:
                    return "elif"


def else_validation(character):
    state = 1
    while (True):
        match (state):
            case 1:
                if (character[0] == 'e'):
                    state = 2
                else:
                    return None
            case 2:
                if (character[1] == "l"):
                    state = 3
                else:
                    return None
            case 3:
                if (character[2] == 's'):
                    state = 4
                else:
                    return None
            case 4:
                if (character[3] == 'e'):
                    state = 5
                else:
                    return None
            case 5:
                try:
                    if (character[4] != " "):
                        return None
                except:
                    return "else"


def function_validation(character):
    state = 1
    while (True):
        match (state):
            case 1:
                if (character[0] == 'f'):
                    state = 2
                else:
                    return None
            case 2:
                if (character[1] == "u"):
                    state = 3
                else:
                    return None
            case 3:
                if (character[2] == 'n'):
                    state = 4
                else:
                    return None
            case 4:
                if (character[3] == 'c'):
                    state = 5
                else:
                    return None
            case 5:
                if (character[4] == 't'):
                    state = 6
                else:
                    return None
            case 6:
                if (character[5] == 'i'):
                    state = 7
                else:
                    return None
            case 7:
                if (character[6] == 'o'):
                    state = 8
                else:
                    return None
            case 8:
                if (character[7] == 'n'):
                    state = 9
                else:
                    return None
            case 9:
                try:
                    if (character[8] != " "):
                        return None
                except:
                    return "function"


def from_validation(character):
    state = 1
    while (True):
        match (state):
            case 1:
                if (character[0] == 'f'):
                    state = 2
                else:
                    return None
            case 2:
                if (character[1] == "r"):
                    state = 3
                else:
                    return None
            case 3:
                if (character[2] == 'o'):
                    state = 4
                else:
                    return None
            case 4:
                if (character[3] == 'm'):
                    state = 5
                else:
                    return None
            case 5:
                try:
                    if (character[4] != " "):
                        return None
                except:
                    return "from"


def to_validation(character):
    state = 1
    while (True):
        match (state):
            case 1:
                if (character[0] == "t"):
                    state = 2
                else:
                    return None
            case 2:
                if (character[1] == "o"):
                    state = 3
                else:
                    return None
            case 3:
                try:
                    if (character[2] != " "):
                        return None
                except:
                    return "to"


def for_validation(character):
    state = 1
    while (True):
        match (state):
            case 1:
                if (character[0] == 'f'):
                    state = 2
                else:
                    return None
            case 2:
                if (character[1] == "o"):
                    state = 3
                else:
                    return None
            case 3:
                if (character[2] == 'r'):
                    state = 4
                else:
                    return None
            case 4:
                try:
                    if (character[3] != " "):
                        return None
                except:
                    return "for"

# END OF KEYWORDS VALIDATION


# INPUT IDENTIFICATIONS

def id_validation(character):
    first_element = 0
    last_element = len(character) - 1
    state = 1
    while (True):
        match (state):
            case 1:
                if (character[first_element] == '_'):
                    state = 2
                else:
                    state = 4
            case 2:
                for i in range(1, last_element - 1):
                    comp = character[i]
                    if ((comp >= 'a' and comp <= "z") or (comp >= "A" and comp <= "Z") or (isdigit_09(comp)) or comp == "_"):
                        pass
                    else:
                        return None
                state = 3
            case 3:
                if (character[last_element] == "_"):
                    return "ID"
                else:
                    state = 4
            case 4:
                return None

# NUMBERS DFA'S


def positive_integer_validation(character):
    first_element = 0
    last_element = len(character) - 1
    state = 1
    while (True):
        match (state):
            case 1:
                if (isdigit_19(character[first_element])):
                    state = 2
                else:
                    return None
            case 2:
                for i in range(1, last_element + 1):
                    comp = character[i]
                    if (isdigit_09(comp)):
                        pass
                    else:
                        return None
                state = 3
            case 3:
                try:
                    if (character[last_element + 1] != " "):
                        return None
                except:
                    return "ConstNum"


def negative_integer_validation(character):
    first_element = 0
    last_element = len(character) - 1
    minus_counter = 0
    state = 1
    while (True):
        match (state):
            case 1:
                if (character[first_element] == "-"):
                    state = 2
                else:
                    return None
            case 2:
                if (isdigit_19(character[1])):
                    state = 3
                else:
                    return None
            case 3:
                for i in range(2, last_element + 1):
                    comp = character[i]
                    if (isdigit_09(comp)):
                        pass
                    elif (comp == "-"):
                        minus_counter += 1
                        if (minus_counter >= 1):
                            return None
                    else:
                        return None
                state = 4
            case 4:
                try:
                    if (character[last_element + 1] != " "):
                        return None
                except:
                    return "ConstNum"


def positive_float_validation(character):
    first_element = 0
    last_element = len(character) - 1
    dot_counter = 0
    state = 1
    while (True):
        match (state):
            case 1:
                if (isdigit_09(character[first_element])):
                    state = 2
                else:
                    return None
            case 2:
                for i in range(1, last_element + 1):
                    comp = character[i]
                    if (isdigit_09(comp)):
                        state = 2
                    elif (comp == "."):
                        dot_counter += 1
                        if (dot_counter > 1):
                            return None
                    else:
                        return None
                state = 3
            case 3:
                try:
                    if (character[last_element + 1] != " "):
                        return None
                except:
                    return "ConstNum"


def negative_float_validation(character):
    first_element = 0
    last_element = len(character) - 1
    minus_counter = 0
    dot_counter = 0
    state = 1
    while (True):
        match (state):
            case 1:
                if (character[first_element] == "-"):
                    state = 2
                else:
                    return None
            case 2:
                for i in range(1, last_element + 1):
                    comp = character[i]
                    if (isdigit_09(comp)):
                        state = 2
                    elif (comp == "."):
                        dot_counter += 1
                        if (dot_counter > 1):
                            return None
                    elif (comp == "-"):
                        minus_counter += 1
                        if (minus_counter > 0):
                            return None
                    else:
                        return None
                else:
                    state = 3
            case 3:
                if (character[last_element] != "."):
                    state = 4
                else:
                    return None
            case 4:
                try:
                    if (character[last_element + 1] != " "):
                        return None
                except:
                    return "ConstNum"


# STRING INPUT
def string_validation(character):
    first_element = 0
    last_element = len(character) - 1
    state = 1
    while (True):
        match (state):
            case 1:
                if (character[first_element] == "\""):
                    state = 2
                else:
                    return None
            case 2:
                state = 3
            case 3:
                if (character[last_element] == "\""):
                    return "STRING"
                else:
                    return None


# SHOWS HOW MANY ELEMENT EXISTS IN SYMBOL TABLE
def symbol_table_contains(count):
    return count - 1


# THIS FUNCTION CONVERT'S LEXEMES TO THE PROPER TOKENS
def tokenize():
    id_counter = 1
    for i in range(len(lexeme_list)):
        word = lexeme_list[i]
        token = lexeme_validation(lexeme_list[i])
        if (token == "ID"):
            keywords_tokens.append(token + "_TK")
            if word in symbol_table.keys():
                pass
            else:
                symbol_table[word] = id_counter
                id_counter += 1
        else:
            keywords_tokens.append(token + "_TK")
    return keywords_tokens


# FUNCTION CALLS
file_to_write = "./errors.txt"

# ATTENTION
# RUN IT ONLY THE FIRST TIME USING THIS PROGRAMME
# error_execution(file_to_write)
# ATTENTION

file_to_read = "./final.txt"
read_file(file_to_read)
tokenize()
print(keywords_tokens)
write_errors(file_to_read, file_to_write)
