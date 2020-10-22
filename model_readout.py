#!/usr/bin/env python
# coding: utf-8



import pickle
import sklearn
from sklearn import datasets




# The training model: Iris experiment -- implicit approach

#modeltrain = open('iris1_training_model100_.txt','rb')
#model = pickle.load(modeltrain)
#model = model.detach().numpy()
#print(model)














# The training model: Explicit experiment -- explicit approach

#modeltrain = open('explicit_training_model100_.txt','rb')
#model = pickle.load(modeltrain)
#model = model.detach().numpy()
#print(model)



# Iris dataset
iris = datasets.load_iris()
X = iris.data[:,1:3]
Y = iris.target

X0 = X[0:50, :]
X1 = X[50:100,:]
X2 = X[100:150,:]

# Training set
X0train = X0[0:10, :]; 
X1train = X1[0:10, :]; 
X2train = X2[0:10, :]; 

# Testing set
X0test  = X0[10:50, :]
X1test = X1[10:50, :]
X2test = X2[10:50,:]



# Circles set
# Training set
traindata = open('explicit_train_data_.txt', 'rb')
Xtrain  = pickle.load(traindata)
X0train = Xtrain[0:15]; 
X1train = Xtrain[15:]


# Testing set
explicitdata = open('explicit_test_data_.txt', 'rb')
X1 = pickle.load(explicitdata)
nsamples1 = 100; ninstance1 = nsamples1/2; ninstance1 = int(ninstance1)
X0test = X1[0:ninstance1]; 
X1test = X1[ninstance1:]











