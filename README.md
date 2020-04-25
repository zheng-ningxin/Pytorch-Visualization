# Pytorch-Visualization
Libs to visuallize the network architecture automaticlly.
The visualization results of example.py is at [here](./example/resnet18.jpg).

Usage:
```
data=torch.rand(10,3,224,224)
pc= Pytorch_Visual(model, data)
pc.visualization('resnet18')
```
