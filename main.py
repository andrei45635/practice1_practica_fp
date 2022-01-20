from validation.validator import ValidatorProd
from repository.repo import FileRepoProduse
from service.services import ServiceProd
from testing.testation import Testing
from presentation.console import Console

if __name__ == '__main__':
    valid_prod = ValidatorProd()

    repo_prod = FileRepoProduse('produse.txt')

    service_prod = ServiceProd(valid_prod, repo_prod)

    teste = Testing()
    #teste.run_all_tests()

    console = Console(service_prod)
    console.run()
