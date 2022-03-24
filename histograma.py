import cv2
import numpy as np
from matplotlib import pyplot as plt


# Posso copiar a imagem, equlizar ela e fazer um novo histograma e mostrar no relatorio
# Procurar outra imagem


class HistogramaTrabalho():
    
    def __init__(self):
        self.loadImage = None


    def setLoadImagem(self, path):
        """Carrega a imagem a ser tratada"""
        self.loadImage = cv2.imread(path, 0) # O zero faz carregar em preto e branco


    def getLoadImagem(self):
        return self.loadImage


    def mostrarImagemCinza(self):
        pass


    def gerarHistograma(self):
        plt.hist(self.loadImage.ravel(), 256, [0, 265])
        plt.show()


    def equalizarImagem(self):
        cv2.equalizeHist(self.loadImage)
        cv2.imshow("Imagem Equalizada", self.loadImage)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()



if __name__ == "__main__":
    
    hist = HistogramaTrabalho()
    hist.setLoadImagem("img/imagemPizza.jpeg")
    #hist.gerarHistograma()
    hist.equalizarImagem()



