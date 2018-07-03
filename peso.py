import sys
print(""" ---------------------
          |                    |
          |~~~~~~~~~~~~~~~~~~~~|
          |~~~~~~~~~~~~~~~~~~~~|
          |                    |
          |                    |
          |                     |
          |       ÁGUA          |
          |                     |
          |                     |
          |                     |
          |                     |
          |                    |
          |                    |
          |--------------------|
                               """)
print("""
A = Calcular 
B = HELP
c = Exit """)
op = input("escolhe uma opção >_: ")
if op == "A":
    while True:#enquanto op IGUAL a A, o trecho abaixo repete
        Nome = input("Nome >_:")
        Peso = float(input("Peso >_"))
        cal = (35*Peso)/1000
        print("{} você deve beber {} ml de água por dia ".format(Nome,cal))
        continue
       

elif op == "B":
    print(""" TABELA DE MEDIDA DO COPO
Peso        Medida
50 a 55  kg 150ml
55 a 65  kg 200ml
65 a 75  kg 250ml
75 a 100 kg 300ml
90 a 100 kg 305ml
acima    kg  400mL """)
elif op == "C":
    sys.exit()
else:
    print("")
