import os

print('███████████████████████████████████████████████████████████████████████████████████████████████')
print('█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░█')
print('█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀░░█')
print('█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░▄▀░░░░█')
print('█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███')
print('█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███')
print('█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███')
print('█░░░░░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███')
print('█████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░███')
print('█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░░░▄▀▄▀▄▀░░░░█░░░░▄▀░░░░█')
print('█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░███░░░░▄▀░░░░███░░▄▀▄▀▄▀░░█')
print('█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██████████░░░░░░█████░░░░░░█████░░░░░░░░░░█')
print('███████████████████████████████████████████████████████████████████████████████████████████████')

# Pedimos al usuario la IP a escanear
ip = input("Introduce la IP a escanear: ")

# Ejecutamos el comando nmap con las opciones indicadas y la IP introducida por el usuario
os.system(f"nmap -p- --open -sS --min-rate 5000 -vvv -n -Pn {ip} -oG allPorts")
