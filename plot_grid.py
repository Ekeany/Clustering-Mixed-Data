import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
from PIL import Image
import sys



if __name__ == "__main__":

    img_dir = sys.argv[1]
    images = os.listdir(img_dir)

    images = [img_dir+'\\'+image for image in images]

    imgs = [Image.open(image) for image in images]
    

    width=200
    height=130
    rows = 2
    cols = 2
    axes=[]
    fig=plt.figure()

    for a in range(rows*cols):
        
        b = imgs[a]
        axes.append( fig.add_subplot(rows, cols, a+1) )
        plt.imshow(b)
        plt.axis('off')



    fig.tight_layout()

    plt.show()
 
    
    fwidth=200
    height=130
    rows = 1
    cols = 1
    axes=[]

        
    b = imgs[-1]
    axes.append( fig.add_subplot(rows, cols, 1) )
    plt.imshow(b)
    plt.axis('off')


    fig.tight_layout()    
    plt.show()

    