from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    maxseenscore = 0
    bestword = None

    for word in wordList:
        if(isValidWord(word, hand, wordList)):
            currentscore = getWordScore(word,n)
            if(currentscore > maxseenscore):
                maxseenscore = currentscore
                bestword = word
    return bestword


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    totalscore = 0
    gameover = False
    handlength = calculateHandlen(hand)
    while(calculateHandlen(hand) > 0 and not(gameover)):
        print "Current Hand: ",
        displayHand(hand)
        
        newword = compChooseWord(hand,wordList,n)
        if (newword == None):
            gameover = True
        else:
            if(not(isValidWord(newword, hand, wordList))):
                print("Invalid word, please try again.")            
            else:
                newscore = getWordScore(newword,n)
                totalscore += newscore
                print('"' + newword + '"' + ' earned ' + str(newscore) + ' points. Total: ' + str(totalscore) + ' points')
                print("")
                hand = updateHand(hand, newword)
    if(calculateHandlen(hand) > 0):
        print("Goodbye! Total score: " + str(totalscore) + ' points.') 
    else:
        print("Ran out of letters. Total score: " + str(totalscore) + ' points.')


#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    exitgame = False
    playedgame = False
    while (not(exitgame)):
        gamechoice = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if (gamechoice.lower() == 'n'):
            hand = dealHand(HAND_SIZE)
            invalidanswer = True
            while invalidanswer:
                player = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if(player.lower() == 'u' or player.lower() == 'c'):
                    invalidanswer=False
                else:
                    print("Invalid command.")
                    print
            if(player == 'c'):
                compPlayHand(hand,wordList,HAND_SIZE)
            else:
                playHand(hand,wordList,HAND_SIZE)
            playedgame = True
        elif (gamechoice.lower() == 'r'):
            if(playedgame == True):
                invalidanswer = True
                while invalidanswer:
                    player = raw_input("Enter u to have yourself play, c to have the computer play: ")
                    if(player.lower() == 'u' or player.lower() == 'c'):
                        invalidanswer=False
                    else:
                        print("Invalid command.")
                        print
                if(player == 'c'):
                    compPlayHand(hand,wordList,HAND_SIZE)
                else:
                    playHand(hand,wordList,HAND_SIZE)
            else:
                print("You have not played a hand yet. Please play a new hand first!")
        elif (gamechoice.lower() == 'e'):
                exitgame = True
        else:
            print("Invalid command.")

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


