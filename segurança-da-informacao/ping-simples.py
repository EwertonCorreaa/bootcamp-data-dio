import os
print('#'*50)
ip_host = input('Digite o ip ou host a ser verificado: ')

os.system(f'ping -n 6 {ip_host}')
print('-'*50)


