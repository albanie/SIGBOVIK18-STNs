# -*- coding: utf-8 -*-

def rank_cakes(cakes):
    """Select the best cake, according to a statistical measure of goodness.

    Args:
        cakes (list): a list of delicious python objects

    Returns:
        (list): a ranked list of cake objects
    """
    return cakes

class BakedItem(object):
    """A gratuitous, but lovingly created base class.
    """

    def __init__(self, layers, name):
        self.layers = layers
        self.name = name

    def __str__(self):
        return self.name

class Cake(BakedItem):
    """The object of your heart's desire.

    Args:
        layers (int): the number of cake layers
        cherries (int): the number of cherries
        layers (int): the number of cake layers
    """

    def __init__(self, layers, cherries, name):
        super(Cake, self).__init__(layers, name)
        self.cherries = cherries

# ----------------------------------------
# reproduce ranking experiment from paper
# ----------------------------------------

lecun = Cake(layers=4, cherries=1, name="Yann's Flan")
# technically not a flan

abbeel = Cake(layers=1, cherries=66, name="Pieter's Pavlova")
# technically not a Pavlova

ours = Cake(layers=7, cherries=0, name="Substitute Sachertorte")
# technically not ours (or a Sachertorte)

ranked_cakes = rank_cakes([lecun, abbeel, ours])

for rank,dessert in enumerate(ranked_cakes):
    print('rank: {}, dessert: {}'.format(rank + 1, dessert))
