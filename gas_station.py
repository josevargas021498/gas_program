import sys
import time
import gas_core1



typing_speed = 12
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()


    
slow_type('\n⛽ WELCOME TO >>>VARGAS\'S<<< GAS STATION! ⛽\n\n PRESS "ENTER" 🔥🔥🔥!')


def print_menu():
    menu = {'regular': 1.89, 'midgrade': 1.99, 'premium': 2.09}
    print(menu)

def gallons(dollars, gas_type):
    if gas_type == 'regular':
        gallons = float(dollars) * 1.89
        return gallons
    elif gas_type == 'midgrade':
        gallons = float(dollars) * 1.99
        return gallons
    elif gas_type == 'premium':
        gallons = float(dollars) * 2.09
        return gallons
    else:
        print('\n\nInvalid Input...\n\n')
        time.sleep(.8)

def total(gallons, gas_type):
    if gas_type == 'regular':
        total = 1.89 * float(gallons)
        return total
    elif gas_type == 'midgrade':
        total = 1.99 * float(gallons)
        return total
    elif gas_type == 'premium':
        total = 2.09 * float(gallons)
        return total
    else:
        print('\n\nInvalid Input...\n\n')
        time.sleep(.8)

pay_option = slow_type('\n\n💲💲 Please Enter Payment Option From The Two We Provide.\n\n"💲>>prepay<<💲" Or "💲>>pay after<<💲": ')
if pay_option == 'prepay':

    slow_type('\n\n➡ Please Take A Look At What We Have Here To Offer...\n\nPRESS "ENTER"...\n\n')
    

    print_menu()
    time.sleep(.4)
    
    gas_type = slow_type('\n\nPlease Enter Type Of Gas Desired: ')



    dollars = slow_type('\n💲💲 Please Enter Cash Desired For Gas: $')

    

    print('\n\n\n✔ Processing... ✔\n\n\n')
    time.sleep(.4)

    print('You Have Chosen To Pump', gas_type, 'for ' + '$' + dollars, 'dollars.\n\n')
    time.sleep(2)
    print('\n\n\nProcessing...😊')
    time.sleep(.9)
    slow_type('\n\n\n\n\n\nPRESS "ENTER" TO START!')
    print('\n\n\n\n⛽ Pumping... ⛽')
    time.sleep(3)
    print('\nDONE!⛽')
    time.sleep(.5)
    slow_type('\n\nPRESS "ENTER" TO SEE RESULTS\n\n')
    
    print('\n\n\n😊Thank You For Your Business..💲💲 \n\nYou Have Successfully Pumped:', gallons(dollars, gas_type), 'gallons!✔✔ \n\n')
    time.sleep(1.2)

elif pay_option == 'pay after':
    slow_type('\n\nPlease Take A Look At What We Have Here To Offer. ↙\n\nPRESS "ENTER".\n')

    print_menu()
    time.sleep(.5)

    gas_type = slow_type('\n\nPlease Enter Type Of Gas Desired: ')
    
    gallons = slow_type('\n\n♺Please Enter Gallons Desired To Pump ♺ : ')

    print('\n\nYou Have Chosen To Pump', gas_type, 'for', gallons, 'gallons.')
    time.sleep(2)

    input('\n\nPRESS "ENTER" TO START!')

    print('\n\n\n✔ Pumping... ⛽\n\n\n')
    time.sleep(2)
    print('\n\n✔✔✔DONE!✔✔✔\n')
    time.sleep(.5)
    slow_type('\n\nPRESS "ENTER" TO SEE RESULTS\n\n')


    print('\n\n\nThank Your Purchase! Your Total Is t: $', total(gallons, gas_type), 'dollars! \n\n')
    time.sleep(.2)


slow_type('\n\n\n\n\n\n😊💲💲Please come again!!😊😊\n\nPRESS "ENTER" TO EXIT!')