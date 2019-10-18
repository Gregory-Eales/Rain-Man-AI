import time

import torch
import numpy
import tqdm

from residual_block import ResidualBlock


class PolicyNetwork(torch.nn.Module):

    def __init__(self, input_size, output_size):

        super(self, RainMainNet).__init__()

        self.rb1 = ResidualBlock(input_size, output_size)
        self.rb2 = ResidualBlock(input_size, output_size)
        self.rb3 = ResidualBlock(input_size, output_size)


    def forward(self, x):
        pass
