# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import torch
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim
import torch.nn as nn
from sklearn.model_selection import train_test_split
import numpy as np
import yaml


def train(net):
    for epoch in range(2):  # loop over the dataset multiple times

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 2000 == 1999:  # print every 2000 mini-batches
                print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
                running_loss = 0.0

    print('Finished Training')

def save_model(net):
    PATH = './cifar_net.pth'
    torch.save(net.state_dict(), PATH)

def test(net):
    correct = 0
    total = 0
    # since we're not training, we don't need to calculate the gradients for our outputs
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            # calculate outputs by running images through the network
            outputs = net(images)
            # the class with the highest energy is what we choose as prediction
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f'Accuracy of the network on the 10000 test images: {100 * correct // total} %')


if __name__ == '__main__':
    with open("config.yaml", "r") as yamlfile:
        cfg = yaml.load(yamlfile, Loader=yaml.FullLoader)

    transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    batch_size = cfg['batch_size']
    dataroot = cfg['dataroot']
    



    # trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
    #                                           shuffle=True, num_workers=2)
    #
    # testset = torchvision.datasets.CIFAR10(root='./data', train=False,
    #                                        download=True, transform=transform)
    # testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
    #                                          shuffle=False, num_workers=2)
    # criterion = nn.CrossEntropyLoss()
    # optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)



