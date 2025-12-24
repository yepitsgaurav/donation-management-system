import json
coll = 0
dic = {}
expenses = {}
col = 0
x = 0
from  colorama import Fore,Back,Style
def save_data(dic, expenses, col, coll, x):
    data = {
        "donors": dic,
        "expenses": expenses,
        "total_collection": col,
        "collection_left": coll,
        "total_expense": x
    }
    with open("donation_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print(Fore.GREEN + "💾 Data saved successfully to donation_data.json" + Fore.RESET)

while True:
    print(Back.LIGHTYELLOW_EX,Fore.LIGHTBLUE_EX,Style.BRIGHT+'Total collection  -->', col,'      ',Style.RESET_ALL)
    print(Back.LIGHTYELLOW_EX,Fore.LIGHTBLUE_EX,Style.BRIGHT+'Total collection left is -->', coll,Style.RESET_ALL)
    try:
        ch = int(input(Fore.GREEN + "1 = Add donor\n2 = donor list \n3 = Search donor\n4 = expenses\n5 = save all data \n6 = exit \n-----> "))
    except ValueError:
        print(Fore.RED + "❌ Invalid choice. Try again")
        continue
    if ch == 1:

        while True:
            doner_name = input('Add donor name or [exit]   --> ').strip().lower()
            if doner_name == 'exit':
                break
            elif not  all(part.isalpha() for part in doner_name.split()):
                print('enter in words')
                continue
            elif not doner_name :
                print('❌ enter name not only spaces')
            elif doner_name not in dic:
                    while True:
                        try :
                            amount = int(input("Enter donation amount:--> ₹"))

                        except ValueError :
                            print(Fore.RED,"print values in numbers.'eg,(1,2,100) ",Fore.RESET)
                            continue
                        dic[doner_name] = amount
                        coll += amount
                        col += amount
                        print(Fore.GREEN + Back.BLACK + f" ✅ Added {doner_name.title()} with donation {amount}",Back.RESET)
                        break
            else:
                print(Fore.GREEN + Back.BLACK +'Name already exists',Back.RESET)
    elif ch == 2:
        print(Fore.LIGHTYELLOW_EX+'<' +"----- Donor List -----".center(45,'-')+'>'+Fore.RESET)
        sorted_dict = dict(sorted(dic.items()))
        for name, amt in sorted_dict.items():
            print(f"{name.title().ljust(25, '-')}> :{str(amt).rjust(10)}")
        print(f"{'Total Collection:'.ljust(25, '-')}> :{str(col).rjust(10)}")
        print(Fore.LIGHTYELLOW_EX+'<' +"---------X-----------".center(45,'-')+'>'+Fore.RESET)
        while True :
            delete = input('enter the name to '+Fore.RED + 'DELETE FROM THE LIST'+Fore.RESET+ ' or (exit) --> ').strip().lower()
            if delete == 'exit':
                break
            elif delete in dic :
                deleted_amount = dic.pop(delete)
                col -= deleted_amount
                coll -= deleted_amount

                print(Fore.RED + delete.title(),'has been deleted from the program'+Fore.RESET)
            elif not delete :
                break
            else:
                print('name not in list')
    elif ch == 3:
        if not dic:
            print(Fore.LIGHTRED_EX + "⚠️ NO NAME IS ADDED" + Fore.RESET)
        else:
            while True:
                search = input( "Enter donor name to search or [Exit]--> ").strip().lower()
                if search == 'exit' or  not search :
                    break
                found = False
                for name, amt in dic.items():
                    if name.startswith(search):
                        highlight = name.replace(search,Fore.BLUE+search+Fore.RESET,1)
                        print( highlight,'donated', amt)
                        found = True
                if not found:
                    print(Fore.LIGHTRED_EX + ' 🔍❌ Donor not found' + Fore.RESET)
    elif ch == 4:
        try:
            chh = int(input('1 add expense\n2 see expense\n----------> '))
        except ValueError:
            print(Fore.RED + "Enter a valid option" + Fore.RESET)
            continue

        if chh == 1:
            while True:
                try:
                    expense_reason = input('enter the reasons for expense --> ').strip().lower()
                    if expense_reason == '':
                        print("enter some reason")
                        continue
                except ValueError:
                    print('enter right value')
                    continue

                if expense_reason == 'exit':
                    print('exiting')
                    break
                try:
                    expense_amount = int(input('enter the amount --> '))
                except ValueError:
                    print(r'enter in numbers only like (123)')
                    continue
                if expense_amount <= coll:
                    x += expense_amount
                    coll = coll - expense_amount
                    expenses[expense_reason] = expense_amount

                    print(Fore.GREEN, Back.BLACK,
                          expense_amount, 'for', expense_reason, 'is added',
                          Fore.RESET, Back.RESET)
                else:
                    print(Fore.RED + '❌not enough funds❌' + Fore.RESET)
                    continue

        elif chh == 2:
            print(Fore.LIGHTYELLOW_EX, 'EXPENSE'.center(30, '-')+Fore.RESET)

            for name, item in expenses.items():
                print(f"{name}".ljust(20, '-'), f": {item}".rjust(10))

            print('Total collection  -->', col)
            print('total expense is --> ', x)
            print('Total collection left is -->', coll)
            print(Fore.LIGHTYELLOW_EX + '<------------------>' + Fore.RESET)

        else:
            print(Fore.RED + 'invalid option' + Fore.RESET)

    elif ch == 5:
        save_data(dic, expenses, col, coll, x)
    elif ch == 6:
        print('exiting -- :-)')
    else :
        print(Fore.RED+'invalid input'+Fore.RESET)