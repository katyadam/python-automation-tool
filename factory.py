import logging

from remover import Remover
from distibutor import Distributor

class Factory:
    
    @staticmethod
    def auto_remove(args: list[str]) -> None:
        if len(args) != 6:
            logging.error("Incorrect number of arguments! Please see the documentation :)")
            return
        
        remover = Remover(args)
        remover.log()
        remover.remove()

    
    @staticmethod
    def auto_distribute(args: list[str]) -> None:
        if len(args) != 4:
            logging.error("Incorrect number of arguments! Please see the documentation :)")
            return
        
        distributor = Distributor(args)
        distributor.log()
        distributor.distribute()

    
    @staticmethod
    def auto_zip(args: list[str]) -> None:
        pass
    
    @staticmethod
    def auto_unzip(args: list[str]) -> None:
        pass