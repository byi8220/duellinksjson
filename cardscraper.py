import urllib.request
from html.parser import HTMLParser
import json

GAMEA_URL = "http://duellinks.gamea.co/"
YGOHUB_CALL = "https://www.ygohub.com/api/card_info?name="


class Card:

    def __init__(self):
        # ygohub obtainables
        self.name = None
        self.img = None
        self.text = None
        self.cardType = None
        self.number = None
        self.isMonster = False
        self.isSpell = False
        self.isTrap = False
        self.property = None
        self.monsterTypes = []
        self.species = None
        self.ATK = None
        self.DEF = None
        self.level = None
        self.attribute = None
        self.isExtraDeck = False
        self.hasMaterials = False
        self.materials = None
        
        # duel links specific info
        self.sources = None
        self.traderCost = None
        self.rarity = None
        self.limit = 3

# Thank you based Stackoverflow
class TitleParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.match = False
        self.title = ''

    def handle_starttag(self, tag, attributes):
        self.match = True if tag == 'title' else False

    def handle_data(self, data):
        if self.match:
            self.title = data
            self.match = False


class CardNotFoundError(Exception):
    pass

# Calls YGOhub to get card info
def getCard(name, sources, rarity, traderCost = None, limit = 3):
    card = Card()
    card.name = name

    ygohubstr = YGOHUB_CALL + urllib.parse.quote(name, encoding="UTF-8")
    # Pull card data from ygo json api
    ygohubpage = urllib.request.urlopen(ygohubstr)
    ygoContent = str(ygohubpage.read().decode("UTF-8"))
    hubData = json.loads(ygoContent)
    try:
        hubCard = hubData["card"]
    except KeyError:
        print("{0} is not found on YGOHUB! This must be entered in manually!".format(name))
        raise CardNotFoundError
    card.name = hubCard["name"]
    card.img = hubCard["image_path"]
    card.text = hubCard["text"]
    card.cardType = hubCard["type"]
    card.number = hubCard["number"]
    card.isMonster = hubCard["is_monster"]
    card.isSpell = hubCard["is_spell"]
    card.isTrap = hubCard["is_trap"]
    if card.isMonster:
        card.monsterTypes = hubCard["monster_types"]
        card.species = hubCard["species"]
        card.ATK = hubCard["attack"]
        card.DEF = hubCard["defense"]
        card.level = hubCard["stars"]
        card.attribute = hubCard["attribute"]
        card.isExtraDeck = hubCard["is_extra_deck"]
        card.hasMaterials = hubCard["has_materials"]
        if card.hasMaterials:
            card.materials = hubCard["materials"]
    else:
        card.property = hubCard["property"]

    # Manual Entry of duel links data
    card.sources = sources
    card.rarity = rarity
    card.traderCost = traderCost
    card.limit = limit
    return card

# GameA scraping
def parseURL(url, sources, rarity, traderCost = None, limit = 3):
    page = urllib.request.urlopen(GAMEA_URL + url)
    pagecontent = str(page.read())
    tp = TitleParser()
    tp.feed(pagecontent)
    cardName = tp.title.split('|')[0]
    return getCard(cardName, sources, rarity, traderCost, limit)

# Exports and OVERWRITES a card to the card library 
def exportCard(card, path, filename = None):
    exportstr = json.dumps(card.__dict__)
    if(filename is None):
        filename = str(card.name) + ".json" 
    # Prune filename
    filename = filename.replace('"','')
    filename = filename.replace("'",'').replace("?","").replace(":","")
    f = open(path+"/"+filename, 'w', encoding="UTF-8")
    f.write(exportstr)
    f.close

# Imports a card.json file and returns a card.
def importCard(filepath):
    card = json.load(filepath)
    return card

def main():
    pass



if __name__ == "__main__":
    main()