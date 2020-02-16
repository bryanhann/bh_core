def padded(_list, n=5, v=''):
    return _list[:] + [v]*n
def getdefault(_list,_index,_default=''):
    try:
        return _list[_index]
    except IndexError:
        return _default

