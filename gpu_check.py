import torch
print(f"PyTorch {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"MPS available:  {torch.backends.mps.is_available()}")
x = torch.tensor([1.0, 2.0, 3.0])
print(f"Test tensor: {x}, sum = {x.sum()}")
