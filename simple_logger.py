import numpy as np

def log2textfile(data,nametxtfile):
    file_open = open(str(str(nametxtfile)),"a")
    file_open.write(str(data))
    file_open.close()


if __name__=="__main__":
    dat = np.random.randint(2, size=10)
    log2textfile(dat,'random_.txt')
