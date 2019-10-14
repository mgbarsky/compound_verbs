from data import Phrase, Key
import csv

#we need combination of verb-part as a key - can be more than one value - list
dictionary = {}

verb_list = []
particle_list=[]

def load_dictionary (csv_name):
    # we need unique verbs
    verb_set = set()

    # we need unique particles
    part_set = set()

    with open(csv_name) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
            phrase = Phrase(row[0],row[1],row[2],row[3])
            verb_set.add(phrase.getVerb())
            part_set.add(phrase.getParticle())
            key = Key (phrase.getVerb(), phrase.getParticle())
            p_list = []
            if key in dictionary:
                p_list = dictionary [key]
            p_list.append(phrase)
            dictionary[key] = p_list


    for v in verb_set:
        verb_list.append(v)

    for p in part_set:
        particle_list.append(p)



if __name__ == '__main__':
    import sys
    #print("This only executes when %s is executed rather than imported" % __file__)
    records = []

    f_name = sys.argv[1]
    load_dictionary (f_name)

    print(verb_list)
    print (particle_list)
    print (dictionary)

