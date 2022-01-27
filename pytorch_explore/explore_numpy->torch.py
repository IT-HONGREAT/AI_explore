import torch
import numpy as np
from pytorch_explore.describe import describe

print('='*20,"numpy",'='*20)
npy = np.random.rand(2,3)

print('='*20,"numpy->torch",'='*20)

describe(torch.from_numpy(npy))
