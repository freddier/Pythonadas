import math

yourrate = int(raw_input('Your rate: ').strip())
yourunspent = int(raw_input('Your unspent: ').strip())
print ""
enemyrate = int(raw_input('Enemy\'s rate: ').strip())
enemyunspent = int(raw_input('Enemy\'s unspent: ').strip())

yoursq =  35 * (0.00137 * yourrate - math.log(yourunspent)) + 240
enemysq = 35 * (0.00137 * enemyrate - math.log(enemyunspent)) + 240

print "\nYour SQ: {}".format(yoursq)
print "Enemy's SQ: {}\n".format(enemysq)

if yoursq > enemysq:
    print "You won at macro!"
else:
    print "You lost at macro :("
