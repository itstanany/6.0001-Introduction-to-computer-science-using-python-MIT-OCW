# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <Ahmed Ali Mohamed>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
     # computing the first component score
    # converitng string to lower case
    word = word.lower()
    #initializing score variable to track the score value
    word_score = 0
    #if the word string is non-empy string, compute the two component scores
    if len(word) > 0:
        #first-compoenent score
        for x in word:
            word_score = word_score + SCRABBLE_LETTER_VALUES[x]
        # calculauting the second possibility for the second component score to get the bigger
        one_possible_comp_two = (7 * len(word)) - (3 * (n- len(word)))
        #test for the bigger second compoenent value, then calculate the final word score
        if one_possible_comp_two > 1:
            word_score = word_score * one_possible_comp_two
        else:
            word_score = word_score * 1
    #return an integer that represnts score of the word
    return word_score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        if i == 0:
            hand["*"] = 1
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    #asserting the word is in lowercase
    word = word.lower()
    #make a copy of hand that's totlly new and any change in it doesn't affect the original dictionary
    copy_hand = copy.deepcopy(hand)
    #eliminate letters of the word form the hand, and if not present make its value negative
    for a in word:
        # eliminate each letter of word that's present in hand, otherwise, ignore it
        if a in copy_hand:
            #reduces its value by 1, even if it's zero, make its value negative
            copy_hand[a] = copy_hand.get(a, 0) - 1
            
    #new updated hand that will be the return value of the function.It contains left letters that are in hand but not used in word
    new_updated_hand = {}
    #add unused letters to the new upadted hand
    for k in copy_hand:
        #if value of the letter is positive, this implies it's unused letter
        if copy_hand[k] > 0:
            #add unused letters a keys and their value is their number left in hand
            new_updated_hand[k] = copy_hand[k]
    #return dictionary that contains string keys which are unused latters, and integer values that indicate their frequencies
    return new_updated_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    #asserting "word" is in lowercase
    word = word.lower()
    #list of all possible words
    possible_words_list = []
    #test whether the word contains asterisk letter or not
    asterisk_index = word.find("*")
    #return false if the word doesn't contains asterisk and doesn't present in word list
    if asterisk_index != -1 or word in word_list:
        #get all possible word if the word contains asterisk
        if asterisk_index != -1:
            for a in VOWELS:
                possible_word = word[0:asterisk_index] + a + word[asterisk_index + 1:len(word)]
                possible_words_list.append(possible_word)
        else:
            # if the word doesn't contains asterisk, list it as the single possible word
            possible_words_list.append(word)
        # loop through each word of possible word and test its valisity
        for i in range(len(possible_words_list)):
            # if the word is presnt in word_list then go forward and test whether it's formed entirely of letters that are present in hand dictionary
            if possible_words_list[i] in word_list:
                #make dictionary contains letters of the word as keys and their number as key value
                word_letters_frequencies = get_frequency_dict(possible_words_list[i])
		#assume all letters in the word is true, 
                #and if any chachter of the word is not in hand, change this var to false and stop checking further charchters
                #and, if inHand remains true after checking all chachters of the word
                #this means it's a valid word, and return the function with True value
                inHand = True
                for c in word_letters_frequencies:
                    if (word_letters_frequencies[c] <= hand.get(c,0)) or possible_words_list[i].index(c) == asterisk_index:
                        pass
                    else:
                        inHand = False
			break
                if inHand:
                    return True
    #return false in two cases: 
    #case one: the word doesn't contain asterisk and in the same time not in word list
    #case two: all possible words aren't valid
    return False

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    #initialize sum variable
    sum = 0
    #loop through each key of hand,
    # if there is no keys in the dictionary, the loop isn't entered
    for k in hand:
        #extract its value and add it to the sum using incremental method
        sum = sum + hand.get(k, 0)
    #return sum variable
    return sum

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # Keep track of the total score
    total_score = 0
    remaining_letters = update_hand(hand, "")
    # As long as there are still letters left in the hand:
    number_remaining_letters = calculate_handlen(remaining_letters)
    while number_remaining_letters > 0:
        # Display the hand
        #if the player run out of letters
        if number_remaining_letters == 0:
            print('-----------------------------------------------------------------------------')
            print('Ran out of letters. ', end = '')
            break
        else:
            print('-----------------------------------------------------------------------------')
            print('Current Hand is:', end = ' ')
            display_hand(remaining_letters)
        # Ask user for input
        user_input = input('Enter word, or "!!" to indicate that you are finished: ')
        # If the input is two exclamation points:
        if user_input == "!!":
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(user_input, hand, word_list):
                # Tell the user how many points the word earned,
                total_score += get_word_score(user_input, number_remaining_letters)
                print(user_input + ' earned ' + str(get_word_score(user_input, number_remaining_letters)) + ' points. Total: ' + str(total_score) + ' points')
                # and the updated total score
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print('That is not a valid word. Please choose another word.')
                
            # update the user's hand by removing the letters of their inputted word
            remaining_letters = update_hand(remaining_letters, user_input)
            number_remaining_letters = calculate_handlen(remaining_letters)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print("Total Score is: " + str(total_score) )
    # Return the total score as result of function
    return total_score



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    # copy the original hand to mutate the copy and not affecting the original hand
    copy_hand = copy.deepcopy(hand)
    #store new letter
    new_letter = ''
    #ask the user which letter wanted to be replaced
    user_input = letter
    #test whether the letter is in the hand or  not
    if copy_hand.get(user_input, 0) != 0:
    #if in hand, replaced it
        #randomly choose letter from VOWELS or CONSONANTS
        new_letter = random.choice(VOWELS + CONSONANTS)
        #the randomly choosed letter should Not be presnent in the hand already
        while copy_hand.get(new_letter, 0) != 0:
            new_letter = random.choice(VOWELS + CONSONANTS)
        #substitute all letters in the hand with the new letter
        #get the value of the user_input
        user_input_value = copy_hand[user_input]
        #add the new chosen letter to the current hand 
        copy_hand[new_letter] = user_input_value
         #delete the user_input from the current hand
        del copy_hand[user_input]
        #return the new hand with the replaced letter/s
        return copy_hand
    #otherwise return the same hand
    else:
        return hand
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
   
    #ask the user to input a total number of hands
    total_hands = int(input("Enter total number of hands: "))
    #INItoalize variable for recording total scores of all hands
    score_total_hands = 0
     #initalize variable to record the substitution option validity, this is can be done once during the game, so they are written outslide number of hands loop
    sub_valid = True
     #initalize varibale for recording replaying preference, this is can be done once during the game, so they are written outslide number of hands loop
    replay_validity = True
    #playing n hands according to user choice
    for i in range(0, total_hands):
        #for each hand:       
        #get the hand
        current_hand = deal_hand(HAND_SIZE)
        #list the two possible scores of a hand
        current_hand_scores = [0, 0]
        #initialize variable for recording the tries of playing the same hand
        current_hand_try = 0
        #initalize variable for recording user prefernece for replying the current hand
        current_replay_pref = True
        #test for replaying preference and number of tries is less that two, as replaying can be done only once
        while (current_replay_pref and (current_hand_try < 2)):
            #if replaying is valid, play again
            print("Current hand:", end = '')
            display_hand(current_hand)
            # if there are two conditions and one is after the other, then make nested loop, with outer loop is the first condition and inner loop the second consequent condition
            #test for substitution validity and user prefernce for sub
            if sub_valid:
                #ask for user if s/he wants to substitute a letter
                us_sub_pref = input("Would you like to substitute a letter? ").lower()
                if (us_sub_pref == "yes"):
                    #ask which letter and do the substituion, 
                    user_sub_letter = input("Which letter would you like to replace: ")
                    current_hand = substitute_hand(current_hand, user_sub_letter)
                    sub_valid = False
                else:
                    pass
            else:
                pass
            #let the user play the game with hand
#Note of fails:
# here, if you want to do the function and use its return function later, you should store its return value in a varibale, because if you call it again in position where you want to use its return value, it will excute again and have return value other than one upo had from the past call
            score_current_try = play_hand(current_hand, word_list)
            #store the score of the play trial at ithe list of possible scores variable using the number tries variable as the index number
            current_hand_scores[current_hand_try] = score_current_try
            #tell user score of this hand try
            print("Total score for this hand try:", current_hand_scores[(current_hand_try)])
# if there are two conditions and one is after the other, then make nested loop, with outer loop is the first condition and inner loop the second consequent condition
            if replay_validity:
                #test for replaying preference,
                print("-------------------------------------------------------------")
                us_replaying_pref = input("Would you like to replay the hand? ").lower()
                 #if so ask the user if they would like to replay the hand. and increase number of rails by 1
                if (us_replaying_pref == "yes"):
                    current_hand_try += 1
                    # tuen replaying option false as replaying can be done only ONCE DURING THE GAME
                    replay_validity = False
                else:
                    current_replay_pref = False
            #otherwise, turn replaying preference of the current hand to false
            else:
                current_replay_pref = False
            
        #add the hisghest score of two tries to the total score
        if current_hand_scores[0] > current_hand_scores[1]:
            #tell user the highest score for this hand that will be added to the final score
            print("Hand score that will be added to overall score is:", current_hand_scores[0])
            score_total_hands += current_hand_scores[0]
        else:
            #tell user the highest score for this hand that will be added to the final score
            print("Hand score that will be added to overall score is:", current_hand_scores[1])
            score_total_hands += current_hand_scores[1]
        #play the next hand
        print("End of Hand number:", (i+1), "------------------------------------------------------------")
    # return the total score for all hand series
    print("Total score over all hands:", score_total_hands)
    print("End of the Game. Hope you enjoyed it. :)")
        
    return score_total_hands
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
