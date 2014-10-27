__author__ = "Tsh"

# dem cheeses
cheeses = {
    "cheddar":
        ("A235-4", "A236-1", "A236-2", "A236-3", "A236-5", "C31-1", "C31-2"),
    "mozarella":
        ("Q456-9", "Q456-8", "A234-5", "Q457-1", "Q457-2"),
    "gombost":
        ("ZLAFS55-4", "ZLAFS55-9", "GOMBOS-7", "A236-4"),
    "geitost":
        ("SPAZ-1", "SPAZ-3", "EMACS45-0"),
    "port salut":
        ("B15-1", "B15-2", "B15-3", "B15-4", "B16-1", "B16-2", "B16-4"),
    "camembert":
        ("A243-1", "A234-2", "A234-3", "A234-4", "A235-1", "A235-2", "A235-3"),
    "ridder":
        ("GOMBOS-4", "B16-3")
}

def saluteThePort():
    for location in cheeses["port salut"]:
        print(location)

def getInfectedCheez():
    infected_shelves = ["A234", "A235", "B13", "B14", "B15", "C31"]
    infected_cheeses = []
    for cheese in cheeses:
        for location in cheeses[cheese]:
            if location.split("-")[0] in infected_shelves:
                if cheese not in infected_cheeses:
                    infected_cheeses.append(cheese)
    return infected_cheeses

def getNonInfectedCheez():
    infected_shelves = ["A234", "A235", "B13", "B14", "B15", "C31"]
    noninfected_cheeses = []
    for cheese in cheeses:
        for location in cheeses[cheese]:
            if location.split("-")[0] not in infected_shelves:
                if cheese not in noninfected_cheeses:
                    noninfected_cheeses.append({"cheese":cheese, "location":location})
    return noninfected_cheeses

if __name__ == "__main__":
    #saluteThePort()
    #print(getInfectedCheez())
    for cheesyelement in getNonInfectedCheez():
        print(cheesyelement["location"], cheesyelement["cheese"])
