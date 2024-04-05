import torch.nn as nn
import torch.nn.functional as F

class MultiLayerPerceptronModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, dropout_rate):
        super(MultiLayerPerceptronModel, self).__init__()
        #input pixel of image feed to hidden layer
        self.layer1 = nn.Linear(input_size, hidden_size) 
        self.layer2 = nn.Linear(hidden_size, hidden_size) 
        self.tanh = nn.Tanh()
        self.dropout = nn.Dropout(dropout_rate)
        self.layer3 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.tanh(self.layer1(x))
        x = self.tanh(self.layer2(x))
        x = self.dropout(x)
        x = self.layer3(x)
        return x