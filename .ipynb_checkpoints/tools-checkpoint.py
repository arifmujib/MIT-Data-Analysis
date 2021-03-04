import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def add_intercept(X):
  return np.concatenate((np.ones_like(X[:,:1]), X), axis=1)

def gradient_descent(X, Y, step_size, precision):
    w = np.zeros(X.shape[1])
    p=1
    while p> precision:
        w = one_step( X, Y, w, step_size)
        precision = np.abs(gradient( X, Y, w))
    loss = loss(X@w, Y)    
    return w, loss        
                 
                
                 
def one_step(X, Y, w, step_size):
                 return w - step_size* gradient( X, Y, w)
    
    
def gradient(X, Y, w):
    return -2*(Y - X@w)@ X

def loss( Y_hat, Y):
    return (Y-Y_hat)@(Y-Y_hat)

