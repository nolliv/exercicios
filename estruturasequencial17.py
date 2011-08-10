area = int(raw_input('digita ae a area: '))
litros = area/6
latoes = litros/18 # cada latao eh R$80
if litros%18!=0:
    latoes+=1
galoes = litros/3.60 # cada galao eh R$25
if litros%3.60!=0:
	galoes+=1
print'se vc soh comprar latoes vai precisar de ', latoes, 'e gastar R$', latoes*80, ',00'
print'se vc soh comprar galoes vai precisar de ', galoes, 'e gastar R$', galoes*25, ',00'

