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
        """Retorna a imagem carregada"""
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
    

    def show_hist(self, img):
        h = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.figure()
        plt.title("Histograma")
        plt.xlabel("Intensidade")
        plt.ylabel("Número de Pixels")
        plt.plot(h)
        plt.xlim([0, 256])
        plt.show()


    def transformation_views(self, img):
        plt.imshow(img)
        plt.show()
        self.show_hist(img)


    def log_transformation(self, img):
        num = float(input("Digite o valor a se calculado o log(>0):"))
        c = 255 / (np.log(num))
        log_img = np.array(c * (np.log(img + 1)), dtype=np.uint8)
        self.transformation_views(log_img)


    def inv_transformation(self, img):
        inv_img = 255 - img
        self.transformation_views(inv_img)


    def expo_transformation(self, img):
        expo = float(input("Digite o valor do expoente:"))
        expo_img = np.array(255 * (img / 255) ** expo, dtype="uint8")
        self.transformation_views(expo_img)



if __name__ == "__main__":
    
    hist = HistogramaTrabalho()
    hist.setLoadImagem("img/imagemPizza.jpeg")
    #hist.gerarHistograma()
    hist.equalizarImagem()



