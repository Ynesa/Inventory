import math

import logging

logging.basicConfig(filename="13paskaita1.py", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def suma(*args):
    logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
    return sum(args)

def saknis(a):
    logging.info(f"Skaiciaus {a} saknis lygi {math.sqrt(a)}")
    return math.sqrt(a)

def simboliu_kiekis(sakinys):
    logging.info(f"simboliu_kiekis{sakinys} lygu {len(sakinys)}")
    return len(sakinys)

def dalyba(x, y):
    logging.info(f"{x} dalinti is {y} lygu {x / y}")
    return x/y




