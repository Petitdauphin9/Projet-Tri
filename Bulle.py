def _remonteBulle(tab : list, k : int) -> bool:
    dejaOrdonne : bool = True
    for i in range(k):
        if tab[i + 1] < tab[i]:
            temp = tab[i]
            tab[i] = tab[i + 1]
            tab[i + 1] = temp
            dejaOrdonne = False
    return dejaOrdonne

def triBulle(tab : list) -> list:
    k = len(tab) - 1
    while k > 0 and not _remonteBulle(tab, k):
        k -= 1
    return tab # si on est arrivé à la fin du tableau, on le retourne trié