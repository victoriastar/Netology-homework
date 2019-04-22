class Animals:
    feed = True
    milk = False
    cut = False
    egg = False
    def __init__(self, species, name, sound, weight):
        self.species = species
        self.name = name
        self.sound = sound
        self.weight = weight
    def feeding(self):
        if self.feed == True:
            return('Животное {} {} нужно кормить'.format(self.species, self.name))
    def milking(self):
        if self.milk == True:
            return('Животное {} {} нужно доить'.format(self.species, self.name))
        else:
            return('Животное {} {} нельзя доить'.format(self.species, self.name))

    def cutting(self):
        if self.cut == True:
            return('Животное {} {} нужно стричь'.format(self.species, self.name))
        else:
            return('Животное {} {} нельзя стричь'.format(self.species, self.name))
    def taking_eggs(self):
        if self.egg == True:
            return('У животного {} {} нужно собирать яйца'.format(self.species, self.name))
        else:
            return('У животного {} {} нельзя собирать яйца'.format(self.species, self.name))


goose_grey = Animals('гусь', 'Серый', 'га-га-га', 3)
goose_grey.egg = True
goose_white = Animals('гусь', 'Белый', 'га-га-га', 2)
goose_white.egg = True
sheep_lamb = Animals('овца', 'Барашек', 'бэээээ', 103)
sheep_lamb.cut = True
sheep_curly = Animals('овца', 'Кудрявый', 'бэээээ', 97)
sheep_curly.cut = True
chicken_coco = Animals('курица', 'Ко-Ко', 'кококо', 1)
chicken_coco.egg = True
chicken_cuca = Animals('курица', 'Кукареку', 'кококо', 2)
chicken_cuca.egg = True
cow = Animals('корова', 'Манька', 'муууууу', 570)
cow.milk = True
goat_horns = Animals('коза', 'Рога', 'мээээээ', 70)
goat_horns.milk = True
goat_hooves = Animals('коза', 'Копыта', 'мээээээ', 89)
goat_hooves.milk = True
duck = Animals('утка', 'Кряква', 'кря-кря', 1)
duck.egg = True

print(sheep_curly.feeding())
print(duck.feeding())
print(chicken_coco.feeding())
print(cow.milking())
print(goat_horns.milking())
print(sheep_lamb.milking())
print(cow.cutting())
print(sheep_curly.cutting())
print(chicken_cuca.taking_eggs())
print(goat_hooves.taking_eggs())

list_animals = [goose_grey, goose_white, sheep_lamb, sheep_curly, chicken_coco, chicken_cuca, cow, goat_horns, goat_hooves, duck]
list_animals.sort(key=lambda x: x.weight)
print('\nСамое тяжелое животное {} {} весит {} килограмм'.format(list_animals[-1].species, list_animals[-1].name, list_animals[-1].weight))

