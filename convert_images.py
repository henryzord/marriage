__description__ = """
    Converte imagens de PNG/JPG para WEBP. Só precisa ser executado quando novas imagens são adicionadas.
"""

import os
import argparse
from PIL import Image
from tqdm import tqdm


def main(path):
    if os.path.isdir(path):
        files = [
            os.path.join(path, x)
            for x in os.listdir(path)
            if x.split('.')[-1].lower() in ('png', 'jpg', 'jpeg')
        ]
    else:
        files = [path]

    for file in tqdm(files, desc='Convertendo imagens'):
        folder = os.path.dirname(file)
        filename = os.path.basename(file).split('.')[0]

        image = Image.open(file)
        image = image.convert('RGBA')
        image.save(os.path.join(folder, f'{filename}.webp'), 'webp', optimize=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__description__
    )

    parser.add_argument(
        '--path', action='store', required=True,
        help='Caminho para um arquivo ou diretório onde as imagens estão armazenadas. Caso seja um arquivo, converte'
             'apenas aquele e armazena a imagem .webp na mesma pasta. Caso seja um diretório, converte todas as imagens'
             'png e jpg em webp e armazena no mesmo diretório.'
    )

    args = parser.parse_args()
    main(path=args.path)
