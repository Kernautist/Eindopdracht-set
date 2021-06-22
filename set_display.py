import set
import os # deze library is nodig om bestanden uit een andere map eenvoudig te kunnen openen
import sys, pygame # importeert de libraries sys en pygame, welke nodig zijn voor het visualiseren
pygame.init() # initialiseert alle pygame modules

grootte = breedte, hoogte = 1400, 800
scherm = pygame.display.set_mode(grootte) # Creëert het scherm, met ingestelde grootte
pygame.display.set_caption("Set") # Zorgt dat het venster 'Set' heet ipv 'pygame window'

scherm_rh = scherm.get_rect() #maakt een rechthoek (rh) van het scherm. Hierdoor kunnen we waarschijnlijk later makkelijker dingen afbeelden op het scherm, zonder de x en y coördinaat te moeten hardcoden
'''is dit nodig??????'''

# Hieronder initialiseren we de afbeeldingen van 12 kaarten
Pot = set.Pot()
Kaarten = []
for i in range(12):
    Kaarten.append(Pot.pop())

def Kaartnaam(invoer): # creëert de naam van de afbeelding van een kaart
    return set.Kaart(invoer).gifnaam()
def Pad(invoer): # geeft het pad naar de afbeelding van de kaart
    return os.path.join('kaarten', Kaartnaam(invoer))
def Afbeelding(invoer): # laadt de afbeelding van de kaart die wordt ingevoerd
    return pygame.image.load(Pad(invoer)).convert()

while True: # deze loop wordt gerund terwijl het spel gespeeld wordt, tot het spel wordt afgesloten
    for event in pygame.event.get(): # Registreert alle events, zoals muisklikken etc.
        if event.type == pygame.QUIT: # Als op het kruisje gedrukt wordt, dan moet het programma afsluiten
            pygame.quit()
            sys.exit()
    
    '''Kaarten rooster ziet er als volgt uit:
    1 4 7 10
    2 5 8 11
    3 6 9 12
    '''
    scherm.blit(Afbeelding(Kaarten[0]), (10,10))
    scherm.blit(Afbeelding(Kaarten[1]), (10,220))
    scherm.blit(Afbeelding(Kaarten[2]), (10,430))
    scherm.blit(Afbeelding(Kaarten[3]), (120,10))
    scherm.blit(Afbeelding(Kaarten[4]), (120,220))
    scherm.blit(Afbeelding(Kaarten[5]), (120,430))
    scherm.blit(Afbeelding(Kaarten[6]), (230,10))
    scherm.blit(Afbeelding(Kaarten[7]), (230,220))
    scherm.blit(Afbeelding(Kaarten[8]), (230,430))
    scherm.blit(Afbeelding(Kaarten[9]), (340,10))
    scherm.blit(Afbeelding(Kaarten[10]), (340,220))
    scherm.blit(Afbeelding(Kaarten[11]), (340,430))
    
    pygame.display.update() # Updatet het scherm
