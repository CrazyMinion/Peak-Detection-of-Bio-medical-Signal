import numpy as np
def avg(y,group):
    p=[]
    for i in range(len(y)):
        if i<=group:
            start=0
        else:
            start=i-group
        temp=y[start:i+1]
        p.append(sum(temp)/len(temp))
    p=np.array(p)
    return p