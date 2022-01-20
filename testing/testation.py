import unittest
from repository.repo import FileRepoProduse
from domain.entitati import Produse
from service.services import ServiceProd
from validation.validator import ValidatorProd
from exceptii.exceptions import ValidatorError


class Testing(unittest.TestCase):
    def SetUp(self):
        pass

    def test_create_repo_file(self):
        filePath = 'test.txt'
        with open(filePath, 'w') as f:
            f.write("")
        try:
            repo = FileRepoProduse(filePath)
        except Exception as ex:
            print(ex)
            return
        self.assertEqual(len(repo), 0)
        return repo

    def test_create_produs(self):
        id_prod = 25
        desc = 'Aliment'
        pret = 19.99
        produs = Produse(id_prod, desc, pret)
        self.assertEqual(produs.get_id_prod(), id_prod)
        self.assertEqual(produs.get_desc(), desc)
        self.assertLess(abs(produs.get_pret() - pret), 0.000001)

    def test_valid_prod(self):
        valid = ValidatorProd()
        id_prod = 25
        desc = 'Aliment'
        pret = 19.99
        produs = Produse(id_prod, desc, pret)
        self.assertEqual(produs.get_id_prod(), id_prod)
        self.assertEqual(produs.get_desc(), desc)
        self.assertLess(abs(produs.get_pret() - pret), 0.000001)
        valid.valid_produs(produs)
        id_prod_g = -25
        desc_g = " "
        pret_g = -25
        produs_g = Produse(id_prod_g, desc_g, pret_g)
        try:
            valid.valid_produs(produs_g)
        except ValidatorError as ve:
            assert(str(ve) == 'id produs invalid!\ndescriere invalida!\npret invalid!\n')
            #self.assertEqual(ve, 'id invalid!' +'\n'+ 'descriere invalida!'+'\n'+'pret invalid!'+'\n')

    def test_add_produs_to_file(self):
        repo = self.test_create_repo_file()
        id_prod = 25
        desc = 'Aliment'
        pret = 19.99
        produs = Produse(id_prod, desc, pret)
        repo.add_produs_to_file(produs)
        self.assertEqual(len(repo), 1)

    def test_add_produs_to_service(self):
        valid = ValidatorProd()
        repo = self.test_create_repo_file()
        service = ServiceProd(valid, repo)
        id_prod = 25
        desc = 'Aliment'
        pret = 19.99
        service.add_produs_service(id_prod, desc, pret)
        self.assertEqual(service.get_nr_prod(), 1)

    def test_delete_produs(self):
        repo = self.test_create_repo_file()
        id_prod = 25
        desc = 'Aliment'
        pret = 19.99
        produs = Produse(id_prod, desc, pret)
        repo.add_produs_to_file(produs)
        id_prod_2 = 26
        desc_2 = 'Mezel'
        pret_2 = 256.44
        produs_2 = Produse(id_prod_2, desc_2, pret_2)
        repo.add_produs_to_file(produs_2)
        self.assertEqual(len(repo), 2)
        repo.delete_produse_from_file(44)
        self.assertEqual(len(repo), 1)


if __name__ == '__main__':
    unittest.main()

