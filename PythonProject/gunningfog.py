import spacy #imports the spacy library
from spacy_syllables import SpacySyllables #imports SpacySyllables from spacy_syllables to count the syllables in words

spacy.cli.download("en_core_web_sm") #downloads the English language pipeline

nlp = spacy.load("en_core_web_sm") #loads and stores this pipeline as nlp

nlp.add_pipe("syllables", after="tagger") #adds the syllables pipeline to our nlp

class GunningFog(object):
    '''
    A simple class for representing a string with a Gunning Fog index, and functions that count: the number of words, number of sentences and number of complex words. 
    Computes a Gunning Fog Index for a string.
    '''
    def __init__(self, txt):
        '''
        When initialized this class creates instance variables to store the string txt, given as an input
        Args: 
            txt: string
        Returns:
            None
        '''
        self.txt = txt #saving txt as self.txt

    def sentences(self):
        '''
        returns the number of sentences in self.txt
        Args:
            None
        Returns:
            Integer (number of sentences)
        '''
        #creats a sequence of token objects (container for accessing linguistic features)
        doc = nlp(self.txt) 
        
        #gets the sentences from doc and counts them and returns the number of sentences
        return len(list(doc.sents))
    
    
    def words(self):
        '''
        returns the number of words in self.txt
        Args:
            None
        Returns:
            Integer (number of words)
        '''
        #creats a sequence of token objects
        doc = nlp(self.txt)
        
        #starts an empty list
        words = []
        
        #loops through the elements in doc
        for token in doc:
            if not (token.pos_ == "PUNCT"):  
                #if the element is not a punctuation then it is a word and it is added to the words list
                words.append(token)
                
        #returns the length of the words list (the number of words in txt)
        return len(words)
    

    def complexWords(self):
        '''
        calculates the number of complex words in txt, according to the Gunning Fog definition of complex words
        Args:
            None
        Returns:
            Integer (number of complex words)
        '''
        #creats a sequence of token objects
        doc = nlp(self.txt)
        
        #starts an empty list of complex words
        complexList = []
        
        #loops through the elements in doc
        for token in doc:
            
            #if statement checks if the element is a word
            if not(token.pos_ == "PUNCT") and not(token.text == "-"):
                if not((token._.syllables_count) is None): 
                    
                    #if the word has more than 2 syllables and add it to the complex words list
                    if (token._.syllables_count > 2): complexList.append(token)
                        
                #if the word is a proper noun then remove it from the complex words list
                if (token.pos_ == "PROPN") and (token in complexList): complexList.remove(token)
                    
                #if the word is a 3 syllable verb and ends in either "ing", "ed" or "es" then remove it from complex words list
                if (token.pos_ == "VERB") and (token in complexList) and (token._.syllables_count ==3):
                    if (token.text[-3:] == "ing"): complexList.remove(token)
                    if (token.text[-2:] == "ed"): complexList.remove(token)
                    if (token.text[-2:] == "es"): complexList.remove(token)
        #returns the length of the complex words list (the number of complex words in txt               
        return len(complexList)

    def gFogIndex(self):
        '''
        calculates the Gunning Fog Index
        Args:
            None
        Returns:
            Integer (Gunning Fog Index)
        '''
        #calculates Gunning Fog Index according to Gunning Fog Formula and stores the number as gFogIndex
        gFogIndex = 0.4*((self.words()/self.sentences()) + 100*(self.complexWords()/self.words()))
        
        #returns Gunning Fog Index (gFogIndex)
        return gFogIndex
    
