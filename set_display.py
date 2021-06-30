import set  # Importeert alle functies van het document set.py
import sys, pygame  # Importeert de libraries sys en pygame, welke nodig zijn voor het visualiseren
import time  # Deze library hebben we nodig om een timer bij te kunnen houden.
pygame.init()  # Initialiseert alle pygame modules

grootte = breedte, hoogte = 1400, 800  # Hier stellen we de grootte van het scherm vast
scherm = pygame.display.set_mode(grootte)  # Creëert het scherm, met ingestelde grootte
pygame.display.set_caption("Set")  # Zorgt dat het venster 'Set' heet ipv 'pygame window'

scherm_rh = scherm.get_rect()  # Maakt een rechthoek (rh) van het scherm. Hierdoor kunnen we waarschijnlijk later makkelijker dingen afbeelden op het scherm, zonder de x en y coördinaat te moeten hardcoden
'''is dit nodig?????? we gebruiken scherm_rh (nog) nergens'''

Pot = set.Pot()  # Maakt een lijst 'Pot' aan met alle mogelijke kaarten
Kaarten = []  # Dit zijn de kaarten die op tafel liggen
for i in range(12):
    Kaarten.append(Pot.pop())  # We halen 12 keer een kaart van de pot af en 'leggen die op tafel', in de verzameling Kaarten.

def Gifnaam(invoer):
    '''
    Genereert de bestandsnaam van de afbeelding van een kaart.
    Zo geeft de invoer '[0,0,0,0]'  als uitvoer 'greendiamondempty1.gif'.

    Parameters
    ----------
    invoer : list
        Deze lijst heeft 4 variabelen en stelt een kaart voor.

    Returns
    -------
    gifnaam : string
        Dit is de naam van het .gif bestand dat bij de kaart 'invoer' hoort.
    
    '''
    gifnaam = set.Kaart(invoer).gifnaam()
    return gifnaam

def Pad(invoer):
    '''
    Genereert het pad om bij een afbeelding van een kaart te komen.
    Omdat dit programma in dezelfde map opgeslagen staat als de map 'kaarten',
    voldoet  om bij de invoer '[0,0,0,0]' als uitvoer
    'kaarten\greendiamondempty1.gif' te geven.

    Parameters
    ----------
    invoer : list
        Deze lijst van 4 variabelen stelt een kaart voor.

    Returns
    -------
    Pad : string
        Deze string stelt dus het pad voor dat je vanaf de locatie van dit
        pythonbestand 'af moet leggen' om bij een .gif afbeelding van een
        kaart te komen.

    '''
    Pad = 'kaarten\\' + Gifnaam(invoer)  # Hier is een dubbele backslash nodig, omdat een enkele backslash op een andere manier geïnterpreteerd wordt door python.
    return Pad

# laadt de afbeelding van de kaart die wordt ingevoerd. Deze afbeelding wordt nog niet afgebeeld, maar slechts ingeladen.
def Afbeelding(invoer):
    '''
    Laadt de afbeelding in die bij een bepaalde kaart hoort.
    Deze afbeelding wordt slechts ingeladen, nog niet op het scherm geplaatst.

    Parameters
    ----------
    invoer : list
        Deze lijst met 4 variabelen stelt een kaart voor.

    Returns
    -------
    afbeelding : pygame.Surface
        Dit is de afbeelding die hoort bij de kaart 'invoer'.

    '''
    afbeelding = pygame.image.load(Pad(invoer)).convert() # wat .convert() dot is lastig uit te leggen, maar dit zorgt ervoor dat het laden van alle pixels sneller gaat.
    return afbeelding

font = pygame.font.SysFont('Arial', 28)
wit = pygame.Color('white')
zwart = pygame.Color('black')
kaart_keuze = []
t0 = time.time()
begonnen = False
tijd_invoer = ''
tijd_invoer_rh = pygame.Rect(630, 400, 40, 32)
tijd_opvraag = font.render('Hoeveel tijd wil je jezelf geven om een set te vinden? Voer een waarde in tussen 1 en 99 seconden.', True, wit)
set_invoer = ''
set_invoer_rh = pygame.Rect(10, 700, 140, 32)

nummer1 = font.render('1', True, zwart)
nummer2 = font.render('2', True, zwart)
nummer3 = font.render('3', True, zwart)
nummer4 = font.render('4', True, zwart)
nummer5 = font.render('5', True, zwart)
nummer6 = font.render('6', True, zwart)
nummer7 = font.render('7', True, zwart)
nummer8 = font.render('8', True, zwart)
nummer9 = font.render('9', True, zwart)
nummer10 = font.render('10', True, zwart)
nummer11 = font.render('11', True, zwart)
nummer12 = font.render('12', True, zwart)

while not begonnen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and len(tijd_invoer) > 0:
                tijd = int(tijd_invoer)
                tijd_invoer = ''
                begonnen = True
            elif event.key == pygame.K_BACKSPACE and len(tijd_invoer) > 0:
                scherm.fill(zwart, tijd_invoer_rh)
                tijd_invoer = tijd_invoer[:-1]
            elif event.unicode in ['0','1','2','3','4','5','6','7','8','9'] and len(tijd_invoer) < 2:
                tijd_invoer += event.unicode
    
    scherm.blit(tijd_opvraag, (190,340))
    
    tijd_invoer_surface = font.render(tijd_invoer, True, wit)
    scherm.blit(tijd_invoer_surface, (tijd_invoer_rh.x + 6, tijd_invoer_rh.y , tijd_invoer_rh.width - 12, tijd_invoer_rh.height - 12))
    
    pygame.draw.rect(scherm, wit, tijd_invoer_rh , 2)
    
    pygame.display.update()

scherm.fill(zwart)  # Hele scherm wordt gereset

while begonnen: # deze loop wordt gerund terwijl het spel gespeeld wordt, tot het spel wordt afgesloten
    t1 = time.time()
    
    '''onderstaande moet weg'''
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
                if set_invoer == 'VindSets':
                    '''cheatcode weghalen wanneer we klaar zijn??'''
                    print(set.VindSets(Kaarten))
                elif set_invoer in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
                    kaart_keuze.append(set_invoer)
                set_invoer = ''
                scherm.fill(zwart, (set_invoer_rh.x, set_invoer_rh.y, 140, 32))
            elif event.key == pygame.K_BACKSPACE and len(set_invoer) > 0:
                set_invoer = set_invoer[:-1]
                scherm.fill(zwart, (set_invoer_rh.x, set_invoer_rh.y, 140, 32))
            elif len(set_invoer) < 8 and (event.unicode in 'VindSets' or event.unicode in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                '''bovenstaande 8 kan een 2 worden als de cheatcode weggehaald wordt.
                Ook kan je hier in zetten dat de event.unicode een cijfer moet zijn'''
                set_invoer += event.unicode
    # Render the current text.
    set_invoer_surface = font.render(set_invoer, True, wit)
    # Blit the text.
    scherm.blit(set_invoer_surface, (set_invoer_rh.x, set_invoer_rh.y))
    # Blit the input_box rect.
    pygame.draw.rect(scherm, wit, (set_invoer_rh.x, set_invoer_rh.y, set_invoer_rh.width, set_invoer_rh.height) , 2)
    
    if len(kaart_keuze) == 0:  # Beeldt de opvraag van de set af
        set_opvraag_surface = font.render('Voer het kaartnummer in van de eerste kaart van je gevonden set:', True, wit)
    elif len(kaart_keuze) == 1:
        set_opvraag_surface = font.render('Voer het kaartnummer in van de tweede kaart van je gevonden set:', True, wit)
    else:
        set_opvraag_surface = font.render('Voer het kaartnummer in van de derde kaart van je gevonden set:', True, wit)
    scherm.fill(zwart, (10, 650, 690, 35))
    scherm.blit(set_opvraag_surface, (10, 650))
    
    if len(kaart_keuze) == 0:
        kaart_keuze_string = 'Ingevoerde kaarten: '
    elif len(kaart_keuze) == 1:
        kaart_keuze_string = 'Ingevoerde kaarten: ' + kaart_keuze[0]
    elif len(kaart_keuze) == 2:
        kaart_keuze_string = 'Ingevoerde kaarten: ' + kaart_keuze[0] + ', ' + kaart_keuze[1]
    kaart_keuze_surface = font.render(kaart_keuze_string, True, wit)
    scherm.fill(zwart, (10, 740, 280, 35))
    scherm.blit(kaart_keuze_surface, (10, 740))
    
    if len(kaart_keuze) == 3:  # Checkt of de ingevoerde kaarten een set zijn
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
        
    if t1 - t0 > tijd and len(Pot) >= 3:
        if len(set.VindSets(Kaarten)) != 0:
            GevondenSet = set.VindSets(Kaarten)[0]
            i = 0
            while i < 3 and len(Pot) != 0:
                Kaarten[int(Kaarten.index(GevondenSet[i]))] = Pot.pop()
                i += 1
        else:
            GevondenSet = []
            set.vervang_kaarten(Kaarten, Pot)
        t0 = time.time()
    
    '''Kaarten rooster ziet er als volgt uit:
    1 4 7 10
    2 5 8 11
    3 6 9 12
    '''         
    scherm.blit(Afbeelding(Kaarten[0]), (10,10))
    scherm.blit(nummer1, (12,12))
    scherm.blit(Afbeelding(Kaarten[1]), (10,220))
    scherm.blit(nummer2, (12,222))
    scherm.blit(Afbeelding(Kaarten[2]), (10,430))
    scherm.blit(nummer3, (12,432))
    scherm.blit(Afbeelding(Kaarten[3]), (120,10))
    scherm.blit(nummer4, (122,12))
    scherm.blit(Afbeelding(Kaarten[4]), (120,220))
    scherm.blit(nummer5, (122,222))
    scherm.blit(Afbeelding(Kaarten[5]), (120,430))
    scherm.blit(nummer6, (122,432))
    scherm.blit(Afbeelding(Kaarten[6]), (230,10))
    scherm.blit(nummer7, (232,12))
    scherm.blit(Afbeelding(Kaarten[7]), (230,220))
    scherm.blit(nummer8, (232,222))
    scherm.blit(Afbeelding(Kaarten[8]), (230,430))
    scherm.blit(nummer9, (232,432))
    scherm.blit(Afbeelding(Kaarten[9]), (340,10))
    scherm.blit(nummer10, (342,12))
    scherm.blit(Afbeelding(Kaarten[10]), (340,220))
    scherm.blit(nummer11, (342,222))
    scherm.blit(Afbeelding(Kaarten[11]), (340,430))
    scherm.blit(nummer12, (342,432))
    
    pygame.display.update()  # Updatet het scherm. Alle afbeeldingen die op het scherm geplaatst zijn, worden hier daadwerkelijk pas afgebeeld.
