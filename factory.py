from remover import Remover

class Factory:
    
    @staticmethod
    def auto_remove(args: list[str]):
        remover = Remover(args)
        remover.log()
        remover.remove()

    
    @staticmethod
    def auto_distribute(args: list[str]):
        pass
    
    @staticmethod
    def auto_zip(args: list[str]):
        pass
    
    @staticmethod
    def auto_unzip(args: list[str]):
        pass