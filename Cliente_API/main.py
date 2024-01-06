import requests
import random
response = requests.get('http://localhost:8000/personajes') #get de la API
data = response.json() #guarlo la respuesta en una variable

lista_personajes = [] #creo una lista con los nombres de los personajes
for i in data:
    lista_personajes.append(i['name'])

#PERSONAJES
class personajes: 
    def __init__(self, nombre, vida, hambre):
        self.nombre = nombre
        self.vida = vida 
        self.hambre = hambre 
        self.habilidad = []
        self.daño = 0
    def comer(self, cantidad):
        self.hambre += cantidad
        if self.hambre > 50:
            self.vida += 20
    def habilidades(self, habilidad):
        self.habilidad.append(habilidad)
        if "pegar" in self.habilidad:
            self.daño = 5
#ENEMIGOS
class enemigos:
    def __init__(self,vida, poder):
        self.nombre =  random.choice(lista_personajes)
        self.estado = ''
        self.vida = vida
        self.poder = poder

    def atacar(self, daño):
        self.daño = daño 
#DECLARACION DE VARIABLES
jugadores = []
nombre = input("introduce el nombre de tu personaje\n")
personaje1 = personajes(nombre, 100, 100)
enemigo_lvl1 = enemigos(10, 5)


#juego
def menu():
    eleccion = input("Elige que deseas hacer:\n->estatus\n->comer\n->explorar\n->batalla\n->salir\n")
    personajes_asesinados = []
    while eleccion != "0":
         #estatus
        if eleccion == "estatus":
            print(f"Tu vida es {personaje1.vida}, tu hambre {personaje1.hambre}, tu poder {personaje1.daño}")
        #comer
        elif eleccion == "comer":
            if personaje1.hambre <= 80:
                personaje1.comer(20)
            else:
                print('No puedes comer, estas lleno')
            print(f"Tu hambre es {personaje1.hambre}")
        #BATALLA, se realiza el PUT que mata al personaje
        elif eleccion == "batalla":
            response = requests.get('http://localhost:8000/personajes') #get de la API con datos actualizados 
            datos = response.json()
            for i in datos:
                if i['name'] == enemigo_lvl1.nombre: #trae el estado del personaje para chequear si se asesino
                    enemigo_lvl1.estado = i['status']
            if enemigo_lvl1.estado == 'muerto': #si el personaje ya ha muerto en ota batalla, que elija otro aleatorio y renueva sus stats
                enemigo_lvl1.nombre = random.choice(lista_personajes)
                enemigo_lvl1.poder = random.choice(range(5, 30))
                print(enemigo_lvl1.poder)
                enemigo_lvl1.vida = 10
            for i in datos:
                if i['name'] == enemigo_lvl1.nombre:
                    link = i['image']
            print(f'Te haz encontrado a {enemigo_lvl1.nombre} {link}. Preparate para pelear')
            if personaje1.daño > 0: 
                while enemigo_lvl1.vida >= 0:
                    personaje1.vida -= enemigo_lvl1.poder 
                    enemigo_lvl1.vida -= personaje1.daño
                    personaje1.hambre -= 10
                if personaje1.vida <= 0:
                    print(f'Lo siento, perdiste {personaje1.nombre}')
                else:
                    print(f"Buena batalla,tu vida quedo en {personaje1.vida}, recuerda comer para recuperar fuerzas")
                    params = {
                        'estado': 'muerto' 
                    }
                    put = requests.put(f'http://localhost:8000/personajes/{enemigo_lvl1.nombre}', params=params)
                    personajes_asesinados.append(enemigo_lvl1.nombre)
            else:
                print("No puedes participar de esta batalla ya que tienes 0 de daño, ve a explorar para conseguir nuevas habilidades")
        elif eleccion == "explorar":
            print("explorando...")
            print("adquiriste una nueva halibidad")
            personaje1.daño += 5  
        elif eleccion == "salir":
            print(f"Gracias por jugar {personaje1.nombre},haz asesinado a {len(personajes_asesinados)}")
            for i in personajes_asesinados:
                print(f'->{i}')
            print('Para salir escribe 0')
        else: 
            print("Elige una opcion valida")
        #Hambre
        if personaje1.vida <= 0:
            print(f'Haz muerto, buena partidad ')
            eleccion = '0'
            print(f"Gracias por jugar, haz asesinado a {len(personajes_asesinados)}")
            for i in personajes_asesinados:
                print(f'->{i}')
        else:
            if personaje1.hambre < 20:
                if personaje1.vida < 10:
                    respuesta = input("¿Estas por morir, deseas comer?")
                    if respuesta == "si":
                        personaje1.hambre += 20
            eleccion = input("Elige que deseas hacer:\n->estatus\n->comer\n->explorar\n->batalla\n->salir\n")
        

if nombre not in jugadores:
    jugadores.append(nombre)
    menu()




