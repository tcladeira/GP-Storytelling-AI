import random
import nltk
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.model = defaultdict(list)      #this is the Markov map that will describe the word transition "Once" -> ["upon", "there", ...]
        self.starts = []
    
    def educate(self, text):        #first we break down the text into sentences.
        if isinstance(text, str):
            sentences = nltk.sent_tokenize(text)    #this nltk function is used to split the text into sentences. 
        else:
            sentences = text
        
        for sentence in sentences:      #second, here, we break down each sentence into words.
            words = nltk.word_tokenize(sentence)
            if len(words) > 1:
                self.starts.append(words[0])
            
            for i in range(len(words) - 1):   #create the map of word transitions here. Probability = frequency of occurrence.
                current_word = words[i]
                next_word = words[i + 1]
                self.model[current_word].append(next_word)
        
    def generate_sentence(self, max_length=12):
        if not self.starts:
            return ValueError("The Markov model is not educated yet.")
        
        current_word = random.choice(self.starts)
        sentence = [current_word]
        
        for _ in range(max_length - 1):
            if current_word not in self.model:
                break
            next_word = random.choice(self.model[current_word])
            sentence.append(next_word)
            current_word = next_word

            if next_word in ['.', '!', '?']:
                break

        text = " ".join(sentence)

        if text[-1] not in ['.', '!', '?']:
            text += '.'
        
        text = text[0].upper() + text[1:]
        
        return text
