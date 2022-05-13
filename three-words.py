def checkio(words: str) -> bool:
    count = 0               # create a count variable
    for i in words.split(): # go through the splited string
        if not i.isalpha(): # if element i contain not letters    
            count = 0       # set counter to zero
        else:               # all characters are letters
            count += 1      # count up   
        if count == 3:      # if the counter is 3 
            return True     # we have three words in a raw
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")