import torch

class ResidualBlock(torch.nn.Module):

    def __init__(self, input_size, output_size):
        super(Block, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, input_size)
        self.fc2 = torch.nn.Linear(input_size, input_size)
        self.fc3 = torch.nn.Linear(input_size, input_size)
        self.batch_norm = torch.nn.BatchNorm1d(input_size)
        self.relu = torch.nn.LeakyReLU()

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.relu(out)
        out = self.fc3(out)
        out = self.relu(out)
        out = out + x
        return out
