import requests
import os
from tqdm import tqdm

IMAGES_URL = 'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz'
LABELS_URL = 'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz'


def download(url, wpath, decompress_gz=True, delete_uncompressed=True):
    print(f'downloading from {url}')
    print(f'writing to {wpath}')
    response = requests.get(url, stream=True)
    chunk_size = 1024*1024
    os.makedirs(os.path.dirname(wpath), exist_ok=True)
    with open(wpath, 'wb') as f:
        for data in tqdm(response.iter_content(chunk_size)):
            f.write(data)
    if decompress_gz:
        import gzip
        import shutil
        print(f'decompressing {wpath}')
        with gzip.open(wpath, 'rb') as inp:
            with open(wpath[:-3], 'wb') as out:
                shutil.copyfileobj(inp, out)
        if delete_uncompressed:
            os.remove(wpath)


if __name__ == '__main__':
    download(IMAGES_URL, 'data/train-images-idx3-ubyte.gz')
    download(LABELS_URL, 'data/train-labels-idx1-ubyte.gz')
