import os
import math

# Imprimir el directorio de trabajo actual

cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# Solicitar un entero y calcular log base 2

num = int(input("Enter an integer: "))
log_val = math.log2(num)
print(f"Log base 2 of {num} is: {log_val}")

#Imprimir piso y  techo del valor logarítmico

print(f"Floor: {math.floor(log_val)}")
print(f"ceiling: {math.ceil(log_val)}")