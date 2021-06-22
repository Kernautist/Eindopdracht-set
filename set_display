import set
import sys, pygame # importeert de libraries sys en pygame, welke nodig zijn voor het visualiseren
pygame.init() # initialiseert alle pygame modules

grootte = breedte, hoogte = 1400, 800
scherm = pygame.display.set_mode(grootte) # Creëert het scherm, met ingestelde grootte
pygame.display.set_caption("Set") # Zorgt dat het venster 'Set' heet ipv 'pygame window'

# Hieronder initialiseren we de afbeeldingen van 12 kaarten

Pot = set.Pot()
Kaarten = []
for i in range(12):
    Kaarten.append(Pot.pop())

for Kaart in Kaarten:
    continue # Hier een functie die de eigenschappen van de kaart omzet naar de naam van de afbeelding

'''kaart1 = pygame.image.load('kaart1.gif').convert()
kaart2 = pygame.image.load('kaart2.gif').convert()
kaart3 = pygame.image.load('kaart3.gif').convert()
kaart4 = pygame.image.load('kaart4.gif').convert()
kaart5 = pygame.image.load('kaart5.gif').convert()
kaart6 = pygame.image.load('kaart6.gif').convert()
kaart7 = pygame.image.load('kaart7.gif').convert()
kaart8 = pygame.image.load('kaart8.gif').convert()
kaart9 = pygame.image.load('kaart9.gif').convert()
kaart10 = pygame.image.load('kaart10.gif').convert()
kaart11 = pygame.image.load('kaart11.gif').convert()
kaart12 = pygame.image.load('kaart12.gif').convert()'''

while True:
    for event in pygame.event.get(): # Registreert alle events, zoals muisklikken etc.
        if event.type == pygame.QUIT: # Als op het kruisje gedrukt wordt, dan moet he programma afsluiten
            pygame.quit()
            sys.exit()
    pygame.display.update() # Updatet het scherm
