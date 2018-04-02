# -*- coding: utf-8 -*-
"""Confectionary Comparator module

The module contains the functionailty required to reproduce the confectionary
comparison experiment, reported in the paper:

    Samuel Albanie, James Thewlis, Joao F. Henriques, Substitute Teacher
	Networks: Learning with Almost No Supervision,	arXiv:1803.11560

----------------------------------------------------------------------
Licensed under The SIG License [see LICENSE.md for details]
Copyright (C) 2018 Samuel Albanie, James Thewlis and Joao F. Henriques
----------------------------------------------------------------------
"""

def rank_cakes(cakes):
    """Rank the cakes, according to a meaningful statistical measure
	of cake goodness.

    Args:
        cakes (list): a list of delicious python objects

    Returns:
        (list): a ranked list of cake objects and their well-judged scores
    """
    scores = [0] * len(cakes)
    for idx,cake in enumerate(cakes):
        scores[idx] += 1 * cake.layers # more layers is better
        scores[idx] += 0 * cake.cherries # no cherry picking
    return sorted(zip(cakes, scores), key=lambda x: x[1], reverse=True)

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

for rank, judged_dessert in enumerate(ranked_cakes):
    dessert, total = judged_dessert # note: we do not count calories
    print('rank: {}, dessert: {}'.format(rank + 1, dessert))

# victory is sweet
