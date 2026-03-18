from utils import*

mensaje = input("Please type your message\n")

mensaje_invertido = flip(mensaje)

num_a =  count_letters(mensaje, 'a')

mensaje_decodificado = mensaje_invertido + str(num_a)

#Imprimir el resultado

print(f"Your encoded message is: {mensaje_decodificado}")