import set  # Importeert alle functies van het document set.py
import sys, pygame  # Importeert de libraries sys en pygame, welke nodig zijn voor het visualiseren
import time  # Deze library hebben we nodig om een timer bij te kunnen houden
pygame.init()  # Initialiseert alle pygame modules

def Kaart(invoer):
    '''
    Initialiseert een kaart, zoals gedefiniëerd in set.py.
    Deze functie voorkomt dat je elke keer 'set.' moet schrijven voor Kaart(),
    wat de code overzichtelijker maakt.

    Parameters
    ----------
    invoer : list
        Een lijst van 4 variabelen die een kaart voorstelt.

    Returns
    -------
    Kaart
        De kaart behorend bij de lijst 'invoer'.

    '''
    return set.Kaart(invoer)

def Afbeelding(invoer):
    '''
    Laadt de afbeelding in die bij die kaart 'invoer' hoort.
    Deze afbeelding wordt slechts ingeladen, nog niet op het scherm geplaatst.

    Parameters
    ----------
    invoer : list of int
        Deze lijst met 4 variabelen stelt een kaart voor. Het kan echter
        voorkomen dat er geen kaarten meer over zijn, dan zal de invoer gelijk
        zijn aan 0.

    Returns
    -------
    afbeelding : pygame.Surface
        Dit is de afbeelding die hoort bij de kaart 'invoer'. Indien de invoer
        '0' is, zal deze afbeelding volledig zwart zijn.

    '''
    if invoer == 0: 
        afbeelding = pygame.image.load('kaarten\\black.gif').convert()  # Dubbele backslash wordt geïnterpreteerd als een enkele.
    else:
        afbeelding = pygame.image.load(Kaart(invoer).Pad()).convert()  # Wat .convert() doet is lastig uit te leggen, maar dit zorgt ervoor dat het laden van alle pixels sneller gaat.
    return afbeelding

'''Het programma staat geschreven in een while-loop. Voordat we daar komen,
definiëren we eerst een aantal variabelen die niet veranderen. Het heeft
immers geen zin om deze talloze keren per seconde opnieuw te definiëren.'''

grootte = breedte, hoogte = 1200, 640  # Hier stellen we de grootte van het scherm vast.
scherm = pygame.display.set_mode(grootte)  # Creëert het scherm, met ingestelde grootte
pygame.display.set_caption("Set")  # Zorgt dat het venster 'Set' heet ipv 'pygame window'

Pot = set.Pot()  # Maakt een lijst 'Pot' aan met alle mogelijke kaarten
Kaarten = []  # Dit zijn de kaarten die op tafel liggen
for i in range(12):
    Kaarten.append(Pot.pop())  # We halen 12 keer een kaart van de pot af en 'leggen die op tafel', in de verzameling Kaarten.

Arial24 = pygame.font.Font('Arial.ttf', 24)
Arial40 = pygame.font.Font('Arial.ttf', 40)
wit = pygame.Color('white')
zwart = pygame.Color('black')
kaart_keuze = []  # Dit is de lijst met kaarten die de speler heeft ingevoerd.
begonnen = False  # Wordt true zodra het spel echt begonnen is.
tijd_invoer = ''  # Hierin voert de gebruiker in hoeveel tijd hij zichzelf geeft.
tijd_invoer_rh = pygame.Rect(580, 400, 40, 32)  # Rechthoek waarin de tijd ingevoerd wordt.
tijd_opvraag = Arial24.render('Hoeveel tijd wil je jezelf geven om een set te vinden? Voer een waarde in tussen 1 en 99 seconden.', True, wit)  # In deze variabele is de afbeelding van deze tekst opgeslagen, maar nog niet afgebeeld.
set_invoer = ''  # Hierin voert de gebruiker de kaartnummers van een set in.
set_invoer_rh = pygame.Rect(450, 568, 140, 32)  # Rechthoek waarin de kaarten van een set ingevoerd worden.
score_speler = 0
score_computer = 0
geen_set = 0
Afgelopen = Arial40.render('Afgelopen!!!', True, wit)

nummer1 = Arial24.render('1', True, zwart)  # Creëert een afbeelding met een zwarte 1, welke later pas afgebeeld wordt.
nummer2 = Arial24.render('2', True, zwart)
nummer3 = Arial24.render('3', True, zwart)
nummer4 = Arial24.render('4', True, zwart)
nummer5 = Arial24.render('5', True, zwart)
nummer6 = Arial24.render('6', True, zwart)
nummer7 = Arial24.render('7', True, zwart)
nummer8 = Arial24.render('8', True, zwart)
nummer9 = Arial24.render('9', True, zwart)
nummer10 = Arial24.render('10', True, zwart)
nummer11 = Arial24.render('11', True, zwart)
nummer12 = Arial24.render('12', True, zwart)

while not begonnen:
    '''Deze while-loop herhaalt zichzelf totdat het programma afgesloten wordt,
    of tot er een geldige waarde ingevoerd wordt.'''
    scherm.fill(zwart)
    for event in pygame.event.get():
        '''In deze for-loop wordt voor alle events die pygame registreert,
        gecheckt of het een event is die voor ons van belang is. Zo ja, dan
        doen we er iets mee.'''
        if event.type == pygame.QUIT:  # Het programma wordt afgesloten.
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # Er wordt een toets ingedrukt.
            if event.key == pygame.K_RETURN and len(tijd_invoer) > 0: # Return is hetzelfde als Enter. Dit doet pas iets als er iets ingevoerd is.
                tijd = int(tijd_invoer)  # Slaat de ingevoerde tijd op.
                tijd_invoer = ''
                begonnen = True
            elif event.key == pygame.K_BACKSPACE and len(tijd_invoer) > 0:  # Backspace doet pas iets als er iets ingevoerd is.
                tijd_invoer = tijd_invoer[:-1]  # Zorgt dat de nieuwe invoer een karakter korter is dan de oude.
            elif event.unicode in ['0','1','2','3','4','5','6','7','8','9'] and len(tijd_invoer) < 2:
                '''Bovenstaand elif-statement checkt of de toets die ingedrukt wordt een cijfer is,
                en of de invoer kleiner dan 2 karakters is. Zo zorgen we dat de invoer altijd bestaat uit maximaal 2 cijfers.'''
                tijd_invoer += event.unicode

    scherm.blit(tijd_opvraag, (100,240))  # Beeldt de tekst af op het scherm.
    
    tijd_invoer_surface = Arial24.render(tijd_invoer, True, wit)  # Creëert een afbeelding met de ingevoerde tijd.
    scherm.blit(tijd_invoer_surface, (tijd_invoer_rh.x + 6, tijd_invoer_rh.y + 2))  # Beeldt de ingevoerde tijd af op het scherm.
    
    
    pygame.draw.rect(scherm, wit, tijd_invoer_rh , 2)  # Tekent een  rechthoek om de invoer-box.
    
    pygame.display.update()  # Updatet het scherm, zodat alle veranderingen zichtbaar worden.

scherm.fill(zwart)  # Hele scherm wordt gereset
t0 = time.time()  # Nodig voor de timer. t0 is het tijdstip op dit moment.

while begonnen: # Deze loop wordt gerund terwijl het spel gespeeld wordt, tot het spel wordt afgesloten
    '''Deze while-loop herhaalt zich tot het programma afgesloten wordt.'''
    scherm.fill(zwart)
    for event in pygame.event.get():
        '''In deze for-loop wordt voor alle events die pygame registreert,
        gecheckt of het een event is die voor ons van belang is. Zo ja, dan
        doen we er iets mee.'''
        if event.type == pygame.QUIT:  # Als op het kruisje gedrukt wordt, dan moet het programma afsluiten
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # Checkt of er een toets wordt ingedrukt.
            if event.key == pygame.K_RETURN:  # Return is hetzelfde als enter.
                if set_invoer in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:  # Checkt of de invoer een geldig kaartnummer is.
                    kaart_keuze.append(set_invoer)  # Registreert de invoer als keuze.
                set_invoer = ''
            elif event.key == pygame.K_BACKSPACE and len(set_invoer) > 0:  # Als er nog niets is ingevoerd, doet backspace niets.
                set_invoer = set_invoer[:-1]  # Verwijdert laatste element van de invoer.
            elif event.unicode in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and len(set_invoer)<2:
                '''Bovenstaand elif-statement checkt of de toets die ingedrukt wordt een cijfer is,
                en of de invoer kleiner dan 2 karakters is. Zo zorgen we dat de invoer altijd bestaat uit maximaal 2 cijfers.'''
                set_invoer += event.unicode

    '''Het onderstaande vraagt de gebruiker zijn/haar eerste, tweede of derde kaartnummer in te voeren.'''
    if len(kaart_keuze) == 0:  # Er waren nog geen kaarten ingevoerd.
        set_opvraag_surface = Arial24.render('Voer het kaartnummer in van de eerste kaart van je gevonden set:', True, wit)
    elif len(kaart_keuze) == 1:  # Er was al één kaart ingevoerd.
        set_opvraag_surface = Arial24.render('Voer het kaartnummer in van de tweede kaart van je gevonden set:', True, wit)
    else:  # Er waren al twee kaarten ingevoerd.
        set_opvraag_surface = Arial24.render('Voer het kaartnummer in van de derde kaart van je gevonden set:', True, wit)
    scherm.blit(set_opvraag_surface, (450, 534))  # Beeldt de tekst af op het scherm.
    
    '''Het onderstaande beeldt de invoer-box af waar de gebruiker de kaartnummers invoert.'''
    set_invoer_surface = Arial24.render(set_invoer, True, wit)  # Maakt een afbeelding van het ingevoerde kaartnummer.
    scherm.blit(set_invoer_surface, (set_invoer_rh.x + 6, set_invoer_rh.y + 2))  # Beeldt het ingevoerde kaartnummer af op het scherm.
    pygame.draw.rect(scherm, wit, set_invoer_rh , 2)  # Tekent een rechthoek om het de invoer-box.
    
    '''Het onderstaande geeft aan welke kaartnummers de gebruiker al eerder ingevoerd heeft, voor op enter te hebben gedrukt.'''
    if len(kaart_keuze) == 0:  # Er waren nog geen kaarten ingevoerd.
        kaart_keuze_string = 'Ingevoerde kaarten: '
    elif len(kaart_keuze) == 1:  # Er was al één kaart ingevoerd.
        kaart_keuze_string = 'Ingevoerde kaarten: ' + kaart_keuze[0]
    elif len(kaart_keuze) == 2:  # Er ware nal twee kaarten ingevoerd.
        kaart_keuze_string = 'Ingevoerde kaarten: ' + kaart_keuze[0] + ', ' + kaart_keuze[1]
    kaart_keuze_surface = Arial24.render(kaart_keuze_string, True, wit)  # Maakt een afbeelding van de tekst
    scherm.blit(kaart_keuze_surface, (450, 605))  # Beeldt de tekst af op het scherm.
    
    '''In het onderstaande checkt de computer of de ingevoerde kaarten door de
    gebruiker een set zijn. Indien dit niet zo is, gebeurt er niets. Indien 
    dit wél zo is, dan wordt de set weggehaald en komen er drie nieuwe kaarten
    uit de pot. Ook wordt de score met 1 verhoogd.'''    
    if len(kaart_keuze) == 3:  # Checkt of er 3 kaarten zijn ingevoerd.
        Kaart1 = Kaart(Kaarten[int(kaart_keuze[0]) -1])  # Maakt een Kaart van de lijst die de eerste kaart voorstelt die de speler ingevoerd heeft.
        Kaart2 = Kaart(Kaarten[int(kaart_keuze[1]) -1])  # Maakt een Kaart van de lijst die de tweede kaart voorstelt die de speler ingevoerd heeft.
        Kaart3 = Kaart(Kaarten[int(kaart_keuze[2]) -1])  # Maakt een Kaart van de lijst die de derde kaart voorstelt die de speler ingevoerd heeft.
        if set.IsSet(Kaart1, Kaart2, Kaart3):
            '''Als de ingevoerde kaarten een set vormen, krijgt de speler een
            punt en worden de drie kaarten vervangen.'''
            score_speler += 1
            for i in range(3):
                if len(Pot) != 0:
                    Kaarten[int(kaart_keuze[i])-1] = Pot.pop()  # De kaarten worden vervangen.
                else:
                    Kaarten[int(kaart_keuze[i])-1] = 0  # Als de pot leeg is, dan kan deze niet aangevuld worden.
            t0 = time.time()  # De tijd wordt gereset.
        kaart_keuze = []  # De ingevoerde kaarten worden gereset.

    '''DE TIJD IS OM'''
    t1 = time.time()  # Slaat de huidige tijd op.
    if t1 - t0 > tijd:
        if len(set.VindSets(Kaarten)) != 0:  # Wanneer er een set op tafel ligt
            score_computer += 1
            GevondenSet = set.VindSets(Kaarten)[0]
            for i in range(3):
                if len(Pot) != 0:
                    Kaarten[int(Kaarten.index(GevondenSet[i]))] = Pot.pop()
                else:
                    Kaarten[int(Kaarten.index(GevondenSet[i]))] = 0
        else:  # Wanneer er geen sets op tafel liggen
            geen_set += 1
            set.vervang_kaarten(Kaarten, Pot)
        t0 = time.time()
    
    '''END CONDITION'''
    if len(set.VindSets(Kaarten)) == 0 and len(Pot) == 0:
        begonnen = False
    
    '''SCORE WEERGEVEN'''
    score_speler_surface = Arial24.render('Score speler: ' + str(score_speler), True, wit)
    score_computer_surface = Arial24.render('Score computer: ' + str(score_computer), True, wit)
    geen_set_surface = Arial24.render('Aantal keer geen set: ' + str(geen_set), True, wit)
    scherm.blit(score_speler_surface, (900, 10))
    scherm.blit(score_computer_surface, (900,42))
    scherm.blit(geen_set_surface, (900,74))
    
    '''POT WEERGEVEN'''
    pot_surface = Arial40.render('Kaarten in pot: ' + str(len(Pot)), True, wit)
    scherm.blit(pot_surface, (450,10))
    
    '''TIMER WEERGEVEN'''
    tijd_surface = Arial40.render('Tijd over: ' + str(round(tijd-(t1-t0), 1)), True, wit)
    scherm.blit(tijd_surface, (450,58))
    
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

'''INVOER OPVRAAG, INVOER BOX, INGEVOERDE KAARTEN RESETTEN'''


while True:
    for event in pygame.event.get():
        '''In deze for-loop wordt voor alle events die pygame registreert,
        gecheckt of het een event is die voor ons van belang is. Zo ja, dan
        doen we er iets mee.'''
        if event.type == pygame.QUIT:  # Het programma wordt afgesloten.
            pygame.quit()
            sys.exit()
    
    '''AFGELOPEN WEERGEVEN'''
    
    scherm.blit(Afgelopen, (500, 400))
    
    pygame.display.update()
