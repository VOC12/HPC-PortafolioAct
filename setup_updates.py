from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize([
        "update_lattice_cython1.pyx",
        "update_lattice_cython2.pyx",
        "update_lattice_cython3.pyx",
        "update_lattice_cython4.pyx"
    ])
)
