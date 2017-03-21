import random
from random import choice
from nltk.corpus import gutenberg, stopwords
from collections import defaultdict
from string import punctuation

customStopWords = set(stopwords.words('english') + list(punctuation))

TEXTS = [
    # 'bible-kjv.txt',
    'blake-poems.txt',
    # 'whitman-leaves.txt',
    # 'austen-sense.txt',
    # 'shakespeare-caesar.txt',
    # 'melville-moby_dick.txt',
    # 'burgess-busterbrown.txt',
    # 'milton-paradise.txt',
    # 'bryant-stories.txt',
    # 'chesterton-thursday.txt',
]

# Feel free to add more texts here. For a full list of texts,
# open the python shell, and run:
# from nltk.corpus import gutenberg
# print(gutenberg.fileids())


def trainText():
    '''Creates array of words of gutenberg text'''

    temp = []
    for t in TEXTS:
        print('Reading:', t)
        for word in gutenberg.words(t):
            if word not in customStopWords:
                temp.append(word.lower())
    return temp


class MarkovPoetry():
    '''Class for training and predicting poetry'''

    def __init__(self, MarkovOrder, data, textLength):
        self.order = MarkovOrder
        self.groupSize = self.order + 1
        self.text = data
        self.textLength = textLength
        self.graph = defaultdict(str)
        return

    def train(self):
        '''Takes data and creates dictionary of a particular order for predicting words'''

        self.text = self.text + self.text[:self.order]

        for i in range(0, len(self.text) - self.groupSize):
            # key is a tuple of MarkovOrder
            key = tuple(self.text[i:i + self.order])
            value = self.text[i + self.order]

            self.graph.setdefault(key, []).append(value)

    def generate(self):
        '''Generates text'''

        # getting a random tuple to start the text with
        index = random.randint(0, len(self.text) - self.order)
        result = tuple(self.text[index:index + self.order])
        currentTuple = result

        # generating sentence by adding new words
        for i in range(self.textLength):

            nextWord = random.choice(self.graph[currentTuple])
            result += (nextWord,)
            currentTuple = tuple(result[-self.order:])

        print(' '.join(result))

MarkovOrder = 3
textLength = 40
data = trainText()
p = MarkovPoetry(MarkovOrder, data, textLength)
p.train()
p.generate()
