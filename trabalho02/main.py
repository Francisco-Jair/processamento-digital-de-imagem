import cv2
import numpy as np


IMG = "aula18_Pratica02.png"

def eliminar_pontos_pretos(imagem):
    black_pixels = np.where(
    (imagem[:, :, 0] == 0) & 
    (imagem[:, :, 1] == 0) & 
    (imagem[:, :, 2] == 0)
    )
    imagem[black_pixels] = [255, 255, 255]
    cv2.imwrite("imagem_sem_pontos.png", imagem)
    return imagem

def preencher_buracos(imagem):
    imagem_complemento = cv2.bitwise_not(imagem)
    contador, mais_alto = cv2.findContours(imagem_complemento, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    for conta in contador:
        cv2.drawContours(imagem_complemento, [conta], 0, 255, -1)
    imagem_preenchida = cv2.bitwise_not(imagem_complemento)
    cv2.imwrite("imagem_preenchida.png", imagem_preenchida)
    return imagem_preenchida
    

def main():
    imagem_original = cv2.imread(IMG)
    imagem_sem_pontos = eliminar_pontos_pretos(imagem_original)
    imagem_escala_cinza = cv2.cvtColor(imagem_sem_pontos, cv2.COLOR_BGR2GRAY)
    imagem_binaria = cv2.threshold(imagem_escala_cinza, 250, 255, cv2.THRESH_BINARY)[1]  
    preencher_buracos(imagem_binaria)
    cv2.waitKey(0)
    
main()