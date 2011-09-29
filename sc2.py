import math

# La teoría es simple
# De la pantalla de "fin del combate" se toma el rate de recolección de recursos "Recolection rate"
# Y se toma la cantidad de recursos no gastados  "Unspent resources".
# Luego el sistema hace un calculo con una función interna de Battle.net y devuelve un número entre 1 y 100
# Ese es el "Spending Quotient" y determina que tan buen macro tienes en Starcraft 2

# Como guia, el tipico Grandmaster tiene un SQ de 70 a 80
# Idra tiene un SQ de 89
# El tipico oro/platino tiene un SQ de 60 a 70

# ENJOY :D

# @freddier - freddier@gmail.com

yourrate = int(raw_input('Your rate: ').strip())
yourunspent = int(raw_input('Your unspent: ').strip())
print ""
enemyrate = int(raw_input('Enemy\'s rate: ').strip())
enemyunspent = int(raw_input('Enemy\'s unspent: ').strip())

yoursq =  35 * (0.00137 * yourrate - math.log(yourunspent)) + 240
enemysq = 35 * (0.00137 * enemyrate - math.log(enemyunspent)) + 240

print "\nYour SQ: {} ".format(yoursq)
print "Enemy's SQ: {} \n".format(enemysq)

if yoursq > enemysq:
    print "You won at macro!"
else:
    print "You lost at macro :("
