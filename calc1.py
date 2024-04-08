# EOF ( End of file ) is used tp indicate trhat there is no more tokens left for lexical analysis

#Token types
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token(object):
    def __init__(self , type , value):
        # token type: INTEGER, PLUS, EOF
        self.type = type
        # token value: 0,1,2,3,4,5,6,7,8,9,'+', None
        self.value = value
    
    def __str__(self):
        """
        Sring representation of the class instance.
        __str__ is a special method in Python, that is called by the str() and print() function
        """
        return "Token({type}, {value})".format(
            type = self.type,
            value = repr(self.value)
        )
    
    def __repr__(self):
        return self.__str__()
    
class Interpreter(object):
    def __init__(self , text):
        # string input from the client , example "3+5"
        self.text = text
        # indexing on the client input text
        self.pos = 0
        # current token instance
        self.current_token = None

    def error(self):
        # raise is an exception and Expectation is an instance of the Expectation class (it inherits from the built in Expectation class)
        raise Exception("Error parsing input")
    
    def gen_next_token(self):
        """
        Lexical analyzer ( scanner or tokenizer)

        This method breaks the sentence into tokens . One token at a time

        """

        # This is a class variable

        text = self.text

        """
        if self.pos > than the self.text then return EOF token because all tokens have been parsed
        """

        if self.pos > len(text) - 1 :
            return Token(EOF , None)
        
        # Get a character at self.pos and decide what token to create based on that single character 
        # text[] is used to access the charcter of the string
        current_char = text[self.pos]

        # .isdigit() is a built in function that return True or False if the character in a string is a digit or not

        """
        If character is a digit then convert it into integer and create the INTEGER token,
        increment the self.pos to the next character after the digit and return the INTEGER token
        """

        if current_char.isdigit():
            token = Token(INTEGER , int(current_char))
            self.pos += 1
            return token
        
        if current_char == "+":
            token = Token(PLUS , current_char)
            self.pos += 1
            return token
        
        self.error()

    def eat(self , token_type):
            # compare the current token type with the passed toekn type and if they match eat the current token ? and assign the next token to the self.current_token othewise raise an exception
            if self.current_token.type == token_type:
                self.current_token = self.gen_next_token()
            else:
                self.error()

    def expr(self):
            # expr -> INTEGER PLUS INTEGER
            # set current token to the first token taken from the input
            self.current_token = self.gen_next_token()

            # expect the current token to be a single digit integer
            left = self.current_token
            self.eat(INTEGER)

            # expect the current token to be a '+' token
            op = self.current_token
            self.eat(PLUS)

            # expect the current token to be a single digit integer
            right = self.current_token
            self.eat(INTEGER)
            # after the above call the self.current_token is set to
            # EOF token

            # at this point INTEGER PLUS INTEGER sequence of tokens
            # has been successfully found and the method can just
            # return the result of adding two integers, thus
            # effectively interpreting client input
            result = left.value + right.value
            return result

def main():
    while True:
        try:
            text = input("calc> ")
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == "__main__":
    main()





