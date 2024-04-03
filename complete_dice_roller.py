import random
import re

def roll_dice(roll_command):
    match = re.match(r'^(\d+)d(\d+)([+\-]\d+)?$', roll_command)
    if match:
        quantity = int(match.group(1))
        sides = int(match.group(2))
        modifier = int(match.group(3)) if match.group(3) else 0
        rolls = [random.randint(1, sides) for _ in range(quantity)]
        total = sum(rolls) + modifier
        return rolls, total
    else:
        return None, None

print("---ROLANDO DADOS COMPLETO---")
print("Role dados com: XdY + Z ou XdY - Z")
print("X -> número de dados")
print("Y ->  quantidade de lados dos dados")
print("Z (opcional) -> modificador")
print("Exemplo: 2d6+3")

while True:
    roll_command = input("Digite o comando para rolar dados ou 'sair' para encerrar: ")

    if roll_command.lower() == 'sair':
        break

    rolls, total = roll_dice(roll_command)
    if rolls is not None and total is not None:
        print('Rolagem: {}'.format(rolls))
        print('Total:   {}'.format(total))
    else:
        print("COMANDO INVÁLIDO!")