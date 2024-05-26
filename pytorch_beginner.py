# -*- coding: utf-8 -*-
"""Untitled46.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QQt6EJkwi6kV8SVFQRewdvDyRFbWdPL8

Set up
"""

import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print(torch.__version__)

!nvidia-smi

"""##Introduction to Tensors

### Creating tensors

Pytorch tensors are created using 'torch.Tensor()' = https://pytorch.org/docs/stable/tensors.html
"""

#scalar
scalar = torch.tensor(7)
scalar

scalar.ndim

# Get tensor back as Python int
scalar.item()

# Vector
vector = torch.tensor([7, 7])
vector

vector.ndim

vector.shape