# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 22:05:51 2016

@author: HansG17
"""

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib as mpl
import random



#fitness function gets a given array and determines 
#aim of function is to maximize the fucntion z = x^2 + y^2
def fitness(test):
    #fit = (-1)*((test[0])**2 + (test[1])**2)
    fit = (-1)* (np.linalg.norm(test))**2
    return fit

#mutate randomly changes the values at a random index of an array
def mutate(gene,size):
    new = gene[:]
    position = random.randint(0,len(gene)-1)
    addition = random.randrange(-size,size)
    new[position] = new[position]+addition
    return new
    
    
# does basic mutation and progression
def basicMutation(start):
    i = 0
    while i<50:
        change = mutate(start,2)
        print(fitness(start)),
        print(fitness(change))
        if fitness(start) < fitness(change):
          print("yes")
          print(fitness(start))
          print(fitness(change))

          print("this")
          start = change
        i= i+1
    return start
    
#creates a population that we will use for evolution
# creates a random selection of points 
def population(pop):
    genes = []
    for i in range(0,pop):
        frog = random.sample(range(30),2)
        genes.append(frog)
    return genes
    
#this performs recombination #sex
#a random length of moms dna is inserted into dads dna 
#and a child list (final) with a mix of data from mom and dad is returned 
def sex(mom,dad):
    child_dna = dad[:]
    start = random.randint(0, len(mom))
    end = random.randint(start,len(mom))
    child_dna[start:end] = mom[start:end]
    # add or subtract 2 from some index of child
    mut_rate = 2;
    final = mutate(child_dna,2)
    return final
    
    
#returns a parent from a genepool     
def rand_prod_parent(genepool):
    # multiplicative random distribution favors higher fitness individuals
    pick = len(genepool) - random.random()*random.random() * (len(genepool)-1)
    parent = genepool[int(pick)]
    return parent
    
    



#change_arr contains record of all points that had higher fitness then anyone in gene
#pool
change_arr = []

# final loop iterates through generations of individuals
# and gradually genertes higher fitness individuals
def final_loop(pop):
    #creates a list of fit individuals
    #sorts individuals by fitness and then seleccts parents from list
  
    animals = population(pop)
    animals = sorted(animals,key=fitness)
    i = 0
    #only one set mates at a time
    while i<100:
        #parents are selected using (1 - rand*rand) distribution to favor higher indices
        momy = rand_prod_parent(animals)
        dady = rand_prod_parent(animals)
        child = sex(momy,dady)
        print(child)
        # check to see if the fitness of child is greater then leed male
        change_arr.append(child)
        if fitness(child) > fitness(animals[-1]):
            change_arr.append(child)
             #take out last elemenet ie least fit
            animals.pop(0)
            animals.append(child)
            print(animals)
            
            
        i = i+1
    print(animals[-1])
        #print(fitness(animals[-1]))
        #ax.scatter(animals[-1][0], animals[-1][1],fitness(animals[-1]))


#graphs x^2 + y^2 = Z^2 (surface to be optimized)
#as well as 
def GrphSrf():
    print("scattering")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(azim = 180+160,elev = 0)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
    X = np.arange(-10,10,2)
    Y = np.arange(-10,10,2)
    X, Y = np.meshgrid(X, Y)


    Z = -.5*(X**2+Y**2)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=True)
   # norm = mpl.colors.Normalize(vmin= 0,vmax = len(change_arr))
    for x in range(0,len(change_arr)):
        
        ax.scatter([change_arr[x][0]],[change_arr[x][1]],fitness(change_arr[x]))
        
    #ax.scatter()                      
    plt.show()
    

#for x in range(0,hlen(change_arr)):
    #    print("scattering")

#testing section
#test each function 
#result when population size is 10

final_loop(10)
GrphSrf()