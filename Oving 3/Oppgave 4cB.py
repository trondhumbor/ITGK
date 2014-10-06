firstnames = [
"johan ", "eli ", "mats ", "lene ", "simon ",
"inger ", "henrik ", "kari ", "per "]

lastnames = [
"Hag ", "Hag ", "Basmestad ", "Grimlavaag ", "Kleivesund ",
"Fintenes ", "Svalesand ", "Molteby ", "Hegesen "]

# Ettersom det er et partall antall elementer i listene, vil det midterste
# navnet være likt

for firstname, lastname in zip(firstnames, reversed(lastnames)):
    print(firstname.capitalize(), lastname)