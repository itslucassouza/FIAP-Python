print("Verificador de frequencias cardiacas")
idade = int(input("Por favor, Digite sua idade"))
bpm = int(input("Por favor, informe sua idade"))


if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("frequencia cardiaca adequada")
    else:
        print("frequencia cardiaca inadequada")
elif idade >= 8 and idade <= 17: 
    if bpm >= 80 and bpm <= 100:
        print("frequencia cardiaca adequada")
    else:
        print("frequencia cardiaca inadequada")
elif idade >= 18 and idade < 60: 
    if bpm >= 70 and bpm <= 80:
        print("frequencia cardiaca adequada")
    else:
        print("frequencia cardiaca inadequada")
elif idade >= 60: 
    if bpm >= 50 and bpm <= 60:
        print("frequencia cardiaca adequada")
    else:
        print("frequencia cardiaca inadequada")
else: 
    print("não existem dados para idade indicada")
