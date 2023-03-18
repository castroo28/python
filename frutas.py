frutas = {'Plátano':4000, 'Manzana':1200, 'Pera':1500, 'Naranja':2000, 'Fresa':3500, 'Mandarina':2000, 'Tomate':3200, 'Durazno':5000}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")