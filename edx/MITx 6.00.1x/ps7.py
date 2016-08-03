import random
import string
import operator
import time

class AdoptionCenter(object):
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = location
    def get_number_of_species(self, animal):
        if animal in self.species_types:
            return self.species_types[animal]
        else:
            return 0
    def get_location(self):
        return (float(self.location[0]),float(self.location[1]))
    def get_species_count(self):
        return self.species_types.copy()
    def get_name(self):
        return self.name 
    def adopt_pet(self, species):
        if species in self.species_types:
            if self.species_types[species] == 1:
                self.species_types.pop(species)
            else:
                self.species_types[species] -= 1


class Adopter(object):
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        return 1.0*adoption_center.get_number_of_species(self.desired_species)


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species
    
    def get_score(self, adoption_center):
        numother = 0
        for animal in self.considered_species:
            numother += adoption_center.get_number_of_species(animal)
        return adoption_center.get_number_of_species(self.desired_species) + 0.3 * numother

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species
    
    def get_score(self, adoption_center):
        return max(0.0,adoption_center.get_number_of_species(self.desired_species) - 0.3 * adoption_center.get_number_of_species(self.feared_species))



class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic t    o a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
    
    def get_score(self, adoption_center):
        numother = 0
        for animal in self.allergic_species:
            numother += adoption_center.get_number_of_species(animal)
        if numother > 0:
            return 0.0
        else:
            return 1.0*adoption_center.get_number_of_species(self.desired_species)


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species,allergic_species)
        self.medicine_effectiveness = medicine_effectiveness
        
    def get_score(self, adoption_center):
        allergyscore=1.0
        for animal in self.allergic_species:
            if adoption_center.get_number_of_species(animal) > 0:
                if animal in self.medicine_effectiveness:
                    effectiveness = self.medicine_effectiveness[animal]
                else:
                    effectiveness = 0.0
                allergyscore = min(allergyscore, effectiveness)
        return adoption_center.get_number_of_species(self.desired_species)*allergyscore
        

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location

    def get_linear_distance(self, to_location):
        d = ((to_location[0]-self.location[0])**2 + (to_location[1]-self.location[1])**2)**.5
        return d

    def get_score(self, adoption_center):
        distToCenter = self.get_linear_distance(adoption_center.get_location())
        if distToCenter  < 1:
            mood = 1
        elif distToCenter < 3 and distToCenter >= 1:
            mood = .8
        elif distToCenter < 5 and distToCenter >= 3:
            mood = random.uniform(.5,.7)
        else:
            mood = random.uniform(.1,.5)
        return mood*adoption_center.get_number_of_species(self.desired_species)
                
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    allCenters = []
    for center in list_of_adoption_centers:
        currentCenterScore = adopter.get_score(center)
        currentCenterName = center.get_name()
        allCenters.append((center, currentCenterScore, currentCenterName))
    allCenters.sort(key=operator.itemgetter(2), reverse=False)
    allCenters.sort(key=operator.itemgetter(1), reverse=True)
    return [row[0] for row in allCenters] #http://stackoverflow.com/questions/15775956/can-i-use-python-slicing-to-access-one-column-of-a-nested-tuple
    

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    allAdopterScores = []
    for adopter in list_of_adopters:
        allAdopterScores.append((adopter.get_score(adoption_center),adopter.get_name(), adopter))
    allAdopterScores = sorted(allAdopterScores,key= lambda x:(-x[0],x[1]))
    outputList = []
    traverselength = min(n,len(allAdopterScores))
    if traverselength >0:
        for i in range(traverselength):
            outputList.append(allAdopterScores[i][2])
    return outputList
    
        
    

a = random.randint(-3000,3000)
random.seed(a)
print 'random seed is', a

adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": random.random()})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat") 

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": random.randint(20, 50), "Dog": random.randint(1, 10)}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": random.randint(20, 50), "Horse": random.randint(1, 10)}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": random.randint(20, 50), "Lizard": random.randint(1, 10)}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": random.randint(20, 50), "Dog": random.randint(1, 10), "Horse": random.randint(1, 10)}, (-10,10))


adopters = [adopter, adopter2, adopter3, adopter4, adopter5, adopter6]
centers = [ac,ac2,ac3,ac4,ac5,ac6]
for a in adopters:
    testCenterRanking = get_ordered_adoption_center_list(a,centers)
    print "adopter", a.get_name()
    for t in testCenterRanking:
        print t.get_name()
    print("---------------------------")


print("------------------------------------------------------")
for c in centers:
    testAdopterRanking = get_adopters_for_advertisement(c,adopters,5)
    print "center", c.get_name()
    for t in testAdopterRanking:
        print(t.get_name())
    print("---------------------------")        

