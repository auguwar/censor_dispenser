path_one = """/home/augusto/Escritorio/PYTHON PROJECTS/censor_dispenser/email_one.txt"""
path_two = """/home/augusto/Escritorio/PYTHON PROJECTS/censor_dispenser/email_two.txt"""
path_three = """/home/augusto/Escritorio/PYTHON PROJECTS/censor_dispenser/email_three.txt"""
path_four = """/home/augusto/Escritorio/PYTHON PROJECTS/censor_dispenser/email_four.txt"""

email_one = open(path_one, "r").read()
email_two = open(path_two, "r").read()
email_three = open(path_three, "r").read()
email_four = open(path_four, "r").read()


def censorsinglephrase(string, word):
    censored = string.replace(word, "CENSORED")
    return censored


def censorbunchofshit(string, list):
    text = string
    for element in list:
        censored = text.replace(element, "CENSORED")
        text = censored
    return text


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset",
                  "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]


proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her", "herself"]


def censor_negative(string, negatives):
    text = censorbunchofshit(string, proprietary_terms)
    for word in negatives:
        if text.count(word) > 2:
            text = text.replace(word, "CENSORED")
    return text


def censor_all(string):
    censored_terms = negative_words + proprietary_terms
    text = string.split()
    position = []
    for word in censored_terms:
        for i in range(len(text)):
            if word == text[i] or word.title() == text or word.upper() == text or word[:-2] == text[i] or word[:-1] == text[i]:
                position.append(i)
        for i in position:
            case_study = text[i]
            if "." in case_study:
                text[i] = "x" * len(text[i]) + "."
                text[i-1] = "x" * len(text[i-1])
            else:
                text[i] = "x" * len(text[i])
                text[i-1] = "x" * len(text[i-1])
                text[i+1] = "x" * len(text[i+1])
    return (" ".join(text))


def checker(string, list):
    print("Las siguientes palabras no se encuentran censuradas:")
    for element in list:
        if element in string:
            print(element + " x " + str(string.count(element)))


# checker(censor_negative(email_three, negative_words), negative_words+proprietary_terms)

# print(censor_negative(email_three, negative_words))

print(censor_all(email_four))
