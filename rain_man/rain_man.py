import time

import torch
from deuces import Evaluator

from policy_network import PolicyNetwork
from value_network import ValueNetwork


class RainMan(object):

    def __init__(self):

        self.policy_network = PolicyNetwork()
        self.value_network = ValueNetwork()
        self.hand_evaluator = Evaluator()

    def move(self, hand, pot, chips):
        pass
