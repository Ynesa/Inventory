import logging
import math
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('13paskaita3.py.log')
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

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

def dalyba(x, y):
    try:
        padalinti = x/y
    except:
        logging.exception("Dalyba is nulio negalima")
    else:
        logging.info(f"{x} dalinti is {y} lygu {x / y}")
    return padalinti


print(suma(5, 8, 2))
print(saknis(4))
print(simboliu_kiekis("suskaiciuokite simboliu kieki"))
print(dalyba(4,0))
