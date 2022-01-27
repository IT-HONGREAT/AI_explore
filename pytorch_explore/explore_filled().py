import torch

from pytorch_explore.describe import describe

print('='*20,"zeros",'='*20)
describe(torch.zeros(2,3))

print('='*20,"ones",'='*20)

x = torch.ones(2,3)
describe(x)

print('='*20,"ones",'='*20)
x.fill_(5)
describe(x)

print('='*20,"리스트로 초기화가능",'='*20)
fromlist = torch.Tensor([[1,2,3],
                         [5,5,5]])
describe(fromlist)