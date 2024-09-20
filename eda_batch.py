import pickle

def unpickle(file: str)-> dict:
    """
    function taken from cifar website to unpickle batches, returns a dictionary
    """
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def dict_batch(batch: dict)-> dict: 
    """
    removes "b" from unpickled batch dictionaries
    """
    return {key.decode(): [item.decode() if isinstance(item, bytes) else item for item in value]for key, value in batch.items()}

def dict_batch_file(file: str)-> dict:
    """
    Converts a batch from file to dictionary
    """
    return dict_batch(unpickle(file))