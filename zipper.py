import os
import logging
import zipfile


class Zipper:
    def __init__(self, args: list[str], remove_on_zip: bool) -> None:
        self.source: str = args[2]
        self.zip_name: str = args[3]
        self.remove_on_zip: bool = remove_on_zip
        self.log()

    def zip(self) -> None:
        sources = self.source.split(",")
        allowed_sources = []

        for s in sources:
            if os.path.exists(s):
                allowed_sources.append(s)
            else:
                logging.warn(f"Incorrect path to a file/directory {s}")

        with zipfile.ZipFile(self.zip_name + ".zip", "w") as zipf:
            for s in allowed_sources:
                zipf.write(s)
                logging.info(f"Adding {s} into {self.zip_name} zip")
                if self.remove_on_zip:
                    os.remove(s)

    def log(self) -> None:
        logging.info("Zipper create!")
