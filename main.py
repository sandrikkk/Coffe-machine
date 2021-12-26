MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def igredientebi(motxovna): # ამოწმებს მოთხოვნილი იგირედიენტები აღემატება თუ არა  drink['ingredients']
    for item in motxovna:
        if motxovna[item] > resources[item]:
            print("ბოდიშით აპარატშია არ არის საკმარისი ",item, " ყავის მოსამზადებლად !")
            return False
        return True

def coins():

    value = int(input("რამდენი 1 ლარიანი ? :"))* 1.0
    value += int(input("რამდენი 50 თეთრიანი ?:"))* 0.5
    value += int(input("რამდენი 20 თეთრიანი ?:")) * 0.2
    value += int(input("რამდენი 10 თეთრიანი ?:")) * 0.1
    return value

def tanxis_dabruneba(migebuli_tanxa, yavis_girebuleba):
    if migebuli_tanxa >= yavis_girebuleba:
        dabruneba = round(migebuli_tanxa-yavis_girebuleba,2)
        print("თქვენ გეკუთვნით ხურდა :",dabruneba)
        global profit
        profit +=yavis_girebuleba
        return True
    else:
        print('ბოდიშით თქვენ არ გაქვთ საკმაირის თანხა !')
        return False

def yavis_gaketeba(drink_name,igredients):
    for item in igredients:
        resources[item]-= igredients[item]
    print("ინებეთ თქვენი ყავა:",drink_name)

def report():
    print("წყალი: ", resources['water'])
    print("რძე : ", resources['milk'])
    print("ყავა : ", resources['coffee'])
    print("თანხა : ",profit)

def yavis_fasebi():
    print("espress = 1.5")
    print("latte = 2.5")
    print("cappuccino = 3")
machine = True
while machine:
    choice = input("რომელ ყავას მიირთმევთ ? espresso/latte/cappuccino:").lower()
    if choice == 'OFF'.lower():
        machine = False
    elif choice == 'REPORT'.lower():
        print(report())
    elif choice == "FASEBI".lower():
        yavis_fasebi()
    else:
        drink = MENU[choice]
        if igredientebi(drink['ingredients']):
            pay = coins()
        if tanxis_dabruneba(pay,drink['cost']):
            yavis_gaketeba(choice,drink['ingredients'])
