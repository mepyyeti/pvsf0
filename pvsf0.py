#!usr/bin/env python3
#pvsf0.py


def fv_of_pv_item(item1, int_free_months):
	interest = float(input('interest rate upfront paid item > '))
	if interest > 1:
		interest /= 100
	fin_charge = int(input('is there a financing charge?  Enter \'0\' for none.'))
	sales_tax = float(input('enter sales tax.  enter \'0\' for none.'))
	if sales_tax >= 1:
		sales_tax /= 100
	future_value = int(item1*(1+interest)**int_free_months)
	future_value *= (1+ sales_tax); future_value += fin_charge
	print(f'future cost of paid upfront item: ${future_value}.')
	return future_value

def pv_of_fv_item(item2, int_free_months):
	interest = float(input('interest rate for financed item > '))
	if interest > 1:
		interest /= 100
	fin_charge = int(input('is there a financing charge?  Enter \'0\' for none.'))
	sales_tax = float(input('enter sales tax.  enter \'0\' for none.'))
	if sales_tax >= 1:
		sales_tax /= 100
	present_value = int(item2/(1+interest)**int_free_months)
	present_value *= 1+ sales_tax; present_value += fin_charge
	print(f'present cost of financed item: ${present_value}.')
	return present_value

pv_item = int(input('please enter the item PRESENT VALUE.  '))
pv_id = True

while pv_id:
	if pv_item =='':
		print(f'{pv_item} is empty.  You entered incorrectly')
		pv_item = int(input('please re-enter item PRESENT VALUE.  '))
		continue
	else:
		print(f'{pv_item} is a number. Thank you for following directions.')
		break

fv_item = int(input('please enter the item FUTURE VALUE.  '))
fv_id = True

while fv_id:
	if fv_item =='':
		print(f'{fv_item} is empty.  You entered incorrectly')
		fv_item = int(input('please re-enter item FUTURE VALUE.  '))
		continue
	else:
		print(f'{fv_item} is a number. Thank you for following directions.')
		break

period = int(input('foo please enter how many months of interest free financing. '))

if pv_item > fv_item:
	print(f'{pv_item} is greater upfront.')
elif pv_item == fv_item:
	print(f'{pv_item} and {fv_item} are a wash')
elif fv_item > pv_item:
	print(f'{fv_item} is greater upfront.')

for_pv_item = fv_of_pv_item(pv_item, period)
for_fv_item = pv_of_fv_item(fv_item, period)


if int(for_pv_item) > int(for_fv_item):
	print(f'financed item with cost of ${fv_item} is a better bargain.  It\'s present cost is {for_fv_item}.')
	print(f'paid upfront item  costing ${pv_item} has a future total cost of {for_pv_item}.')
elif int(for_fv_item) > int(for_pv_item):
	print(f'paid upfront item costing ${pv_item} is a better bargain. it\'s future cost is {for_pv_item}.')
	print(f'financed item costing ${fv_item} has a future total cost of {for_fv_item}.')

if __name__=='__main__':
	print(f'{__name__} being run as main file.')
else:
	print('sorry no can do...')
