from sys import argv,exit
print '[+]...:::Bem Vindo a Cifra de Cesar:::...'
print '[+]...:::By Rei_Gelado <3 POG      :::...'
if len(argv) == 1: #so os fortes entenderam...
	print '[+]Erro!!!\n[+]Voce nao digitou nenhum comando...\n[+]Exemplos de comandos....\n[+]cesar.py palavra_a_ser_cifrada\n[+]cesar.py 2 palavra_a_ser_descifrada'
	exit()
elif argv[1] == '2':
	if len(argv) == 2:
		print '[+]Voce esqueceu da palavra...'
		exit()
	else:
		palavra = argv[2]
		lista4 = []
		lista5 = []
		for rei in palavra:
			lista4.append(ord(rei) - 3)
		for gelado in lista4:
			lista5.append(chr(gelado))
		print '[+]Sua chave descifrada e %s' % ''.join(lista5)
		exit()
else:
	palavra = argv[1]
lista = []
lista2 = []
for t in palavra: 
	lista.append(ord(t) + 3)
for y in lista:
	lista2.append(chr(y))
print '[+]Sua chave cifrada e %s' % ''.join(lista2)
exit()