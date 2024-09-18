# Crie um programa que faça uma contagem regressiva de 10 até 0 e exiba "FIM!" ao final.
import time

# Contagem regressiva de 10 a 0
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)  # Espera 1 segundo entre os números


print("FIM!")
