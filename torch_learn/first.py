import torch
print(torch.__version__)
print(torch.cuda.is_available())

x = torch.rand(5, 3)
print(x)

y = torch.zeros(5, 3, dtype=torch.long)
print(y)

x = torch.tensor([5.5, 3])
print(x)

x = x.new_ones(5, 3, dtype=torch.double)
print(x)
x = torch.randn_like(x, dtype=torch.float)
print(x)

print(x.size())
print(x.stride())
