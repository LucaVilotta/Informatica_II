def cad_mas_larga(cadenas):
    n = -1
    for cad in cadenas:
        if len(cad)>n:
            n = len(cad)
            cad_buscada = cad
    return cad_buscada

