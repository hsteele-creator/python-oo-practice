"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    # def __init__(self, path):
    #     self.path = path
    #     self.file = open(path, "r")
    #     self.lines = 0
    #     self.read = []
    #     self.reader()
        
    #     for line in self.file:
    #         self.lines += 1
    #     print(f"{self.lines} words read")
    
    def __init__(self, path):
        file = open(path)
        
        self.words = self.parse(file)
        
        print(f"{len(self.words)} words read")
        
        
    # def reader(self):
    #     """reads every word in the passed in file and prints out the total"""
    #     for line in self.file:
    #         self.read.append(line)
    #         self.lines += 1
    #     return f"{self.lines} words read"
    
    def parse(self, file):
        return [word.strip() for word in file]
    
          
    # def random(self):
    #     """returns a random word from the passed in file"""
    #     random_word = random.choice(self.read)
    #     size = len(random_word)
    #     return random_word[:size-2]
    
    def random(self):
        return random.choice(self.words)
    
    def __repr__(self):
        return "returns a random word from the words in the file"
    

    
class SpecialWordFinder(WordFinder):
        
    def parse(self, file):
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]
    
    
        
            
    