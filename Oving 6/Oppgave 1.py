__author__ = "Tsh"

# Oppgave 1

# a
li = list(range(1, 7))  # vil inneholde heltall fra 1 tilogmed 6

# b
for index, element in enumerate(li):
    if element % 2 == 0:
        li[index] = element * -1
# c

li.sort(reverse=True)  # hoyest til lavest

# d

for element in li:
    print(element)