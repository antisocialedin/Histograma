import numpy as np
from PIL import Image


def main():
    img_filename = '../Images/enhance-me.gif'
    save_equalizacao = '../Images/equalizacao.jpg'

    # Carrega a Imagem
    image = Image.open(img_filename)

    # Converte para numpy array
    img_array = np.array(image)

    # Passo 1: Histograma cumulativo normalizado

    # Nivela a image array e calcula o histograma por meio de binning
    histogram_array = np.bincount(img_array.flatten(), minlength=256)

    # Normaliza
    num_pixels = np.sum(histogram_array)
    histogram_array = histogram_array / num_pixels

    # Histograma cumulativo normalizado
    chistogram_array = np.cumsum(histogram_array)

    # Passo 2: Tabela de pesquias de mapeamento do pixel
    transform_map = np.floor(255 * chistogram_array).astype(np.uint8)

    # Passo 3: Transformação

    # Achata a image array em uma lista 1D
    img_list = list(img_array.flatten())

    # Transforma os valores dos pixels para equalizar
    eq_img_list = [transform_map[p] for p in img_list]

    # Remodela e escreve de volta em img_array
    eq_img_array = np.reshape(np.asarray(eq_img_list), img_array.shape)

    # Converte o numPy array para imagem Pillow e salva para o arquivo de saída
    eq_img = Image.fromarray(eq_img_array)
    eq_img.save(save_equalizacao)

    # Passo 4: Aplicando o filtro de mediana
    img_equalizada = '../Images/equalizacao.jpg'

    # Carrega a Imagem
    image = Image.open(img_equalizada)

    # Converte para numpy array
    npImage = np.array(image)

    # Filtro da mediana
    m = npImage.shape[0]  # qtd linhas
    n = npImage.shape[1]  # qtd colunas

    for x in range(1, m - 2):
        for y in range(1, n - 2):
            w = npImage[x - 1:x + 2, y - 1:y + 2]
            # print(x, y)
            # print(w)
            # print(np.mean(w).astype(int))
            npImage[x, y] = np.median(w).astype(int)

    # Converte o numPy arrya para Imagem Pillow e salva o arquivo
    image_tratada = Image.fromarray(npImage)
    image_tratada.show()
    image_tratada.save('../Images/Enhance-me-Tratada.jpg')


if __name__ == "__main__":
    main()
