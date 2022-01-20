from domain.entitati import Produse
from exceptii.exceptions import FileRepoError
from copy import deepcopy


class FileRepoProduse(object):
    def __init__(self, filePath):
        self.__filePath = filePath
        self.__produse = []

    def read_file(self):
        """
        functie care citeste fiecare linie si parseaza elementele din fisier
        apoi append uieste in lista self.__produse, produsul produs format
        :return:
        """
        self.__produse = []
        with open(self.__filePath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    parts = line.split(",")
                    id_prod = int(parts[0])
                    desc = str(parts[1])
                    pret = float(parts[2])
                    produs = Produse(id_prod, desc, pret)
                    self.__produse.append(produs)

    def append_to_file(self, produs):
        """
        functie care scrie in fisier un produs produs
        :param produs: obiect de tip produs
        :return:
        """
        with open(self.__filePath, 'a') as f:
            f.write(str(produs.get_id_prod()) + ',' + str(produs.get_desc()) + ',' + str(produs.get_pret()) + ',' + '\n')

    def add_produs_to_file(self, produs):
        self.read_file()
        for produse in self.__produse:
            if produse == produs:
                raise FileRepoError("produs existent!\n")
        self.__produse.append(produs)
        self.append_to_file(produs)

    def __len__(self):
        """
        suprascrierea metodei __len__
        :return: lungimea len a listei de produse
        """
        self.read_file()
        return len(self.__produse)

    def get_all_prod(self):
        """
        functie care returneaza toate elementele listei self.__produse
        :return: lista truncata self.__produse
        """
        self.read_file()
        return self.__produse[:]

    def delete_produse_from_file(self, user_input):
        """
        functie care sterge produsele din file daca (,) contin o cifra din user_input
        :param user_input: string
        :return: lista dupa stergere si numarul de stergeri
        """
        self.read_file()
        nr_sterse = 0
        index = 0
        #somelist = [prod for prod in self.__produse if not str(user_input) in str(prod.get_pret())]
        #return somelist
        produse_list = deepcopy(self.__produse)
        for prod in self.__produse:
            if str(user_input) in str(prod.get_pret()):
                nr_sterse += 1
                del self.__produse[index]
            index += 1
        print(index)
        print("Au fost sterse " + str(nr_sterse) + " elemente")
        self.write_to_file()

    def write_to_file(self):
        with open(self.__filePath, 'w') as f:
            for prod in self.__produse:
                f.write(str(prod.get_id_prod()) + ',' + str(prod.get_desc()) + ',' + str(prod.get_pret()) + ',' + '\n')
