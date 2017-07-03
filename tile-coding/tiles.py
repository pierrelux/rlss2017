import os
import ctypes
import numpy as np
from numpy.ctypeslib import as_ctypes

lib = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), './libtilecoding.so'))

lib.GetTiles.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int,
                        ctypes.c_int, ctypes.POINTER(ctypes.c_float),
                        ctypes.c_int]
lib.GetTiles.restype = ctypes.c_void_p

class TileCoding:
    def __init__(self, ntiling, memory_size=1e6):
        self.ntiling = ntiling
        self.memory_size = int(1e6)
        self.tiles = np.empty((ntiling,), dtype=np.int32)

    def __call__(self, values):
        lib.GetTiles(as_ctypes(self.tiles), self.ntiling, self.memory_size, as_ctypes(values.astype(np.float32)), values.size)
        return self.tiles

if __name__ == "__main__":
    features = TileCoding(32)
    values = np.array([2.8, 2.9], dtype='float32')
    phi = features(values)
    print(phi)
    print(phi.shape)
