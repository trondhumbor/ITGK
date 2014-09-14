firstnames = [
"johan ", "eli ", "mats ", "lene ", "simon ",
"inger ", "henrik ", "kari ", "per "]

lastnames = [
"Hag ", "Hag ", "Basmestad ", "Grimlavaag ", "Kleivesund ",
"Fintenes ", "Svalesand ", "Molteby ", "Hegesen "]

# Vi antar at listene er like lange. zip zipper sammen listene
for firstname, lastname in zip(firstnames, lastnames):
	print(firstname, lastname)