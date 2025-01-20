from .cnn import SimpleCNN
from .unet import UNet
from .random_forest import get_random_forest

def get_model(model_name, **kwargs):
    if model_name == 'cnn':
        return SimpleCNN(**kwargs)
    elif model_name == 'unet':
        return UNet(**kwargs)
    elif model_name == 'random_forest':
        return get_random_forest(**kwargs)
    else:
        raise ValueError(f"Unknown model: {model_name}")