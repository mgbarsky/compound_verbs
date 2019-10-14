from simplemodel import *


def one_game(model, iter):
    result = 0
    verb = model.get_rand_verb()
    particle = model.get_rand_particle()
    print ("Question "+str(iter))

    print("Can we say:")
    print(verb.upper(), particle.upper(), "?")
    choice = input("y for yes, n for no, any key to quit: ")
    if choice.lower()[0] != 'y' and choice.lower()[0] != 'n':
        return -1

    test_result = model.get_result()
    if (choice.lower()[0] == 'y' and test_result["valid"])\
            or (choice.lower()[0] == 'n' and not test_result["valid"]):
        result = 1
        print ("This is correct!")
    else:
        if test_result["valid"]:
            print ("Not correct:",verb.upper(), particle.upper(),"is a valid combination")
        else:
            print("This does not seem to be correct:", verb.upper(), particle.upper())

    if test_result["valid"]:
        print("That is how we can use",verb.upper(), particle.upper())
        lst = test_result["phraselist"]
        for item in lst:
            print ("MEANING: " + item.getExplanation())
            print ("\tEXAMPLE: " + item.getExample())
    else:
        print ("No such phrasal verb exist in my dictionary")

    print()
    return result


def text_app():
    total_correct = 0
    total_asked = 0
    model = Model()
    iteration = 1

    while True:
        total_asked +=1
        result = one_game(model,iteration)
        if result == -1:
            print ("\nGoodbye!")
            print("Your score is:", str(total_correct), "out of", str(total_asked))
            exit (0)
        if result == 1:
            total_correct += 1
        iteration += 1
        model.rand_question()


if __name__ == '__main__':
    text_app()
