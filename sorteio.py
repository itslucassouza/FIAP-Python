voto1 = input("Informe qual premio deseja ganhar: PLAYSTATION, XOBX OU NINTENDO ")
voto2 = input("Informe qual premio deseja ganhar: PLAYSTATION, XOBX OU NINTENDO ")
voto3 = input("Informe qual premio deseja ganhar: PLAYSTATION, XOBX OU NINTENDO ")
voto4 = input("Informe qual premio deseja ganhar: PLAYSTATION, XOBX OU NINTENDO ")
voto5 = input("Informe qual premio deseja ganhar: PLAYSTATION, XOBX OU NINTENDO ")


playstation = 0
xbox = 0 
nintendo = 0

if voto1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto1.upper() == "XBOX":
    xbox = xbox + 1
elif voto1.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O Colaborador 1 digitou um console inexistente e o voto será desconsiderado")

if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O Colaborador 2 digitou um console inexistente e o voto será desconsiderado")

if voto3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto3.upper() == "XBOX":
    xbox = xbox + 1
elif voto3.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O Colaborador 3 digitou um console inexistente e o voto será desconsiderado")

if voto4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto4.upper() == "XBOX":
    xbox = xbox + 1
elif voto4.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O Colaborador 4 digitou um console inexistente e o voto será desconsiderado")

if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O Colaborador 5 digitou um console inexistente e o voto será desconsiderado")

if playstation > xbox and playstation > nintendo:
    print("o console escolhido foi playstation")
elif xbox > playstation and xbox > nintendo:
    print("o console escolhido foi xbox")
elif nintendo > playstation and nintendo > xbox:
    print("o console escolhido foi nintendo")
else: ("houve empate, por favor entrar em contato com a direção")

