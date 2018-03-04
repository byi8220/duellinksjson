import cardscraper
import json
import sys

# Creates card json files for everything in the list
# Usage: python packscraper.py [pack file] [outputfolder] [pack name]

def main():
    cardlist = sys.argv[1]
    outpath = sys.argv[2]
    packname = sys.argv[3]
    cardfile = open(cardlist, 'r',encoding="UTF-8")
    rarity = "NA"
    for line in cardfile:
        # Check rarity
        line = line.rstrip()
        if line == "UR CARDS":
            rarity = "UR"
        elif line == "SR CARDS":
            rarity = "SR"
        elif line == "R CARDS":
            rarity = "R"
        elif line == "N CARDS":
            rarity = "N"
        elif len(line) > 0:
            srcs = [packname]
            currentCard = None
            filename = None
            print("Exporting {0} [{1}]".format(line, rarity))
            try:
                currentCard = cardscraper.getCard(line, srcs, rarity)
            except cardscraper.CardNotFoundError:
                currentCard = cardscraper.Card()
                currentCard.name = line
                currentCard.sources = srcs
                currentCard.rarity = rarity
                filename = "[NOT FOUND ON YGOHUB] " + line + ".json"
            finally:
                cardscraper.exportCard(currentCard,outpath,filename)

            





if __name__ == "__main__":
    main()