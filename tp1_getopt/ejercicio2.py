import getopt
import sys

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'i:o:')
    if len(opt) != 2:
        print("Por favor ingrese bien la cantidad de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f"Ha habido un error: {error}")
    exit()

for (op,ar) in opt:
    if op == '-i':
        old_file = ar
    elif op == '-o':
        new_file = ar

try:
    file_open = open(old_file, "r")
except FileNotFoundError as error:
    print(f"El archivo {old_file} no existe en el disco, error: {error}")
    exit()

lines = file_open.readlines()
file_open.close()

def write_file():
    file_to_write = open(new_file, "w")
    file_to_write.writelines(lines)
    file_to_write.close()
    print(f"El archivo {new_file}, fue sobreescrito correctamente")

write_file()


