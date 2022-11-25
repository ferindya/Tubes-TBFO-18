from argparse import ArgumentParser
from FA import *
from parserCFG import *
from ConvertCFG import *
from cykparser import *

def printASCII():
    print('''welcome to....
                                                            
                                                                  .--..--..--..--..--..--.
                                                                .' \  (`._   (_)     _   \
                                                            .'    |  '._)         (_)  |
                                                            \ _.')\      .----..---.   /
                                                            |(_.'  |    /    .-\-.  \  |
                                                            \     0|    |   ( O| O) | o|
                                                            |  _  |  .--.____.'._.-.  |
                                                            \ (_) | o         -` .-`  |
                                                                |    \   |`-._ _ _ _ _\ /
                                                                \    |   |  `. |_||_|   |
                                                                | o  |    \_      \     |     -.   .-.
                                                                |.-.  \     `--..-'   O |     `.`-' .'
                                                            _.'  .' |     `-.-'      /-.__   ' .-'
                                                            .' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
                                                            `-._  `.  |________/\_____|    `-.'
                                                            .'   ).| '=' '='\/ '=' |
                                                            `._.`  '---------------'
                                                                    //___\   //___\
                                                                        ||       ||
                                                                LGB      ||_.-.   ||_.-.
                                                                        (_.--__) (_.--__)
                                                        ░▀▀█░█▀▀░░░█▀▀░█▀█░█▄█░█▀█░▀█▀░█░░░█▀▀░█▀▄
                                                        ░░░█░▀▀█░░░█░░░█░█░█░█░█▀▀░░█░░█░░░█▀▀░█▀▄
                                                        ░▀▀░░▀▀▀░░░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀                                      
        ''')
   



if __name__ == "__main__":
    printASCII()
    argument_parser = ArgumentParser()
    argument_parser.add_argument("nama_file", type=str, help="Nama File yang hendak diparse.")

    args = argument_parser.parse_args()

   

    if CYKParser(cfgtocnf(readGrammar("grammar.txt")), createToken(args.nama_file)):
        print("ACCEPTED")
    else:
        print("SYNTAX ERROR")

    