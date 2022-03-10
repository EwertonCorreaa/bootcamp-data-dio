import os
import time

with open('hosts.txt') as file: #importa o txt
    dump = file.read() #ler o txt
    dump = dump.splitlines() #organiza a impressão do txt

    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-' * 50)
        os.system(f'ping -n 2+ {ip}')
        print('-' * 50)
        time.sleep(3) #espera em 5s para realizar as ações
