import set
import os # deze library is nodig om bestanden uit een andere map eenvoudig te kunnen openen
import sys, pygame # importeert de libraries sys en pygame, welke nodig zijn voor het visualiseren
import time
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

text = ''
font = pygame.font.Font(None, 32)
input_box = pygame.Rect(100, 100, 140, 32)
kleur = pygame.Color('lightskyblue3')
kaart_keuze = []
start_ticks=pygame.time.get_ticks()
t0 = time.time()
while True: # deze loop wordt gerund terwijl het spel gespeeld wordt, tot het spel wordt afgesloten
    t1 = time.time()
    if len(Pot) == 0:
        Pot = set.Pot()
        for kaart in Kaarten:
            Pot.remove(kaart)
    for event in pygame.event.get(): # Registreert alle events, zoals muisklikken etc.
        if event.type == pygame.QUIT: # Als op het kruisje gedrukt wordt, dan moet het programma afsluiten
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if text == 'VindSets':
                    print(set.VindSets(Kaarten))
                else:
                    kaart_keuze.append(text)
                text = ''
                scherm.fill(pygame.Color("black"), (input_box.x + 450, input_box.y + 5, 140, 32))
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
                scherm.fill(pygame.Color("black"), (input_box.x + 450, input_box.y + 5, 140, 32))
            else:
                text += event.unicode
    # Render the current text.
    txt_surface = font.render(text, True, kleur)
    # Resize the box if the text is too long.
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    # Blit the text.
    scherm.blit(txt_surface, (input_box.x + 450, input_box.y + 5))
    # Blit the input_box rect.
    pygame.draw.rect(scherm, kleur, (input_box.x + 450, input_box.y + 5, input_box.w, input_box.height) , 2)
    '''Kaarten rooster ziet er als volgt uit:
    1 4 7 10
    2 5 8 11
    3 6 9 12
    '''
    if len(kaart_keuze) == 3:
        Kaart1 = set.Kaart(Kaarten[int(kaart_keuze[0]) -1])
        Kaart2 = set.Kaart(Kaarten[int(kaart_keuze[1]) -1])
        Kaart3 = set.Kaart(Kaarten[int(kaart_keuze[2]) -1])
        
        if set.IsSet(Kaart1, Kaart2, Kaart3):
            for i in range(3):
                if len(Pot) != 0:
                    Kaarten[int(kaart_keuze[i])-1] = Pot.pop()
                else:
                    Kaarten[int(kaart_keuze[i])-1] = 0
        t0 = time.time()
        kaart_keuze = []
        
    if t1 - t0 > 1 and len(Pot) >= 3:
        if len(set.VindSets(Kaarten)) != 0:
            gevonden = set.VindSets(Kaarten)[0]
        else:
            gevonden = []
        if len(gevonden) == 0:
            set.vervang_kaarten(Kaarten, Pot)
        else:
            lijst = []
            for i in range(3):
                if i == 0:
                    lijst += [set.Kaart(gevonden[0]).lijst()]
                elif i == 1:
                    lijst += [set.Kaart(gevonden[1]).lijst()]
                else:
                    lijst += [set.Kaart(gevonden[2]).lijst()]
            i = 0
            while i < 3 and len(Pot) != 0:
                Kaarten[int(Kaarten.index(lijst[i]))] = Pot.pop()
                i += 1
        t0 = time.time()

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
