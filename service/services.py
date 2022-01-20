from domain.entitati import Produse
from domain.DTOs import ProduseDTO
from repository.repo import FileRepoProduse
from validation.validator import ValidatorProd


class ServiceProd(object):
    def __init__(self, valid_prod, repo_prod):
        self.__valid_prod = valid_prod
        self.__repo_prod = repo_prod

    def add_produs_service(self, id_prod, desc, pret):
        """
        functie care adauga in service un produs
        :param id_prod: int
        :param desc: string
        :param pret: float
        :return: lista cu produse
        """
        produs = Produse(id_prod, desc, pret)
        self.__valid_prod.valid_produs(produs)
        self.__repo_prod.add_produs_to_file(produs)

    def get_nr_prod(self):
        """
        functie care returneaza numarul de produse din service
        :return: numarul de produse din service
        """
        return len(self.__repo_prod)

    def get_prod(self):
        """
        functie care returneaza toate elementele listei produse
        :return: element din lista produse
        """
        return self.__repo_prod.get_all_prod()

    def delete_prod(self, user_input):
        """
        functie care sterge produsele din file daca (,) contin o cifra din user_input
        :param user_input: string
        :return: lista dupa stergere si numarul de stergeri
        """
        return self.__repo_prod.delete_produse_from_file(user_input)

    def filtrare_prod(self, filtru_text, filtru_numar):
        """
        functie care filtreaza lista de produse si returneaza lista filtrata
        :param filtru_text:
        :param filtru_numar:
        :return:
        """
        produse = self.__repo_prod.get_all_prod()
        prod_dict = {}
        descrieri_produse = []
        ok = 0
        for prod in produse:
            descriere = prod.get_desc()
            descrieri = descriere.split(",")
            for desc in descrieri:
                if desc not in prod_dict:
                    prod_dict[desc] = []
                    prod_dict[desc].append(prod.get_pret())
                elif desc in prod_dict:
                    prod_dict[desc].append(prod.get_pret())
        for items in prod_dict.items():
            descr = items[0]
            pret = items[1]
            for preturi in pret:
                prod_dict_dto = ProduseDTO(descr, preturi)
                descrieri_produse.append(prod_dict_dto)
                if filtru_numar == -1 or filtru_text == "":
                    pass
                elif filtru_text in items[0]:
                    ok += 1
                elif str(filtru_numar) in str(items[1]):
                    ok = 0
        if ok > 0:
            sorted_dto = sorted(descrieri_produse, key=lambda prod: prod.get_pret_DTO(), reverse=True)
            print('filtru_text')
            return sorted_dto
        elif ok < 0:
            sorted_dto_2 = sorted(descrieri_produse, key=lambda prod: prod.get_desc_DTO(), reverse=False)
            print('filtru_numar')
            return sorted_dto_2
        #return descrieri_produse[:]


