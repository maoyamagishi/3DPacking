import numpy

class Tensor: 
    def Make(MaxSize):
        Maxinstance = numpy.array([0])                           #3次元テンソルの作成

        for i in range(MaxSize[0] -1):                            #1次元
            y = Maxinstance
            y = numpy.append(Maxinstance,0)
            Maxinstance = y

        Maxinstance = numpy.expand_dims(Maxinstance,1)              #2次元に拡張
        x_desk = Maxinstance
        for i in range(MaxSize[1]-1):
            y = Maxinstance
            y = numpy.append(Maxinstance,x_desk,axis=1)
            Maxinstance = y

        Maxinstance = numpy.expand_dims(Maxinstance,2)            #3次元に拡張
        y_desk = Maxinstance
        for i in range(MaxSize[2]-1):  
            y = Maxinstance
            y = numpy.append(Maxinstance,y_desk,axis=2)
            Maxinstance = y
        
        return Maxinstance
