area = int(raw_input('digita ae a area: '))
litros = area/3
latas = litros/18
if litros%18!=0:
	latas +=1
print 'vc vai precisar de ', latas, ' lata e vai levar uma facada de R$', latas*80, ',00 pra compra-las'
