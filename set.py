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
    
    def __init__(self, kleur=0, figuur=0, opvulling=0, aantal=0):
        if type(kleur)==list:
            self.kleur = kleur[0] #dit 'attatcht' de kleur daadwerkelijk aan het object self.
            self.figuur = kleur[1]
            self.opvulling = kleur[2]
            self.aantal = kleur[3]
        else:
            self.kleur = kleur #dit 'attatcht' de kleur daadwerkelijk aan het object self.
            self.figuur = figuur
            self.opvulling = opvulling
            self.aantal = aantal
    
    def lijst(self):
        return [self.kleur, self.figuur, self.opvulling, self.aantal]
    
    ''' Onderstaande functie kan wat mij betreft verwijderd worden na het programma af is, het heeft namelijk geen functie in het computerprogramma zelf.'''
    
    def __str__(self): #zo kunnen we kaarten printen en dus de eigenschappen chekken.
        # Onderstaand geeft een string van de vorm 'Kleur = 1 = purple', waar 1 en purple eigenlijk hetzelfde zijn.
        stringkleur = 'Kleur = ' + str(self.kleur) + ' = ' + LegendaKleur[self.kleur]
        stringfiguur = '\nFiguur = ' + str(self.figuur) + ' = ' + LegendaFiguur[self.figuur] #\n creëert nieuwe regel
        stringopvulling = '\nOpvulling = ' + str(self.opvulling) + ' = ' + LegendaOpvulling[self.opvulling] #\n creëert nieuwe regel
        stringaantal = '\nAantal = ' + str(self.aantal) + ' = ' + LegendaAantal[self.aantal] #\n creëert nieuwe regel
        
        outputstring = stringkleur + stringfiguur + stringopvulling + stringaantal
    
        return outputstring
    
    def gifnaam(self): # Deze functie creëert de naam van het .gif bestand bijbehorend bij de kaart
        kleur = LegendaKleur[self.kleur]
        figuur = LegendaFiguur[self.figuur]
        opvulling = LegendaOpvulling[self.opvulling]
        aantal = LegendaAantal[self.aantal]
        
        output = kleur + figuur + opvulling + aantal + '.gif'
        
        return output
    
def IsSet(kaart1, kaart2, kaart3): #algoritme dat voor 3 gegeven kaarten controleert of ze een set vormen
    for eigenschap in ['kleur', 'figuur', 'opvulling', 'aantal']: # we gaan alle eigenschappen los bijlangs.
        #We willen nu per eigenschap checken dat ofwel alle kaarten gelijk zijn, ofwel allemaal verschillend       
        #Dit checken we in onderstaand if-statement:
        if getattr(kaart1, eigenschap) == getattr(kaart2, eigenschap): #dit is True als kaart 1 en 2 gelijke eigenschap hebben, maar False als ze andere eigenschap hebben.
            #Als het True is, moet kaart 3 ook gelijke eigenschap hebben als kaart1 (en daarmee ook kaart2).
            if getattr(kaart1, eigenschap) == getattr(kaart3, eigenschap):
                #Als kaart3 ook dezelfde eigenschap heeft, dan levert deze eigenschap geen problemen op en kan het een set zijn, afhankelijk van de andere eigenschappen. We gaan dus door naar de volgende eigenschap
                continue
            else:
                #Als kaart3 verschilt in deze eigenschap, kan het kaartentrio dus geen set zijn. We stoppen met checken en returnen False
                return False
        else:
            #Als 1is2 False is, moet kaart 3 verschillende eigenschap hebben van kaart1 én van kaart2.
            if getattr(kaart1, eigenschap) != getattr(kaart3, eigenschap) and getattr(kaart2, eigenschap) != getattr(kaart3, eigenschap):
                #In dit geval hebben dus alledrie de kaarten een verschillende eigenschap, wat betekent dat we door kunnen met het checken van de volgende eigenschap
                continue
            else:
                #In dit geval heeft kaart3 gelijke eigenschap als kaart1 of kaart2, terwijl kaart1 en kaart2 verschillende eigenschap hebben.
                #Het is dus geen set, en we returnen False.
                return False        
    #Als deze code bereikt wordt, betekent dat dat er geen foute set is aangetroffen. We returnen daarom True
    return True

def VindSets(kaarten): #algoritme dat voor een willekeurig aantal kaarten alle mogelijke sets geeft.
    sets = [] #de gevonden sets
    for i in range(len(kaarten)-1):
        kaart1 = kaarten[i]
        for j in range(i + 1,len(kaarten)-1): #door kaarten met index 0 t/m i niet mee te rekenen, voorkomen we dat er dubbele sets gevonden worden. Ook zorgt dit ervoor dat kaarten geen set met zichzelf vormen.
            kaart2 = kaarten[j]
            for k in range(j + 1,len(kaarten)-1): #door kaarten met index 0 t/m j niet mee te rekenen, voorkomen we dat er dubbele sets gevonden worden.
                kaart3 = kaarten[k]
                if IsSet(Kaart(kaart1),Kaart(kaart2),Kaart(kaart3)): #Als ze een set vormen, voeg ze dan toe aan de lijst met sets.
                    sets.append([kaart1, kaart2, kaart3]) #Voegt de drie kaarten toe aan de lijst met gevonden sets.
    return sets

                    
def PrintVindSets(kaarten):
    if len(VindSets(kaarten)) == 0:
        print('Geen sets gevonden!')
    else:
        print(VindSets(kaarten)[0])

def Pot(): #creëert een lijst met alle mogelijke kaarten
    pot = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    kaart = Kaart(i,j,k,l).lijst() #zorgt ervoor dat de kaart als lijst opgeslagen wordt.
                    pot.append(kaart) #voegt de gevonden kaart toe aan de pot.
    random.shuffle(pot) #Zorgt ervoor dat de pot in een willekeurige volgorde is.
    return pot

def vervang_kaarten(kaarten, pot):      
    if len(VindSets(kaarten)) == 0:
        for i in range(3):
            kaarten[i] = pot.pop()
    return kaarten, pot
