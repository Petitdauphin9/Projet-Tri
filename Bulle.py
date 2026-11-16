def _remonteBulle(tab : list, k : int) -> bool:
    dejaOrdonne : bool = True
    for i in range(len(tab)- 1):
        if tab[i + 1] < tab[i]:
            temp = tab[i]
            tab[i] = tab[i + 1]
            tab[i + 1] = temp
            dejaOrdonne = False
    return dejaOrdonne

def triBulle()