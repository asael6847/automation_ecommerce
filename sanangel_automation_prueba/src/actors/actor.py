from src.abilities.browse_the_web import BrowseTheWeb

class Actor:
    def __init__(self,name):
        self.name = name
        self.abilities = {}

    def can(self,ability):
        self.abilities[type(ability)] = ability

    def ability_to(self,ability_class):
        return self.abilities[ability_class]