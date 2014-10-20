__author__ = "Tsh"

# a)

def strcmp(str1, str2):
    if len(str1) != len(str2):
        return False

    # nå vet vi at begge strengene er like lange, derfor er
    # likegyldig hvilken streng vi tar len() av
    for index in range(len(str1)):
        if str1[index] != str2[index]:
            return False
    return True

# b)

def strreverse(string):
    out = []
    for char in string:
        out.insert(0, char)
    return "".join(out)

# c)

def palindrome(string):
    return strcmp(string, strreverse(string))

# d)

def contains(str1, str2):
    if not str2 in str1:
        return False
    startpoint = 0
    for index in range(len(str1)):
        if str1[index:(index+len(str2))] == str2:
            startpoint = index
    return startpoint


if __name__ == "__main__":
    #print(strcmp("Hello", "Hello"))
    #print(strreverse("Hello"))
    #print(palindrome("radar"))
    print(contains("Hello", "llo"))