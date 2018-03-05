# Yugioh Duel Links Json Project

A **very** early start at JSONifying all the cards available in YGO Duel Links.

## Main Tools

The bulk of this project lies in `packscraper.py`

Usage: `python packscraper.py [pack file] [outputfolder] [pack name]`

`pack file` : A text file that contains all the cards to be parsed, sorted by rarity. See the gamea_lists folder for examples

`outputfolder` : The path to store the json files in.

`pack name` : The pack that these cards "belong to" i.e. their source. 

**WARNING**: A CARD THAT COMES FROM ONE PACK THAT SHARES A NAME WITH ANOTHER PACK WILL **OVERWRITE** THE PREVIOUS ENTRY IF IT IS TO BE WRITTEN IN THE SAME DATABASE.

`packscraper` is intended to be used before consulting some form of master list.

## Issues and Further Work

This is an early, somewhat informal script that has much, much work needed for it to be usable on a large scale

* Some cards need to be manually entered as the YGOHub API could not find them (likely not in TCG yet?)
* Only the main boxes have been parsed. Structure Decks, Events, and such have not been parsed
* Cards that can be obtained in multiple ways are not been merged into one entry.
* Related to the above, importing cards from JSON for further modification is actually not implemented yet. It is currently suggested that the user writes their own scripts to import the card JSON for modification then exporting.

### Example JSON files

#### Monster Card JSON Example

```
{"name": "Gladiator Beast Bestiari", 
"img": "https://ygohub.com/card_images/5b42191f-b37e-48e5-8986-9e5f0f0ad0ea.jpg", 
"text": "If this card is Special Summoned by the effect of a \"Gladiator Beast\" monster: Target 1 Spell/Trap Card on the field; destroy that target. At the end of the Battle Phase, if this card attacked or was attacked: You can shuffle it into the Deck; Special Summon 1 \"Gladiator Beast\" monster from your Deck, except \"Gladiator Beast Bestiari\".", 
"cardType": "Monster", 
"number": "41470137", 
"isMonster": true, 
"isSpell": false, 
"isTrap": false, 
"property": null, 
"monsterTypes": ["Effect"], 
"species": "Winged Beast", 
"ATK": "1500", 
"DEF": "800", 
"level": "4", 
"attribute": "WIND", 
"isExtraDeck": false, 
"hasMaterials": false, 
"materials": null, 
"sources": ["Galactic Origin"], 
"traderCost": null, 
"rarity": "R", 
"limit": 3}
```
#### Spell Card JSON Example

```
{"name": "Degenerate Circuit", 
"img": "https://ygohub.com/card_images/696d53af-3f84-4f02-a6b0-dff31ec545c1.jpg", 
"text": "The controller of this card pays 500 Life Points during each of their Standby Phases (this is not optional). Monster Cards that would be returned from the field to the hand are removed from play instead.", 
"cardType": "Spell", 
"number": "36995273", 
"isMonster": false, 
"isSpell": true, 
"isTrap": false, 
"property": "Continuous", 
"monsterTypes": [], 
"species": null,
"ATK": null, 
"DEF": null, 
"level": null, 
"attribute": null, 
"isExtraDeck": false, 
"hasMaterials": false, 
"materials": null, 
"sources": ["Wonders of the Sky"], 
"traderCost": null, 
"rarity": "R", 
"limit": 3}
```