class Console(object):
    def __init__(self, srv_prod):
        self.__srv_prod = srv_prod

    def __print_produse(self):
        produse = self.__srv_prod.get_prod()
        if len(produse) == 0:
            print("Nu exista produse!")
        else:
            for _prod in produse:
                print(_prod)

    def __add_produse_file(self):
        try:
            id_prod = int(input("Introduceti ID-ul produsului: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        desc = input("Introduceti descrierea produsului: ")
        try:
            pret = float(input("Introduceti pretul produsului: "))
        except ValueError:
            print("valoare numerica invalida!")
            return
        self.__srv_prod.add_produs_service(id_prod, desc, pret)
        print("Produs adaugat cu succes!")

    def __delete_produse_ui(self):
        try:
            user_input = int(input("Introduceti ce vreti sa stergeti: "))
        except ValueError:
            print("GRESIT FRAIERE!")
            return
        self.__srv_prod.delete_prod(user_input)

    def __filtru_prod(self):
        filtru_text = input("Introduceti string ul: ")
        filtru_numar = float(input("Introduceti numarul: "))
        prods = self.__srv_prod.filtrare_prod(filtru_text, filtru_numar)
        for prod in prods:
            print(prod)

    def __filtru_to_file(self):
        filtru_text = input("Introduceti string ul: ")
        filtru_numar = float(input("Introduceti numarul: "))
        prods = self.__srv_prod.filtrare_prod(filtru_text, filtru_numar)
        with open('output.txt', 'w') as f:
            for prod in prods:
                f.write(str(prod))
                f.write('\n')
        print('output.txt')

    def __add_random_products(self):
        try:
            user_input = int(input("Adaugati numarul de intrari: "))
        except ValueError:
            print("valoare gresita boule")
            return
        self.__srv_prod.create_products_randomly(user_input)

    def run(self):
        while True:
            cmd = input(">>>")
            if cmd == "print_produse":
                self.__print_produse()
            elif cmd == "add_produs":
                self.__add_produse_file()
            elif cmd == "delete_prod":
                self.__delete_produse_ui()
            elif cmd == "filt":
                self.__filtru_prod()
            elif cmd == 'filtext':
                self.__filtru_to_file()
            elif cmd == "random":
                self.__add_random_products()
            elif cmd == "exit":
                return
            elif cmd == " ":
                continue
