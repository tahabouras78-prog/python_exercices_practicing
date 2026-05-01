import datetime

def main():
    print("--- Welcome to the Vegetable Shop ---")
    ClientFN = input("Please enter your Full Name: ")
    print("\nAvailable Vegetables & Prices (DH/Kg):")
    print("- Tomatoes: 12 DH")
    print("- Potatoes: 15 DH")
    print("- Carrots:  19 DH")
    print("- Celery:   21 DH")
    print("- Onions:   25 DH")
    print("-" * 40)
    
    V1 = input("Enter vegetable 1 name: ").capitalize()
    V1Q = float(input("Enter quantity (Kg): "))

    V2 = input("Enter vegetable 2 name: ").capitalize()
    V2Q = float(input("Enter quantity (Kg): "))

    V3 = input("Enter vegetable 3 name: ").capitalize()
    V3Q = float(input("Enter quantity (Kg): "))

    def get_info(veg_name):
        
        if veg_name == "Tomatoes": return 12.0, 0.20
        elif veg_name == "Potatoes": return 15.0, 0.10
        elif veg_name == "Carrots":  return 19.0, 0.10
        elif veg_name == "Celery":   return 21.0, 0.20
        elif veg_name == "Onions":   return 25.0, 0.20
        else: return 0.0, 0.0 

    P1, Rate1 = get_info(V1)
    P2, Rate2 = get_info(V2)
    P3, Rate3 = get_info(V3)
    
    Line1_Total = P1 * V1Q
    Line2_Total = P2 * V2Q
    Line3_Total = P3 * V3Q

    TotalBT = Line1_Total + Line2_Total + Line3_Total

    TotalAT = (Line1_Total * (1 + Rate1)) + \
              (Line2_Total * (1 + Rate2)) + \
              (Line3_Total * (1 + Rate3))

    
    names_list = ClientFN.split()
    if names_list:
        family_name = names_list[-1] 
        first_letter = family_name[0].upper() 
    else:
        first_letter = 'Z' 

    discount_amount = 0.0
    
    if 'A' <= first_letter <= 'F':

        discount_amount = TotalBT * 0.30
    
    TotalTBP = TotalAT - discount_amount
    if TotalTBP < 0: TotalTBP = 0

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    print("\n" + "="*40)
    print(f"{'OFFICIAL BILL':^40}")
    print("="*40)
    print(f"Date:   {current_date}")
    print(f"Client: {ClientFN}")
    print("-" * 40)
    print(f"{'Product':<10} | {'Qty':<5} | {'Price':<5} | {'Line Total'}")
    print(f"{V1:<10} | {V1Q:<5.2f} | {P1:<5.2f} | {Line1_Total:.2f}")
    print(f"{V2:<10} | {V2Q:<5.2f} | {P2:<5.2f} | {Line2_Total:.2f}")
    print(f"{V3:<10} | {V3Q:<5.2f} | {P3:<5.2f} | {Line3_Total:.2f}")
    print("-" * 40)
    print(f"Total Before Taxes (TotalBT): {TotalBT:.2f} DH")
    print(f"Total After VAT (TotalAT)   : {TotalAT:.2f} DH")
    
    if discount_amount > 0:
        print(f"Good Client Discount (30%)  : -{discount_amount:.2f} DH")
    
    print("-" * 40)
    print(f"TOTAL TO BE PAID (TotalTBP) : {TotalTBP:.2f} DH")
    print("="*40)

if __name__ == "__main__":
    main()