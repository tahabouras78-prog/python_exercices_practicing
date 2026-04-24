sold_initial = 1000.0
code_pin = 1234
rep = 3
i = 1
while ( i <= rep) :
     code = int (input("saisir le mot de passe :"))
     
     if code != code_pin :
          print("code incorrect")           
     if i == 3 :
          print("carte bloquee")
          break
     i+=1

if code == code_pin :
          while True:
            print("menu principal: ")
            print("1.consulter le solde ")
            print("2.deposer de largent:  ")
            print("3.retirer de largent ")
            print("4.quitter ")
            trait = input("entrer le traitement qui tu veut:  ")
            match trait :
                case "1":
                    print(f"votre solde est : {sold_initial}DH")
                case "2":
                    dep = float(input("entrer le montant a deposer : "))
                    sold_initial += dep 
                    print(f"votre nouveau solde est : {sold_initial}DH")
                case "3":
                    ret = float(input("entrer le montant a retirer : "))
                    if ret > sold_initial:
                        print("solde insuffisant")
                    else:
                        sold_initial -= ret 
                        print(f"votre nouveau solde est : {sold_initial}DH")
                case "4":
                    print("fin du programme au revoir ")
                    break
                case _:
                    print("choix invalid")

              
     





