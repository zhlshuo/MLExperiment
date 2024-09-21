from protoc.trainer_pb2_grpc import ModelTrainerServicer, add_ModelTrainerServicer_to_server
from protoc.trainer_pb2 import ModelTrainerResponse
import logging
from python_rpc_server.ml.models.cnn import Net
import torch.optim as optim
import torch.nn as nn
import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def imshow(img):
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

class ImageLoaderServicer(ModelTrainerServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        pass

    def train(self, request, context):
        code = request.code
        exec(code)

        transform = transforms.Compose(
            [transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

        batch_size = 4

        trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                                download=True, transform=transform)
        trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                                shuffle=True, num_workers=2)

        testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                            download=True, transform=transform)
        testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                                shuffle=False, num_workers=2)

        classes = ('plane', 'car', 'bird', 'cat',
                'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

        net = Net()
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

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
                if i % 2000 == 1999:    # print every 2000 mini-batches
                    print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
                    yield ModelTrainerResponse(log=f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
                    running_loss = 0.0
                    
        PATH = './cifar_net.pth'
        torch.save(net.state_dict(), PATH)
        dataiter = iter(testloader)
        images, labels = next(dataiter)

        # imshow(torchvision.utils.make_grid(images))
        print('GroundTruth: ', ' '.join(f'{classes[labels[j]]:5s}' for j in range(4)))
        yield ModelTrainerResponse(log='GroundTruth: ' + ' '.join(f'{classes[labels[j]]:5s}' for j in range(4)))

        net = Net()
        net.load_state_dict(torch.load(PATH))

        outputs = net(images)
        _, predicted = torch.max(outputs, 1)

        print('Predicted: ', ' '.join(f'{classes[predicted[j]]:5s}' for j in range(4)))
        yield ModelTrainerResponse(log='Predicted: ' + ' '.join(f'{classes[predicted[j]]:5s}' for j in range(4)))

        logging.info('Model training finished')


def add_servicer_to_server(server):
    add_ModelTrainerServicer_to_server(ImageLoaderServicer(), server)