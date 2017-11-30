import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
    "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip().decode('ascii'))
#print (WORDS)


def convert(snippet, phrase):
    print ("in convert function")
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    print (class_names)
    print (other_names)
    results = []
    results2 = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    print (param_names)
        
    #for sentence in snippet:
    #    result = sentence[:]
    #print (result)
    result = snippet
    
    #for sentence in phrase:
    #    result2 = sentence[:]
    #print (result2)
    result2 = phrase
        
    # fake class names
    for word in class_names:
        result = result.replace("%%%", word, 1)
        result2 = result2.replace("%%%", word, 1)
    print (result)
    print (result2)
        
    # fake other names
    for word in other_names:
        result = result.replace("***", word, 1)
        result2 = result2.replace("***", word, 1)
    print (result)
    print (result2)
        
    # fake parameter lists
    for word in param_names:
        result = result.replace("@@@", word, 1)
        result2 = result2.replace("@@@", word, 1)
    print (result)
    print (result2)
        
    results.append(result)
    results2.append(result2)
    print (results)
    print (results2)

    return results,results2


# keep going until they hit CTRL- D
try:
    #while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            print (snippet)
            print (phrase)
            question, answer = convert(snippet, phrase)
            print (question)
            print (answer)
            #print (PHRASE_FIRST)
            if PHRASE_FIRST:
                question, answer = answer, question

            print (question)

            input("> ")
            print ("ANSWER: %s\n\n" % answer)
except EOFError:
    print ("\nBye")