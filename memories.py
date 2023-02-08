import numpy as np
from numpy.linalg import norm
import re

class Memories:
    def __init__(self, vector, logs):
        self.vector = vector
        self.logs = logs

    def get_memories(self, count):
