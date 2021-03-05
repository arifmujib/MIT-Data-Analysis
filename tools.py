import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def add_intercept(X):
  return np.concatenate((np.ones_like(X[:,:1]), X), axis=1)

def gradient_descent(X, Y, step_size, precision):
    w = np.zeros(X.shape[1])
    p = 1
    while p > precision:
        
        w = one_step( X, Y, w, step_size)
        
        precision = np.linalg.norm(gradient( X, Y, w))
        #print('New W: ', w)
    l = loss(X@w, Y)    
    return w, l     
                 
                
                 
def one_step(X, Y, w, step_size):
    #print('w shape: ',w.shape)
    ans = w - step_size* gradient( X, Y, w)
    #print('w shape: ',ans.shape)
    return ans
    
    
def gradient(X, Y, w):
    """print('X shape: ',X.shape)
    print('Y shape: ',Y.shape)
    print('w shape: ',w.shape)"""
    ans = -2.*(Y - X@w)@ X
    #print(ans.shape)
    return ans

def loss( Y_hat, Y):
    return (Y-Y_hat)@(Y-Y_hat)

