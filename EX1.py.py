#ex 1
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize 

tau = 0.25
mu1 = 0.5
sigma1 = 0.2
mu2 = 1.5
sigma2 = 0.7
n = 100000

x_1 = np.random.normal(mu1, sigma1, int(tau*n))
x_2 = np.random.normal(mu2, sigma2, int((1-tau)*n))
data = np.r_[x_1, x_2]
print(data)

def add(params, x):
    gama, a1, sigma1, a2, sigma2 = params
    return -np.sum(np.log(gama*(1/(np.sqrt(2*np.pi*sigma1**2))*np.exp(-((a1-x)**2)/2*sigma1**2))+
                          (1-gama)*(1/(np.sqrt(2*np.pi*sigma2**2))*np.exp(-((a2-x)**2)/2*sigma2**2))))
t = 0.5
mu1 = np.mean(data)-np.std(data)
mu2 = np.mean(data)+np.std(data)
sigma1=np.std(data)
sigma2=np.std(data)                   
x0 = [t, mu1, sigma1, mu2, sigma2]
temp = scipy.optimize.minimize(add, x0, args=data)
print(temp)
