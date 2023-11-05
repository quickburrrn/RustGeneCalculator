import math
import time
import os
from itertools import combinations
import xml.etree.ElementTree as ET


def clear():
    os.system("cls")


# clears the scream because colors wont work if i don't
os.system("cls")


class colors():
    red = "\u001b[31m"
    blue = "\u001b[34m"
    white = "\u001b[37m"
    yellow = "\u001b[33;1m"


def printcolor(message, color):
    # return (color+text+colors.white)
    print(color, message, colors.white)


# gets the xml file
try:
    tree = ET.parse('seeds.xml')
except:
    printcolor("error missing xml file, -an xml file should be in the same file as this script if it isnt make one",
               colors.red)
    print("this is how you structure your xml file for this script:")
    print('<?xml version="1"?>')
    print("<Seeds>")
    print('   <Seed genes = "XGGGGG"/>')
    print('   <Seed genes = "GGGGGG"/>')
    print('   <Seed genes = "XXXXXX"/>')
    print('   ...')
    print("</Seeds>")

root = tree.getroot()


# contains gene letter and value
class Gene:
    def __init__(self, gene):
        self.gene = gene
        self.value = 0.0
        if (self.gene == "W" or self.gene == "X"):
            self.value = 1.0
        elif (self.gene == ""):
            # null gene
            self.value == 0.0
        else:
            self.value = 0.6

    def verify(self):
        if (self.gene == "W" or self.gene == "X"):
            self.value = 1.0
        elif (self.gene == ""):
            # null gene
            self.value == 0.0
        else:
            self.value = 0.6


# contains 6 genes
class seed:
    def __init__(self, a, b, c, d, e, f):
        self.genes = [a, b, c, d, e, f]

    def GetSeedString(self):
        # gets the gene from the genes list
        genes = []
        for i in range(len(self.genes)):
            genes.append(self.genes[i].gene)
        return genes

    def VerifySeed(self):
        for i in range(len(self.genes)):
            self.genes[i].verify()
        return

    def GetValue(self):
        # virifies the seed
        self.VerifySeed()

        # add togheter the gene values
        value = 0.0
        for i in range(len(self.genes)):
            value += self.genes[i].value
        return float(value)

    def GetSingleValue(self, index):
        # returns the value of a single gene
        return self.genes[index].value


class Calculator:
    def __init__(self):
        # takes data from seeds.xml
        self.Seeds = []
        for n in root:
            genestring = str(n.get("genes"))
            self.Seeds.append(seed(Gene(genestring[0]), Gene(genestring[1]), Gene(genestring[2]), Gene(genestring[3]),
                                   Gene(genestring[4]), Gene(genestring[5])))

        printcolor(f"succesfully loaded {len(self.Seeds)} seeds", colors.yellow)
        printcolor(f"estimated calculation time {210*2**(len(self.Seeds)-20)}s!", colors.yellow)


    def DebugSeed(self):
        # need to fix this
        for n in range(len(self.Seeds)):
            print(n+1, self.Seeds[n].GetSeedString())

    # NOT IN USE
    def GetSeeds(self):
        # ask for how many seeds you have

        # disabled for now
        self.SeedCount = int(input("how many seeds shall i add to the equation? "))
        print()

        # prints warning if more than 8 seeds
        if (self.SeedCount > 8):
            printcolor("WARRNING gamebreaking mechanincs detected this might not work in game", colors.yellow)

        print("You can now define the genes of each seed")
        print("type the seed like this:GGGYYY")
        print("you can only use the letters GYHWX")
        print()

        # disabled for now
        for i in range(self.SeedCount):
            print("write the stats for seed", i)
            seed_ = ""
            seed_ = input(": ")
            self.Seeds.append(
                seed(Gene(seed_[0]), Gene(seed_[1]), Gene(seed_[2]), Gene(seed_[3]), Gene(seed_[4]), Gene(seed_[5])));
            print()

        printcolor("success these are your seeds: ", colors.yellow)
        for n in self.SeedCount:
            print(n)

    def GetBestSeed(self, seeds):

        for n in range(len(seeds)):
            seeds[n].VerifySeed();

        bestseed = 0
        bestscore = 2
        for i in seeds:
            if (i.GetValue() < bestscore):
                bestscore = i.GetValue
                bestseed = i

        return seeds[bestseed]

    def CalculateCrossbreed(self, seeds):

        # verfies the seeds
        for n in range(len(seeds)):
            seeds[n].VerifySeed();

        # creates a list of all the genes each list inside the list is going to get calculated creating the result
        Genes = [[] for n in range(6)]
        for i in range(len(seeds)):
            for n in range(6):
                Genes[n].append(seeds[i].genes[n])

        # merge the genes
        MergedGenes = Genes
        for x in range(len(Genes)):
            for y in range(len(Genes[1])):
                for z in range(len(Genes[1])):
                    if Genes[x][y].gene == Genes[x][z].gene:
                        MergedGenes[x][z].value += MergedGenes[x][y].value

        # calculates
        FinalSeed = []
        for x in range(len(MergedGenes)):
            BestGene = Gene("")
            for y in range(len(MergedGenes[1])):
                if MergedGenes[x][y].value > BestGene.value:
                    BestGene = MergedGenes[x][y]
            FinalSeed.append(BestGene)

        # converts the list to seed and returns
        FinalSeed = seed(FinalSeed[0], FinalSeed[1], FinalSeed[2], FinalSeed[3], FinalSeed[4], FinalSeed[5])
        FinalSeed.VerifySeed()
        return FinalSeed

    def Bruteforce(self, seeds):
        # starts the timer
        beginTime = time.time()

        # goes through every possible combination this needs optimization

        # gives the good seeds a starting seed because i need something to compare to
        GoodSeeds = [seed(Gene("X"), Gene("X"), Gene("X"), Gene("X"), Gene("X"), Gene("X"))]
        GoodSeedsCrossbreed = []
        # contains the string of the resepies
        GoodSeedsString = []
        # skips the first combination
        for n in range(1, len(seeds)):

            # this is a loading screen
            print("\r", round(n / len(seeds) * 100), "%     ", round(time.time()-beginTime),"s", end="")

            # goes trough every combinations and finds the best seed
            _combinations = list(combinations(seeds, r=n))
            for i in range(len(_combinations)):

                # the numbers wont work corectly if i don't verify two times
                self.CalculateCrossbreed(list(_combinations[i])).VerifySeed()
                # self.CalculateCrossbreed(list(_combinations[i])).VerifySeed()

                # add a list of the best combinations and seeds
                if (((Seed := self.CalculateCrossbreed(_combinations[i])).GetValue()) <= 3.6):

                    # this is just an example on how to unpack the combinations
                    # for n in range(1, len(_combinations)):
                    #    print()
                    #    for i in range(len(_combinations[1])):
                    #        print(list(_combinations[n])[i].GetSeedString())

                    # checks if there already is a solution to achinve that seed if not then add it to the good seed list

                    Seed.VerifySeed()

                    if (Seed.GetSeedString() not in GoodSeedsString):
                        GoodSeedsString.append(Seed.GetSeedString())
                        GoodSeeds.append(Seed)
                        GoodSeedsCrossbreed.append(list(_combinations[i]))

        # returns the best seed

        print("100%", end="")

        for n in range(1, len(GoodSeeds)):
            print()
            print(GoodSeeds[n].GetSeedString())
            print("to get this seed you have to crossbreed: ")
            for i in range(len(GoodSeedsCrossbreed[n - 1])):
                print(GoodSeedsCrossbreed[n - 1][i].GetSeedString())

        printcolor(f"DONE! in {round(time.time()-beginTime)}s", colors.yellow)
        print(f"found {len(GoodSeeds)} Good Combinations \n")


calculator = Calculator()

while True:
    # ask for command from the user
    print("these are the current commands you can use")
    print("seeds : displays your current seeds")
    print("best : finds your best seed")
    print("crossbreed : crossbreed the seeds you select")
    print("bruteforce : finds the best combinations using pure force this can take som time")
    print("clear : clears the console")

    request = input()

    if (request == "bruteforce"):
        calculator.Bruteforce(calculator.Seeds)
    elif (request == "crossbreed"):
        calculator.DebugSeed()
        print("write what seeds i should add to the equation, write it like this: 3627...")
        request = input()
        try:
            SeedsInCalcultaion = []
            for n in request:
                SeedsInCalcultaion.append(calculator.Seeds[int(n)])
            printcolor(calculator.CalculateCrossbreed(SeedsInCalcultaion).GetSeedString(), colors.blue)
        except:
            printcolor("error wrong input method did you write only numbers with no whitespace?", colors.red)
    elif (request == "best"):
        printcolor(calculator.GetBestSeed(calculator.Seeds).GetSeedString(), colors.blue)
    elif (request == "seeds"):
        calculator.DebugSeed()
    elif (request == "clear"):
        clear()
    else:
        printcolor("error did you mean bruteforce?", colors.red)
