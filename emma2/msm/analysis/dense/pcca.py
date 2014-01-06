'''
Created on 30.11.2013

@author: jan-hendrikprinz
'''

import pcca_impl
import decomposition

import numpy

def pcca(T, n):
    
    # TODO: Here decomposition.eigenvectors could be used but they are not properly normalized!
    eigenvalues,left_eigenvectors,right_eigenvectors = decomposition.rdl_decomposition(T, n)
    
    right_eigenvectors = numpy.real(right_eigenvectors)
    
    # create initial solution that works using the old method
    
    (c_f, indic, chi, rot_matrix) = pcca_impl.cluster_by_isa(right_eigenvectors, n)
        
    rot_matrix = pcca_impl.opt_soft(right_eigenvectors, rot_matrix, n)
                
    memberships = numpy.dot(right_eigenvectors[:,:], rot_matrix)
    
    return memberships