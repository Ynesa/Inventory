import math

import logging

logging.basicConfig(filename="13paskaita1.py", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def suma(*args):
    logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
    return sum(args)

def saknis(a):
    try:
        istraukta_saknis = math.sqrt(a)
    except:
        logging.exception("Istraukta saknis")
    else:
        logging.info(f"Skaiciaus {a} saknis lygi {math.sqrt(a)}")
        return istraukta_saknis

def simboliu_kiekis(sakinys):
    logging.info(f"simboliu_kiekis{sakinys} lygu {len(sakinys)}")
    return len(sakinys)

def dalyba(x, 0):
    try:
        padalinti = x/0
    except:
        logging.exception("Dalyba is nulio negalima")
    else:
        logging.info(f"{x} dalinti is {y} lygu {x / y}")
    return padalinti