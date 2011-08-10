litros = 0
tipo = ''


litros = int(raw_input('digita ae quantos litros: '))
tipo = raw_input('digita ae qual o tipo de combustivel, alcool , gasolina ou inseticida: ')
if tipo == 'alcool':
	preco = 1.90*litros	
	if litros <= 20:
		preco -= preco*0.03
	else:
		preco -=preco*0.05	
elif tipo == 'gasolina':
	preco = 2.50*litros
	if litros <= 20:
		preco -= preco*0.04
	else:
		preco -= preco*0.06
else:
	preco = 0	
	print 'inseticida so eh combustivel se vc tem o carro do double dragon'	
print 'vc vai pagar R$ %2.2d'%preco


