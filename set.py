'''
Dit bestand bevat alle algoritmen, functies en klassen die nodig zijn voor het functioneren van het spel set.
Denk hierbij bijvoorbeeld aan een algoritme voor het checken of drie kaarten een set vormen.
'''

import random

#In het programma zullen we de eigenschappen van de kaarten aangeven met 0, 1 of 2
#In onderstaande dictionaries staat wat voor betekenis dit getal daadwerkelijk heeft
LegendaKleur = {
0 : 'green',
1 : 'purple',
2 : 'red'}

LegendaFiguur = {
0 : 'diamond',
1 : 'oval',
2 : 'squiggle'}

LegendaOpvulling = {
0 : 'empty',
1 : 'filled',
2 : 'shaded'}

LegendaAantal = {
0 : '1',
1 : '2',
2 : '3'}

class Kaart:
    '''
    De klasse van kaarten in het spel set. 
    Alle kaarten hebben een unieke combinatie van vier eigenschappen: 
        - kleur
        - figuur
        - opvulling
        - aantal.
    '''
    def __init__(self, invoer = [0,0,0,0]):
        '''
        Initialiseert een kaart. Deze functie wordt dus aangeroepen wanneer er
        een nieuwe kaart gegenereerd wordt.
        
        Parameters
        ----------
        invoer : list
            Elk van de elementen van deze lijst representeert een eigenschap
            van de kaart. De standaardwaarde is [0,0,0,0].
        '''
        self.kleur, self.figuur, self.opvulling, self.aantal = invoer  # Hier worden alle eigenschappen daadwerkelijk toegekend aan het object self
    
    def __eq__(self, other):
        '''
        Checkt of twee kaarten gelijk zijn aan elkaar

        Parameters
        ----------
        self : Kaart
        
        other : Kaart

        Returns
        -------
        bool
            True als alle eigenschappen hetzelfde zijn, maar False als er
            minstens één eigenschap niet gelijk is.

        '''
        for eigenschap in ['kleur', 'figuur', 'opvulling', 'aantal']:  # We gaan alle eigenschappen los bijlangs
            if getattr(self, eigenschap) == getattr(other, eigenschap):  # Per eigenschap controleren we of de kaarten overeenkomen wat betreft die eingenschap
                '''
                Simpelweg 'self.eigenschap' werkt hierboven niet, aangezien 'eigenschap' geen attribute is van self.
                Daarom moeten we de functie getattr() gebruiken, deze gebruikt wel de attribute kleur als eigenschap='kleur'
                '''
                continue  # Als de eigenschap overeenkomt, gaan we door met het checken van de volgende eigenschap.
            else:
                return False  # Als de eigenschap niet overeenkomt, zijn de kaarten niet gelijk.
        return True  # Als deze code bereikt wordt, betekent dit dat alle eigenschappen overeenkomen en dus dat de kaarten gelijk zijn.

    def gifnaam(self):
        '''
        Creëert de naam van het gifbestand van de afbeelding die bij een kaart
        hoort. Zo wordt '[0,0,0,0]' 'greendiamondempty1.gif'.

        Returns
        -------
        gifnaam : string
            De naam van het .gif bestand dat bij een kaart hoort.

        '''
        kleur = LegendaKleur[self.kleur]
        figuur = LegendaFiguur[self.figuur]
        opvulling = LegendaOpvulling[self.opvulling]
        aantal = LegendaAantal[self.aantal]
        
        gifnaam = kleur + figuur + opvulling + aantal + '.gif'
        
        return gifnaam
    
    def Pad(self):
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
        Pad = 'kaarten\\' + self.gifnaam()  # Hier is een dubbele backslash nodig, omdat een enkele backslash op een andere manier geïnterpreteerd wordt door python.
        return Pad

def IsSet(kaart1, kaart2, kaart3):
    '''
    Deze functie controleert of drie gegeven kaarten samen een set vormen.

    Parameters
    ----------
    kaart1 : Kaart
        Dit is de eerste van de drie kaarten.
    kaart2 : Kaart
        Dit is de tweede van de drie kaarten.
    kaart3 : Kaart
        Dit is de derde en laatste kaart.

    Returns
    -------
    bool
        Als de drie kaarten een set vormen, dan is deze bool True. Zo niet,
        dan is de bool False.

    '''
    if kaart1 == kaart2 == kaart3:
        return False  # Een kaart kan natuurlijk geen set vormen met zichzelf
    else:
        for eigenschap in ['kleur', 'figuur', 'opvulling', 'aantal']: # we gaan alle eigenschappen los bijlangs.
            #We willen nu per eigenschap checken dat ofwel alle kaarten gelijk zijn, ofwel allemaal verschillend
            if getattr(kaart1, eigenschap) == getattr(kaart2, eigenschap): #dit is True als kaart 1 en 2 gelijke eigenschap hebben, maar False als ze andere eigenschap hebben.
                #Als het True is, moet kaart 3 ook gelijke eigenschap hebben als kaart1 (en daarmee ook kaart2).
                if getattr(kaart1, eigenschap) == getattr(kaart3, eigenschap):
                    #Als kaart3 ook dezelfde eigenschap heeft, dan levert deze eigenschap geen problemen op en kan het een set zijn, afhankelijk van de andere eigenschappen. We gaan dus door naar de volgende eigenschap
                    continue
                else:
                    #Als kaart3 verschilt in deze eigenschap, kan het kaartentrio dus geen set zijn. We stoppen met checken en returnen False
                    return False
            else:
                #Als kaart1 en kaart2 verschillen, moet ook kaart 3 verschillende eigenschap hebben van kaart1 én van kaart2.
                if getattr(kaart1, eigenschap) != getattr(kaart3, eigenschap) and getattr(kaart2, eigenschap) != getattr(kaart3, eigenschap):
                    #In dit geval hebben dus alledrie de kaarten een verschillende eigenschap, wat betekent dat we door kunnen met het checken van de volgende eigenschap
                    continue
                else:
                    #In dit geval heeft kaart3 gelijke eigenschap als kaart1 of kaart2, terwijl kaart1 en kaart2 verschillende eigenschap hebben.
                    #Het is dus geen set, en we returnen False.
                    return False        
        #Als deze code bereikt wordt, betekent dat dat er geen fout is aangetroffen. We returnen daarom True.
        return True

def VindSets(kaarten):
    '''
    Voor een gegeven verzameling kaarten, geeft deze functie alle mogelijke
    sets die gemaakt kunnen worden. Dit doen we door alle mogelijke
    combinaties van 3 kaarten bijlangs te gaan en dan met de functie IsSet te
    kijken of ze een set vormen.

    Parameters
    ----------
    kaarten : list
        Deze lijst bevat, zoals de naam suggereert, kaarten (waar elke kaart
        als een lijst met 4 variabelen weergeven wordt). In de praktijk zullen
        dit altijd de 12 kaarten zijn die op tafel liggen.

    Returns
    -------
    sets : list
        Deze lijst bevat alle mogelijke sets die gemaakt kan worden met de
        gespecificeerde kaarten. Hier is een set weergeven als een lijst met
        daarin weer drie lijsten die ieder een kaart voorstellen.

    '''
    sets = []
    for i in range(len(kaarten)):
        if kaarten[i] == 0:
            continue  # Als kaarten[i]==0, dan ligt er op de i-de plek eigenlijk geen kaart. We slaan deze daarom over.
        else:
            kaart1 = kaarten[i]  # kaart1 is de eerste van de drie kaarten die we op een set controleren. 
            for j in range(i + 1,len(kaarten)): #door kaarten met index 0 t/m i niet mee te rekenen, voorkomen we dat er dubbele sets gevonden worden. Ook zorgt dit ervoor dat kaarten geen set met zichzelf vormen.
                if kaarten[j] == 0:  # Als kaarten[j]==0, dan ligt er op de j-de plek eigenlijk geen kaart. We slaan deze daarom over.
                    continue
                else:
                    kaart2 = kaarten[j]
                    for k in range(j + 1,len(kaarten)): #door kaarten met index 0 t/m j niet mee te rekenen, voorkomen we dat er dubbele sets gevonden worden.
                        if kaarten[k] == 0:  # Als kaarten[k]==0, dan ligt er op de k-de plek eigenlijk geen kaart. We slaan deze daarom over.
                            continue
                        else:
                            kaart3 = kaarten[k]
                            if IsSet(Kaart(kaart1),Kaart(kaart2),Kaart(kaart3)):
                                sets.append([kaart1, kaart2, kaart3]) # Als de drie kaarten een set vormen, worden ze toegevoegd aan de lijst met gevonden sets.
    return sets

def Pot():
    '''
    Creëert een lijst die de pot voor moet stellen.
    
    Returns
    -------
    pot : list
        Dit is de pot, de stapel (in ons geval lijst) met alle nog ongebruikte
        kaarten.

    '''
    pot = []
    for i in range(3):  # Hier staat elk van de 4 for-loops voor één van de eigenschappen van een kaart. Alle mogelijke combinaties van eigenschappen worden zo bijlangs gegaan.
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    pot.append([i,j,k,l])  # Voegt de gevonden kaart toe aan de pot, maar dit is nog op een systematische volgorde.
    random.shuffle(pot)  # Zorgt ervoor dat de pot in een willekeurige volgorde is.
    return pot

def vervang_kaarten(kaarten, pot):
    '''
    Haalt drie kaarten van tafel, en vervangt deze voor kaarten uit de pot.
    
    Parameters
    ----------
    kaarten : list
        Dit is de lijst met alle kaarten die op tafel liggen.
    pot : list
        Dit is de lijst met alle nog ongebruikte kaarten, de pot.

    Returns
    -------
    kaarten : list
        De lijst met alle kaarten op tafel,
        na het evt. vervangen van de eerste 3 kaarten.
    pot : list
        De lijst met alle kaarten in de pot na het vervangen van de eerste 3 kaarten.
    
    '''
    for i in range(3):
        kaarten[i] = pot.pop()  # Vervang 3 kaarten voor een kaart uit de pot.
    return kaarten, pot
