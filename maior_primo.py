def maior_primo(x):
    i=x
    if (i==2):
        return x
    while (i!=0):
        if (i%2)==0:
            i=i-1
        if (i%3)==0:
            i=i-1
        elif (i%1)==0:
            if (i%1)==0:
                return i
            else:
                i=i-1
