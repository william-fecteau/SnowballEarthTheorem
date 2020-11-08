import numpy as np
import math

class Earth:
    TEMP_INDEX = 0
    ENERGY_INDEX = 1
    ALBEDO_INDEX = 2

    SIGMA = 5.670400*10**(-8)
    SOLAR = 1368
    RADIUS = 6_371_000 # meters


    def __init__(self, nbCell, albedoCloud, greenHouse, matTempIni):
        self.nbCell = nbCell # Number of cells in the simulation
        self.albedoCloud = albedoCloud # Albedo cloud constant?
        self.greenHouse = greenHouse # Green house constant?
        self.matSize = int(math.sqrt(nbCell))

        if(matTempIni.size != nbCell):
            raise Exception("Initial temperature matrix does not fit with the number of cells")
        
        # Creation of the cell matrix (3xNxN)
        self.cells = np.zeros((3, self.matSize, self.matSize))

        matRandom = np.random.rand(self.matSize, self.matSize)
        self.cells[self.TEMP_INDEX, :, :] = matRandom + matTempIni
        print(self.cells[self.TEMP_INDEX, :, :])


    def iterate(self):
        self.calculateTempVariation()
        print(self.cells[self.TEMP_INDEX, :, :])


    def calculateTempVariation(self):
        albedo = self.cells[self.ALBEDO_INDEX, :, :]
        temp = self.cells[self.TEMP_INDEX, :, :]
        dTemp = np.zeros((self.matSize, self.matSize))

        for i,j in np.ndindex(albedo.shape):
            if temp[i,j] <= 263:
                albedo[i,j] = 0.62
            else:
                albedo[i,j] = 0.3
            
            entree = self.SOLAR*(1 - albedo[i,j])
            output = 4*(1-self.greenHouse)*self.SIGMA*(temp[i,j]**4)
            dt = (entree - output) / (16*(1-self.greenHouse)*self.SIGMA*temp[i,j]**3)

            dTemp[i,j] = dt

        self.cells[self.TEMP_INDEX, :, :] = temp + dTemp





