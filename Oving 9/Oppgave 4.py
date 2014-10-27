__author__ = "Tsh"

def number_of_lines(filename):
    with open(filename, "r") as f:
        return len(f.readlines())

def number_frequency(filename):
    occurences = {}
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            if line not in occurences:
                occurences.update({line: 1})
            else:
                occurences[line] += 1
    return occurences

if __name__ == "__main__":
    occurences = number_frequency("nummer.txt")
    for number in occurences:
        print(number + ":", occurences[number])