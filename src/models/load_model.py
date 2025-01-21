import torch

def load_pretrained(model, path, device='cpu'):
    checkpoint = torch.load(path, map_location=device)
    model.load_state_dict(checkpoint)
    model.to(device)
    model.eval()
    return model