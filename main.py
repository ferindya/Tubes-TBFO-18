from argparse import ArgumentParser
from fileprocesing import *
from  parserCFG import *
from ConvertCFG import *
from cykparser import *

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("nama_file", type=str, help="Nama File yang hendak diparse.")

    args = argument_parser.parse_args()

   

    if CYKParser(cfgtocnf(read_grammar("grammar.txt")), createToken(args.nama_file)):
        print("ACCEPTED")
    else:
        print("SYNTAX ERROR")

    