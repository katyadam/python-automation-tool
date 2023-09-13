import logging

from remover import Remover
from distibutor import Distributor
from zipper import Zipper

class Factory:
    
    @staticmethod
    def auto_remove(args: list[str]) -> None:
        if len(args) != 6:
            logging.error("Incorrect number of arguments! Please see the documentation :)")
            return
        
        remover = Remover(args)
        remover.remove()

    
    @staticmethod
    def auto_distribute(args: list[str]) -> None:
        if len(args) != 4:
            logging.error("Incorrect number of arguments! Please see the documentation :)")
            return
        
        distributor = Distributor(args)
        distributor.distribute()

    
    @staticmethod
    def auto_zip(args: list[str]) -> None:
        if len(args) != 4:
            logging.error("Incorrect number of arguments! Please see the documentation :)")
            return
        remove_on_zip_input = input("Would you like also to remove files that will be zipped?\nPlease type Y or N.\n")

        zipper = Zipper(args, remove_on_zip_input == "Y")
        zipper.zip()

    @staticmethod
    def auto_unzip(args: list[str]) -> None:
        pass