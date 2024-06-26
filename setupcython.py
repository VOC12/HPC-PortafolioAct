from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize("kmeans_cython.pyx"),
    include_dirs=[np.get_include()]  # This line is added to include NumPy headers
)
