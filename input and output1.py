# The project provides guidance for ticket printing in KCB bank
# He or she is headed to teller agents for assistance

ticket =int(input('Hello , welcome to KCB bank.enter ticket number'))
if ticket>= 1 and ticket<=5:
   print('Proceed to counter number 2,Agency banking')
elif ticket>=6 and ticket<=10:
   print('Proceed to counter number 3, Bulk withdrawal') 
elif ticket>=11 and ticket<=15:
    print('Proceed to counter number 4,Account opening') 
elif ticket>=16 and ticket<=20:
    print('Proceed to counter number 5,Customer care')  
else:
    print('wait in the lobby to be called')            
