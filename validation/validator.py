from exceptii.exceptions import ValidatorError


class ValidatorProd(object):
    def valid_produs(self, produs):
        err = ""
        if produs.get_id_prod() < 0:
            err += "id produs invalid!\n"
        if produs.get_desc() == " ":
            err += 'descriere invalida!\n'
        if produs.get_pret() < 0:
            err += 'pret invalid!\n'
        if len(err) > 0:
            raise ValidatorError(err)

