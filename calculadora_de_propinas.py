"""
CALCULADORA DE PROPINAS
Escribir un programa que calcule la propina que se debe dejar en un restaurante.
El script debe solicitar al usuario el monto total de la cuenta y el porcentaje de propina que desea dejar.
Utilizando operadores aritméticos, calcular la cantidad de propina y el total a pagar (incluyendo la propina).
Mostrar el resultado en la pantalla.
"""

monto_total = float(input("Por favor, ingrese su monto total a abonar: $"))
porcentaje_propina = int(input("Por favor, ingrese el porcentaje de porcentaje_propina que desea abonar: %"))

propina_abonada = (monto_total * porcentaje_propina) / 100
total_con_propina = monto_total + propina_abonada

print(f"La propina abonada es de ${propina_abonada:.0f}, por lo que su pago total, con propina incluida, es de ${total_con_propina:.0f}.\n ¡Muchas gracias por su colaboración!")
