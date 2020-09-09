import string as str
string = "This is the way things are."
print(str.capwords(string, ' '))


def toJadenCase(string):
    return " ".join(w.capitalize() for w in string.split())
