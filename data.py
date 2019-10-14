class Phrase:
    def __init__(self, verb="", particle="",explanation="",example=""):
        self.verb = verb
        self.particle = particle
        self.explanation = explanation
        self.example=example

    def getVerb(self):
        return self.verb


    def getParticle (self):
        return self.particle


    def getExplanation(self):
        return self.explanation


    def getExample (self):
        return self.example

    def __hash__(self):
        return hash((self.verb, self.particle,self.explanation))

    def __eq__(self, other):
        return (self.verb, self.particle, self.explanation) == (other.verb, other.particle, other.explanation)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)

    def __str__(self):
        return "%s %s: %s" % (self.verb, self.particle, self.explanation)

    def __repr__(self):
        return (str(self))


class Key:
    def __init__(self, verb="", particle=""):
        self.verb = verb
        self.particle = particle


    def __hash__(self):
        return hash((self.verb, self.particle))

    def __eq__(self, other):
        return (self.verb, self.particle) == (other.verb, other.particle)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)

    def __str__(self):
        return "KEY: %s %s" % (self.verb, self.particle)

    def __repr__(self):
        return (str(self))

