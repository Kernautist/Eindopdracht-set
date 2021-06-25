import set # importeert alle functies van het document set.py
import sys, pygame # importeert de libraries sys en pygame, welke nodig zijn voor het visualiseren
import time # deze library hebben we nodig om een timer bij te kunnen houden.
pygame.init() # initialiseert alle pygame modules

grootte = breedte, hoogte = 1400, 800 # hier stellen we de grootte van het scherm vast
scherm = pygame.display.set_mode(grootte) # Creëert het scherm, met ingestelde grootte
pygame.display.set_caption("Set") # Zorgt dat het venster 'Set' heet ipv 'pygame window'

scherm_rh = scherm.get_rect() # maakt een rechthoek (rh) van het scherm. Hierdoor kunnen we waarschijnlijk later makkelijker dingen afbeelden op het scherm, zonder de x en y coördinaat te moeten hardcoden
'''is dit nodig?????? we gebruiken scherm_rh (nog) nergens'''

Pot = set.Pot() # maakt een pot aan met alle mogelijke kaarten
Kaarten = [] # dit zijn de kaarten die op tafel liggen, in onderstaande for-loop zorgen we dat er 12 kaarten komen te liggen die gelijk van de pot afgehaald worden.
for i in range(12):
    Kaarten.append(Pot.pop()) # Zoals je ziet, halen we 12 keer een kaart van de pot af en 'leggen we die op tafel', in de verzameling Kaarten.

def Kaartnaam(invoer): # creëert de naam van de afbeelding van een kaart
    return set.Kaart(invoer).gifnaam() # bijvoorbeeld de invoer '[0,0,0,0]' geeft als uitvoer 'greendiamondempty1.gif'
def Pad(invoer): # geeft het pad naar de afbeelding van de kaart
    return 'kaarten\\' + Kaartnaam(invoer) # dit geeft voor de invoer '[0,0,0,0]' de uitvoer 'kaarten\greendiamondempty1.gif'. Als we dit nu proberen te openen, opent de computer eerst de map kaarten en daarna het document greendiamondempty1.gif
def Afbeelding(invoer): # laadt de afbeelding van de kaart die wordt ingevoerd. Deze afbeelding wordt nog niet afgebeeld, maar slechts ingeladen.
    return pygame.image.load(Pad(invoer)).convert() # wat .convert() dot is lastig uit te leggen, maar dit zorgt ervoor dat het laden van alle pixels sneller gaat.

tekst = ''
font = pygame.font.Font(None, 32)
input_box = pygame.Rect(100, 100, 140, 32)
kleur = pygame.Color('lightskyblue3')
kaart_keuze = []
t0 = time.time()
begonnen = False
tekst_invoer = pygame.Rect(630, 400, 40, 32)

while not begonnen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and len(tekst) > 0:
                tijd = int(tekst)
                tekst = ''
                begonnen = True
            elif event.key == pygame.K_BACKSPACE and len(tekst) > 0:
                scherm.fill(pygame.Color('black'), tekst_invoer)
                tekst = tekst[:-1]
            elif event.unicode in ['0','1','2','3','4','5','6','7','8','9'] and len(tekst) < 2:
                tekst += event.unicode
    tekst_surface = font.render(tekst, True, kleur)
    scherm.blit(tekst_surface, (tekst_invoer.x + 6, tekst_invoer.y + 6, tekst_invoer.width - 12, tekst_invoer.height - 12))
    pygame.draw.rect(scherm, kleur, tekst_invoer , 2)
    
    pygame.display.update()

scherm.fill(pygame.Color('black'))  # Hele scherm wordt gereset

while begonnen: # deze loop wordt gerund terwijl het spel gespeeld wordt, tot het spel wordt afgesloten
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
                if tekst == 'VindSets':
                    '''cheatcode weghalen wanneer we klaar zijn??'''
                    print(set.VindSets(Kaarten))
                else:
                    kaart_keuze.append(tekst)
                tekst = ''
                scherm.fill(pygame.Color("black"), (input_box.x + 450, input_box.y + 5, 140, 32))
            elif event.key == pygame.K_BACKSPACE and len(tekst) > 0:
                tekst = tekst[:-1]
                scherm.fill(pygame.Color("black"), (input_box.x + 450, input_box.y + 5, 140, 32))
            elif len(tekst) < 8:
                '''bovenstaande 8 kan een 2 worden als de cheatcode weggehaald wordt'''
                tekst += event.unicode
    # Render the current text.
    txt_surface = font.render(tekst, True, kleur)
    
    ''' box groter maken als tekst lang is mogen we van mij weghalen.
    invoer wordt toch niet langer dan 2 cijfers, misschien kunnen we dit er nog in programmeren?
    Ik vind dit iig een beetje onoverzichtelijk en vooral ook overbodig.
    '''
    # Resize the box if the text is too long.
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    # Blit the text.
    scherm.blit(txt_surface, (input_box.x + 450, input_box.y + 5))
    # Blit the input_box rect.
    pygame.draw.rect(scherm, kleur, (input_box.x + 450, input_box.y + 5, input_box.w, input_box.height) , 2)

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
