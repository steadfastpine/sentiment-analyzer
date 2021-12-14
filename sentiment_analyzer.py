
# Program Name:		Word Frequency
# Program Author:	Scott Forsberg
# Creation Date:	2019-02-07
# Class:		CSE 110
# Python Version:	3.7.1


# define dictionary for counting all of the present words in text body
wordCounts={}
# define dictionary for counting all of the negative keywords found in main text
negWordCounts={}
# define dictionary for counting all of the positive keywords found in main text
posWordCounts={}


#function to sort converted dictionary tuples by the count (value)
def byFreq(pair):
    return pair[1]


# read negative words into a list
negWords = open('negative-words.txt','r', encoding='utf-8', errors='ignore').read().splitlines()[35:]
# read positive words into a list
posWords = open('positive-words.txt','r', encoding='utf-8', errors='ignore').read().splitlines()[35:]


# reads body of text to be analyzed
main_text_body_words = open('text_to_analyze.txt','r').read()

# defines special characters to be omitted
special_characters = '\n!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'

# defines stop-words to be omitted# 
stop_words="a,an,and,as,at,be,but,etc,for,if,in,it,its,is,of,or,so,such,the,this,to,with"
# places stop words into a list
stop_words=stop_words.split(',')


# iterate through each special character
for special_character in special_characters:

        # replace the occurance of each special character found in the text with a space
        main_text_body_words=main_text_body_words.replace(special_character," ")


# in main body text, concatinate multiple spaces into one
main_text_body_words=main_text_body_words.replace("  "," ")
main_text_body_words=main_text_body_words.replace("  "," ")
main_text_body_words=main_text_body_words.replace("  "," ")


# places main body text into a list
main_text_body_words=main_text_body_words.split(" ")


# iterate through each main body text word
for main_text_body_word in main_text_body_words:

        # define stop word found variable
        stopWordFound=0

        # iterate through each stop word
        for stop_word in stop_words:

                #check if stop word is the current dictionary word being checked
                if stop_word == main_text_body_word:     

                        # current main body word is stop word
                        stopWordFound=1

        # if no stop words found in current main body word
        if stopWordFound == 0:
                
                # increment the count of each word by one, for each appearance
                wordCounts[main_text_body_word]=wordCounts.get(main_text_body_word,0)+1



# convert the wordCounts dictionary into a list, with each list item containing a tuple representing the key and value
sort_main_text_body_words = list(wordCounts.items())


# sort the counted dictionary list by key, in alphabetical order
sort_main_text_body_words.sort()
# sort the counted dictionary list by counted value, in decending order
sort_main_text_body_words.sort(key=byFreq, reverse=True)


# define a numerical range with 25 total items (0-24)
wordItems=range(0,25)


# newline
print("\n")

# title
print("# Top Total Keywords", end="\n\n")

# iterate through numerical range
for wordItem in wordItems:

        # Print the list number "wordItem" of each "sort_main_text_body_words", both key and value
        print("{0:<15}{1:>5}".format(sort_main_text_body_words[wordItem][0],sort_main_text_body_words[wordItem][1]))




# set initial posSentiment value
posSentiment = 0

# cycle through each positive word
for posWord in posWords:

        # set the dictionary value of each positive word key to the value of the occurances in main text body
        posWordCounts[posWord]=main_text_body_words.count(posWord)

        # add count of positive words to posSentiment
        posSentiment=posSentiment+main_text_body_words.count(posWord)


# convert the posWordCounts dictionary into a list, with each list item containing a tuple representing the key and value
posWordsOut = list(posWordCounts.items())

# sort the counted dictionary list by key, in alphabetical order
posWordsOut.sort()
# sort the counted dictionary list by counted value, in decending order
posWordsOut.sort(key=byFreq, reverse=True)

# define a numerical range with 5 total items (0-4)
wordItems=range(0,5)


# newline
print("\n")

# title
print("# Top Positive Keywords", end="\n\n")


# iterate through numerical range
for wordItem in wordItems:

        # Print the list number "wordItem" of each "negWordsOut" list item, both key and value
        print("{0:<15}{1:>5}".format(posWordsOut[wordItem][0],posWordsOut[wordItem][1]))




# set initial negSentiment value
negSentiment = 0

# cycle through each negative word
for negWord in negWords:

        # set the dictionary value of each negative word key to the value of the occurances in main text body
        negWordCounts[negWord]=main_text_body_words.count(negWord)

        # add count of positive words to posSentiment
        negSentiment=negSentiment+main_text_body_words.count(negWord)

# convert the negWordCounts dictionary into a list, with each list item containing a tuple representing the key and value
negWordsOut = list(negWordCounts.items())

# sort the counted dictionary list by key, in alphabetical order
negWordsOut.sort()
# sort the counted dictionary list by counted value, in decending order
negWordsOut.sort(key=byFreq, reverse=True)

# define a numerical range with 5 total items (0-4)
wordItems=range(0,5)


# newline
print("\n")

# title
print("# Top Negative Keywords", end="\n\n")


# iterate through numerical range
for wordItem in wordItems:

        # Print the list number "wordItem" of each "negWordsOut" list item, both key and value
        print("{0:<15}{1:>5}".format(negWordsOut[wordItem][0],negWordsOut[wordItem][1]))


# newline
print("\n")

# title
print("# Sentiment Score", end="\n\n")


# calculate total sentiment
sentiment=posSentiment-negSentiment

# print sentiment scores
print(sentiment)

# newline
print("\n")

