import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix_3x3 = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [matrix_3x3.mean(axis=0).tolist(),matrix_3x3.mean(axis=1).tolist(), matrix_3x3.flatten().mean()],
        'variance': [matrix_3x3.var(axis=0).tolist(), matrix_3x3.var(axis=1).tolist(), matrix_3x3.flatten().var()],
        'standard deviation': [matrix_3x3.std(axis=0).tolist(), matrix_3x3.std(axis=1).tolist(), matrix_3x3.flatten().std()],
        'max': [matrix_3x3.max(axis=0).tolist(), matrix_3x3.max(axis=1).tolist(), matrix_3x3.flatten().max()],
        'min': [matrix_3x3.min(axis=0).tolist(), matrix_3x3.min(axis=1).tolist(), matrix_3x3.flatten().min()],
        'sum': [matrix_3x3.sum(axis=0).tolist(), matrix_3x3.sum(axis=1).tolist(), matrix_3x3.flatten().sum()]
    }

    return calculations