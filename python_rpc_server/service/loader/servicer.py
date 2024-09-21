from protoc.loader_pb2_grpc import ImageLoaderServicer, add_ImageLoaderServicer_to_server
from protoc.loader_pb2 import ImageLoaderResponse
import pickle
import numpy as np
import logging
import torch
import torchvision
import torchvision.transforms as transforms


class ImageLoaderServicer(ImageLoaderServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        pass

    def unpickle(self, file):
        with open(file, 'rb') as fo:
            data = pickle.load(fo, encoding='bytes')
        return data

    def load(self, request, context):
        # transform = transforms.Compose(
        #     [transforms.ToTensor(),
        #     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

        # batch_size = 4

        # trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
        #                                         download=True, transform=transform)
        # trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
        #                                         shuffle=True, num_workers=2)

        # testset = torchvision.datasets.CIFAR10(root='./data', train=False,
        #                                     download=True, transform=transform)
        # testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
        #                                         shuffle=False, num_workers=2)

        # classes = ('plane', 'car', 'bird', 'cat',
        #         'deer', 'dog', 'frog', 'horse', 'ship', 'truck')



        data_dir = request.name

        # get the meta_data_dict
        # num_cases_per_batch: 1000
        # label_names: ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
        # num_vis: :3072
        meta_file = data_dir + '/batches.meta'
        meta_data_dict = self.unpickle(meta_file)
        cifar_label_names = meta_data_dict[b'label_names']
        cifar_label_names = np.array(cifar_label_names)

        # training data
        cifar_train_data = None
        cifar_train_filenames = []
        cifar_train_labels = []

        # cifar_train_data_dict
        # 'batch_label': 'training batch 5 of 5'
        # 'data': ndarray
        # 'filenames': list
        # 'labels': list

        for i in range(1, 6):
            cifar_train_data_dict = self.unpickle(
                data_dir + "/data_batch_{}".format(i))
            if i == 1:
                cifar_train_data = cifar_train_data_dict[b'data']
            else:
                cifar_train_data = np.vstack(
                    (cifar_train_data, cifar_train_data_dict[b'data']))
            cifar_train_filenames += cifar_train_data_dict[b'filenames']
            cifar_train_labels += cifar_train_data_dict[b'labels']

        cifar_train_data = cifar_train_data.reshape(
            (len(cifar_train_data), 3, 32, 32))
        cifar_train_data = np.rollaxis(cifar_train_data, 1, 4)
        cifar_train_filenames = np.array(cifar_train_filenames)
        cifar_train_labels = np.array(cifar_train_labels)

        logging.info('load finished')

        return ImageLoaderResponse(isFinished=True)


def add_servicer_to_server(server):
    add_ImageLoaderServicer_to_server(ImageLoaderServicer(), server)
