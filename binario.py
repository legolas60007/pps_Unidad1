def esBinario(strBinario):
    try:
        p = set(strBinario)
        Binario = {'0', '1'}
        v = True
        if Binario == p or p == {'0'} or p == {'1'}:
            decimal = int(strBinario, 2)
            return print("Es Binario {}".format(v), "y en decimal es {}".format(decimal))
        else:
            return print(False)
    except TypeError:
        return print(False)
esBinario('gg')