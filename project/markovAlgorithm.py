import random
import matplotlib.pyplot as plt
import regex
import nltk
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.model = defaultdict(list)
        self.starts = []
    
    def educate(self, text):
        if isinstance(text, str):
            sentences = nltk.sent_tokenize(text)
        else:
            sentences = text
        
        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            if len(words) > 1:
                self.starts.append(words[0])
            
            for i in range(len(words) - 1):
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
            current_word = random.choice(self.model[next_word])
            sentence.append(current_word)
        
        return ' '.join(sentence)
