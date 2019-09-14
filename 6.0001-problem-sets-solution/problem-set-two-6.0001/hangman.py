# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def list_to_lowercase(list_parameter):
    '''
    list_parameter: list contains english charchters -uppercase and lowercase-
    it reurns a list that all its elements are lowercase strings
    '''
    lower_letters_guessed = []
    for a in list_parameter:
        a = str(a).lower()
        lower_letters_guessed.append(a)
    return lower_letters_guessed


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word = str(secret_word).lower()
    lower_letters_guessed = list_to_lowercase(letters_guessed)
    # it will contain True if the charchter of secret_word is present in the letters_gueesed list
    # it will contains false if the charchter in secret_word isn't guessed
    trues_falses = []
    # for each charchter in secret_word,, append false if the charchter isn't in list and true otherwise
    for c in secret_word:
        trues_falses.append(c in lower_letters_guessed)
    # return true if all charchters of the secret word are present in list of charchters guessed
    # this code returns true if "False" isn't present in the list or trues_falses, that means that 
    return (False not in trues_falses)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word = str(secret_word).lower()
    lower_letters_guessed = list_to_lowercase(letters_guessed)
    guessed_word = ''
    length_secret_word = len(secret_word)
    for i in range(0, length_secret_word):
        if secret_word[i] in lower_letters_guessed:
            guessed_word = guessed_word + secret_word[i]
        else:
            guessed_word = guessed_word + '_ '
    return guessed_word




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_english_lowercase = string.ascii_lowercase
    length_lowercase = len(all_english_lowercase)
    lower_letters_guessed = list_to_lowercase(letters_guessed)
    available_letters = ''
    # loop through all english alphabet, only that haven't been guessed yet is added to available letters
    for c in range(0, length_lowercase) :
        if all_english_lowercase[c] in lower_letters_guessed:
            available_letters = available_letters
        else:
            available_letters = available_letters + all_english_lowercase[c]
    return available_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    # Available number of guesses as stated in the game requirements
    num_guess_left = 6
    # Available number of warnings as stated in the game requirements
    num_warning_left = 3
    # vowels charchters in English
    vowels = 'aeoui'
    # list contains all letters the user input
    guessed_letters_from_user = []
    # loop that establishes the the interactive agme between the computer and the user
    # it loops as far as the there are availables guess trails and the word isn't compeletely guessed yet.
    while num_guess_left > 0 and not is_word_guessed(secret_word, guessed_letters_from_user):
        # print dashes at every time to separate different sessions
        print('--------------')
        # informing the user with remainig available warning left
        print('You have',num_warning_left  ,' warning/s left.')
        # informing the user with remainig available guesses/trails left
        print('You have',num_guess_left  ,' guess/es left.')
        # Showing the valid user input only
        print('ALPHABET Letters are the only valid Input')
        # Showing the user the available letters that haven't been gueesed so for and he/she can choose from
        print('Available Letters are:', get_available_letters(guessed_letters_from_user))
        # asking the user to enter an engkish letter then casting it into lowercase
        user_guess = input('Please guess a letter: ').lower()
        # building the part of secret word that has been guessed so far and representing it as guessed letters and dashes
        guessed_word = get_guessed_word(secret_word, guessed_letters_from_user + list(user_guess))
        # checking the user input if it's valid and meets the game requirements, printing the user statement of achievement
        if str.isalpha(user_guess) and len(user_guess) == 1 and user_guess not in guessed_letters_from_user and user_guess in secret_word:
            print('Good guess: ', guessed_word)
        # if the user input isn't valid, the user should lose warnings first then guess trails according to the gane requirements
        else:
            if num_warning_left <= 0:
                    # according to the game requirements, user should lose 2 guesses or warnings if the invalid input is vowel, othersie the lose is only one either guess or warning
                    if user_guess in vowels:
                        num_guess_left = num_guess_left - 2
                        if user_guess in guessed_letters_from_user:
                            print("Oops! You've already guessed that letter. You have", num_guess_left, "guess/es left: ", guessed_word)
                        else: 
                            print("Oops! That is not a valid letter. You have", num_guess_left, "guess/es left: ", guessed_word)
                    else:
                        num_guess_left = num_guess_left - 1
                        if user_guess in guessed_letters_from_user:
                            print("Oops! You've already guessed that letter. You have", num_guess_left, "guess/es left: ", guessed_word)
                        else: 
                            print("Oops! That is not a valid letter. You have", num_guess_left, "guess/es left: ", guessed_word)
                # if the user still has warnings availble, he should lose warnings first
            else:
                    # according to the game requirements, user should lose 2 guesses or warnings if the invalid input is vowel, othersie the lose is only one either guess or warning
                    if user_guess in vowels:
                        # if ther eis only one warning left, the user lose the remaining one warning and one guess trail
                        if num_warning_left == 1:
                            num_warning_left = num_warning_left - 1
                            num_guess_left = num_guess_left - 1
                            if user_guess in guessed_letters_from_user:
                                print("Oops! You've already guessed that letter. You have", num_guess_left, "guess/es left: ", guessed_word)
                            else: 
                                print("Oops! That is not a valid letter. You have", num_warning_left, "warning/s left: ", guessed_word)
                            # if ther is more than one warning, the user hsould lose two warnings for invalid vowel
                        else:
                            num_warning_left = num_warning_left - 2
                            if user_guess in guessed_letters_from_user:
                                print("Oops! You've already guessed that letter. You have", num_warning_left, "warning/s left: ", guessed_word)
                            else: 
                                print("Oops! That is not a valid letter. You have", num_warning_left, "warning/s left: ", guessed_word)
                            # if the invalid input is consonant, the user should lose only one either warning or guess trail.
                    else:
                        num_warning_left = num_warning_left -1
                        if user_guess in guessed_letters_from_user:
                            print("Oops! You've already guessed that letter. You have", num_warning_left, "warnings left: ", guessed_word)
                        else: 
                            print("Oops! That is not a valid letter. You have", num_warning_left, "warning/s left: ", guessed_word)
        # saving all user input either valid or not to use it in the fnction "get_gueesed_word" and "is_word_guessed"
        guessed_letters_from_user.append(user_guess)
    
    if is_word_guessed(secret_word, guessed_letters_from_user):
        unique_letters_of_secret_word = []
        for h in secret_word:
            if h not in unique_letters_of_secret_word:
                unique_letters_of_secret_word.append(h)
        total_score = num_guess_left * len(unique_letters_of_secret_word)
        print('Congratulations, you won!')
        print('Your total score for this game is:', total_score)
    else:
        print('Sorry, you ran out of guesses. The word was', secret_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # casting my_word to string, then removing all whitespaces, then casting it to lowercase
    my_word = str(my_word).replace(" ", "").lower()
    # casting my_word to string, then removing all whitespaces, then casting it to lowercase
    other_word = str(other_word).replace(" ", "").lower()
    # for efficiency, make sure that the two words have the same length, if so check the equality and other ckecks, otherwise, return false
    if (len(my_word) == len(other_word)):
        # saving the result of the tests of the equality between each lettters in my_wor and other_word
        trs_fls = []
        # loop through each word in 'my_word'
        for e in range(0, len(other_word)):
            # at th bgging, return true if the two chachters with the same index are the same
            if my_word[e] == other_word[e]:
                trs_fls.append(True)
            # else if, uf the chachter in my_word is spechial symol "_" return true after....
            # we check if the the chachter with the same index in "other_word" has no occurences at all in "my_word"
            # because the game requirement stated if an chachter isn't guessed once, it is revealed in all its occurences
                '''
                This is the game requirement
                Remember that when a letter is guessed, your code reveals all the positions at which
                that letter occurs in the secret word. Therefore, the hidden letter (_ ) ​cannot be ​one
                of the letters in the word that has already been revealed.
                '''
            elif my_word[e] == '_' and not (other_word[e] in my_word):
                trs_fls.append(True)
            # otherwise, return false
            else:
                trs_fls.append(False)
        '''
        if there is no "False" occurence at all in "trs_fls" list, this means that: the same indices in two words "my_word and other_word" have the same letter or it is "_"
        '''
        return (not (False in trs_fls))
    # return falsse if the length of "my_word" and "other_word" is different
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = ""
    for s in range(0, len(wordlist)):
        current_word = wordlist[s]
        if(match_with_gaps(my_word, current_word)):
            possible_matches = possible_matches + " " + current_word
    return print("Possible word matches are:\n", possible_matches)




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    # Available number of guesses as stated in the game requirements
    num_guess_left = 6
    # Available number of warnings as stated in the game requirements
    num_warning_left = 3
    # vowels charchters in English
    vowels = 'aeoui'
    # list contains all letters the user input
    guessed_letters_from_user = []
    # loop that establishes the the interactive agme between the computer and the user
    # it loops as far as the there are availables guess trails and the word isn't compeletely guessed yet.
    while num_guess_left > 0 and not is_word_guessed(secret_word, guessed_letters_from_user):
        # print dashes at every time to separate different sessions
        print('--------------')
        # informing the user with remainig available warning left
        print('You have',num_warning_left  ,' warning/s left.')
        # informing the user with remainig available guesses/trails left
        print('You have',num_guess_left  ,' guess/es left.')
        # Showing the valid user input only
        print('ALPHABET Letters are the only valid Input')
        # Showing the user the available letters that haven't been gueesed so for and he/she can choose from
        print('Available Letters are:', get_available_letters(guessed_letters_from_user))
        # asking the user to enter an engkish letter then casting it into lowercase
        user_guess = input('Please guess a letter: ').lower()
        # building the part of secret word that has been guessed so far and representing it as guessed letters and dashes
        guessed_word = get_guessed_word(secret_word, guessed_letters_from_user + list(user_guess))
        if user_guess == '*':
            show_possible_matches(guessed_word)
        else:
            # checking the user input if it's valid and meets the game requirements, printing the user statement of achievement
            if str.isalpha(user_guess) and len(user_guess) == 1 and user_guess not in guessed_letters_from_user and user_guess in secret_word:
    #            if user_guess in guessed_word:
                print('Good guess: ', guessed_word)
    #            else:
    #                print('Oops! That letter is not in my word: ', guessed_word)
            # if the user input isn't valid, the user should lose warnings first then guess trails according to the gane requirements
            else:
                # in case of the user lose all available warnings
                if num_warning_left <= 0:
                    # according to the game requirements, user should lose 2 guesses or warnings if the invalid input is vowel, othersie the lose is only one either guess or warning
                    if user_guess in vowels:
                        num_guess_left = num_guess_left - 2
                        if user_guess in guessed_letters_from_user:
                            print("Oops! You've already guessed that letter. You have", num_guess_left, "guess/es left: ", guessed_word)
                        else: 
                            print("Oops! That is not a valid letter. You have", num_guess_left, "guess/es left: ", guessed_word)
                    else:
                        num_guess_left = num_guess_left - 1
                        if user_guess in guessed_letters_from_user:
                            print("Oops! You've already guessed that letter. You have", num_guess_left, "guess/es left: ", guessed_word)
                        else: 
                            print("Oops! That is not a valid letter. You have", num_guess_left, "guess/es left: ", guessed_word)
                # if the user still has warnings availble, he should lose warnings first
                else:
                    # according to the game requirements, user should lose 2 guesses or warnings if the invalid input is vowel, othersie the lose is only one either guess or warning
                    if user_guess in vowels:
                        # if ther eis only one warning left, the user lose the remaining one warning and one guess trail
                        if num_warning_left == 1:
                            num_warning_left = num_warning_left - 1
                            num_guess_left = num_guess_left - 1
                            if user_guess in guessed_letters_from_user:
                                print("Oops! You've already guessed that letter. You have", num_guess_left, "guess/es left: ", guessed_word)
                            else: 
                                print("Oops! That is not a valid letter. You have", num_warning_left, "warning/s left: ", guessed_word)
                            # if ther is more than one warning, the user hsould lose two warnings for invalid vowel
                        else:
                            num_warning_left = num_warning_left - 2
                            if user_guess in guessed_letters_from_user:
                                print("Oops! You've already guessed that letter. You have", num_warning_left, "warning/s left: ", guessed_word)
                            else: 
                                print("Oops! That is not a valid letter. You have", num_warning_left, "warning/s left: ", guessed_word)
                            # if the invalid input is consonant, the user should lose only one either warning or guess trail.
                    else:
                        num_warning_left = num_warning_left -1
                        if user_guess in guessed_letters_from_user:
                            print("Oops! You've already guessed that letter. You have", num_warning_left, "warnings left: ", guessed_word)
                        else: 
                            print("Oops! That is not a valid letter. You have", num_warning_left, "warning/s left: ", guessed_word)
            # saving all user input either valid or not to use it in the fnction "get_gueesed_word" and "is_word_guessed"
            guessed_letters_from_user.append(user_guess)
        
    if is_word_guessed(secret_word, guessed_letters_from_user):
        unique_letters_of_secret_word = []
        for h in secret_word:
            if h not in unique_letters_of_secret_word:
                unique_letters_of_secret_word.append(h)
        total_score = num_guess_left * len(unique_letters_of_secret_word)
        print('Congratulations, you won!')
        print('Your total score for this game is:', total_score)
    else:
        print('Sorry, you ran out of guesses. The word was', secret_word)




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

'''
if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
'''