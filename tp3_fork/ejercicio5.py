from os import getpid, fork, getppid
import sys
import getopt

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'n:')
    if len(opt) != 1:
        print("Por favor ingrese bien la cantidad de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f"Ha habido un error: {error}")
    exit()

def show_processes():
    process_child_id = getpid()
    parent_id = getpid()
    print(f'Soy el proceso, {process_child_id}, y mi padre es: {parent_id}')
    exit()

child_number = 0
for (op,ar) in opt:
    if op == '-n':
        child_number = int(ar)
        print(f'Cantidad de procesos hijos: {child_number}\n')

for i in range(child_number):
    create_child = fork()
    if create_child == 0:
        show_processes()


    