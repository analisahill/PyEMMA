
# This file is part of PyEMMA.
#
# Copyright (c) 2015, 2014 Computational Molecular Biology Group, Freie Universitaet Berlin (GER)
#
# PyEMMA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


r"""
===============================================================================
transform - Transformation Utilities (:mod:`pyemma.coordinates.transform`)
===============================================================================
.. currentmodule:: pyemma.coordinates.transform

.. autosummary::
    :toctree: generated/

    PCA - principal components
    TICA - time independent components
    VAMP - Variational approach for Markov processes
    VAMPModel - Kinetic model form the Variational approach for Markov processes
    VAMPChapmanKolmogorovValidator - Chapman Kolmogorov test for the Variational approach for Markov processes
"""

from .pca import *
from .tica import *
from .nystroem_tica import *
from .vamp import *
