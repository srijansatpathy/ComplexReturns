import spacy
from spacy_syllables import SpacySyllables

spacy.cli.download("en_core_web_sm")

nlp = spacy.load("en_core_web_sm")

nlp.add_pipe("syllables", after="tagger")

class GunningFog(object):
    def __init__(self, txt):
        self.txt = txt

    def sentences(self):
        doc = nlp(self.txt)
        return len(list(doc.sents))

    def words(self):
        doc = nlp(self.txt)
        words = []
        for token in doc:
            if not (token.pos_ == "PUNCT"): 
                words.append(token)
        return len(words)

    def complexWords(self):
        doc = nlp(self.txt)
        complexList = []
        for token in doc:
            if not(token.pos_ == "PUNCT") and not(token.text == "-"):
                if not((token._.syllables_count) is None): 
                    if (token._.syllables_count > 2): complexList.append(token)
                if (token.pos_ == "PROPN") and (token in complexList): complexList.remove(token)
                if (token.pos_ == "VERB") and (token in complexList) and (token._.syllables_count ==3):
                    if (token.text[-3:] == "ing"): complexList.remove(token)
                    if (token.text[-2:] == "ed"): complexList.remove(token)
                    if (token.text[-2:] == "es"): complexList.remove(token)
        return len(complexList)

    def gFogIndex(self):
        gFogIndex = 0.4*((self.words()/self.sentences()) + 100*(self.complexWords()/self.words()))
        return gFogIndex
    