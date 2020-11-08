import numpy as np
import math

class Earth:
    TEMP_INDEX = 0
    ENERGY_INDEX = 1
    ALBEDO_INDEX = 2

    SIGMA = 5.670400*10**(-8)
    STELLAR = 1368
    RADIUS = 6_371_000 # meters


    def __init__(self, nbCell, albedoCloud, greenHouse, tempInit):
        self.nbCell = nbCell # Number of cells in the simulation
        self.albedoCloud = albedoCloud # Albedo cloud constant?
        self.greenHouse = greenHouse # Green house constant?
        self.matSize = int(math.sqrt(nbCell))

        if(tempInit.size != nbCell):
            raise Exception("Initial temperature matrix does not fit with the number of cells")

        self.tempInit = tempInit
        
        # Creation of the cell matrix (3xNxN)
        self.cells = np.zeros((3, self.matSize, self.matSize))
        self.cells[self.TEMP_INDEX, :, :] = tempInit


    def iterate(self):
        print("Itération")

    def calculateEnergyVariation(self):
        aire = 1
        hInSec = 2 * 60 * 60

        albedo = self.cells[self.TEMP_INDEX, :, :]
        dEnergy = np.zeros((self.matSize, self.matSize))

        print(self.STELLAR)
        for i,j in np.ndindex(albedo.shape):
            dE = aire * self.STELLAR * hInSec * (1 - self.albedoCloud) * (1 - albedo[i,j]) * (1 + albedo[i,j] * (1 - self.greenHouse) + (albedo[i,j] * self.greenHouse)**2)
            dEnergy[i,j] = dE