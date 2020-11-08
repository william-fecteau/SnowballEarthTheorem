import numpy as np
import math

class Earth:
    SIGMA = 5.670400*10**(-8)
    SOLAR = 1368
    RADIUS = 6_371_000 # meters


    def __init__(self, nbCell, albedoCloud, greenHouse, matTempIni):
        self.nbCell = nbCell # Number of cells in the simulation
        if(nbCell < 0):
            raise Exception("Number of cells must be greater than 0")

        self.albedoCloud = albedoCloud # Albedo cloud constant
        if(albedoCloud < 0 or albedoCloud > 1):
            raise Exception("Cloud albedo must be between 0 and 1")        

        self.greenHouse = greenHouse # Green house constant
        if(greenHouse < 0 or greenHouse > 1):
            raise Exception("Green house must be between 0 and 1")   

        self.matSize = int(math.sqrt(nbCell))
        if(matTempIni.size != nbCell):
            raise Exception("Initial temperature matrix does not fit with the number of cells")
        
        # Adding some randomness to our temperature data
        matRandom = np.random.rand(self.matSize, self.matSize)
        self.matTemp = matRandom + matTempIni


    def iterate(self):
        self.calculateTempVariation()
        print("=======================================Itération=======================================")
        print(self.matTemp)


    def calculateTempVariation(self):
        dTemp = np.zeros((self.matSize, self.matSize))
        for i,j in np.ndindex(self.matTemp.shape):
            albedo = 0.62 if self.matTemp[i,j] <= 263 else 0.3
            
            teta = (math.pi/2 / self.matSize) + math.pi * i / self.matSize  
            inpt = self.SOLAR*abs(math.sin(teta))*(1 - albedo)
            output = 4*(1-self.greenHouse)*self.SIGMA*(self.matTemp[i,j]**4)
            dt = (inpt - output) / (16*(1-self.greenHouse)*self.SIGMA*self.matTemp[i,j]**3)

            dTemp[i,j] = dt

        self.matTemp += dTemp

    def getMatTemp(self):
        return self.matTemp

    def getAvgPerZone(self):
        # May be more optimize with numpy but can't figure out how xd
        avgTempsArray = np.zeros(self.matSize)
        for i in range(self.matSize):
            lineAvgTemp = 0
            for j in range(self.matSize):
                lineAvgTemp += self.matTemp[i,j]

            lineAvgTemp /= self.matSize
            avgTempsArray[i] = lineAvgTemp

        return avgTempsArray