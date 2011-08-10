morangos = int(raw_input('coma morangos! '))
macas = int(raw_input('coma macas! '))
if morangos <= 5:
	preco_morangos = morangos * 2.50
else:
	preco_morangos = morangos * 2.20
if macas <= 5:
	preco_macas = macas*1.80
else:
	preco_macas = macas*1.50 	

preco_total = preco_morangos+preco_macas
if (morangos+macas) > 8 or preco_total > 25:
	preco_total  -= preco_total/10

print 'pague R$', preco_total

