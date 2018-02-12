from Car import Car
from Track import Track
import numpy as np

class Optimization:
    '''
    Current parameters:
    6x8 layer1
    1x8 thresh1
    8x2 layer2
    1x2 thresh2

    Total genome length:
    72
    '''
    def __init__(self, pop_size, gene_length, mutation, crossover, selection):
        self.pop_size = pop_size
        self.gene_length = gene_length
        self.mutation_rate = mutation
        self.crossover_rate = crossover
        self.selection_rate = selection
        
        self.population = [[np.random.rand()*2 - 1 for _ in range(gene_length)]
                for __ in range(pop_size)]
        self.fitness = [0 for _ in range(pop_size)]

    def generation(self):
        pass

    def mutate(self, idx):
        pass


    #Crossover of a section of the genome
    def crossover(self, idx1, idx2):
        start = np.random.randint(self.gene_length)
        stop = np.random.randint(self.gene_length)
        section1 = self.population[idx1][start:stop]
        section2 = self.population[idx2][start:stop]
        for i in range(start, stop):
            self.population[idx1][i] = section2[i-start]
            self.population[idx2][i] = section1[i-start]


