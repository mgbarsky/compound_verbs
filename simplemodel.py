import reader
import random
from data import *


class Model:

    def __init__(self):
        reader.load_dictionary('phrasalverbs.csv')
        self.v_list = reader.verb_list
        self.p_list = reader.particle_list
        self.dictionary = reader.dictionary
        self.rand_verb = ""
        self.rand_particle = ""
        self.result = {}
        self.rand_question()

    def get_rand_verb (self):
        return self.rand_verb

    def get_rand_particle(self):
        return self.rand_particle

    def get_result(self):
        return self.result

    def rand_question(self):
        self.rand_verb = random.choice(self.v_list)
        self.rand_particle = random.choice(self.p_list)
        self.result = {}
        key = Key(self.rand_verb, self.rand_particle)
        if key in self.dictionary:
            self.result["valid"] = True
            self.result["phraselist"] = self.dictionary[key]
        else:
            self.result["valid"] = False






