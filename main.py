import sys
import logging

from factory import Factory

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def run() -> None:
    if sys.argv[1] == "-r":
        Factory.auto_remove(sys.argv)

    elif sys.argv[1] == "-d":
        Factory.auto_distribute(sys.argv)

    elif sys.argv[1] == "-z":
        Factory.auto_zip(sys.argv)

    elif sys.argv[1] == "-u":
        Factory.auto_unzip(sys.argv)

    else:
        logging.warn("""
                        Invalid option, please select from:\n
                        -r: remove files
                        -d: distribute files
                        -z: zip files
                        -u: unzip files
                      """)
    logging.info("Quitting program...")


if __name__ == "__main__":
    run()
