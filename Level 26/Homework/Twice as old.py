def twice_as_old(do, so):
    if do/2 > so:
        x=do-2*so
        return x
    elif do/2 < so:
        x=2*so-do
        return x
    else:
        return 0
    
    