def fake_bin(x):
    y = ''
    for i in x:
        if int(i)>=5:
            i=str(i)
            y += '1'
        else:
            y += '0'
    return y
            