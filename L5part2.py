import datetime
import os
import sys

VEGGIE_INFO = {
    "Tomatoes": (12.00, 0.20),
    "Potatoes": (15.00, 0.10),
    "Carrots": (19.00, 0.10),
    "Celery": (21.00, 0.20),
    "Onions": (25.00, 0.20)
}


TotalEarnedSoFar = 0.0
TotalClientsSoFar = 0
HighestAmount = -1.0
LowestAmount = sys.float_info.max 
stop_flag = False

while not stop_flag:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    ClientFN = input("Enter Full Name ('ENDDAY' to stop): ")
    
    if ClientFN.upper() == "ENDDAY":
        stop_flag = True
        continue

    print("\nMenu: Tomatoes (12), Potatoes (15), Carrots (19), Celery (21), Onions (25)")
    

    V_Names, V_Quantities = [], []
    try:
        for i in range(3):
            V_Names.append(input(f"Veg {i+1} name: ").capitalize())
            V_Quantities.append(float(input(f"Veg {i+1} quantity (Kg): ")))
    except ValueError:
        print("ERROR: Quantity must be number. Skipping transaction.")
        input("Press Enter...")
        continue

    # Assignation des variables obligatoires (Darouri khasshom ykouno)
    V1, V2, V3 = V_Names[0], V_Names[1], V_Names[2]
    V1Q, V2Q, V3Q = V_Quantities[0], V_Quantities[1], V_Quantities[2]
    
    # Récupération des Prix et Taux
    P1, R1 = VEGGIE_INFO.get(V1, (0.0, 0.0))
    P2, R2 = VEGGIE_INFO.get(V2, (0.0, 0.0))
    P3, R3 = VEGGIE_INFO.get(V3, (0.0, 0.0))
    
    # Calcul des Totaux
    TotalBT = (P1*V1Q) + (P2*V2Q) + (P3*V3Q)
    TotalAT = (P1*V1Q*(1+R1)) + (P2*V2Q*(1+R2)) + (P3*V3Q*(1+R3))
    
    # Discount Logic
    names_list = ClientFN.split()
    first_letter = names_list[-1][0].upper() if names_list else 'Z'
    discount_amount = 0.0
    if 'A' <= first_letter <= 'F':
        discount_amount = TotalBT * 0.30
    
    # Total To Be Paid (TotalTBP)
    TotalTBP = TotalAT - discount_amount
    if TotalTBP < 0: TotalTBP = 0

    # Mise à Jour Totals
    TotalClientsSoFar += 1
    TotalEarnedSoFar += TotalTBP

    # Mise à jour HighestAmount et LowestAmount
    if TotalClientsSoFar == 1:
        HighestAmount = TotalTBP
        LowestAmount = TotalTBP
    else:
        if TotalTBP > HighestAmount: HighestAmount = TotalTBP
        if TotalTBP < LowestAmount: LowestAmount = TotalTBP

    AverageAmount = TotalEarnedSoFar / TotalClientsSoFar
    
    # 7. Affichage Minimaliste (Natija bla zwa9)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("--- Bill Summary ---")
    print(f"Client: {ClientFN}")
    print(f"TotalTBP: {TotalTBP:.2f} DH")

    print("\n--- Day Totals ---")
    print(f"TotalEarnedSoFar: {TotalEarnedSoFar:.2f} DH")
    print(f"TotalClientsSoFar: {TotalClientsSoFar}")
    print(f"AverageAmount: {AverageAmount:.2f} DH")
    print(f"HighestAmount: {HighestAmount:.2f} DH")
    print(f"LowestAmount: {LowestAmount:.2f} DH")

    input("\nPress Enter to continue...")

# 8. Final Summary
os.system('cls' if os.name == 'nt' else 'clear')
print("--- BUSINESS DAY ENDED ---")
if TotalClientsSoFar > 0:
    print(f"TotalEarnedSoFar: {TotalEarnedSoFar:.2f} DH")
    print(f"TotalClientsSoFar: {TotalClientsSoFar}")
    AverageAmount = TotalEarnedSoFar / TotalClientsSoFar 
    print(f"AverageAmount: {AverageAmount:.2f} DH")
    print(f"HighestAmount: {HighestAmount:.2f} DH")
    print(f"LowestAmount: {LowestAmount:.2f} DH")
else:
    print("No transactions were processed.")
