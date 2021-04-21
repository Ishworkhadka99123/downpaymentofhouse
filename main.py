''' Price of a house is $1M. If buyer has good credit, they need to put down 10% otherwise
 the need to put down by 20%
 Print the down payment '''
House_price= 100000
good_credit=True
if good_credit:
    down_payment=(10/100)*House_price
else:
    down_payment=(20/100)*House_price
print(f"Down payment:${down_payment}")
