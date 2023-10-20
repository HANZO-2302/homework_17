import os
from collections import namedtuple
import logging


FileInfo = namedtuple('FileInfo', ['name', 'ext', 'is_dir', 'parent'])

logging.basicConfig(filename='file_info.log', level=logging.INFO)


def gather_file_info(dirpath):
    for root, dirs, files in os.walk(dirpath):
        for f in files:
            name, ext = os.path.splitext(f)
            info = FileInfo(name, ext, False, root)
            logging.info(info)

        for d in dirs:
            info = FileInfo(d, None, True, root)
            logging.info(info)


if __name__ == '__main__':
    import sys

    dirpath = sys.argv[1]
    gather_file_info(dirpath)
