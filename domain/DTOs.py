class ProduseDTO(object):
    def __init__(self, descriere, pret):
        self._descriere = descriere
        self._pret = pret

    def get_pret_DTO(self):
        return self._pret

    def get_desc_DTO(self):
        return self._descriere

    def __str__(self):
        return str(self._descriere) + ": " + str(self._pret) + " de lei"

