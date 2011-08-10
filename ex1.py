#1
def oi():
    return "Alo mundo"
#2
def informaNumero(num):
    a = str(num)
    return "o numero informado foi "+ a
#3
def somaNumeros(a, b):
    return a+b
#4
def media(a, b, c, d):
    return (a+b+c+d)/4
#5
def conversor(metros):
    return metros*100
#6
def circulo(raio):
    return raio*2*3.14
#7
def dobroArea(lado):
    return (lado**2)*2
#8
def calculaSalario(salhora, horas):
    return salhora*horas
#9
def conversorFerenheitCelcius(f):
    c = 5*(f-32)/9
    return c
#10
def conversorCelciusFarenheit(c):
    f = (9*c/5)+32
#11
def aleatorio1(i1, i2, f):
    a = (2*i1)*(i2/2)
    b = (3*i1)+f
    c = f**3
    print a
    print b
    print c
#12
def calculaPesoIdeal(altura):
    peso = 71.7*altura - 58
    return peso
#13
def calculaPoneisMalditos(altura, sexo, peso):
    if sexo == 'homem':
        peso_ideal = (72.7*altura) - 58
    else: 
	peso_ideal = (62.1*altura) - 44.7
    if peso == peso_ideal print "vc eh uma caveira."
    else if peso < peso_ideal print "vc tah sussa"
    else print "vc eh um gordo maldito"
#14
def pescador(peso):
    excesso = 0
    multa = 0
    if peso > 50 :
	excesso = peso - 50
	multa = excesso * 40
#15
def aleatorio2(hora, horasmes):
    bruto = hora*horasmes
    print "+ Salario Bruto : R$ ", bruto
    print "- IR (11%) : R$ ", bruto*0.11
    print "- INSS (8%) : R$ ", bruto*0.08
    print "- Sindicato ( 5%) : R$ ", bruto*0.05
    print "= Salario Liquido : R$ ", bruto - bruto*0.24
#16
def tintas(area):
    litros = area/3
    latas = litros/18
	if litros % 18 != 0:
		latas ++
	preco = latas*80
	print 'numero de latas ', latas, ' facada eh ', preco 
#17

#18

