# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:35:44 2022

@author: admin
"""

import numpy as np
from scipy.stats import multivariate_normal
import matplotlib as mpl
import matplotlib.pyplot as plt 


q = np.array([x, y, Vx, Vy])
N = 1000 #количество элементов матрицы q
t = np.array([t1, t2, 1-t1-t2])
M_1 = np.array([Mx1, My1, MVx1, MVy1])
M_2 = np.array([Mx2, My2, MVx2, MVy2])
M_3 = np.array([0, 0, 0, 0])
E_1 = E_2 = [[(Qx)**2, 0, 0, 0], [0, (Qy)**2, 0, 0], [0, 0,(QVx)**2, 0], [0, 0, 0, (QVy)**2]]
E_3= [[0, 0, 0, 0], [0, 0, 0, 0], [ 0, 0, (Q0)**2, 0], [ 0, 0, 0, (Q0)**2]]

def T1(params, q):
    params = t, M1, E
     return (t*N(q; M1; E)/(np.sum(t*N(q; M1; E)))
             
def T2(params, q):
    params = t, M1, E
     return (t*N(q; M2; E)/(np.sum(t*N(q; M2; E)))

def sigmaX22(params, q):
    params = t, M1, M2, T1, T2, E
    return (np.sum((T1*((q[1][1]-M1[1][1])**2+((q[1][2]-M1[1][2])**2))+
                   T2((q[1][1]-M2[1][1])**2+((q[1][2]-M2[1][2])**2)))/(2*np.sum(T1 + T2))))

def sigmaV22(params, q):
    params = t, M1, M2, T1, T2, E
    return (np.sum((T1*((q[1][3]-M1[1][3])**2+((q[1][4]-M1[1][4])**2))+
                   T2((q[1][3]-M2[1][3])**2+((q[1][4]-M2[1][4])**2)))/(2*np.sum(T1 + T2))))
            
def MM1(T1, q):
    return (np.sum(T1 * q) / (np.sum(T1)))

def MM2(T2, q):
    return (np.sum(T2 * q) / (np.sum(T2)))
            
            
            
            
            
            
            
            
            
            
            
            