#!/bin/env python 
import torch 
import torch.nn as nn
import torchvision
import torchvision.models as models
from lib.pytorch_visual import Pytorch_Visual
model = models.resnet18()

data=torch.rand(10,3,224,224)
pc= Pytorch_Visual(model, data)
pc.visualization('resnet18')