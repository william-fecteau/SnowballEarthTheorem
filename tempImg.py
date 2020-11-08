from PIL import Image
from PIL import ImageColor
import numpy as np

# ICE : 115, 255, 255
# RED : 255, 0, 0

class BuildTempsImage:
    def __init__(self, mat, mini, maxi):
        arrayWidth = mat.shape[0]


        im = Image.new('RGBA', (arrayWidth, arrayWidth))

        for i,j in np.ndindex(mat.shape):
            r = (mat[i,j] - mini) * 255 / (maxi - mini)

            im.putpixel((i,j), (int(r), 50, 200, 255))

        im.save("temperatureImage.png")