

import torch

from pytorch_explore.describe import describe

print("차원만지정")
describe(torch.Tensor(2,3))
print("균등분포")
describe(torch.rand(2,3))
print("표준정규분포")
describe(torch.randn(2,3))



