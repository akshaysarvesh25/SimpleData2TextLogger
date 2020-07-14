import numpy as np
from datetime import datetime
import os


def log2textfile(data,nametxtfile):
    file_open = open(str(str(nametxtfile)),"a")
    file_open.write(str(data))
    file_open.close()


if __name__=="__main__":
    dat = np.random.randint(2, size=10)
    date_ = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    directory = str('log_')+str(date_)
    if not os.path.exists(directory):
        os.makedirs(directory)
    log2textfile(dat,(str(directory)+'/'+('random_.txt')))
