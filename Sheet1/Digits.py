"""
Confirmed with Bernhard that it's cool to share these, enjoy! // Edvard
"""
import itertools

def digits():
    zero = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, 1, 1, 1, 1, -1, -1, -1],
            [-1, -1, 1, 1, 1, 1, 1, 1, -1, -1]] +\
           [[-1, 1, 1, 1, -1, -1, 1, 1, 1, -1] for _ in range(10)] +\
           [[-1, -1, 1, 1, 1, 1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1, 1, 1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

    one = [[-1, -1, -1, 1, 1, 1, 1, -1, -1, -1] for _ in range(16)]

    two = [[1, 1, 1, 1, 1, 1, 1, 1, -1, -1],
           [1, 1, 1, 1, 1, 1, 1, 1, -1, -1]] +\
          [[-1, -1, -1, -1, -1, 1, 1, 1, -1, -1] for _ in range(5)] +\
          [[1, 1, 1, 1, 1, 1, 1, 1, -1, -1],
           [1, 1, 1, 1, 1, 1, 1, 1, -1, -1]] +\
          [[1, 1, 1, -1, -1, -1, -1, -1, -1, -1] for _ in range(5)] +\
          [[1, 1, 1, 1, 1, 1, 1, 1, -1, -1],
           [1, 1, 1, 1, 1, 1, 1, 1, -1, -1]]

    three = [[-1, -1, 1, 1, 1, 1, 1, 1, -1, -1],
             [-1, -1, 1, 1, 1, 1, 1, 1, 1, -1]] +\
            [[-1, -1, -1, -1, -1, -1, 1, 1, 1, -1] for _ in range(5)] +\
            [[-1, -1, -1, -1, 1, 1, 1, 1, -1, -1],
             [-1, -1, -1, -1, 1, 1, 1, 1, -1, -1]] +\
            [[-1, -1, -1, -1, -1, -1, 1, 1, 1, -1] for _ in range(5)] +\
            [[-1, -1, 1, 1, 1, 1, 1, 1, 1, -1],
             [-1, -1, 1, 1, 1, 1, 1, 1, -1, -1]]

    four = [[-1, 1, 1, -1, -1, -1, -1, 1, 1, -1] for _ in range(7)] +\
           [[-1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
            [-1, 1, 1, 1, 1, 1, 1, 1, 1, -1]] +\
           [[-1, -1, -1, -1, -1, -1, -1, 1, 1, -1] for _ in range(7)]

    digits = [zero, one, two, three, four]
    return [list(itertools.chain.from_iterable(digit)) for digit in digits]