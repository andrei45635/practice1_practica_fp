class Produse(object):
    def __init__(self, id_prod, desc, pret):
        self.__id_prod = id_prod
        self.__desc = desc
        self.__pret = pret

    def get_id_prod(self):
        """
        getter pentru id_prod
        :return: id_prod
        """
        return self.__id_prod

    def get_desc(self):
        """
        getter pentru descrierea produsului
        :return: descriere
        """
        return self.__desc

    def get_pret(self):
        """
        getter pentru pret
        :return: pret
        """
        return self.__pret

    def __str__(self):
        """
        suprascrierea metodei __str__
        :return:
        """
        return "[" + str(self.__id_prod) + "]: " + str(self.__desc) + ", pret: " + str(self.__pret)
